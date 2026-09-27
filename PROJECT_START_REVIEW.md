# Project start review: evidence, budget, and next batch

**Date:** 27 September 2026 (Asia/Riyadh)
**Scope executed:** all of Sections 1 and 3A–D of [the $100 project prompt](CLAUDE_100_DOLLAR_PROJECT_PROMPT.md).
**Status (revised 27 Sep, evening):** Documents delivered: this review, R02.1, R03–R05 and later R06. **Experiments actually executed:** the intake re-check, and a Phase B run that was blocked by the network. Its planned repeated first-party retrieval was **not** executed. Direct retrieval was later performed by another researcher (Sol) in [R02.2](R02_2_Source_Access_Recovery_and_Review.md), on one date only. Observations on different dates, operator permission and user sessions have **not** been executed. See §12. The $20 reserve is untouched.

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

**What I needed before Phase B.** *Update 27 Sep:* you replied that about $2 had been used and asked me to proceed. The Usage-credits setting (item 1) was not explicitly confirmed, so it remains your control to check.

1. Open **claude.ai → Settings → Usage**. Either confirm **Usage credits are off**, or set the **monthly spend limit** to the amount you are willing to risk beyond the promotional allowance.
2. Confirm whether the "$100" is the promotional allowance shown there, or a self-imposed cap on a larger allowance. In the second case, my estimates are the only control, and I will stop at $80 by estimate.
3. Tell me the session cost figure the app shows, if it is visible to you. I will reconcile my estimate against it.

### Budget table

Estimates use Opus 5.5 list prices and approximate token counts: about 20 model calls this turn, context growing from roughly 40k to 175k tokens, about 135k new cached tokens, and about 15k output tokens. They are **not billing records**.

| Phase | Allocation | Observed spend | Estimated spend | Source of number | Cumulative (estimate) | Remaining initial-work budget | Reserve |
|---|---:|---:|---:|---|---:|---:|---:|
| 0. Billing Q&A (turn 1) | — | $0.35 | — | Session `cost_usd` (list-price estimate by Claude Code) | $0.35 | $79.65 | $20 |
| A. Intake and focused evidence review (turn 2) | $10 | $3.03 (reported cumulative $3.38 minus turn 1) | — | Session `cost_usd`, read at start of turn 3 | $3.38 | $76.62 | $20 |
| B–E. Practical data, R03–R05, stress tests, synthesis (turn 3) | $70 combined | not yet reported (telemetry lags a turn) | $4–6 | Token estimate: about 60 calls at about 230k average cached context ($0.20/MTok read), about 120k cache writes, about 55k output, 9 searches | $7.4–9.4 | $70.6–72.6 | $20 |

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

## 10. Stress tests and contradiction review (Phase D)

### Model stress tests

Each case from the prompt was run against [R03](R03_Domain_and_Identity_Model.md) and [R04](R04_Trust_and_Freshness_Policy.md).

| Stress case | Evidence used | Handled by | Result |
|---|---|---|---|
| Separate nearby chain branches | Two Escape The Room Khobar records 9 km apart (R02.1 §6) | R03 §5 cannot-merge, and `undecided` blocks fact flow | **Holds.** Facts from `/rooms/…-khobar/` attach only to the branch concept. The second record stays undecided and gets no hours or travel claims. |
| Venue hours vs activity slots | Scitech hours vs IMAX showtimes; escape room "open" vs a slot for four | R03 offering and occurrence; R04 §4 (no-booking and group are blocking) | **Holds.** C04 is omitted, not shown as "open tonight". |
| Exception hours outside their valid date | Scitech National Day 23–24 Sep; Diriyah free access ends 30 Sep | R04 §7 | **Holds.** Exceptions are ignored outside their interval. |
| Event cancellation | No cancellation source exists (R01 §18, R02.1) | R04 §7, §10 | **Holds conceptually** ("status as of <time>"). **No data path exists**, so occurrence cases stay blocked. |
| Ambiguous price unit | Scitech adult/child/"group 5+" per-person prices; "under 300 total" with unknown adults | R04 §4 at first **(gap found)** | **Gap.** Price claims had no unit or conditions. Fixed: added [R04 §6a](R04_Trust_and_Freshness_Policy.md#6a-price-claims-added-after-the-stress-test-in-project_start_review-11). |
| Unknown group availability | Escape The Room group 2–6, but no slot evidence | R04 §4 (blocking) | **Holds.** Capacity is never inferred from group-size rules. |
| Missing accessibility evidence | Ithra centre-level statement (E4); Scitech unknown | R03 §4 containment; R04 §4, §6 | **Holds.** The centre-level claim is inherited only as qualified, and the need stays blocking. |
| Same fact copied by several websites | Index summaries repeating operator figures; one produced a conflicting IMAX price | R04 §5 **(gap found)** | **Gap.** The rule did not say what to do when lineage cannot be established. Fixed: unknown lineage counts as the same lineage. |

### Contradictions found across the artifacts, and how they were handled

1. **R02.1 "supported (weak)" vs R04 tier E4.** Resolved in R04's favour. [R02.1 §8 reconciliation](R02_1_Practical_Data_Feasibility_Followup.md#8-consequences): 0 of 24 practical constraints are supported for product claims. The original tables are kept.
2. **§7 falsifier (a) too weak.** Annotated in place (§7), pointing to R02.1 §8.
3. **§9 promised raw captures with hashes.** This was impossible because of the egress block. Recorded in R02.1 §3 and §9. No substitute data was presented as a capture.
4. **R02's "154 culture/heritage" in E vs R02.1's plausibility judgments.** R02.1 §6 records the overstatement (81 of 85 nearby `historic_site` implausible). R02 is not rewritten.
5. **§6 assumption 4 ("identity adequate") now has evidence against it** for anchor operators (R02.1 §6). See §11.2.

No contradiction was found between R03, R04 and R05 after the two R04 fixes. The residual unsupported-claim risk is the analyst name judgments (single annotator, non-native for Arabic), which are labeled wherever used.

---

## 11. Final handoff

### 11.1 Decisions supported now, with evidence

| Decision | Evidence |
|---|---|
| Keep automation-first; no routine manual verification | R01.2 §3, §31. Nothing in R02 or R02.1 argues otherwise. |
| No global confidence threshold; calibrate by source and family | R02 §8. Recount §4: 614 of 941 removals are Meta-origin. |
| Keep identity acquisition separate from practical-fact acquisition | R02 §22. R02.1 §5–6. |
| **Search-index or LLM summaries are never a product evidence source** | R02.1 §5: IMAX price conflict. R04 §2 tier E4. |
| Identity cleanup of anchor operators **before** attaching practical facts | R02.1 §6: Scitech records up to 4 km apart, Ithra and Escape The Room duplicates |
| Culture candidate generation must not rely on `historic_site` in this area | R02.1 §6: 81 of 85 implausible (analyst judgment) |
| Unknown ≠ false ≠ true; blocking vs qualifiable per constraint | R02 §14, R04 §3–4, stress tests §10 |
| Use R03's site / offering / occurrence / containment model for any future data work | R03, stress tests §10 |

### 11.2 Hypotheses worth testing, and what would overturn them

| Hypothesis | Overturned if |
|---|---|
| *[27 Sep, R02.2: based on name screening only; it does not measure supply or demand share.]* **H-a. Culture in a compact area is operator-concentrated,** so 2–3 operator agreements cover most cultural decisions (R02.1 §6) | Ground-truth labeling finds many real cultural venues missing from the open data, or the plausible set is larger than about six destinations |
| **H-b. Operators will permit fact retrieval or supply a simple feed** | Both drafted requests (R02.1 §9) are declined or unanswered after a reasonable follow-up |
| **H-c. A qualified shortlist reduces remaining checks** vs participants' usual tools (R00 H2) | In observed sessions, checks per chosen outing and time to decision are not lower than the usual method, or Google Maps matches it |
| **H-d. Residents face this decision often enough** (R00 H1) | A 4-week recall shows rare hard decisions or strong defaults |
| **H-e. Activities need a booking-system path** for price, sessions and capacity, while culture can work from published operator facts | Activity operators publish price, hours and slots in retrievable form, or cultural operators turn out not to |

### 11.3 What could not be established, and why

| Item | Reason |
|---|---|
| Live or repeat first-party retrieval, freshness, latency | Environment egress policy blocked all operator domains (R02.1 §3) |
| Permission to retrieve, retain or display for Scitech and Escape The Room | No terms found; robots.txt unreadable; operators not contacted (not authorised) |
| Escape The Room price, hours and slots; Scitech duration, last entry and accessibility | Not in any accessible source |
| Travel times | No permitted routing account; R02's demo servers failed on TLS |
| Correct locations of anchors | No ground truth; records conflict |
| User value, frequency, remaining checks | No participants (primary research) |
| Maintenance and exception cost | Requires an operating period, not a one-session test |

### 11.4 Precise next experiment

**"Two-operator feasibility plus eight-person decision test", Khobar–Dhahran.**

- **Users:** 8 residents who arranged a same-day or weekend outing in the past month, per the R00 §29 profile mix (at least 3 group organisers, 2 families, 1 solo/couple, 2 default-choosers). Directional, not representative.
- **Area:** within about 12 km of the fixed origin (R02.1). Replace the origin with each participant's broad starting area.
- **Categories:** culture (Scitech, the Ithra complex, plus about four other plausible venues) and indoor activity (escape rooms, bowling, one play centre).
- **Inputs:**
  - E2/E3 facts for Scitech and Escape The Room: permission, plus an allowlisted retrieval repeated on 3 dates, including one weekend.
  - The R05 fixed cases, used as vignettes.
  - A routing free tier for 20 origin–destination pairs.
- **Measurements:**
  - Per practical constraint, the share supported at E1–E3 (target denominator: the 24 R02.1 constraints, re-evaluated).
  - Retrieval failures and changes between dates.
  - Per participant task: checks made with their own tools, then with a static evidence card for the same case. Record remaining checks, time to a confident choice, choices made, and any false-feasibility observed.
- **Proposed acceptance criteria** (for your judgment, not fixed):
  - At least half of the practical constraints are supported at E1–E3 for the cultural cases.
  - Zero false-feasibility claims.
  - Median remaining checks with the card lower than with own tools for at least 5 of 8 participants.
- **Cost dependencies:** agent time (roughly $5–10 at list price); a routing free tier ($0); participant incentives (unpriced, your decision); no data purchases.
- **Stop conditions:**
  - Both operators decline, or can't be reached after one follow-up: stop the data arm and reassess promise level (§7).
  - Fewer than 5 participants recruitable: run as a pilot and report as such.
  - Any false-feasibility claim: halt card use until the cause is fixed.

### 11.5 Can R06 (retrieval architecture) proceed?

**Only in a narrow, provisional form.**
- **Can proceed now:** comparing candidate-generation rules on the retained extract. Examples: dropping or reclassifying `historic_site`, name-based rescue of misclassified venues (Bujairi, muvi), and containment extraction for "not the mall". Label about 200 records first (R03 §7).
- **Must stay provisional:** any retrieval over practical facts, semantic/vector search (no labeled benefit), engine choice, and ranking (R07).

### 11.6 Is application implementation justified?

**No.**
- The binding uncertainties are data permission (H-b), user benefit (H-c) and frequency (H-d). Software cannot resolve any of them.
- R02.1 shows that under R04 no result today could carry a single supported practical fact.
- A static evidence card for the §11.4 sessions can be produced as a document. That is not an application.
- Revisit this once §11.4's acceptance criteria are met.

### 11.7 Next five actions, in order

1. **You (judgment, permission):** decide whether to send the two permission requests in [R02.1 §9](R02_1_Practical_Data_Feasibility_Followup.md#9-what-remains-unresolved-and-what-would-resolve-it). Adapt the sender identity. I have not contacted anyone.
2. **You (account and settings access):** add the four operator domains to this environment's allowed network domains (environment settings → Network access), and optionally create a free routing account.
3. **Agent:** rerun Phase B as E2 retrieval on 3 dates, fix the Scitech and Escape The Room identity with labeled evidence, and label about 200 candidate records for R03/R06.
4. **Real users:** recruit and run the 8-person sessions (§11.4) using R00 §28–32 materials and R05 cases as vignettes.
5. **Agent plus your judgment:** re-evaluate the promise (§7) against the acceptance criteria, then decide whether R06/R08 work is warranted.

### 11.8 Files, checks, spending, reserve

**Files created:**
- `PROJECT_START_REVIEW.md`
- `R02_1_Practical_Data_Feasibility_Followup.md`
- `R02_1_evidence/`: `case_pools.py`, `case_pools.json`, `culture_name_judgments.json`, `source_observations.json`, `request_log.json`, `case_outcomes.json`, `check_phase_b.py`
- `R03_Domain_and_Identity_Model.md`
- `R04_Trust_and_Freshness_Policy.md`
- `R05_Query_Intent_and_Evaluation_Seed.md`

README links were updated. No existing report or evidence file was modified; `audit_validation.json` was restored after each validator run.

**Checks:**
- `R02_evidence/validate_audit.py` → `checks_pass: true`.
- An independent recount of R02 figures (§4).
- `R02_1_evidence/check_phase_b.py` → `checks_pass: true` (12 cases, valid classes, shortlist cases fully supported, practical tally 8 of 24 before the R04 reconciliation).
- The eight stress tests in §10.

**Spending:** reported $3.38 through turn 2, plus an estimated $4–6 for turn 3. **Estimated cumulative total: $7.4–9.4**, against the $80 initial-work ceiling. Reconcile against the session cost figure at your next message. **The $20 reserve is untouched**, and about $70 of the initial allocation is unused by design.

---

## 12. Follow-up, 27 Sep (evening), after R02.2

**Source of new evidence:** [R02.2](R02_2_Source_Access_Recovery_and_Review.md), by another researcher (Sol), on branch `codex/source-access-followup` at commit `276c418`. It was fast-forwarded into this branch with no conflicts; this branch had no newer work. Sol's observations are **transferred evidence**: this agent's network is still blocked (`api.escapetheroomsa.com` gave no connection at 16:56 UTC). Full operator bodies are kept outside the repository by Sol and were not seen here.

### 12.1 What changed because of the new evidence

| Before (R02.1 / R03–R05 v0.1) | Now |
|---|---|
| No activity price, hours or slot path found | Escape The Room publishes a branch → room → party/date **slot-quote path** through its public site (technical access only; no reuse grant) |
| Khobar room URLs resolve branch ambiguity | **Wrong.** The old URL serves the homepage app shell. There are **two Khobar branches** (operator IDs 1 and 3). Overture `b4fdc657…` is 2.3 m from branch 1's point (provisional link). `8a251b82…` stays undecided. |
| The IMAX price conflict came from search summaries | The Scitech page **itself** conflicts: body 20/25/45 vs metadata 23/28.75/46. The AR and EN exception end-times also differ. No ordinary Sunday hours were observed. |
| "About six cultural destinations; 2–3 operators cover most" | A name-screening result and a hypothesis, not a measurement (notes added to R02.1 and §11.2) |
| Travel unmeasured | Two OSRM demo routes measured: 149 s out, 196.9 s back (model output, non-commercial demo) |
| R04 v0.1 single tier ladder; "qualifiable" unknowns; blanket legal lines | [R04 v0.2](R04_Trust_and_Freshness_Policy.md#12-change-log): authority × channel × scope × valid time × rights × publication. Unknown hard constraints are never satisfied. Strict "under". Representation-conflict and app-shell rules. Source-specific rights findings plus labeled project policy. |
| R03 "source records immutable"; containment inheritance | [R03 v0.2](R03_Domain_and_Identity_Model.md#8-change-log): retention subject to rights (tombstones); operator branch and room IDs; containment is not inheritance |
| R05 "under 150" = ≤150; default origins | [R05 v0.2](R05_Query_Intent_and_Evaluation_Seed.md#6-change-log): strict "under"; origins never invented; three separate outcome columns |

### 12.2 Corrected case outcomes

These come from the [v2 pass](R02_1_evidence/case_outcomes_v2_2026-09-27.json); the original [v1](R02_1_evidence/case_outcomes.json) is kept unchanged, verified by hash. Run `python R02_1_evidence/check_case_pass_v2.py` to check it.

| Case | Research support (key constraints) | Publication | Query satisfied? | vs R02.1 |
|---|---|---|---|---|
| C01 | Price < 50: supported for this threshold (both 20 and 23 below). Sunday hours: **unknown** | Not eligible | **No** (hours) | Was "supported shortlist" (index): **downgraded** |
| C02 | Group 4 ✓, 60 min ✓, derived SAR 96 each < 150 ✓, 18:15 slot available **as of 12:01 UTC** | Not eligible | **At observation time only**, as a historical quote | Was missing facts: **upgraded, time-bounded** |
| C03 | Cultural duration, hours and travel unknown | — | No | Unchanged |
| C04 | Slot quote ✓; "no advance booking" **unknown, blocking** (the FAQ recommends booking) | Not eligible | No (walk-in reading); ambiguity if same-day booking is acceptable | Refined |
| C05 | Party count missing; room 1 age fields 8–80 (meaning unverified); Scitech child age band unknown | — | No | Refined |
| C06 | Containment and weekend hours unknown | — | No | Unchanged |
| C07 | Ithra timed out in Sol's environment too | — | No (access failure, not "no exhibitions") | Unchanged |
| C08 | Hours and last entry unknown | — | No | Unchanged |
| C09 | No occurrence inventory | — | No | Unchanged |
| C10 | Needs user history | — | No | Unchanged |
| C11 | R02.1's Ithra statement was a search summary: now inadmissible | — | No | **Downgraded** |
| C12 | Drive ≤15 min: model estimate only. Room 1 sessions **contradict** the 18:30–20:00 window (18:15 too early; 19:30–20:30 too late) | — | **No, known failure for room 1 only**; other venues unevaluated | Was missing facts: **known failure** |

**No aggregate success rate is given.** Research support, publication eligibility and query satisfaction are different outcomes. Remaining unknowns concentrate on Scitech's ordinary hours, cultural visit duration, current (not historical) availability, occurrences, containment, accessibility and user context.

### 12.3 Offline checks performed

| Check | Result | Does not prove |
|---|---|---|
| `R02_evidence/validate_audit.py` | Pass (file restored after run) | Real-world truth |
| `R02_1_evidence/check_phase_b.py` | Pass: validates the **historical v1** structure only | That v1 matches R04 v0.2 (it does not; see v2) |
| `R02_1_evidence/check_case_pass_v2.py` | Pass: v1 unchanged, 12 cases, evidence IDs exist in R02.2 manifests, no satisfaction without full support, no publication claimed | That Sol's observations are true now |
| `R06_research_harness/check_harness.py` | 23/23 (12 real-transferred, 11 synthetic), plus 2 mutation sanity runs that each fail as expected | User value, current availability, rights, licensed integration, recall |

Sol's `summarize_checks.py` needs private local bodies that are not in the repository, so it cannot be re-run here. This is as R02.2 states.

### 12.4 Does the first promise need narrowing?

**Yes, in one direction.**
- The only research-supported fit so far is a **bookable activity with a party/date quote** (C02). Cultural cases fail on ordinary hours, duration and occurrences.
- Proposed working promise (hypothesis): *"For a small group and a time window, show a few bookable indoor activities and cultural options. For each, state which party-specific facts (price for your group, session times, duration, age range) are confirmed by the operator, as of when, and what you must still check."*
- The cultural side stays **discovery-with-caveats** until ordinary hours and duration evidence exist.
- Do not promise current availability. Every slot claim carries its observation time.
- This does not shrink the product into a booking site: mixed-type discovery remains, but feasibility claims are limited to where evidence exists.

### 12.5 Smallest next evidence run

- **What:** 3 operators (Escape The Room branch 1 and branch 3, Scitech, and one more bookable indoor operator in the area), repeated on **3 different dates** including one weekend, ≥2 query times per date.
- **Scope:** only the fields the harness evaluates (branch/room IDs, party range, duration, slot quotes for 2 and 4 players, Scitech hours and price representations).
- **Where:** a new dated evidence directory, with no full bodies published.
- **Plus:** the 5 R05 fixed cases re-evaluated per date, and 10 routing pairs.

**Acceptance criteria (proposed, your judgment):**
- (a) Branch and room identifiers stable across dates.
- (b) Slot-quote price per party size consistent or explainable.
- (c) Quote age at query time recorded, with no stale quote used as current.
- (d) Scitech's ordinary hours established by an admissible observation, or recorded as missing.
- (e) Harness outcomes reproducible from the new observations.
- (f) No publication until permission.

**Who does what:**
- Network access (allowlist `api.escapetheroomsa.com`, `www.escapetheroomsa.com`, `scitech.sa`, `router.project-osrm.org` in this environment, or Sol repeats the run): **owner**.
- Collection script review and running on dates: **agent** (or Sol).
- Operator permission: **owner**.
- User sessions (R00 §28, 8 participants with the evidence card): **owner / real users**.

**Cost:** agent time roughly $3–6 per date at list price. $0 in data or provider spend.

### 12.6 Revised operator request drafts (not sent)

These supersede the drafts in R02.1 §9, which wrongly framed the project as permanently non-commercial.

**To Escape The Room:**
> We are developing a discovery service that helps small groups choose an indoor outing that fits their time and budget. It is at the research stage now, and may become a commercial product. We would like **approved read-only access** to room, branch and slot information for your Khobar branches: room names, player range, duration, age range, price for a given party size, and session times with availability status.
>
> Could you tell us:
> 1. whether you offer a partner or read-only feed, or permit use of your public site data for this purpose;
> 2. what we may **store** (and for how long), **display** (with attribution and a booking link to you), and not do;
> 3. acceptable **refresh limits** (requests per minute or day);
> 4. how **changes and cancellations** are signalled, and how quickly we must reflect them;
> 5. any fees or conditions.
>
> We would send users to your own booking flow, never take bookings ourselves, and remove data on request.

**To Scitech:**
> We are developing a discovery service, research stage now and potentially commercial later, that helps people choose a cultural outing that fits their time. We would like **approved read-only access** to your visiting hours (including dated exceptions), ticket prices by type, typical visit duration, and show times. Could you tell us:
> 1. whether a feed exists (spreadsheet, calendar or JSON) or whether reading your public pages is acceptable;
> 2. permitted **storage and display**, with attribution and links to you;
> 3. **refresh limits**;
> 4. how **changes** (special hours, cancellations) are announced;
> 5. which of the price representations on your price page is current. The visible table and the page's description differ.

### 12.7 Next three actions

1. **Owner:** allowlist the four domains above in this environment's network settings, or ask Sol to repeat the dated run. Then authorise the next run (§12.5).
2. **Owner:** decide whether to send the §12.6 requests. Adapt the sender identity and business description truthfully.
3. **Agent (after 1):** run §12.5 on 3 dates, re-run the v2 pass and the harness on the new observations, and report against the acceptance criteria. In parallel, the **owner** recruits the 8 R00 participants.

### 12.8 Spending for this batch

Figures below are session list-price telemetry, not billing.
- **Reported at batch start:** $7.64 cumulative (`get_session` `cost_usd`), matching the earlier $7.4–9.4 estimate.
- **This batch (estimate):** $3.5–5.
  - About 30 calls at about 400k cached context and $0.20/MTok read ≈ $2.4.
  - About 70k cache writes ≈ $0.6.
  - About 40k output ≈ $0.8.
- **Estimated cumulative:** $11–12.5. That is below your $15 batch ceiling, and well inside the $72 initial-work allowance from your $92 baseline.
- **Remaining by your baseline:** about $87–88.5 of the $92, and **the $20 reserve is intact.**
- Reconcile against the reported figure at the next message, because telemetry lags one turn.
