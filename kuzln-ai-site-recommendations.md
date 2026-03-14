# kuzln.ai — Site Recommendations
## Grounded in Passes 1–3 of the Kuzln Labs Strategic Analysis

*March 13, 2026*

---

## What the Site Is Today

A single-page static site with four sections:

1. **Hero** — "We build brands that move businesses forward." Two CTAs: Start a Project + See Services.
2. **Services** — Three tier cards (Brand $500, Web $2,500, Automation $1,500/mo) with bullet-point deliverables and Get Started buttons.
3. **Process** — Three steps: Tell us what you need → We build it fast → You scale with it.
4. **Contact** — "Ready to build?" with a mailto link to hello@kuzln.ai.

Nav: Services | Process | Contact. Dark theme, starfield canvas animation, Inter font, orange accent. Clean, minimal, well-designed. Good bones.

---

## What the Site Needs to Do (Per Our Analysis)

The site serves **four distinct audiences** that arrive with different intent:

| Audience | How They Arrive | What They Need to See |
|---|---|---|
| **Services prospects** (Segment A) | Referral, networking, Google | Proof you can deliver. Portfolio. Testimonials. Speed + price clarity. |
| **ClawdBot email recipients** | Click "Is this legit?" link in outreach email | Instant trust. Evidence Kuzln is real. Local proof. Not a scam. |
| **ClawdBot subscribers considering upgrade** | Already paying $29/mo, curious about Brand/Web/Automation | Bridge from ClawdBot → services. "Want more? Here's the next level." |
| **Google searchers** (future) | Organic search for local web services | SEO-optimized content. Local keywords. Structured data. |

Right now the site speaks to Audience 1 only, and even then it's missing the proof layer. It doesn't acknowledge ClawdBot at all, isn't indexed by Google, and has no social proof of any kind.

---

## The Recommendations

Organized from highest-impact to lowest. Each one ties back to a specific finding from our strategic analysis.

---

### 1. Add a Portfolio / Work Section

**Strategic basis:** The Credibility Bridge (Pass 2, Growth Loop #2) requires case studies on kuzln.ai. ClawdBot email #3 and #4 link to kuzln.ai for legitimacy. Services prospects evaluate you based on past work. Without a portfolio, every conversation starts at zero trust.

**What to add:**
- A new "Work" section between Services and Process (and in the nav).
- Start with 2–3 pieces. If you don't have paid client work yet, create spec projects — a brand identity for a fictional contractor, a website mockup for a local salon. The Pass 3 prioritization plan deprioritized this in favor of landing real clients first, but even 1–2 spec pieces are better than nothing.
- Each piece should show: the business type, what was delivered, a before/after if applicable, and a result or testimonial (even if it's from the spec process).

**Format:** Visual grid. Click to expand into a mini case study. Keep it image-heavy — the work should speak for itself.

**When:** Before Batch 1 goes out. ClawdBot recipients who click through to verify legitimacy need to see something.

---

### 2. Add Social Proof / Testimonials

**Strategic basis:** Pass 1 Value Proposition analysis identified trust as the core barrier for both segments. Services prospects are burned by agencies. ClawdBot recipients are skeptical of unsolicited email. The single fastest way to overcome both is named, verifiable testimonials.

**What to add:**
- A testimonial strip or section — even one quote from a real client changes the dynamic.
- Format: Name, business name, city, photo if available. "Jay rebuilt our brand in a week. We went from a Canva logo to something that looks like a $10K agency job." — Mike R., M&R Plumbing, Grand Rapids.
- If you have zero testimonials yet, add this section as a placeholder in your HTML (commented out or hidden) and activate it the moment your first Brand client gives you a quote. The Pass 3 plan has you collecting a testimonial in Week 3.

**Placement:** Between the Work section and the Process section. Or as a horizontal scrolling strip anywhere below the fold.

---

### 3. Add Timelines to the Service Cards

**Strategic basis:** Pass 1 Value Proposition identified speed as the #1 differentiator against agencies. The current cards show deliverables and price but not timeline. The value prop statement was: "Agency-quality brand, web, and automation — at fixed prices, in days not months." The "in days not months" part is invisible on the site.

**What to change:**
- Add a timeline line to each card, directly below the price:

  Brand: "Starting at $500 · **Delivered in 1 week**"
  Web: "Starting at $2,500 · **Delivered in 2–3 weeks**"
  Automation: "Starting at $1,500/mo · **Live in 30 days**"

This is a small copy change with outsized impact. When a prospect is comparing you to an agency quoting 6–16 weeks, the timeline is what closes the deal.

---

### 4. Add a ClawdBot Legitimacy Anchor

**Strategic basis:** Pass 2 GTM Strategy and the Credibility Bridge loop both identify kuzln.ai as the trust verification point for ClawdBot email recipients. When a contractor in Grand Rapids gets an email saying "We built your website," the first thing they'll do before clicking anything is Google "Kuzln Labs" or click the link in the email footer. If they land on a site that only talks about premium services ($500–$2,500) and has no mention of the free preview program, there's a trust gap.

**What to add:**
- A small, dedicated section or page (either a section on the main page or a separate `/clawdbot` page) that says something like:

  > **ClawdBot by Kuzln Labs**
  > We build free preview websites for local businesses using public Google data. If you received an email from us with a link to your preview site, it's real — we built it because we think your business deserves a web presence that matches your reputation. Claim it, or let it expire. No obligation.

- This serves a very specific purpose: when a skeptical recipient Googles you or clicks through, they land on a page that explains what just happened in a trustworthy, non-salesy way. It validates the email and reduces the "is this a scam?" friction.

**Placement:** Either a footer link ("Received a preview site? Learn more") or a dedicated `/clawdbot` route. Keep it simple — this isn't a sales page. It's a trust page.

**When:** Before Batch 1. This is part of the email infrastructure.

---

### 5. Replace the Email-Only Contact with a Real Intake

**Strategic basis:** Pass 3 ICE prioritization identified landing services clients as a P0 task. The current contact section is a mailto link — which means the prospect has to open their email client, compose a message, figure out what to say, and send it. Every step is friction. The Process section says "15-minute call or a quick form" but there's no form and no way to book a call.

**What to add (pick one or both):**
- **A Calendly/Cal.com embed** for booking a 15-minute intro call. This is the lowest-friction path for a warm lead. They click, pick a time, done. No email composition required.
- **A simple intake form** (3–5 fields: name, business, what you need, budget range, email). Can be a Tally embed, Typeform, or even a static HTML form that sends to your email via Formspree/Basin.

**What to keep:** The hello@kuzln.ai button stays as a secondary option for people who prefer email. But it shouldn't be the only option.

**When:** Week 1. This takes 30 minutes with Calendly and directly increases services conversion.

---

### 6. Make the Site Indexable by Google

**Strategic basis:** The site returned zero results on `site:kuzln.ai` — meaning Google hasn't indexed it at all. This could be a missing sitemap, a robots.txt blocking crawlers, or the site simply hasn't been submitted to Google Search Console. For now, all acquisition is network-based, so this isn't urgent. But as the portfolio grows and ClawdBot generates local social proof, organic search becomes a channel. "web design Grand Rapids" or "small business branding Michigan" are long-tail queries with real volume and low competition.

**What to do:**
- Submit the site to Google Search Console.
- Add a `sitemap.xml` and ensure `robots.txt` allows crawling.
- Add proper `<meta>` tags: title, description, Open Graph tags for social sharing.
- Add a `<title>` tag that includes your target keywords: "Kuzln Labs — Brand, Web & Automation for Small Businesses"
- Add `<meta name="description" content="...">` with your value prop.

**When:** Week 1. Takes 20 minutes. Zero cost. Compounds over time.

---

### 7. Speak to a Specific Buyer, Not Everyone

**Strategic basis:** Pass 1 ICP identified three launch verticals (contractors, salons, restaurants). Pass 1 Value Props showed that the services buyer is "a small business owner priced out of agencies and burned out on DIY." The current site copy is generic — "businesses," "your vision," "a system that runs itself." None of this tells a contractor in Grand Rapids that this site is *for them*.

**What to change:**

The hero subline currently reads: "From logo to launch to automation. Kuzln Labs turns your vision into a system that runs itself."

Consider something closer to: "Brand, web, and automation for small businesses — at fixed prices, delivered in days. No proposals. No surprises."

And somewhere below the fold (in the Work section or a new "Who We Work With" strip), show the verticals you serve: contractors, restaurants, salons, professional services. Even just logos/icons of industry types + one line ("We help local service businesses look as good online as they are in person") signals to your ICP that this isn't a generic agency — it's *for them*.

**The key principle from the value prop analysis:** The services value prop is "agency-quality at fixed prices, in days not months, from one operator who actually picks up the phone." The current site communicates the first part (quality + tiers) but misses speed, fixed-price emphasis, and the personal operator angle entirely.

---

### 8. Add an "About" or Operator Section

**Strategic basis:** Pass 1 Value Props identified that services clients value "working with a single operator who understands their business, not an account manager at a faceless agency." The current site says "we" throughout but gives no indication of who's behind it. For a solo-operator business, the operator *is* the brand. A small business owner choosing between Kuzln and a faceless agency will pick the one where they know who they're working with.

**What to add:**
- A brief section — doesn't need to be a full bio page. A photo, a name (Jay), and 2–3 sentences: who you are, why you do this, what makes you different. Something like:

  > I'm Jay. I build brands, websites, and automation systems for small businesses — using AI to deliver agency-quality work at a fraction of the cost and timeline. Every project is hands-on, fixed-scope, and built to grow with you.

- This humanizes the brand, builds trust, and differentiates you from every template agency site that says "we are a team of passionate professionals."

**Placement:** Between Process and Contact. Or as a small aside near the footer.

---

### 9. Add Outcome Language to Service Cards

**Strategic basis:** The current cards list features (logo design, CMS integration, AI-powered workflows). Features tell the buyer *what they get*. Outcomes tell them *what changes*. The Pass 1 Value Props defined the "What After" state for each segment. The cards should reflect this.

**What to change — add a one-line outcome above the bullet list on each card:**

- **Brand:** "Your first impression, rebuilt from scratch. Clean identity that makes people take you seriously." → This is already good. Now add below the bullets: *"Most clients go from Canva logo to professional brand in 5 business days."*
- **Web:** "A site that converts, built on your new brand." → Add: *"Fast enough to pass Google's Core Web Vitals. Built to rank locally and turn visitors into calls."*
- **Automation:** "Systems that work while you sleep." → Add: *"Clients typically reclaim 5–10 hours/week of manual follow-up and admin."*

The pattern: Feature list + one concrete outcome statement = much stronger card.

---

### 10. Add a "How This Compares" Anchor (Optional, Lower Priority)

**Strategic basis:** Pass 1 Lean Canvas mapped six competitor categories and why each fails. The value prop analysis showed that both segments compare Kuzln against agencies ($5K+, 6–16 weeks), DIY builders (requires their time), and doing nothing. A subtle comparison — not a competitor-bashing table, but a "what makes us different" statement — addresses the objections before the prospect voices them.

**What to add (optional):**
A strip or small section that addresses the top 3 objections implicitly:

> **Not an agency.** No $10K proposals. No 12-week timelines. Fixed scope, fixed price, every time.
> **Not a DIY builder.** You don't touch a template. We do all the work.
> **Not a subscription trap.** Brand and Web are one-time projects. Automation is month-to-month, cancel anytime.

**Placement:** Below the tier cards or above the Process section. Keep it understated — this isn't a competitor comparison page. It's objection handling disguised as positioning.

---

## Recommended Priority Order

What to do first, given that Jay is a solo operator and the Pass 3 plan already has a full 90-day calendar:

| Priority | Change | Effort | When |
|:---:|---|---|---|
| **1** | Add timelines to service cards | 10 minutes | Today |
| **2** | Make site indexable (Search Console, meta tags, sitemap) | 20 minutes | Today |
| **3** | Replace mailto-only contact with Calendly + intake form | 30 minutes | This week |
| **4** | Add ClawdBot legitimacy anchor (`/clawdbot` or footer section) | 1–2 hours | Before Batch 1 |
| **5** | Add operator/About section | 30 minutes | This week |
| **6** | Rewrite hero subline to be more specific | 15 minutes | This week |
| **7** | Add portfolio/Work section (even with spec pieces) | 3–5 hours | Before Batch 1 |
| **8** | Add outcome language to service cards | 20 minutes | This week |
| **9** | Add testimonial section (activate when first quote arrives) | 1 hour to build shell, 0 min to activate later | Build shell now, activate Week 3+ |
| **10** | Add "How this compares" strip | 1 hour | Month 2 |

**Total estimated effort for priorities 1–6: ~3 hours.** These are all small changes that meaningfully improve the site's ability to convert both services prospects and ClawdBot verification clicks.

**Total estimated effort for priorities 7–9: ~5–6 hours.** These are bigger additions but directly support the Credibility Bridge growth loop and should be in place before ClawdBot Batch 1 sends.

---

## What NOT to Change

The site has real strengths. Protect them:

- **The visual design.** The dark theme, starfield animation, orange accent, and Inter font create a distinctive, premium feel that sets you apart from every generic Wix agency template. Don't dilute this.
- **The tier structure.** "Three tiers. One trajectory." is a strong framing. The cards are clear and scannable. The escalation logic (Brand → Web → Automation) is intuitive. Keep this architecture.
- **The copy tone.** Clean, confident, no fluff. "Real timelines, not agency bloat" is exactly right. Don't add corporate filler or buzzwords.
- **The simplicity.** This is a single-page site and it should stay that way (with the possible exception of a `/clawdbot` route). Don't turn it into a 10-page agency site. The constraint is a feature — it signals that you're focused and efficient, which is exactly the brand promise.

---

*These recommendations are designed to be implemented in hours, not weeks — matching the solo-operator reality from the Pass 3 prioritized plan. The site is already 70% of the way there. The missing 30% is proof (portfolio, testimonials), specificity (who this is for, how fast, what changes), and infrastructure (indexing, contact flow, ClawdBot trust anchor).*
