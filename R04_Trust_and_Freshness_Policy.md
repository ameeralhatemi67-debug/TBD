# R04: Trust and freshness policy (provisional, v0.2)

**Dates:** v0.1 on 27 September 2026 (morning). **v0.2 revised on 27 September 2026 (evening)** after [R02.2](R02_2_Source_Access_Recovery_and_Review.md) (see §12, change log).
**Inputs:** [R01 §25–26](R01_Source_Rights_and_Economics.md#25-provenance--rights-metadata), [R01.2 §2.3–2.4, §12](R01.2_Automation_First_Data_Strategy_and_Architecture_Correction.md), [R02 §12, §14](R02_Automated_Coverage_and_Feasibility_Audit.md#14-revise-the-automation-coverage-metric), [R02.1](R02_1_Practical_Data_Feasibility_Followup.md), [R02.2](R02_2_Source_Access_Recovery_and_Review.md), [R03](R03_Domain_and_Identity_Model.md)
**Status:** Provisional policy. It covers what a result may claim, from which evidence, for which date. It sets **no numeric confidence probabilities and no universal refresh intervals**. Statements about rights are **source-specific findings or labeled project policy**, not general legal conclusions.

## 1. Dimensions of a claim, kept separate

| Dimension | Question | Example from the evidence |
|---|---|---|
| **Evidence authority** | Is the asserting party in a position to know this fact? | Escape The Room's own API is authoritative for its own slots. A blog is not. |
| **Extraction channel** | How did the value reach us, and how faithfully? | Scitech page body vs the same page's description metadata. A search summary. |
| **Fact scope** | Which concept, branch, offering, party size and language does it apply to? | Room 1 at branch 1, four players. Not "Escape The Room". |
| **Observation time** | When was it observed, and by whom? | Sol's HTTP request at 12:01:26 UTC on 27 Sep (transferred to this project). |
| **Valid time** | For which dates or times does the fact apply? | Scitech National Day exception, 23–24 Sep only. |
| **Freshness** | Is the observation recent enough for this field and this query date? | A slot response goes stale within minutes. A room's player range is slower-changing. |
| **Conflict** | Do admissible observations disagree? | Scitech price: body 20 vs metadata 23 (adult halls). AR vs EN exception end 22:00 vs 23:00. |
| **Rights** | What may we store, display, index or transform? | No reuse grant found for Scitech or Escape The Room. A robots allow rule is not a licence. |
| **Publication eligibility** | May this claim appear in a product result? | Derived from the rows above plus project policy (§9). |

**Research support** (is the fact supported for this query?) and **publication eligibility** (may a product show it?) are separate outputs. A third output is **whether the complete query is satisfied**, which needs every hard constraint. None of the three may be merged into a single success rate.

## 2. Evidence authority and extraction channel

### Authority (per fact type)

| Class | Meaning | Examples |
|---|---|---|
| **A1** | The operator itself: its website, API, official social account or submission | Escape The Room branches/rooms/slots API. Scitech hours page. An operator's own cancellation post. |
| **A2** | A provider the operator authorises for this fact type | A licensed ticketing or booking provider, for inventory and price |
| **A3** | An official body for the facts it governs | A licensed government dataset field |
| **A4** | An independent third party | Directories, blogs, open POI datasets used for hours (OSM `opening_hours`) |
| **A5** | Untraceable | Generated summaries whose source cannot be established |

### Channel fidelity

| Class | Channel | Notes |
|---|---|---|
| **C1** | Direct structured response (API/JSON), hashed | R02.2 Escape The Room endpoints |
| **C2** | Direct page body (visible content), hashed | R02.2 Scitech hours pages |
| **C3** | Page metadata (description or social tags) | Can diverge from the visible body (Scitech price). Admissible only when consistent with C1/C2 or when no body value exists, and then as a conflict-prone value. |
| **C4** | Alternate-language version | Can diverge (Scitech exception end). Each language is a separate observation. |
| **C5** | Researcher reading or notes, including observations **transferred from another researcher** with provenance | R02 page readings. R02.2 observations used by this project are C1/C2 **as recorded by Sol**, labeled "transferred". |
| **C6** | Search-index or model-generated summary | Can only prompt a check. Cannot support a fact (R02.1's IMAX figures). |

**Research support for a hard constraint requires all of:**
- authority A1–A3 for that fact type;
- channel C1, C2 or C5 (C3/C4 only when consistent with a C1/C2 value);
- matching scope;
- a valid time covering the query;
- no unresolved conflict among admissible observations.

A4 can support low-stakes, slow facts only, such as opening hours for a café, and is always labeled. It never supports accessibility, age eligibility, booking rules or capacity. A5/C6 never supports anything.

This corrects v0.1, which put "aggregator" and "social post" into one never-supporting tier with generated summaries. An operator's own social post (A1) and a licensed booking provider (A2) can be authoritative. An untraceable summary cannot.

## 3. Constraint states

For each (candidate, hard constraint, query window):

| State | Meaning |
|---|---|
| **Supported** | Meets §2's research-support rule |
| **Contradicted** | An admissible observation shows the constraint fails. **Known failure.** |
| **Unknown** | No admissible observation (only C6, out-of-scope or out-of-date values). **Unverified feasibility.** |
| **Conflict** | Admissible observations disagree on something that decides the constraint. For pass/fail, treated as unknown. |

Missing information is never recorded as failure in coverage analysis, and never as a pass in recommendations (R02 §14).

## 4. Hard constraints stay hard

**A query is satisfied only when every hard constraint is supported.** An unknown hard constraint is never satisfied, whatever warning accompanies it.

Results fall into three groups:

1. **Fits.** All hard constraints are supported (research support), plus a separate publication decision.
2. **Unverified leads.** Some hard constraints are unknown and none is contradicted. They are shown **only as an explicit, labeled relaxation**, in a separate section naming each unknown. They are never counted as matches.
3. **Excluded.** Contradicted constraints, and unknowns of a *blocking* type unless the user explicitly relaxes that constraint.

| Constraint type | Unknown is… | Note |
|---|---|---|
| Accessibility need, age eligibility for a stated party, "no advance booking", strict travel ceiling | **Blocking** (not even a lead unless relaxed) | An overclaim is severe (R00 §9) |
| Open in window, last entry, duration fit, budget, occurrence exists | **Lead-eligible** when nothing is contradicted | Still **not satisfied** |

**Price unit and boundary.**
- A strict budget is satisfied only if the price's unit matches the phrase ("each" vs "total"), the party composition is known, and the comparison passes (§6a).
- **"Under X"** is strict (< X) by default. Because colloquial usage may mean ≤, a value exactly equal to X is recorded as a **boundary ambiguity**, not a pass.
- **"At most / max / up to X"** is inclusive (≤ X).
- A derived per-person share (total ÷ party size) may be used for "each" only when labeled as derived. Unverified final fees keep a residual caveat.

**Duration and deadline.** An unknown duration cannot satisfy "finish by" or a "90 minutes total" window.

## 5. Provenance and copied facts

- Record **lineage**: the original asserting party and each copying channel. The operator's figure, copied to a portal and a blog, is one lineage.
- Corroboration counts **demonstrably independent** lineages.
- **Unknown lineage earns no independence bonus.** It is not assumed to be the same lineage either; it simply doesn't count toward corroboration. *(Corrects v0.1, which asserted shared lineage.)*
- Search and generated summaries are channels (C6). They add no lineage and can introduce errors.

## 6. Scope and containment

Containment (R03) is a **relationship, not an inheritance rule.** Each field has its own scope rule:

| Field | Parent → contained site | Operator → branch | Notes |
|---|---|---|---|
| Opening hours | Not inherited. The parent's hours may be shown labeled "centre hours". | Not inherited | Ithra Children's Museum closes earlier than the centre (index hint, C6). |
| Accessibility assistance | Shown only as a **parent-scope claim**, labeled. Never a child eligibility claim. | Not inherited | Ithra's centre-level desk registration |
| Price, duration, age, group | Offering-specific | Offering-specific | Room 1 values do not apply to other rooms |
| Booking policy (FAQ) | — | Operator-scope unless branch-specific | "Advance booking recommended" (Escape The Room FAQ) is brand-wide guidance |
| Location / access point | Never inherited | Never inherited | Location conflicts block travel claims (R03 §5) |

District hours are never tenant hours (R02 Q15).

### 6a. Price claims

A price claim needs:
- a unit: per person, per ticket type, per party total, or per session;
- conditions: age band, group threshold, VAT and fees;
- a type: **displayed quote**, **derived value** or **final payable**.

For example, the Escape The Room slot response gives a displayed party total of SAR 384 for four players (C1, A1, transferred). SAR 96 each is **derived**. The final payable amount is **not verified**, because no checkout was performed.

### 6b. Representation conflicts and false successes

| Pattern | Rule | Real example |
|---|---|---|
| Same-page metadata vs body | Separate observations. Conflict if they disagree. | Scitech `/p/24`: body adult halls 20 / IMAX 25 / combined 45 vs metadata 23 / 28.75 / 46 |
| Language versions | Separate observations per language. Conflict if they disagree. | Scitech exception ends 22:00 (AR) vs 23:00 (EN) |
| Column mapping | Keep the offering column. Never collapse columns to one "price". | Metadata's 28.75 and 46 belong to different columns; a summary mixed them |
| Shared app shell | Identical content hash across different URLs ⇒ the page does not identify an offering | Escape The Room homepage and old room URL return identical hashes |
| HTTP 200 with an error body | Status ≠ content | Scitech robots URL returns the text `404` with status 200 |
| Expired notice on a fresh page | Observation time ≠ valid time | Scitech National Day notice seen on 27 Sep |

## 7. Valid time, exceptions and sessions

- Every schedule claim has a valid interval. **Exceptions apply only inside it.** Scitech's 23–24 Sep hours do not apply on 27 Sep, and nothing in them establishes ordinary Sunday hours.
- An ambiguous line near an exception (Scitech's "Friday 16:00–21:00") is recorded with **ambiguous scope**. It is not applied to 2 Oct.
- Holiday or seasonal query dates: a regular-hours claim alone becomes lead-eligible, with a holiday caveat.
- **Slots:** keep explicit timestamps with offsets (`+03:00`). A query's business date ≠ each slot's calendar date (late slots cross midnight).
- **Quote ≠ availability ≠ booking.**
  - A slot response is a **historical quote observation at time T** ("available at T").
  - Current availability needs a fresh observation at query time.
  - "Booking-confirmed" needs a completed transaction. That is out of scope for research.
- Cancellation: absence of a cancellation observation is not confirmation. Status is "as of <time>".

## 8. Freshness: demand-driven, no universal schedule

Refresh a claim when it is decision-critical for a live query and older than its class bound for that source. Classes are slow, medium, fast and very fast (R01 §26). **Bounds are set per source only after repeated observations on different dates**, which have not yet been made. Until then, show observation times. Slot quotes are very fast: stale for current-availability purposes almost immediately.

## 9. Rights and publication: findings and project policy

**Source-specific findings (R02.2 §9):**
- Escape The Room's robots file has a wildcard allow rule for its host. Under RFC 9309, robots rules are not access authorisation, and they are not a reuse licence.
- Scitech's robots URL returned no rules.
- Neither operator's privacy text grants data reuse.
- No terms of use were found for either. This does not prove that no terms or permission exist.
- Ithra's terms page timed out on 27 Sep. R01 §14's earlier reading (reproduction restricted beyond personal non-commercial use) is not re-verified.

**Project policy (conservative choice, not a legal conclusion):**
1. Research use may record short factual observations with provenance. Full operator bodies are not redistributed (R02.2 boundary).
2. **Product publication** of an operator's facts requires operator permission or a source-specific legal review. Until then, those facts are research-supported but **not publication-eligible**.
3. Linking to an operator's official page is treated by the project as low-risk and used as the fallback. This is a project judgment; no universal legal rule is claimed.
4. C6 content is kept only in research logs.

## 10. Examples under v0.2

| Example | Research support | Publication | Query satisfied? |
|---|---|---|---|
| Scitech adult halls price vs "under 50 each" (C01) | **Conflict** (20 body vs 23 metadata), but **both are below 50**, so the price constraint's outcome is the same either way. Treat it as supported **for this threshold only**, with the conflict recorded. | Not eligible (rights) | No: ordinary Sunday hours are unknown |
| Scitech hours on Sun 27 Sep | Unknown. The only schedule observed is an expired exception plus an ambiguous Friday line. | — | — |
| Escape The Room room 1, four players, 27 Sep, 18:15 (C02) | Group 2–8 supported. 60 min supported. Displayed total 384 ⇒ derived 96 each < 150, supported as derived. Available **as of 12:01 UTC**. | Not eligible (rights) | Only as a historical quote. "Active" is soft. Age not at issue. Final fees are unverified. |
| Escape The Room "no advance booking" (C04) | The FAQ recommends advance booking. An online same-day slot ≠ walk-in. **Unknown**, and blocking. | — | No |
| Room 1 for 18:30 departure, finish by 20:00 (C12) | 18:15 session starts before departure. The next session, 19:30–20:30, ends after the deadline. **Contradicted for this room on this date.** | — | No (for this room) |
| Diriyah visit page vs FAQ hours | Conflict (A1 vs A1) | — | No |
| JAX studio drop-in | Contradicted by the JAX FAQ (studios generally not open to casual visits outside sessions) | — | No |

## 11. Open items

- Volatility bounds per source (needs observations on different dates).
- Whether users accept "unverified leads" as a separate section (R00 sessions).
- Source-specific legal review or operator permission for publication (§9).
- Scitech's ordinary schedule (a new observation or operator answer).

## 12. Change log

**v0.2, 27 Sep 2026, after R02.2:**
- Split the single E1–E5 ladder into authority (A1–A5), channel (C1–C6), scope, rights and publication eligibility (§1–2).
- Operator social posts and licensed booking providers are no longer grouped with generated summaries.
- Added representation-conflict and false-success rules (§6b).
- Hard constraints: qualifiable unknowns are now "unverified leads", an explicit relaxation that is never satisfaction.
- Strict "under" vs inclusive "at most" (§4).
- Unknown lineage: no bonus, not assumed shared (§5).
- Containment is not inheritance; per-field scope table (§6).
- Quote vs availability vs booking (§7).
- Replaced "displaying a link is always allowed" and similar blanket statements with source-specific findings plus labeled project policy (§9).
- Examples updated with R02.2 evidence (§10).

**v0.1 (same day):** the tiered E1–E5 policy, §6a price claims and the lineage default. Kept in git history (commits `ae983a8` and earlier).
