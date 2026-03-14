#!/usr/bin/env python3
"""
Apollo.io Lead Enrichment Tool for SpinSite Pipeline

Enriches scraped GBP leads with owner emails and company data.
Supports single and bulk enrichment (up to 10 per call).

Usage:
    # Single enrichment by domain
    python3 apollo_enrichment.py enrich --domain "example.com"

    # Single enrichment by name + company
    python3 apollo_enrichment.py enrich --name "John Smith" --company "Smith HVAC"

    # Bulk enrichment from CSV (expects columns: business_name, domain or website_url)
    python3 apollo_enrichment.py bulk --input leads.csv --output enriched.csv

    # Search for people at a company
    python3 apollo_enrichment.py search --company "Smith HVAC" --city "Grand Rapids"

Requires: APOLLO_API_KEY environment variable
"""

import os
import sys
import json
import csv
import argparse
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode

API_BASE = "https://api.apollo.io/api/v1"


def get_api_key():
    key = os.environ.get("APOLLO_API_KEY")
    if not key:
        print("Error: APOLLO_API_KEY environment variable not set.")
        print("Get your API key at: https://app.apollo.io/#/settings/integrations/api")
        sys.exit(1)
    return key


def api_request(endpoint, data, api_key):
    url = f"{API_BASE}/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "X-Api-Key": api_key,
    }
    req = Request(url, data=json.dumps(data).encode(), headers=headers, method="POST")
    try:
        with urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        body = e.read().decode()
        print(f"API error {e.code}: {body}")
        return None


def enrich_person(api_key, domain=None, name=None, company=None, email=None):
    """Enrich a single person. Returns enriched data dict or None."""
    data = {}
    if domain:
        data["domain"] = domain
    if name:
        parts = name.strip().split(" ", 1)
        data["first_name"] = parts[0]
        if len(parts) > 1:
            data["last_name"] = parts[1]
    if company:
        data["organization_name"] = company
    if email:
        data["email"] = email

    if not data:
        print("Error: provide at least --domain, --name, or --email")
        return None

    result = api_request("people/match", data, api_key)
    if not result or not result.get("person"):
        return None

    person = result["person"]
    return {
        "name": f"{person.get('first_name', '')} {person.get('last_name', '')}".strip(),
        "title": person.get("title", ""),
        "email": person.get("email", ""),
        "phone": (person.get("phone_numbers") or [{}])[0].get("sanitized_number", ""),
        "linkedin": person.get("linkedin_url", ""),
        "company": person.get("organization", {}).get("name", ""),
        "city": person.get("city", ""),
        "state": person.get("state", ""),
        "company_domain": person.get("organization", {}).get("primary_domain", ""),
        "company_industry": person.get("organization", {}).get("industry", ""),
        "company_size": person.get("organization", {}).get("estimated_num_employees", ""),
    }


def search_people(api_key, company=None, city=None, state=None, title_keywords=None, limit=10):
    """Search for people matching criteria. Returns list of person dicts."""
    data = {
        "page": 1,
        "per_page": min(limit, 25),
        "person_titles": title_keywords or ["owner", "founder", "president", "manager"],
    }
    if company:
        data["q_organization_name"] = company
    if city:
        data["person_locations"] = [city]

    result = api_request("mixed_people/search", data, api_key)
    if not result or not result.get("people"):
        return []

    people = []
    for p in result["people"]:
        people.append({
            "name": f"{p.get('first_name', '')} {p.get('last_name', '')}".strip(),
            "title": p.get("title", ""),
            "email": p.get("email", ""),
            "company": p.get("organization", {}).get("name", "") if p.get("organization") else "",
            "city": p.get("city", ""),
            "linkedin": p.get("linkedin_url", ""),
        })
    return people


def bulk_enrich(api_key, input_file, output_file):
    """Bulk enrich leads from CSV. Writes enriched data to output CSV."""
    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} leads from {input_file}")
    enriched = []

    for i, row in enumerate(rows):
        domain = row.get("domain") or row.get("website_url", "").replace("https://", "").replace("http://", "").split("/")[0]
        name = row.get("owner_name", "")
        company = row.get("business_name", "")

        print(f"[{i+1}/{len(rows)}] Enriching: {company or domain}...", end=" ")

        result = enrich_person(api_key, domain=domain or None, name=name or None, company=company or None)

        if result and result.get("email"):
            enriched_row = {**row, **result}
            enriched.append(enriched_row)
            print(f"found: {result['email']}")
        else:
            enriched_row = {**row, "email": "", "phone": "", "linkedin": ""}
            enriched.append(enriched_row)
            print("no email found")

        # Rate limiting: Apollo free tier = 50 requests/min
        if (i + 1) % 10 == 0:
            time.sleep(2)

    if enriched:
        fieldnames = list(enriched[0].keys())
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(enriched)

    found = sum(1 for r in enriched if r.get("email"))
    print(f"\nDone. {found}/{len(rows)} emails found. Written to {output_file}")
    return enriched


def main():
    parser = argparse.ArgumentParser(description="Apollo.io Lead Enrichment for SpinSite Pipeline")
    sub = parser.add_subparsers(dest="command")

    # enrich
    p_enrich = sub.add_parser("enrich", help="Enrich a single person/business")
    p_enrich.add_argument("--domain", help="Company domain (e.g., example.com)")
    p_enrich.add_argument("--name", help="Person name (e.g., 'John Smith')")
    p_enrich.add_argument("--company", help="Company name")
    p_enrich.add_argument("--email", help="Known email to enrich")

    # search
    p_search = sub.add_parser("search", help="Search for people at a company/location")
    p_search.add_argument("--company", help="Company name")
    p_search.add_argument("--city", help="City name (e.g., 'Grand Rapids')")
    p_search.add_argument("--titles", nargs="+", default=["owner", "founder", "president"], help="Job title keywords")
    p_search.add_argument("-n", "--limit", type=int, default=10, help="Max results")

    # bulk
    p_bulk = sub.add_parser("bulk", help="Bulk enrich leads from CSV")
    p_bulk.add_argument("--input", required=True, help="Input CSV file")
    p_bulk.add_argument("--output", default="enriched_leads.csv", help="Output CSV file")

    args = parser.parse_args()
    api_key = get_api_key()

    if args.command == "enrich":
        result = enrich_person(api_key, domain=args.domain, name=args.name, company=args.company, email=args.email)
        if result:
            print(json.dumps(result, indent=2))
        else:
            print("No match found.")

    elif args.command == "search":
        results = search_people(api_key, company=args.company, city=args.city, title_keywords=args.titles, limit=args.limit)
        if results:
            for r in results:
                email_str = f" <{r['email']}>" if r.get("email") else ""
                print(f"  {r['name']}{email_str} — {r['title']} at {r['company']}")
        else:
            print("No results found.")

    elif args.command == "bulk":
        bulk_enrich(api_key, args.input, args.output)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
