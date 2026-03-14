# Kuzln Labs — Execution Plan (Pass 3)
## North Star Metric · Prioritized 90-Day Plan · Assumption Risk Map

*Generated March 13, 2026 — builds on Pass 1 (Lean Canvas, Value Props, ICP) and Pass 2 (Beachhead, GTM, Growth Loops)*

---

## Part 1: North Star Metric

### Step 1 — Classify the Business Game

Kuzln Labs plays the **Transaction Game**.

The core value event is a transaction: a business claims a website (ClawdBot) or purchases a service tier (Brand/Web/Automation). Revenue scales with the number of transactions and their recurring retention, not with time-spent-in-product (Attention) or task-completion efficiency (Productivity). The ClawdBot subscriber doesn't "use" their site daily — they pay for it to exist and work on their behalf. The services client pays for a deliverable, not ongoing software usage.

Transaction Game = North Star should measure the volume and quality of value-delivering transactions between Kuzln and SMBs.

---

### Step 2 — Evaluate North Star Candidates

Four candidates were proposed. Evaluating each against the seven criteria:

#### Candidate A: ClawdBot Conversion Rate

*Definition: Percentage of emailed leads who become paying subscribers.*

| Criterion | Score (1–5) | Notes |
|---|:---:|---|
| Easy to understand | 5 | Simple ratio. Everyone gets it. |
| Customer-centric | 2 | Measures Kuzln's sales efficiency, not customer value. A higher conversion rate doesn't mean customers are getting more value — it could mean better copy or lower prices. |
| Sustainable value | 2 | A rate can stay at 5% whether you have 15 subscribers or 1,500. It doesn't capture growth or cumulative value. |
| Vision alignment | 3 | Aligned with the ClawdBot engine, but ignores services entirely. |
| Quantitative | 5 | Clean number, easily tracked per batch. |
| Actionable | 4 | Teams can optimize email copy, templates, targeting. But it's influenced by many confounding variables (vertical, metro, season). |
| Leading indicator | 3 | Predicts ClawdBot unit economics, but doesn't predict total business health. |
| **Total** | **24/35** | |

**Verdict: Strong operational metric. Wrong North Star.** Conversion rate is a critical input metric for the data flywheel (Growth Loop #1), but it fails the customer-centricity and vision alignment tests. Optimizing for conversion rate alone could lead to chasing easy-to-convert but low-retention segments.

---

#### Candidate B: Total MRR (Monthly Recurring Revenue)

*Definition: Sum of all recurring revenue from ClawdBot subscribers and Automation retainers.*

| Criterion | Score (1–5) | Notes |
|---|:---:|---|
| Easy to understand | 5 | Everyone knows what MRR means. |
| Customer-centric | 1 | Pure financial metric. Says nothing about whether customers are getting value. MRR goes up when you raise prices, even if customers hate it. |
| Sustainable value | 3 | Recurring revenue implies retention, which implies ongoing value. But MRR includes customers who haven't churned yet but will. |
| Vision alignment | 4 | Aligned with "scale" and financial sustainability. |
| Quantitative | 5 | Dollar figure, tracked automatically via Stripe. |
| Actionable | 3 | Revenue is a lagging output of many upstream actions. Hard to say "optimize MRR" — optimize what, exactly? |
| Leading indicator | 2 | MRR is a trailing indicator. By the time MRR drops, the problem happened weeks ago. |
| **Total** | **23/35** | |

**Verdict: Essential financial tracking metric. Wrong North Star.** MRR belongs on the dashboard but fails the customer-centricity test entirely. It's the outcome you want, not the thing you optimize for.

---

#### Candidate C: Active Subscribers

*Definition: Total number of ClawdBot subscribers who are currently paying and whose sites are live.*

| Criterion | Score (1–5) | Notes |
|---|:---:|---|
| Easy to understand | 5 | A count. Unambiguous. |
| Customer-centric | 3 | An active subscriber implies they're getting enough value to keep paying. But "active" ≠ "getting value" — some might just not have gotten around to canceling. |
| Sustainable value | 3 | Grows only if acquisition > churn, which implies ongoing value delivery. But doesn't capture services at all. |
| Vision alignment | 3 | Aligned with ClawdBot scale, ignores services engine. |
| Quantitative | 5 | Clean integer. |
| Actionable | 4 | Directly influenced by acquisition (batches) and retention (churn). |
| Leading indicator | 3 | Leading for MRR, but lagging for acquisition health. |
| **Total** | **26/35** | |

**Verdict: Better than MRR, still incomplete.** Captures ClawdBot health but ignores services entirely. A month where you gain 50 ClawdBot subscribers but lose all services clients would look great on this metric and terrible for the business.

---

#### Candidate D: Sites Claimed (cumulative count of ClawdBot sites moved from preview to paid)

*Definition: Total lifetime count of preview sites that were claimed by a paying customer.*

| Criterion | Score (1–5) | Notes |
|---|:---:|---|
| Easy to understand | 5 | "How many businesses claimed their site?" Everyone gets it. |
| Customer-centric | 4 | A claimed site = a business that saw a preview and decided it was worth paying for. The moment of claiming is the moment of realized value. |
| Sustainable value | 3 | Cumulative, so it only goes up. But doesn't distinguish between a subscriber who stays 12 months and one who churns in 30 days. |
| Vision alignment | 4 | Directly tied to ClawdBot's core promise: "We already built your website. Claim it." But excludes services. |
| Quantitative | 5 | Clean integer. |
| Actionable | 4 | Driven by batch volume, conversion rate, template quality, and email copy. |
| Leading indicator | 4 | Leading for MRR (claimed sites generate revenue) and for the data flywheel (more claims = more learning). |
| **Total** | **29/35** | |

**Verdict: Strongest candidate so far, but still ignores services.**

---

### The Recommendation: A Modified Metric

None of the four candidates unifies both engines. The challenge is that services and ClawdBot deliver value in fundamentally different ways — one is a relationship, the other is a transaction. But they share one thing: **both engines result in an SMB having a better digital presence than they had before.**

**Recommended North Star Metric:**

> ### SMBs Activated
> *The cumulative number of businesses that have a live, Kuzln-delivered digital asset (website, brand, or automation system) currently in use.*

**Definition:** A business counts as "activated" if any of the following are true:
- They claimed a ClawdBot site and it's currently live (not churned)
- They received a Brand, Web, or Automation deliverable from services
- They upgraded from ClawdBot to a services tier (counts once, not twice)

**Why this works:**

| Criterion | Score (1–5) | Notes |
|---|:---:|---|
| Easy to understand | 5 | "How many businesses are using something we built?" |
| Customer-centric | 5 | Every activated SMB is a business that has a better digital presence because of Kuzln. This is the mission, stated as a number. |
| Sustainable value | 4 | Active = currently in use. Counts churn. Not just cumulative — a churned subscriber drops out of the count. |
| Vision alignment | 5 | Directly embodies "Brand. Web. Automation. At Scale." Every activation is progress toward the vision. |
| Quantitative | 5 | Integer count. Tracked via Stripe (ClawdBot subs) + project tracker (services clients). |
| Actionable | 5 | Influenced by both engines. Every batch, every services client, every retained subscriber moves the number. |
| Leading indicator | 5 | Leading for MRR (each activated SMB generates revenue). Leading for referrals (activated businesses drive word-of-mouth). Leading for the credibility bridge (activated businesses generate case studies). |
| **Total** | **34/35** | |

**The single number Jay should check every morning: "How many businesses are running on something I built?"**

---

### Step 3 — Input Metrics (the Constellation)

Five input metrics that drive the North Star:

```
                    ┌─────────────────────────┐
                    │   NORTH STAR METRIC      │
                    │   SMBs Activated         │
                    │   (currently live)        │
                    └────────────┬────────────┘
                                 │
            ┌────────────────────┼────────────────────┐
            │                    │                     │
   ┌────────▼────────┐ ┌────────▼────────┐ ┌─────────▼────────┐
   │  ClawdBot New    │ │  Services New   │ │  Retention Rate   │
   │  Subscribers/mo  │ │  Clients/mo     │ │  (monthly)        │
   └────────┬────────┘ └────────┬────────┘ └──────────────────┘
            │                    │
   ┌────────▼────────┐ ┌────────▼────────┐
   │  Conversion Rate │ │  Tier Escalation │
   │  (email → paid)  │ │  Rate            │
   └─────────────────┘ └─────────────────┘
```

| Input Metric | Definition | Target | Engine |
|---|---|---|---|
| **ClawdBot new subscribers/month** | Count of new paying subscribers in a calendar month | 15 (M4) → 120 (M12) | ClawdBot |
| **Services new clients/month** | Count of new Brand/Web/Automation clients started | 3–4 (M1) → 5–8 (M12) | Services |
| **Monthly retention rate** | % of previous month's activated SMBs still active this month | >92% (ClawdBot), >95% (services) | Both |
| **Conversion rate** | % of emailed ClawdBot leads who pay | >5% | ClawdBot |
| **Tier escalation rate** | % of Brand clients → Web, or ClawdBot subscribers → services | 30–40% Brand→Web; 5–10% ClawdBot→services | Both |

**How to use the constellation:** If the North Star (SMBs Activated) is flat or declining, diagnose by checking the input metrics in order: (1) Is retention dropping? (2) Are new subscribers/clients declining? (3) Is conversion rate falling? (4) Is escalation stalling? The input metrics tell you *where* the problem is; the North Star tells you *that* there's a problem.

---

### Dashboard Mock

What Jay checks each morning (one screen):

```
┌────────────────────────────────────────────────────┐
│  SMBs Activated: 147  (+12 this week)              │
├────────────────────┬───────────────────────────────┤
│  ClawdBot Subs: 112│  Services Clients: 35         │
│  New this month: 38│  New this month: 4            │
│  Churn this month:5│  Completed this month: 2      │
├────────────────────┼───────────────────────────────┤
│  Conversion Rate   │  Retention Rate               │
│  5.2% (last batch) │  93.1% (ClawdBot, rolling 30d)│
├────────────────────┼───────────────────────────────┤
│  Tier Escalation   │  MRR                          │
│  Brand→Web: 33%    │  $16,240 (ClawdBot + Auto)    │
│  CB→Services: 7%   │  (+$2,100 from last month)    │
└────────────────────┴───────────────────────────────┘
```

---

## Part 2: Prioritized 90-Day Plan (ICE Framework)

### The Constraint

Jay is one person. The Pass 2 GTM plan identified ~20 workstreams across the first 90 days. Even with AI leverage, a solo operator has roughly **40–50 productive hours per week**. Every hour spent on one thing is an hour not spent on another. The binding constraint isn't money — it's attention.

The ICE framework (Impact × Confidence × Ease) is the right tool here because it balances value delivered against execution risk and effort — exactly what a solo operator needs.

---

### Scoring All 90-Day Workstreams

| # | Workstream | Impact (1–10) | Confidence (1–10) | Ease (1–10) | ICE Score | Priority |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | Finalize services tier playbooks | 8 | 9 | 8 | **576** | **P0** |
| 2 | Land first 3 paying services clients | 10 | 7 | 6 | **420** | **P0** |
| 3 | Build kuzln.ai portfolio site | 6 | 8 | 7 | **336** | **P1** |
| 4 | Build ClawdBot DB schema + lead storage | 8 | 9 | 7 | **504** | **P0** |
| 5 | Build scraping pipeline (GBP → Supabase) | 9 | 8 | 6 | **432** | **P0** |
| 6 | Build contractor template v1 | 9 | 8 | 6 | **432** | **P0** |
| 7 | Build auto-generation pipeline (template + Claude → deploy) | 9 | 7 | 5 | **315** | **P1** |
| 8 | Set up email infrastructure (Resend/Postmark) | 7 | 9 | 8 | **504** | **P0** |
| 9 | Register + warm 2–3 outreach domains | 7 | 9 | 9 | **567** | **P0** |
| 10 | Write 4-email sequence copy (contractors) | 8 | 7 | 7 | **392** | **P0** |
| 11 | Build Stripe payment links + flow | 7 | 9 | 8 | **504** | **P0** |
| 12 | **Run first 50-business batch (GR contractors)** | 10 | 6 | 5 | **300** | **P1** |
| 13 | Run parallel 50-business batch (Lansing control) | 5 | 6 | 5 | **150** | **P2 — CUT** |
| 14 | Build salon/barbershop template | 6 | 7 | 6 | **252** | **P2 — DEFER** |
| 15 | Build restaurant template | 5 | 7 | 6 | **210** | **P2 — DEFER** |
| 16 | Expand to Kalamazoo metro | 5 | 5 | 5 | **125** | **P3 — DEFER** |
| 17 | Attend 2+ local networking events | 5 | 6 | 7 | **210** | **P2 — DEFER 1** |
| 18 | Set up AI reply triage for ClawdBot responses | 4 | 6 | 4 | **96** | **P3 — CUT** |
| 19 | A/B test email subject lines | 5 | 5 | 6 | **150** | **P2 — DEFER** |
| 20 | Build analytics dashboard for batch tracking | 4 | 7 | 5 | **140** | **P2 — DEFER** |
| 21 | Formalize ClawdBot → Services upsell funnel | 3 | 4 | 4 | **48** | **P3 — CUT** |

---

### The Ruthless Cut: What Changes

**What gets CUT entirely from the first 90 days:**

| Workstream | Why Cut |
|---|---|
| **Lansing control batch (#13)** | Nice for scientific rigor, but costs 10+ hours of setup and attention for a comparison that doesn't change the M4 decision. If Grand Rapids works, scale it. If it doesn't, the diagnosis comes from batch data analysis, not a control city. Run Lansing in M5 if you want the comparison. |
| **AI reply triage (#18)** | Over-engineering. At 50 emails/batch, you'll get 5–15 replies. Read them yourself. The manual reading is *valuable* — it's how you learn what objections look like, what language SMBs use, what signals conversion intent. Automate this when you're doing 500+ emails/batch. |
| **Formalized upsell funnel (#21)** | Zero subscribers exist yet. You can't formalize a funnel for a customer segment that doesn't exist. When a ClawdBot subscriber asks for more, say "yes" and serve them manually. Formalize in M7+ when you see the pattern. |

**What gets DEFERRED to Month 3+:**

| Workstream | Deferred To | Why Defer |
|---|---|---|
| **Salon template (#14)** | M3 (after first batch data) | Build the second vertical *after* you have contractor conversion data, not before. If contractors convert at 7%, you may want more contractor batches, not a new vertical. |
| **Restaurant template (#15)** | M3–M4 | Same logic. The data flywheel (Loop #1) should inform which vertical comes second. |
| **Kalamazoo expansion (#16)** | M4+ | Go deep in GR first. Metro Domination loop requires density before expansion. |
| **A/B testing subject lines (#19)** | M3 (after 2+ batches) | You need a baseline before you can A/B test. Run Batch 1 with your best guess. Run Batch 2 with a variation. Compare. That's your A/B test — no infrastructure needed. |
| **Analytics dashboard (#20)** | M3 | A spreadsheet tracks 50-business batches just fine. Build a dashboard when you're running 3+ batches/month and the spreadsheet breaks. |
| **2nd networking event (#17)** | Defer 1 of 2 to Month 2 | Attend one event in Month 1 to seed conversations. The second event is lower ROI than building pipeline. |

**What gets RESEQUENCED:**

| Original Sequence | Revised Sequence | Why |
|---|---|---|
| Build portfolio → Land clients | Land 1–2 clients → Build portfolio from their work | You don't need a portfolio to land network-based clients. You need conversations. Build the portfolio from real deliverables, not spec work. |
| Build entire ClawdBot pipeline → Run batch | Build scraping + template → Generate sites manually → Send emails semi-manually → Automate after validation | Don't fully automate before validating. A "manual ClawdBot" batch (scrape with a tool, generate sites one at a time, send emails via Resend dashboard) takes 10–15 hours but validates the concept without building a full pipeline. |
| Domain warmup starts Week 1 | Domain warmup starts **now (today)** | Domains take 2–4 weeks to warm. Every day you delay is a day ClawdBot can't launch. Register domains and begin sending warmup volume immediately, even before the pipeline is built. |

---

### Revised 90-Day Calendar (Solo Operator Reality)

#### Phase 1: Weeks 1–4 — Revenue + Pipeline Foundation

**Week 1 (20 hrs services / 20 hrs ClawdBot)**

| Day | Services (AM) | ClawdBot (PM) |
|---|---|---|
| Mon | Finalize Brand playbook. Draft 5 outreach messages to network. | Register 3 outreach domains. Set up Resend account. Begin warmup (10 emails/day to seed addresses). |
| Tue | Send 5 outreach messages. Follow up on any existing leads. | Set up Supabase project. Define lead table schema. |
| Wed | Send 5 more outreach messages. Book 2 discovery calls. | Sign up for Outscraper. Test scrape 10 GR contractors. Inspect data quality. |
| Thu | Run 1 discovery call. Draft Brand proposal. | Build contractor template v1 in Astro/Next.js. Hero + About sections. |
| Fri | Run 2nd discovery call. Close first Brand client if possible. | Finish template: Services + Reviews + Contact sections. |

**Week 2**

| Focus | Services | ClawdBot |
|---|---|---|
| Goal | Close 1st Brand client. Begin delivery. | Finish scraping pipeline. Generate 10 test sites. |
| Activities | Deliver logo concepts, color palette, type. | Scrape 50 GR contractors via Outscraper. Run Hunter.io enrichment. Score leads. Generate 10 preview sites (Claude API → template → Vercel). |
| Milestone | First $500 in revenue. | 10 live preview sites at {slug}.clawdbot.com. |

**Week 3**

| Focus | Services | ClawdBot |
|---|---|---|
| Goal | Deliver Brand. Collect testimonial. Close 2nd client. | Write email copy. Set up Stripe. Generate remaining sites. |
| Activities | Finalize Brand deliverable. Ask for written testimonial. Outreach for 2nd client. | Write all 4 emails (contractor-specific). Create 3 Stripe payment links (Starter, Pro, Launch). Generate 40 more preview sites from scored leads. |
| Milestone | First case study. Second client in pipeline. | 50 preview sites live. Email sequence ready. Payment flow ready. |

**Week 4**

| Focus | Services | ClawdBot |
|---|---|---|
| Goal | Close 2nd Brand + 1st Web client. | **Send Batch 1.** |
| Activities | Begin 2nd Brand delivery. Scope Web project. Attend 1 networking event. | **Email 50 contractors in Grand Rapids.** Monitor opens, clicks, preview views, replies in real-time. Respond to all replies within 4 hours. |
| Milestone | $3,000+ total services revenue. | **ClawdBot is live. First data is flowing.** |

#### Phase 2: Weeks 5–8 — Validate and Iterate

| Week | Services | ClawdBot | Key Decision |
|---|---|---|---|
| **5** | Deliver 2nd Brand. Begin Web build. Ask for 2nd testimonial. | Analyze Batch 1: open rate, preview views, replies, conversions. Document every reply and objection. | Is open rate >30%? Is preview view rate >10%? If yes → Batch 2. If no → diagnose. |
| **6** | Continue Web delivery. Close 3rd Brand via referral. | If metrics viable: run Batch 2 (100–200 GR contractors). Revise email copy based on Batch 1 learnings. | Are conversions happening? At what rate? |
| **7** | Deliver Web project ($2,500). Case study + testimonial. Pitch first Automation prospect. | Analyze Batch 2. Calculate CPA, conversion rate, revenue per batch. | Is the unit economics positive? Is CPA <$20? |
| **8** | Close Automation client ($1,500/mo). Services revenue at ~$6K–$8K/mo. | **Decision point: build salon template or run more contractor batches?** Let the data decide. | What does the conversion data say about vertical expansion vs. depth? |

#### Phase 3: Weeks 9–13 — Scale What Works

| Week | Services | ClawdBot | Focus |
|---|---|---|---|
| **9** | Deliver Automation setup. Continue Brand pipeline. | Build 2nd vertical template (salons OR restaurants, based on data). Run first batch in new vertical. | Second vertical validation. |
| **10** | Services stable at $8–10K/mo. First ClawdBot→Services upsell if it happens naturally. | Run 200+ business batch in GR (mixed verticals). Refine scoring model based on conversion data. | Blended vertical performance. |
| **11** | Use ClawdBot conversion data in services conversations. "We've helped 50+ GR businesses launch sites." | Analyze cross-vertical data. Which vertical wins? Begin building analytics spreadsheet to track at scale. | Vertical ranking finalized. |
| **12–13** | Continue services pipeline. Consider first contractor hire if hitting $12K+/mo. | Scale winning vertical. Run 500+ lead batches. Consider 2nd metro (Kalamazoo) if GR depth allows. | **Day 90 checkpoint: full system assessment.** |

---

### What This Calendar Cuts vs. Pass 2

| Pass 2 Plan Element | Pass 3 Reality |
|---|---|
| 3 vertical templates in first 90 days | 1 template at launch, 2nd only after data validates |
| Lansing control batch | Cut. Run Lansing in M5 if desired |
| AI reply triage | Cut. Manual replies for first 6 months |
| Formal upsell funnel | Cut. Handle upsells ad hoc until M7 |
| 2 networking events in first 6 weeks | 1 event. Second deferred. |
| Full analytics dashboard | Spreadsheet until M3 |
| A/B testing infrastructure | Manual A/B via batch-to-batch copy changes |

**Net effect: ~15 hours/week recovered** and redirected toward the two things that matter most in the first 30 days: landing services revenue and sending Batch 1.

---

## Part 3: Assumption Risk Map

### Framework

Eight risk categories from Teresa Torres' extended model, adapted for Kuzln Labs. Each assumption is rated on:

- **Impact (1–10):** How badly does the business fail if this assumption is wrong?
- **Uncertainty (1–10):** How little evidence do we have? (10 = pure guess)
- **Risk Score:** Impact × Uncertainty. Higher = test first.

---

### The Complete Assumption Map

#### Category 1: Value Risk — Will SMBs find this valuable?

| ID | Assumption | Impact | Uncertainty | Risk Score | Current Evidence |
|---|---|:---:|:---:|:---:|---|
| **V1** | SMB owners will click a link in an unsolicited email to see a preview site built for their business | 10 | 8 | **80** | Zero. No batch has been sent. Gift-first model is theorized, not tested. |
| **V2** | Preview sites built from GBP data will feel "bespoke" enough that owners perceive them as valuable, not generic | 8 | 7 | **56** | Zero. Templates haven't been shown to real business owners. |
| **V3** | 5% of emailed leads will convert to a paid plan | 7 | 8 | **56** | Zero. The 5% figure is an estimate from comparable cold-outreach SaaS benchmarks, not Kuzln-specific data. |
| **V4** | ClawdBot sites will actually generate measurable results (more calls, bookings) for subscribers | 7 | 7 | **49** | Zero. Sites haven't been live long enough to measure impact. |

#### Category 2: Usability Risk — Will SMBs understand and complete the flow?

| ID | Assumption | Impact | Uncertainty | Risk Score | Current Evidence |
|---|---|:---:|:---:|:---:|---|
| **U1** | Business owners can go from email → preview → Stripe payment with no human help | 6 | 6 | **36** | Medium — Stripe payment links are well-tested UX, but the full flow (email → click → view → pay) is untested for this audience. |
| **U2** | The $29/mo price point is low enough to be an impulse buy for a contractor | 5 | 4 | **20** | High confidence — $29/mo is trivially small relative to contractor revenue. |

#### Category 3: Viability Risk — Can we sustain this economically?

| ID | Assumption | Impact | Uncertainty | Risk Score | Current Evidence |
|---|---|:---:|:---:|:---:|---|
| **Vi1** | Starter plan churn stays below 8%/month with quarterly content refreshes | 8 | 8 | **64** | Zero. No subscribers exist. Churn is the #1 long-term viability risk. SMBs at $29/mo have notoriously high churn in other SaaS products. |
| **Vi2** | Services clients escalate tiers at 30–40% (Brand → Web) | 6 | 6 | **36** | Low — based on general freelance/agency experience, not Kuzln-specific data. |
| **Vi3** | Solo-operator model can sustain both engines without burnout through M12 | 7 | 5 | **35** | Medium — Jay has AI leverage and fixed-scope productization, but no historical data on sustained dual-engine operation. |

#### Category 4: Feasibility Risk — Can we actually build this?

| ID | Assumption | Impact | Uncertainty | Risk Score | Current Evidence |
|---|---|:---:|:---:|:---:|---|
| **F1** | Claude API can generate sufficiently high-quality, bespoke-feeling copy for each site at <$0.30/site | 6 | 4 | **24** | Medium-high — Claude is capable, but prompt engineering for consistency at scale is untested. |
| **F2** | GBP data is rich enough across contractors in Grand Rapids to generate compelling sites | 7 | 5 | **35** | Low — GBP data quality varies by business. Some contractors have detailed profiles; others have a name, phone, and 3-star rating. |

#### Category 5: Ethics Risk — Should we do this?

| ID | Assumption | Impact | Uncertainty | Risk Score | Current Evidence |
|---|---|:---:|:---:|:---:|---|
| **E1** | Gift-first framing is perceived as genuine value delivery, not deceptive or manipulative | 7 | 6 | **42** | Zero. The line between "gift" and "unsolicited sales tactic" is subjective. Some recipients will perceive this negatively regardless of intent. |

#### Category 6: Go-to-Market Risk — Can we reach and convert customers?

| ID | Assumption | Impact | Uncertainty | Risk Score | Current Evidence |
|---|---|:---:|:---:|:---:|---|
| **G1** | Email deliverability holds at >40% open rate with gift-first framing and warmed domains | 9 | 7 | **63** | Zero. Cold email deliverability is fragile. One spam complaint spike can tank a domain. |
| **G2** | Owner emails are discoverable for >60% of qualified GBP leads via Hunter.io/Apollo | 7 | 6 | **42** | Low — enrichment rates vary by vertical. Contractors who operate as LLCs may have more discoverable emails than sole proprietors. |
| **G3** | Grand Rapids has sufficient depth of contractors without websites to sustain 3+ batches | 6 | 5 | **30** | Low — Outscraper test scrape will answer this quickly. |

#### Category 7: Strategy Risk — Is this the right approach?

| ID | Assumption | Impact | Uncertainty | Risk Score | Current Evidence |
|---|---|:---:|:---:|:---:|---|
| **S1** | Contractors are the highest-converting vertical (beachhead hypothesis) | 6 | 7 | **42** | Zero for Kuzln. Based on structural reasoning (high-ticket services, review density, referral networks) but no empirical validation. |
| **S2** | The data flywheel produces meaningful conversion improvements within 3–5 batches | 5 | 6 | **30** | Medium — the logic is sound (more data → better targeting) but the rate of improvement is unknown. |
| **S3** | Competitors won't replicate the gift-first model in the next 12 months | 4 | 4 | **16** | High confidence — the model requires building an entire pipeline, not just copying an idea. Execution speed is the moat. |

#### Category 8: Team Risk — Can Jay execute this?

| ID | Assumption | Impact | Uncertainty | Risk Score | Current Evidence |
|---|---|:---:|:---:|:---:|---|
| **T1** | One person can build the full ClawdBot pipeline (scraping + generation + email + payments) in 8–10 weeks while simultaneously running services | 8 | 5 | **40** | Medium — Jay has the technical skills, but the scope is ambitious for a solo builder alongside revenue-generating services work. |
| **T2** | 70/20/10 time allocation (Kuzln / other ventures / learning) is sustainable | 5 | 5 | **25** | Medium — depends on the pull of other ventures. If another opportunity demands attention, Kuzln suffers. |

---

### Ranked by Risk Score (Test Priority)

| Rank | ID | Assumption | Risk Score | Validation Test |
|:---:|---|---|:---:|---|
| **1** | V1 | SMB owners will click the preview link in the email | **80** | **The 50-business batch.** This is the first test. Send 50 emails. Measure open rate and preview view rate. If preview view rate is <5%, the model needs fundamental rethinking. Cost: ~$15 + 10 hours. Timeline: 1 day to send, 12 days to complete sequence. |
| **2** | Vi1 | Churn stays below 8%/month | **64** | **Cohort tracking from Day 1.** Tag every subscriber with their acquisition date, vertical, and metro. Measure 30/60/90-day retention. Can't fully validate until M7+ (need 3 months of subscriber data), but early warning signs (cancellations in first 30 days) appear immediately. Cost: $0 (Stripe data). |
| **3** | G1 | Email deliverability holds | **63** | **Monitor from Batch 1.** Track open rate (proxy for deliverability), bounce rate, and spam complaint rate in Resend/Postmark. Set hard stop: if spam complaints >0.3% or open rate <25% on any batch, pause and diagnose before sending more. Cost: $0 (built into email platform). |
| **4** | V2 | Preview sites feel bespoke, not generic | **56** | **The "show 5 people" test.** Before Batch 1, generate 5 contractor sites and show them to 5 people (friends, family, other business owners — not the actual businesses). Ask: "Does this look like it was built specifically for this business, or does it look like a template?" If 3+ say "template," iterate on the template before sending. Cost: $0 + 2 hours. Timeline: 1 afternoon. |
| **5** | V3 | 5% conversion rate | **56** | **Batches 1–3.** You can't validate a conversion rate without running batches. The test is the first 3 batches (150 emails total). If conversion is 0% across 150 emails, the model needs rethinking. If it's 1–3%, it's viable but slower than projected. If it's 5%+, you're on plan. Cost: ~$45 + 30 hours. Timeline: 6 weeks. |
| **6** | V4 | ClawdBot sites generate measurable results | **49** | **Track subscriber outcomes.** For the first 20 subscribers, manually check after 30 days: Did their Google calls/directions increase? Can they report more inbound leads? This is hard to measure definitively but qualitative feedback ("I got 3 calls this week that mentioned my website") is sufficient early signal. Cost: 30 min/subscriber. Timeline: M5–M6. |
| **7** | E1 | Gift-first framing perceived positively | **42** | **Monitor Batch 1 sentiment.** Track tone of replies (positive, neutral, negative, hostile). If >20% of replies are negative ("stop emailing me," "this is a scam"), the framing needs work. If <5% are negative, the framing is working. Cost: $0 (read every reply). |
| **8** | G2 | Owner emails discoverable for >60% of leads | **42** | **Run enrichment on the first 50 scraped leads.** Before building any sites, run the 50 Grand Rapids contractor leads through Hunter.io and Apollo. Count how many return a valid email. If <40%, you have an enrichment problem that must be solved (try Snov.io, PeopleDataLabs, or LinkedIn scraping as fallbacks). Cost: ~$5 (Hunter.io credits). Timeline: 1 hour. |
| **9** | S1 | Contractors are the highest-converting vertical | **42** | **Cross-vertical batch in M2–M3.** After 2 contractor batches, run one salon batch and one restaurant batch in the same metro with identical email structure. Compare conversion rates. If salons beat contractors, pivot the beachhead. Cost: ~$30 + 15 hours for 2 new templates. |
| **10** | T1 | Solo operator can build pipeline + run services | **40** | **Weekly time audit.** Every Friday for the first 8 weeks, log hours spent on services vs. ClawdBot build. If services consistently consume >60% of time, either (a) reduce services volume, (b) simplify the pipeline, or (c) hire a contractor sooner. Cost: $0, 10 min/week. |

---

### Validation Sequence: What Gets Tested When

| Week | Tests Running | What You Learn |
|---|---|---|
| **Week 1** | G2 (email enrichment rate on 50 leads) | Can you even reach these businesses? |
| **Week 2** | V2 ("show 5 people" template quality test) | Does the preview site pass the bespoke test? |
| **Week 3** | Domain warmup metrics (deliverability baseline) | Are your domains healthy enough to send? |
| **Week 4** | **V1 (Batch 1: 50 emails sent)** — the big test | Do owners click? Do they view? Do they reply? |
| **Week 5** | V1 continued (12-day sequence completes) + G1 (deliverability metrics) + E1 (reply sentiment) | Full Batch 1 results: open, view, reply, convert, sentiment |
| **Week 6–8** | V3 (conversion rate across batches 1–3) + T1 (time audit) | Is the unit economics real? Can Jay sustain the pace? |
| **Week 9–10** | S1 (cross-vertical batch comparison) + Vi2 (first escalation data from services) | Which vertical wins? Do services clients upgrade? |
| **Week 11–13** | Vi1 (first churn data from early subscribers) + V4 (subscriber outcomes) | Are subscribers staying? Are their sites working? |

**The critical early kill switch:** If Batch 1 produces <5% preview view rate AND <15% open rate, **pause and diagnose before Batch 2.** Possible causes: deliverability failure (domain issue), subject line failure (wrong hook), or targeting failure (wrong leads). Each has a different fix. Do not throw more volume at a broken funnel.

---

### The One-Page Risk Summary

```
HIGHEST RISK (test in weeks 1–4):
  ┌─────────────────────────────────────────────────────────┐
  │ V1: Will they click?          → Batch 1 (Week 4)       │
  │ G1: Will emails deliver?      → Warmup metrics (Week 3) │
  │ G2: Can we find their email?  → Enrichment test (Week 1)│
  │ V2: Does the site look real?  → Show 5 people (Week 2)  │
  └─────────────────────────────────────────────────────────┘

MEDIUM RISK (test in weeks 5–10):
  ┌─────────────────────────────────────────────────────────┐
  │ V3: Will 5% convert?          → Batches 1–3 (Weeks 4–8)│
  │ S1: Are contractors #1?       → Cross-vertical (Week 9) │
  │ T1: Can Jay sustain this?     → Weekly time audit       │
  │ E1: Is the framing OK?        → Reply sentiment (Week 5)│
  └─────────────────────────────────────────────────────────┘

DEFERRED RISK (test in months 3–6):
  ┌─────────────────────────────────────────────────────────┐
  │ Vi1: Will churn stay <8%?     → Cohort data (M5+)      │
  │ V4: Do sites generate calls?  → Subscriber check (M5+) │
  │ Vi2: Do services tiers escalate? → Track over 10 clients│
  │ S2: Does the data flywheel work? → Batch-over-batch Δ  │
  └─────────────────────────────────────────────────────────┘
```

---

*Pass 3 complete. Three artifacts — North Star Metric (SMBs Activated), ICE-prioritized 90-day calendar (with cuts and deferrals), and Assumption Risk Map (18 assumptions ranked with validation tests) — complete the strategic planning stack for Kuzln Labs' Year 1 launch.*

*Full stack across all three passes:*
- *Pass 1: Lean Canvas, Value Propositions, ICP*
- *Pass 2: Beachhead Segment, GTM Strategy, Growth Loops*
- *Pass 3: North Star Metric, Prioritized Plan, Assumption Map*
