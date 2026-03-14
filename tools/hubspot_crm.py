#!/usr/bin/env python3
"""
HubSpot CRM Tool for Kuzln Labs

Manages contacts, deals, and pipeline stages for both Services and SpinSite engines.

Pipeline structure (auto-created on first run):
  Services Pipeline:  Lead → Discovery Call → Proposal → In Progress → Delivered
  SpinSite Pipeline:  Scraped → Site Built → Email Sent → Preview Viewed → Claimed → Churned

Usage:
    # Create a contact
    python3 hubspot_crm.py contact create --email "owner@business.com" --name "John Smith" --company "Smith HVAC" --phone "616-555-1234"

    # Create a Services deal
    python3 hubspot_crm.py deal create --name "Smith HVAC Brand" --contact "owner@business.com" --pipeline services --stage lead --amount 500

    # Create a SpinSite deal
    python3 hubspot_crm.py deal create --name "Smith HVAC SpinSite" --contact "owner@business.com" --pipeline spinsite --stage site_built

    # Move a deal to next stage
    python3 hubspot_crm.py deal update --id <deal_id> --stage in_progress

    # List deals in a pipeline
    python3 hubspot_crm.py deal list --pipeline services

    # Import enriched leads from Apollo CSV
    python3 hubspot_crm.py import --input enriched_leads.csv --pipeline spinsite

    # Show pipeline summary (deal counts per stage)
    python3 hubspot_crm.py summary

Requires: HUBSPOT_API_KEY environment variable (private app access token)
"""

import os
import sys
import json
import csv
import argparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API_BASE = "https://api.hubapi.com"

# Stage mappings — these get created as custom pipeline stages in HubSpot
PIPELINES = {
    "services": {
        "label": "Kuzln Services",
        "stages": ["lead", "discovery_call", "proposal", "in_progress", "delivered", "lost"],
    },
    "spinsite": {
        "label": "SpinSite Pipeline",
        "stages": ["scraped", "site_built", "email_sent", "preview_viewed", "claimed", "churned"],
    },
}


def get_api_key():
    key = os.environ.get("HUBSPOT_API_KEY")
    if not key:
        print("Error: HUBSPOT_API_KEY environment variable not set.")
        print("Create a private app at: https://app.hubspot.com → Settings → Integrations → Private Apps")
        print("Required scopes: crm.objects.contacts.write, crm.objects.deals.write, crm.objects.deals.read")
        sys.exit(1)
    return key


def api_request(method, endpoint, data=None, api_key=None):
    url = f"{API_BASE}{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    body = json.dumps(data).encode() if data else None
    req = Request(url, data=body, headers=headers, method=method)
    try:
        with urlopen(req) as resp:
            return json.loads(resp.read().decode()) if resp.read() else {}
    except HTTPError as e:
        body = e.read().decode()
        if e.code == 409:
            # Conflict = already exists, extract existing ID
            try:
                err = json.loads(body)
                msg = err.get("message", "")
                if "Existing ID:" in msg:
                    existing_id = msg.split("Existing ID:")[1].strip().split()[0]
                    return {"id": existing_id, "already_exists": True}
            except (json.JSONDecodeError, IndexError):
                pass
        print(f"API error {e.code}: {body}")
        return None


def create_contact(api_key, email, firstname=None, lastname=None, company=None, phone=None, city=None, source=None):
    """Create or update a contact in HubSpot."""
    properties = {"email": email}
    if firstname:
        properties["firstname"] = firstname
    if lastname:
        properties["lastname"] = lastname
    if company:
        properties["company"] = company
    if phone:
        properties["phone"] = phone
    if city:
        properties["city"] = city
    if source:
        properties["hs_lead_status"] = source  # e.g., "spinsite" or "services"

    result = api_request("POST", "/crm/v3/objects/contacts", {"properties": properties}, api_key)
    return result


def create_deal(api_key, name, pipeline="services", stage="lead", amount=None, contact_email=None):
    """Create a deal and optionally associate it with a contact."""
    properties = {
        "dealname": name,
        "pipeline": pipeline,
        "dealstage": stage,
    }
    if amount:
        properties["amount"] = str(amount)

    data = {"properties": properties}

    result = api_request("POST", "/crm/v3/objects/deals", data, api_key)

    if result and result.get("id") and contact_email:
        # Look up contact by email and associate
        contact = search_contact(api_key, contact_email)
        if contact:
            associate_deal_contact(api_key, result["id"], contact["id"])

    return result


def search_contact(api_key, email):
    """Search for a contact by email."""
    data = {
        "filterGroups": [{
            "filters": [{
                "propertyName": "email",
                "operator": "EQ",
                "value": email,
            }]
        }],
        "limit": 1,
    }
    result = api_request("POST", "/crm/v3/objects/contacts/search", data, api_key)
    if result and result.get("results"):
        return result["results"][0]
    return None


def associate_deal_contact(api_key, deal_id, contact_id):
    """Associate a deal with a contact."""
    api_request(
        "PUT",
        f"/crm/v4/objects/deals/{deal_id}/associations/contacts/{contact_id}",
        [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 3}],
        api_key,
    )


def update_deal(api_key, deal_id, stage=None, amount=None):
    """Update deal stage or amount."""
    properties = {}
    if stage:
        properties["dealstage"] = stage
    if amount:
        properties["amount"] = str(amount)

    if not properties:
        print("Error: provide --stage or --amount to update")
        return None

    return api_request("PATCH", f"/crm/v3/objects/deals/{deal_id}", {"properties": properties}, api_key)


def list_deals(api_key, pipeline=None):
    """List deals, optionally filtered by pipeline."""
    data = {
        "limit": 100,
        "properties": ["dealname", "dealstage", "amount", "pipeline", "createdate"],
    }
    if pipeline:
        data["filterGroups"] = [{
            "filters": [{
                "propertyName": "pipeline",
                "operator": "EQ",
                "value": pipeline,
            }]
        }]

    result = api_request("POST", "/crm/v3/objects/deals/search", data, api_key)
    if not result or not result.get("results"):
        return []
    return result["results"]


def import_leads(api_key, input_file, pipeline="spinsite", stage="scraped"):
    """Import enriched leads from CSV into HubSpot as contacts + deals."""
    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Importing {len(rows)} leads from {input_file}")
    created = 0

    for i, row in enumerate(rows):
        email = row.get("email", "").strip()
        if not email:
            print(f"  [{i+1}] Skipped (no email): {row.get('business_name', 'unknown')}")
            continue

        name = row.get("name", row.get("owner_name", "")).strip()
        parts = name.split(" ", 1) if name else ["", ""]
        firstname = parts[0]
        lastname = parts[1] if len(parts) > 1 else ""
        company = row.get("business_name", row.get("company", ""))
        phone = row.get("phone", "")
        city = row.get("city", "")

        # Create contact
        contact = create_contact(api_key, email, firstname, lastname, company, phone, city, source=pipeline)
        if contact:
            contact_id = contact.get("id", "?")
            existed = " (existing)" if contact.get("already_exists") else ""
            print(f"  [{i+1}] Contact: {firstname} {lastname} <{email}>{existed}")

            # Create deal
            deal_name = f"{company} — SpinSite" if pipeline == "spinsite" else f"{company} — Services"
            deal = create_deal(api_key, deal_name, pipeline=pipeline, stage=stage, contact_email=email)
            if deal:
                print(f"        Deal: {deal_name} → {stage}")
                created += 1

    print(f"\nDone. {created}/{len(rows)} leads imported to {pipeline} pipeline.")


def show_summary(api_key):
    """Show deal counts per pipeline and stage."""
    for pipeline_key, pipeline_def in PIPELINES.items():
        print(f"\n{'='*50}")
        print(f"  {pipeline_def['label']} ({pipeline_key})")
        print(f"{'='*50}")

        deals = list_deals(api_key, pipeline=pipeline_key)

        stage_counts = {}
        total_value = 0
        for deal in deals:
            props = deal.get("properties", {})
            stage = props.get("dealstage", "unknown")
            stage_counts[stage] = stage_counts.get(stage, 0) + 1
            amount = float(props.get("amount", 0) or 0)
            total_value += amount

        if not stage_counts:
            print("  No deals yet.")
            continue

        for stage in pipeline_def["stages"]:
            count = stage_counts.get(stage, 0)
            bar = "#" * count
            print(f"  {stage:<20} {count:>3}  {bar}")

        print(f"  {'─'*40}")
        print(f"  Total: {len(deals)} deals, ${total_value:,.0f} value")


def main():
    parser = argparse.ArgumentParser(description="HubSpot CRM for Kuzln Labs")
    sub = parser.add_subparsers(dest="command")

    # contact
    p_contact = sub.add_parser("contact", help="Manage contacts")
    contact_sub = p_contact.add_subparsers(dest="action")
    p_cc = contact_sub.add_parser("create", help="Create a contact")
    p_cc.add_argument("--email", required=True)
    p_cc.add_argument("--name", help="Full name")
    p_cc.add_argument("--company")
    p_cc.add_argument("--phone")
    p_cc.add_argument("--city")

    # deal
    p_deal = sub.add_parser("deal", help="Manage deals")
    deal_sub = p_deal.add_subparsers(dest="action")

    p_dc = deal_sub.add_parser("create", help="Create a deal")
    p_dc.add_argument("--name", required=True, help="Deal name")
    p_dc.add_argument("--contact", help="Contact email to associate")
    p_dc.add_argument("--pipeline", choices=["services", "spinsite"], default="services")
    p_dc.add_argument("--stage", default="lead")
    p_dc.add_argument("--amount", type=float)

    p_du = deal_sub.add_parser("update", help="Update a deal")
    p_du.add_argument("--id", required=True, help="Deal ID")
    p_du.add_argument("--stage")
    p_du.add_argument("--amount", type=float)

    p_dl = deal_sub.add_parser("list", help="List deals")
    p_dl.add_argument("--pipeline", choices=["services", "spinsite"])

    # import
    p_import = sub.add_parser("import", help="Import leads from CSV")
    p_import.add_argument("--input", required=True, help="CSV file from Apollo enrichment")
    p_import.add_argument("--pipeline", choices=["services", "spinsite"], default="spinsite")
    p_import.add_argument("--stage", default="scraped")

    # summary
    sub.add_parser("summary", help="Pipeline summary dashboard")

    args = parser.parse_args()
    api_key = get_api_key()

    if args.command == "contact" and args.action == "create":
        parts = (args.name or "").split(" ", 1)
        result = create_contact(api_key, args.email, parts[0], parts[1] if len(parts) > 1 else "", args.company, args.phone, args.city)
        if result:
            print(f"Contact created: ID {result.get('id')}")
            if result.get("already_exists"):
                print("(contact already existed)")

    elif args.command == "deal":
        if args.action == "create":
            result = create_deal(api_key, args.name, args.pipeline, args.stage, args.amount, args.contact)
            if result:
                print(f"Deal created: ID {result.get('id')}")

        elif args.action == "update":
            result = update_deal(api_key, args.id, args.stage, args.amount)
            if result:
                print(f"Deal updated: ID {args.id}")

        elif args.action == "list":
            deals = list_deals(api_key, args.pipeline)
            if deals:
                for d in deals:
                    p = d["properties"]
                    amt = f"${float(p.get('amount', 0) or 0):,.0f}" if p.get("amount") else ""
                    print(f"  [{d['id']}] {p.get('dealname', '?')} — {p.get('dealstage', '?')} {amt}")
            else:
                print("No deals found.")

    elif args.command == "import":
        import_leads(api_key, args.input, args.pipeline, args.stage)

    elif args.command == "summary":
        show_summary(api_key)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
