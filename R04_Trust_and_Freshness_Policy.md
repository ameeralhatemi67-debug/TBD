# R04: Trust and freshness policy (provisional)

**Date:** 27 September 2026
**Inputs:** [R01 §25–26](R01_Source_Rights_and_Economics.md#25-provenance--rights-metadata), [R01.2 §2.3–2.4, §7, §12](R01.2_Automation_First_Data_Strategy_and_Architecture_Correction.md), [R02 §8, §12, §14](R02_Automated_Coverage_and_Feasibility_Audit.md#14-revise-the-automation-coverage-metric), [R02.1](R02_1_Practical_Data_Feasibility_Followup.md), [R03](R03_Domain_and_Identity_Model.md)
**Status:** Provisional policy. It covers what a result may claim, from which evidence, for which date. It sets **no numeric confidence probabilities and no universal refresh intervals**; none has been measured. Every rule is tied to a concrete example.

## 1. Seven dimensions of a claim, kept separate

| Dimension | Question | Example from the evidence |
|---|---|---|
| **Provenance** | Who asserted it, through what channel, and with what transformation? | Scitech hours came through a search-index summary, not a page we retrieved (R02.1 §4). |
| **Observation time** | When did we (or the channel) see it? | R02 read Scitech's hours page on 26 Sep. The index date is unknown. |
| **Valid time** | For which dates or times does the fact apply? | The Scitech National Day exception applies 23–24 Sep only. Diriyah free access ends 30 Sep (R02 §12). |
| **Freshness** | Is the observation recent enough, **for this field and this query date**? | A two-month-old regular-hours claim may be usable for a museum. A two-month-old occurrence claim is not. |
| **Confidence** | How strongly does the evidence support the claim? | Ordinal evidence tiers (§2), not a decimal. Source "confidence 0.77" is not a claim confidence (R02 §8). |
| **Rights** | What may we store, display, index or transform? | Ithra terms restrict reproduction. Scitech and Escape The Room rights are unknown (R02.1 §4). |
| **Conflict** | Do credible claims disagree? | Diriyah visit page vs FAQ hours (R02 §12). IMAX price 46.00 vs 28.75 across two index summaries (R02.1 §5). |

A claim can score well on one dimension and badly on another. Diriyah's first-party page is authoritative but conflicts with its own FAQ. A retrieval made today of a stale page is **new observation time, not new valid time**.

## 2. Evidence tiers

Tiers are ordinal. They do not represent probabilities.

| Tier | Source type | Example | May support a hard constraint? |
|---|---|---|---|
| **E1** | Operator-authorised feed, agreement or verified operator submission | None obtained yet | Yes, within its valid time |
| **E2** | First-party page or structured data retrieved by us, timestamped, where retrieval and display are permitted | None yet; blocked in this environment (R02.1) | Yes, within valid time, if no E1/E2 conflict |
| **E3** | First-party page observed by a researcher, or a licensed open dataset field | R02's Scitech and teamLab page readings. OSM `opening_hours` (26 of 353). | Only as **qualified**: "per operator page as of <date>" |
| **E4** | Third-party copy, aggregator, search-index summary, social post | R02.1 index summaries | **Never.** It can prompt a check or a refresh only. |
| **E5** | Inference from category or name | "Escape room ⇒ indoor"; "museum ⇒ cultural" | Only for low-risk constraints (indoor for an escape room), always disclosed; never for accessibility, age, booking or price |

The index-summary conflict in R02.1 (two IMAX prices within minutes) is the reason E4 can never support a hard constraint.

## 3. Constraint states and how results use them

For each (candidate, hard constraint, query window) the state is one of the four from R02 §14:

| State | Meaning | Result behaviour |
|---|---|---|
| **Supported** | E1–E3 claim, valid for the requested time, no unresolved conflict at E1–E3 | May be stated. E3 is stated as "per operator page, seen <date>". |
| **Contradicted** | E1–E3 claim shows the constraint fails (closed then, over budget, age not permitted) | **Known failure.** Exclude, and optionally explain ("closes 22:00, before your window"). |
| **Unknown** | No usable claim, or only E4 | **Unverified feasibility.** Never shown as a fit. See §4. |
| **Conflict** | Two E1–E3 claims disagree on something that decides the constraint | Treated as unknown for pass/fail. Show both and name the sources. |

**Known failure is not unverified feasibility.** "Scitech closes at 22:00 (E3)" makes C08 (a one-hour visit from 21:00) at best unknown, because last entry is unknown. It would be *contradicted* only if a claim said entry ends before 21:00. Missing information is never recorded as a failure in coverage analysis, and never as a pass in recommendations (R02 §14).

## 4. When unknown may appear, and when it blocks

Each hard constraint is **blocking** or **qualifiable** when unknown.

| Constraint type | Unknown is… | Rationale and example |
|---|---|---|
| Explicit accessibility need (wheelchair, step-free) | **Blocking** from the main list. It may appear only in a separate "not confirmed" section when the user allows it. | An overclaim is severe (R00 §9, v0.2 §20). C11: Ithra's centre-level assistance statement is inherited as qualified (§6), not as a pass. |
| Age or eligibility for a stated party | **Blocking** unless the user relaxes it | C05: no age rule found for Scitech; a child price existing ≠ a 6-year-old admitted. |
| "No advance booking" or walk-in | **Blocking** | C04: in-person booking offered ≠ walk-in slot tonight. |
| Hard travel ceiling ("15 min max", "don't send me across Riyadh") | **Blocking** when strict, qualifiable when phrased as "nearby" | C12: no routing, so all unknown. A straight-line distance may be shown **labeled as straight-line**, never as minutes. |
| Open in the window (regular hours) | **Qualifiable** when a regular-hours claim exists and no exception is known for the date; **blocking** when no hours claim exists at all | C01: "open until 22:00 per operator page seen <date>; special-hours notices not checked". |
| Last entry or duration fit for a tight window | **Qualifiable**, shown as the main residual check | C03, C08 |
| Budget | **Qualifiable** when the price exists but the unit is ambiguous; **blocking** when no price is known and the budget is strict | C02 (Escape The Room price unknown, so blocking under "under 150 each"). |
| Occurrence exists ("exhibition this weekend", "workshop Thursday") | **Blocking.** Without an occurrence claim there is no candidate. | C07, C09: say "we could not find dated programme information" and link the organiser. This is not "nothing is on". |
| Soft preferences (quiet, new, romantic) | Not a constraint; affects ranking and explanation only | C08 "quiet", C10 "new to me" (needs user history, never inferred). |

Results are ordered in tiers. First, all hard constraints supported. Then candidates with qualifiable unknowns, each naming its residual checks. Blocked candidates are omitted unless the user asks. An empty tier must say which constraint caused the scarcity (v0.2 §7).

## 5. Provenance and copied facts

- Record the **lineage** of each claim: the original asserting party and each copying channel. A fact on the operator page, copied to a tourism portal and then to a blog, is **one lineage**.
- **Corroboration counts independent lineages.** Three websites repeating the operator's hours do not raise the tier above the operator's own claim. If the copies are stale versions, they show up as a conflict with the operator's current claim, and the operator wins **only if** it is E1–E2 and newer in valid time.
- Search-index summaries and LLM summaries are channels. They add no lineage and can introduce errors (R02.1 IMAX example).
- **Unknown lineage defaults to the same lineage.** Pages with identical wording or figures, and no stated independent check, do not corroborate each other. (Added after the stress test in PROJECT_START_REVIEW §11.)

## 6. Scope and inheritance (uses R03)

- A claim applies to the concept it was made about. Operator-level claims (brand, head-office phone) do **not** become branch hours.
- A complex-level claim is inherited by a contained site **only as qualified**. "Ithra centre: wheelchair assistance via information desks" becomes "reported for the Ithra centre as a whole" on the Museum Galleries.
- District hours are never inherited as tenant hours (R02 Q15).
- A claim attached to one of several records under a **location conflict** (Scitech's three records) may support opening or price constraints, but **no travel claim** until an access point is confirmed (R03 §5).
- Offering claims attach to the branch-specific offering. A room page with branch-mixed cues produces a conflict claim (R02 §12).

## 6a. Price claims (added after the stress test in PROJECT_START_REVIEW §11)

A price claim is incomplete without its **unit and conditions**:
- per person, per ticket type, per group or room, or per session;
- the age band for child prices;
- the group-size threshold (Scitech "groups 5+");
- VAT and fees included or not;
- the payment method, only where it blocks the user (Escape The Room "cash on site", E4).

A budget constraint passes only when the price unit matches the user's phrasing ("each" vs "total") **and** the party composition is known. Otherwise it is qualifiable (unit ambiguous) or missing context (party unknown, R05 F05).

## 7. Valid time and exceptions

- Every schedule claim has a valid interval: regular pattern (open-ended until superseded), dated exception, or seasonal programme.
- **Exceptions apply only inside their interval.** The Scitech National Day hours do not apply on 26 Sep or 27 Sep. The Diriyah free access announcement does not apply on 2–3 Oct.
- Holiday-aware checks: for query dates on known holidays or seasons (National Day, Eid, Ramadan evening shifts), a regular-hours claim alone becomes **qualifiable with an explicit holiday caveat**, unless an exception claim for that date exists.
- Future dates (e.g., next month) use regular claims only as "usual hours, not confirmed for your date".
- Cancellation: a cancellation claim at E1–E3 contradicts the occurrence. Absence of a cancellation claim is **not** confirmation that it runs; an occurrence's status is only as fresh as its last observation.

## 8. Freshness: demand-driven, not a universal schedule

No universal refresh intervals are set. None were measured, and repeat retrieval was impossible in R02.1. The policy is:

1. A claim is **refreshed when it is decision-critical for a live query** and its observation is older than the **volatility bound of its class for that source**. Classes (slow, medium, fast, very fast) follow R01 §26 without numbers.
2. Bounds are **set per source after measurement**: repeat retrievals across ordinary days, a weekend and one exception period, as R02 §15 requires. Until then, every E3 claim is displayed with its observation date.
3. Stale beyond bound, and refresh impossible (blocked, rights) → downgrade to unknown for pass/fail, and keep it as a displayed hint only if rights allow.
4. Occurrence and availability claims are never refreshed from caches older than their own status cadence. Live capacity stays at source (R01.2 §17).

## 9. Rights gating

- Rights are checked **before** a claim is stored, indexed, displayed or used in any derived text (R01 §37).
- A claim with unknown rights may inform internal research and evaluation labels. It may **not** be displayed in a product result or used to generate a description.
- Displaying a link to the official page is always allowed. It is the fallback for every unknown.
- E4 content is never stored beyond the research log.

## 10. Examples applied end to end

| Example | Decision under this policy |
|---|---|
| Scitech tonight, halls ticket, 18:00–23:00 (C01) | Regular hours: **E4 only**. R02's page reading recorded the National Day exception and the no-booking statement, not regular hours. Price amounts: E4; R02 saw the per-offering price structure at E3 but did not record amounts. **Under this policy the hours constraint is unknown and blocking, because no E1–E3 hours claim exists.** The card may show only "check hours: <official link>". One E2/E3 observation of the regular-hours page would make it qualifiable. |
| Scitech IMAX price | E4 conflict (46.00 vs 28.75). Unknown. Never shown. |
| Scitech National Day hours on 27 Sep | Exception outside its valid time. Ignored. |
| Diriyah At-Turaif hours, visit page vs FAQ (R02 Q05) | E3 conflict. Constraint "open at 10 Tuesday" is conflict, so unknown. Show both sources. |
| Escape The Room, "four, no booking, tonight" (C04) | Group: E3/E4 supports four. No-booking: unknown and blocking. **Omitted from the main list.** Offered only as "call to ask for a same-night slot" if the user relaxes it. |
| teamLab "90 minutes total" (R02 Q10) | Typical visit about 2 h (E3). Duration contradicts a full visit, which is a known failure for "complete visit". It may appear as an explicitly abbreviated visit only if the user accepts it. |
| Ithra wheelchair at the Museum Galleries (C11) | Centre-level E4 (index) statement. Inherited qualified. Blocking for an explicit need, so shown in the "not confirmed" section with a phone number to call. |
| JAX studio drop-in (R02 Q06) | District access ≠ studio access. JAX FAQ (E3) says studios generally do not accept casual visits outside announced sessions. The constraint is **contradicted** unless an occurrence claim exists. |
| The same hours on the operator site and three blogs | One lineage. Tier set by the operator claim. |
| Event cancelled after our last observation | Occurrence status is as of the last observation. Show "status last confirmed <time>". Never "happening". |

## 11. Open items

- Volatility bounds per source (needs repeat E2 retrieval: environment allowlist plus rights).
- Whether users accept tiered results with qualifiable unknowns. This needs R00 observation sessions.
- Display wording for qualified claims. That is an interface question, deferred.
- Legal review of whether transient, per-query display of operator facts with a link is acceptable where no terms exist (Scitech, Escape The Room). This is **the** gating legal question for Model B (PROJECT_START_REVIEW §3).
