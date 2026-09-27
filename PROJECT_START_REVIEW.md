# Project start review: evidence, budget, and next batch

**Date:** 27 September 2026 (Asia/Riyadh)
**Scope executed so far:** Section 1 intake and Section 3A evidence review of [the $100 project prompt](CLAUDE_100_DOLLAR_PROJECT_PROMPT.md).
**Status:** **Stopped for a billing check** after the bounded intake, as the prompt requires (§2). Phases B–E have not started. Section 9 locks the proposed next batch so it can be run as soon as budget control is confirmed.

Labels used: **Measured** (recomputed here from retained files), **Documented** (stated in a cited current source), **Interpretation**, **Hypothesis**, **Requires primary research**.

---

## 1. Budget visibility and control

### What was found (checked 27 Sep 2026)

| Question | Finding | Source |
|---|---|---|
| Which model is serving this work? | Configured `claude-opus-5-5`, and the last served model was also `claude-opus-5-5`. | Session metadata (`get_session`: `session_context.model`, `external_metadata.last_served_model`) |
| What kind of credits pay for it? | This is a Claude Code on the web (cloud) session billed against a claude.ai account. Its rate-limit type is `ccr_promotional` with `isUsingOverage: false`. That points to a **promotional cloud-session allowance, not API Console credits or cloud-provider credits**. I cannot see the remaining balance or confirm that it equals $100. | Session metadata |
| Is live cost telemetry available? | **Partly.** The session reports `usage.cost_usd`, which was $0.35 after the first (billing question) turn. It **did not update during this turn**, so it lags by at least one turn. The Claude Code docs say this figure is computed locally from token counts at list price. It is an estimate, not billing. | Session metadata. [Claude Code costs](https://code.claude.com/docs/en/costs) |
| Current list prices (Opus 5.5) | $4/MTok input, $5 (5-min) or $8 (1-hour) cache write, **$0.20/MTok cache read**, $20/MTok output. WebFetch has no surcharge. Web search costs $10 per 1,000 searches. | [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing) |
| Is there a provider-enforced $100 cap I can set? | **No.** I have no access to billing settings, and a natural-language instruction does not enforce a cap. | — |
| What stops spend beyond the credits? | For Pro/Max, **usage credits** (extra usage) let work continue past plan limits and are controlled at **claude.ai → Settings → Usage → Usage credits**. You can switch them off there or set a monthly spend limit. With usage credits off, exhausting the allowance should stop or throttle work instead of billing you. I could not verify your current setting. | [Claude Code costs: usage credits](https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription) |

**What I need from you before Phase B:**

1. Open **claude.ai → Settings → Usage**. Either confirm **Usage credits are off**, or set the **monthly spend limit** to the amount you are willing to risk beyond the promotional allowance.
2. Confirm whether the "$100" is the promotional allowance shown there, or a self-imposed cap on a larger allowance. In the second case, my estimates are the only control, and I will stop at $80 by estimate.
3. Tell me the session cost figure the app shows, if it is visible to you. I will reconcile my estimate against it.

### Budget table

Estimates use Opus 5.5 list prices and approximate token counts: about 20 model calls this turn, context growing from roughly 40k to 175k tokens, about 135k new cached tokens, and about 15k output tokens. They are **not billing records**.

| Phase | Allocation | Observed spend | Estimated spend | Source of number | Cumulative (estimate) | Remaining initial-work budget | Reserve |
|---|---:|---:|---:|---|---:|---:|---:|
| 0. Billing Q&A (turn 1) | — | $0.35 | — | Session `cost_usd` (list-price estimate by Claude Code) | $0.35 | $79.65 | $20 |
| A. Intake and focused evidence review (turn 2) | $10 | $3.03 (reported cumulative $3.38 minus turn 1) | — | Session `cost_usd`, read at start of turn 3 | $3.38 | $76.62 | $20 |
| B. Practical-data feasibility (turn 3) | $25 | not yet reported | $1.5–2.5 | Token estimate at list price plus 9 searches | $4.9–5.9 | $74.1–75.1 | $20 |
| C. R03/R04/R05 provisional artifacts | $25 | — | proposed $8–15 | Plan | — | — | $20 |
| D. Stress tests and corrections | $10 | — | proposed $2–5 | Plan | — | — | $20 |
| E. Synthesis, validation, and handoff | $10 | — | proposed $2–5 | Plan | — | — | $20 |

Reconciliation rule: at the start of each phase I will read the session cost again, replace the estimate for the previous phase with the reported figure where it is available, and stop if cumulative spend (reported, or estimated if higher) is within $5 of $80.

---

## 2. Working summary of the project (for reuse without rereading)

| Topic | Current position | Where |
|---|---|---|
| Product | Help someone choose a worthwhile outing that fits location, time window, constraints, and intent, across venues, activities, and dated occurrences. Discovery comes before planning. | v0.1 §1. v0.2 §1–3 |
| First user (unvalidated) | A resident arranging a same-day or weekend outing for 1–4 others. Domestic visitors are secondary. | R00 §6, "Recommended First User Hypothesis" |
| Candidate promises | A: "feasible outing tonight". B: "something new locally this weekend". C–E are variants. | R00 §23 |
| Content scope | Cultural venues and exhibitions, repeatable indoor activities, selected dated events and workshops, and a small curated set of local stops. Defer restaurants, malls, hiking, and live availability. | R00 §24 |
| Domain concepts | Site/branch, operator, offering, occurrence/session, geometry, availability claim, collection, discovery item. | v0.2 §5 |
| Rights | FSQ OS (Apache-2.0) and Overture (CDLA/Apache/CC0 per row) are open identity layers. Google, webook, and operator pages are **not** corpus sources without agreement. OSM joins need legal review. Practical facts should come from operator permission or feeds. | R01 §8, §11, §13–14, §21–22, §34 |
| Operating model | Automation-first, query-time enrichment, explicit unknowns, humans for exceptions and curation. No routine manual verification of hundreds of records. | R01.2 §3–7, §25 |
| Measured audit | 13,764 Overture records and 1,379 category-selected candidates in 4 rectangles. No practical fields in schema. The 0.8 confidence cutoff removes 68.2% of the pool. OSM: 26 of 353 Eastern elements have hours. Routing failed on TLS. Public pages show conflicts and branch mix-ups. | R02 §5–13 |
| Claim levels | Discovery lead, then feasibility-supported candidate, then booking-confirmed option. Per hard constraint the state is supported, contradicted, unknown, or conflict. | R02 §14 |
| Next dependency | One lawful, repeatable practical-data path, applied to fixed cases, followed by observing remaining user checks. | R02 §15, §27, conclusion |
| Research ladder | R00 users, R01 rights, R02 coverage, R03 identity, R04 trust, R05 intent/eval, R06 retrieval, R07 ranking, R08 travel, R09 field test, R10 planning. | R01.2 §24 |

---

## 3. Corrections between documents

### Explicit corrections (the later document says so)

| Original | Corrected by | Correction |
|---|---|---|
| v0.1's eight peer object types | v0.2 §5, §23 | Replaced by site, operator, offering, occurrence, geometry, and collection. |
| v0.1 research numbering R01–R08 | v0.2 §22, then R01.2 §24 | Revised ladder R00–R10. |
| v0.1 ranking with freshness applied after diversification | v0.2 §7, §9 | A feasibility gate comes before ranking. |
| R01 §28 manual-verification cost scenario (SAR 2,333–7,000/month) as an operating model | R01.2 §1, §31 | Retained only as a stress case. |
| R01.2 §22 "Automation Coverage Ratio" | R02 §14 | Replaced by several measures reported together with fixed denominators, because the ratio can be gamed and is undefined without ground truth. |
| Earlier expectation of an Overture `categories` column | R02 §22 | The actual release uses `taxonomy` and `basic_category`. |

### Unresolved disagreements (not reconciled by any document)

1. **Where practical facts come from under Model B.** R01 §14/§30 makes operator permission the practical-data path. R01.2 §6/§14 assumes query-time refresh "from permitted sources" at scale. R02 §23 notes that reading a page does not create a right to retrieve it repeatedly. If permission must be negotiated operator by operator, Model B carries a small version of Model A's partnership burden. No document settles whether transient, per-query retrieval of public operator pages with a link back is acceptable. **This is the central open question for Phase B.**
2. **Human verification for evaluation vs. operation.** R00 §34 and R01 §38 ask R02 to count verified usable choices and time manual verification. R01.2 rejects manual verification as a prerequisite, and R02 measured none. These are compatible only if one-off **evaluation labeling**, which is still needed for ground truth, is kept separate from **operational maintenance**. That distinction is not written down anywhere. I propose to adopt it.
3. **Which open baseline.** R01 prefers FSQ OS Places as the primary identity layer. R02 tested only Overture; direct FSQ OS access needs a portal account. Overture's embedded Foursquare rows are not a test of FSQ OS (R02 §15). This is a gap, not a contradiction.
4. **Global thesis vs. local evidence.** R01.2 §28 frames a global "discovery intelligence layer". All evidence is from four Saudi rectangles on one date. R02 §24 already says so. The global framing remains an unevidenced aspiration and should not drive current decisions.

---

## 4. Evidence re-check

### Checks performed

| Check | Method | Result |
|---|---|---|
| R02 validator | `python R02_evidence/validate_audit.py` | `checks_pass: true`. All 4 raw-file SHA-256 hashes match, row counts match, 13,764 total, 1,379 candidates, 438 screened = 438 CSV rows, no missing local links, sections 1–29. |
| Evidence integrity | `git diff` after the validator run | The validator **rewrites** `audit_validation.json`. The only change was CRLF→LF line endings with identical content. I restored the committed file, so no evidence file is modified. |
| Independent recount | New script over the raw JSON (not the R02 helpers) | Confirmed 13,764 unique IDs. Pools are E 1,056, D 44, J 84, B 195. 438 records have confidence ≥0.8. All 1,916 Foursquare-origin records have confidence 0.77. 327 of them are in the pool. All pool records lack operating status. |
| Cause of the 0.8 cutoff loss | Removed records broken down by upstream source | Of the 941 pool records removed, **614 are Meta-origin and 327 Foursquare-origin**. In the **culture** family, 181 of 190 removed records are Meta-origin. |
| Same-name duplicates | Exact normalized-name pairs within 100 m across the **full 1,379 pool** (R02 only tested the 438) | **0** same-name pairs, while **1,387** candidate pairs lie within 100 m and 166 within 15 m. |
| SAMoCA/JAX absence | Wider Arabic/English pattern search across all four raw files | No SAMoCA or JAX record matched. This is consistent with R02 §9 and still not proof of absence. |

**What these checks establish:** the retained evidence is **internally consistent**, and R02's headline numbers reproduce from the raw files with independent code. They do **not** independently validate that any venue exists, is correctly placed, or is open. No ground-truth comparison was made.

### Where R02 is right but could be read too strongly

- **"Automated place acquisition works."** True for retrieval. The recount shows many co-located candidates (1,387 pairs within 100 m) and zero identical-name pairs. Duplicate and branch risk is therefore about name variants and cross-language names, which the simple test cannot see. Usable distinct-venue density remains unknown (R02 §6 says so).
- **Discovery "leads" are achievable.** Only with identity plausibility. Low-confidence Meta-origin rows make up most of the cultural records the cutoff removed. Some may be genuine and some may be noise. Nobody has inspected a sample.

### Where R02 could be read too pessimistically

- **"0/1,379 practical completeness"** is true **by construction**: the Overture schema has no such columns (R02 §7, §13). It is a schema fact, not an observed failure rate. It says nothing about whether enrichment would work.
- **The 0.8 cutoff story.** The cutoff does remove all Foursquare rows, but Foursquare explains only 35% of the loss. The larger effect, and nearly all of the cultural loss, comes from Meta-origin rows below 0.8. The finding that no global threshold should be used stands. The emphasis should shift from "Foursquare is penalised" to "confidence needs source- and category-specific calibration against ground truth".
- **No travel times.** Every failure was an expired-certificate error on community demo servers in the research environment (`route_results.json`). This is evidence about that environment, not about routing feasibility. *Interpretation:* travel time is probably a lower-risk dependency than practical facts, but it remains unmeasured.
- **OSM "almost four months old."** The 31 May timestamp is the **mirror's** replication state. It says the mirror was stale, not how fresh OSM itself is. R02 §10 frames this correctly. Finding 6 in R02's "Most important findings" is easier to misread.

---

## 5. Strongest supported findings

1. **Measured:** open identity data for the sampled areas can be retrieved automatically and reproducibly. It is dominated by cafés (77.7% of the pool) and carries no practical fields (R02 §6–7; recount above).
2. **Measured:** source confidence is not a usable eligibility score. It is constant within one source and uncalibrated across sources (R02 §8; recount above).
3. **Observed page evidence (R02 §11–12):** first-party pages hold the decision-critical facts, including date exceptions, per-offering prices, duration, and group size. They also contain conflicts (Diriyah), expired exceptions (Scitech), and branch mix-ups (Escape The Room). Scope, date validity, and conflict state must be preserved through any parser.
4. **Documented (R01 §13–14, R02 §23):** public operator and ticketing pages are not reusable data without permission. Ithra's site terms bar reproduction, and webook's terms bar automated collection.
5. **Not established by any document:** user demand, frequency of the decision, whether a qualified shortlist reduces checking, maintenance cost, travel times, and launch geography.

---

## 6. Five most consequential unresolved assumptions

Ranked first by impact on the product decision, then by how cheaply better evidence can be obtained.

| Rank | Assumption | Impact if false | Cost of better evidence | Who can obtain it |
|---:|---|---|---|---|
| 1 | **A lawful, repeatable practical-data path exists** for hours (with date exceptions), price unit, duration, and booking/group rules, for enough candidates in one compact area. | The product falls back from feasibility (Level 2) to discovery (Level 1), which is close to a directory. | **Low–moderate.** A desk rights check and a bounded retrieval test are agent work (Phase B). The permission itself needs you or an operator. | Agent, then you |
| 2 | **A qualified shortlist reduces the user's remaining checks** compared with their current tools, especially Google Maps/Search (R00 H2). | There is no product advantage even if the data works. | **High.** Needs 12–20 observed sessions (R00 §28). | Real users |
| 3 | **Residents face this decision often enough** to return (R00 H1, §21–22). | The product is only episodic, or niche. | **High.** Needs a 4-week recall or diary study. | Real users |
| 4 | **Identity quality is adequate in a compact area**: branches, duplicates, and recall of anchors. | Wrong-branch facts or missing anchors cause false feasibility. | **Low–moderate.** Label about 50 records against first-party branch directories. | Agent, with your judgment on ground truth |
| 5 | **Permitted travel-time estimates are good enough** for 15-minute and 90-minute constraints. | Tight-window promises fail. Discovery without a travel ceiling still works. | **Low**, but needs a keyed API account (Mapbox/Google/HERE free tiers). | You (account), then agent |

Maintenance and exception cost (R01.2 Gate D) is folded into assumption 1 ("repeatable"). It can only be measured over weeks, not in one session.

---

## 7. Narrowest credible first product promise

**Proposed (hypothesis):**

> For one chosen area and time window, show two or three *different* cultural or indoor-activity options that plausibly fit. For each, say which decision-critical facts are supported by a named, dated official source, which are unknown or conflicting, and exactly what the user must still check, with a direct link.

This sits between R02's claim levels: a **qualified discovery shortlist** with feasibility facts where supported. It is not a directory, because every result carries its known/unknown/conflict state per hard constraint. It is not a concierge, because nothing is confirmed by staff and no routine manual verification is involved.

| | Qualified discovery shortlist (proposed) | Confirmed feasibility (R01.2 Level 2 / R02 "feasibility-supported") |
|---|---|---|
| Claim | "Plausible, with these facts supported and these unknown." | "Fits your time, budget, and group, on stated evidence." |
| Data needed | Open identity, plus whatever permitted practical facts exist, with links for the rest. | Permitted hours, duration, price, and booking rules, plus routing, for each result. |
| Evidence today | Identity: yes. Practical facts: observed on pages, retrieval rights unresolved. | Not demonstrated (R02 Gates B–C). |
| Risk | Collapses into a directory if almost every fact is "unknown". | Unsupported claims cause false feasibility, the most damaging error (R00 §9). |

**What would falsify the shortlist promise:**

- **(a)** Across the locked cases (§9), fewer than about half of surfaced candidates have *any* case-relevant hard constraint supported by a lawful source. Every card would say "check everything". The threshold is proposed here and is not yet a decision.
  - *Correction (27 Sep, after Phase B):* this test is too weak, because category-level constraints are trivially supported. Count practical hard constraints only. See [R02.1 §8](R02_1_Practical_Data_Feasibility_Followup.md#8-consequences).
- **(b)** In observed sessions, remaining checks per chosen outing and time to decision are no better than the participant's usual method.
- **(c)** Independent checks find supported-but-contradicted facts at a rate users will not tolerate.
- **(d)** Google Maps or Search answers the same cases with the same or fewer remaining checks.

---

## 8. What this review changes

- Keep the R01.2 correction. Nothing here reintroduces routine manual verification. The one exception is proposed one-off evaluation labeling, kept separate from operations (§3, item 2).
- Add to R04 (when written): confidence cutoffs must be calibrated per source and per family. The largest cultural loss comes from Meta-origin rows, not Foursquare.
- The most useful next step is not more data. It is resolving whether practical facts can be obtained lawfully and repeatably for two operators (Phase B).

---

## 9. Proposed next batch (Phase B), locked before any answers are examined

### Test area and operators

- **Area:** the Khobar–Dhahran part of R02 rectangle E. It holds R02's richest evidence and all three anchor operators below. Fixed synthetic origin: **lon 50.200, lat 26.300**, the same origin as `R02_evidence/route_results.json`. This is not a user location.
- **Cultural operator: Scitech (Al Khobar).** The Overture record has confidence ≈0.99 and a website. R02 found readable first-party hours (including a dated exception) and per-offering prices (halls, IMAX, combined) on scitech.sa. It is Arabic-first, which tests multilingual extraction. It exercises the exception-validity problem directly.
- **Repeatable indoor activity: Escape The Room, Khobar branch.** The Overture record links to the operator domain. Room pages expose player count and duration, which are exactly the group and duration fields. The known Riyadh/Khobar branch mix-up makes it an honest test of branch resolution.
- **Contrast cases, desk-only unless rights are clear:** Ithra (direct fetch returned 403, and site terms bar reproduction), representing a rights-blocked path; and Sparky's (a branch-hours directory), as the fallback activity operator.

### Method

1. **Rights and access desk check** for each operator: site terms, robots.txt, and any feed, API, ICS, or JSON-LD. Record URLs and check dates. No accounts, contacts, or purchases.
2. **Bounded retrieval**, only where terms and robots do not prohibit it: at most 6 page fetches per operator per session. Record timestamps, source URL, applicable dates, branch identity, and failures. Keep raw responses in scratch storage only and commit hashes plus field-level research observations. Do a second pass in a later session if you approve; two fetches in one session do not prove freshness.
3. **Evaluate the 12 locked cases** below against the Overture E extract plus whatever phase-B sources yielded. For every candidate and every hard constraint, record supported, contradicted, unknown, or conflict. For every case, record the outcome class.
4. **Prepare the permission request** you could send to each operator (fields, format, cadence, display, retention). I will not send it.

**Outcome classes (kept separate, never merged into one rate):** no candidates · missing facts · source-access failure · rights uncertainty · genuine constraint violation · supported qualified shortlist. The denominator is all 12 cases.

**Time anchors:** D0 is the Asia/Riyadh date on which Phase B runs. "Tonight" means D0 18:00–23:00. "This weekend" means the next Friday–Saturday after D0. "Thursday" means the next Thursday after D0.

### Locked outing cases

Sources: R00 §25 query IDs and R02 §13 case IDs. The wording is adapted to area E. These are analyst-authored cases, not user quotes.

| ID | Case (area E, origin above) | From | Dimensions exercised |
|---|---|---|---|
| C01 | "A museum near Khobar tonight, under 50 SAR each." | R02 Q01 | tonight, budget, culture |
| C02 | "Four of us, something active indoors tonight, under 150 SAR each." | R02 Q02; R00 012/016/031 | tonight, group 4, budget, indoor |
| C03 | "Got 90 minutes before dinner at 19:30 back at the origin, something cultural." | R02 Q03; R00 021 | 90-minute gap, duration, travel |
| C04 | "Four of us want an escape room tonight without booking ahead." | R00 014/017; R02 Q14 variant | negative constraint (no booking), group |
| C05 | "Family with kids aged 6 and 9, indoors this weekend, under 300 SAR total." | R00 051/052 | weekend, ages, total-price unit |
| C06 | "Something to do this weekend that isn't food and isn't the mall." | R00 005/010 | weekend, two negative constraints |
| C07 | "Any exhibition still running this weekend around Dhahran?" | R00 042/050; R02 Q12 | occurrence dates |
| C08 | "Solo, about an hour, a quiet indoor cultural stop after 21:00 tonight." | R00 072/078 | late hours, duration, soft mood |
| C09 | "Two of us, a workshop we can join this Thursday evening." | R00 045 | occurrence plus registration |
| C10 | "Somewhere new to me in Khobar this weekend, not a café." | R00 082; R02 Q04 | novelty (untestable without history), negative |
| C11 | "Wheelchair-accessible museum open this Saturday." | R00 054 | accessibility evidence (unknown must not pass) |
| C12 | "Starting 18:30 tonight, something we can finish by 20:00 within a 15-minute drive." | R00 028/030 | travel ceiling (no routing source, so expect unknown) |

Coverage: tonight (C01–C04, C08, C12), weekend (C05–C07, C10, C11), 90-minute gap (C03), group size (C02, C04, C05, C09), budget (C01, C02, C05), indoor (C02, C05, C08), negative constraint (C04, C06, C10). Cases C09–C11 are expected to test "no candidates" and "missing facts" honestly.

### Phase B budget and stop conditions

- Ceiling $25; my expectation is **$6–15**.
- Stop retrieval from an operator after one failure plus one justified retry.
- Stop the phase at an estimated $20, or once all 12 cases have outcomes.
- If rights prohibit automated retrieval, record that and complete the cases desk-only. **That result is itself the answer to assumption 1** and changes the promise (§7).

Phase C (R03–R05) follows only after the Phase B result, per the prompt's priority order.

---

## 10. Interim handoff (full version due at the end of Phase E)

1. **Decisions supported now:** keep the automation-first model (R01.2). Do not use a global confidence threshold (R02 §8, recount). Keep open identity separate from practical facts (R02 §22). Test one compact area rather than choosing a launch city (R02 §19).
2. **Hypotheses to test:** the §6 assumptions 1–5. The §7 promise and what would falsify it.
3. **Not established, and why:** user demand, frequency, and checking burden (no participants); practical-data rights (no permission requested); travel times (environment TLS failure, no keyed provider); maintenance cost (no operation over time).
4. **Next experiment:** Phase B as specified in §9.
5. **R06 retrieval architecture:** **not yet.** It depends on R05 labels and on the Phase B result for which fields exist.
6. **Application implementation:** **not justified.** The binding uncertainties are data rights and user value, which code would not resolve.
7. **Next five actions, in order:**
   1. **You:** confirm budget control (§1).
   2. **Agent:** Phase B.
   3. **You:** decide whether to send the operator permission requests Phase B prepares.
   4. **Real users:** run the R00 observation sessions using the §9 cases as vignettes.
   5. **Agent:** R03–R05 on the Phase B evidence.
8. **Files, checks, spend:** created this file and linked it from README. Checks as in §4. Spend is in §1: about $2.5–4.5 estimated, cumulative. The $20 reserve is untouched.
