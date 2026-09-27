# R02.1: Practical-data feasibility follow-up

**Date:** 27 September 2026 (Asia/Riyadh). All retrieval attempts ran between 11:36 and 11:40 UTC.
**Follows:** [R02 §15 "The next specific enrichment proof"](R02_Automated_Coverage_and_Feasibility_Audit.md#15-query-time-refresh-what-is-real-and-what-remains-hypothetical) and [PROJECT_START_REVIEW §9](PROJECT_START_REVIEW.md#9-proposed-next-batch-phase-b-locked-before-any-answers-are-examined), where the operators and 12 cases were locked before this work began.
**Evidence:** [`R02_1_evidence/`](R02_1_evidence/). Run `python R02_1_evidence/check_phase_b.py` to check structural consistency.
**Status:** Bounded experiment completed. **The practical-data path was not demonstrated.** The reasons are separated below.

Labels: **Measured** (recomputed from retained files), **Index evidence** (a search tool's summary of indexed pages, with unknown index date), **Observed R02** (a page observation recorded in R02 on 26 Sep), **Documented**, **Interpretation**, **Hypothesis**.

## 1. Answer in brief

1. **Access.** This research environment's egress policy blocks all four operator domains, both from the container and through the page-fetch tool. No page was retrieved live, robots.txt could not be read, and no repeat retrieval was possible. This says nothing about the operators; it is a property of this environment.
2. **What the index shows.** Search-index summaries confirm that the operators publish several decision-critical facts. For Scitech: regular hours, per-offering prices, and a no-reservation rule. For Escape The Room Khobar: players per room, duration, and age guidance. Neither shows Escape The Room's price, hours or sessions, nor Scitech's visit duration, last entry or accessibility.
3. **The search layer adds its own errors.** Two searches minutes apart gave **different IMAX prices** (46.00 vs 28.75 SAR adult). A search summary cannot be used as an enrichment source.
4. **Rights.** No permission to retrieve, retain or display was established for either operator. No terms-of-use page, feed, API or calendar was found. Ithra's terms remain restrictive (R01 §14).
5. **Case results** (12 locked cases). **One** case had a candidate with every stated hard constraint supported, and only at weak index provenance. Of the 24 practical hard constraints across the cases, **8 were weakly supported, 0 contradicted, and 16 unknown**. Under [R04](R04_Trust_and_Freshness_Policy.md)'s strict evidence tiers, **none** of these can support a product claim (see the reconciliation in §8).
6. **Two new measured findings.**
   - The cultural candidate pool around Khobar is mostly noise: **81 of 85 `historic_site` records are implausible by name**.
   - The real cultural supply is concentrated in a handful of operators, and the anchor operators each have duplicated or displaced records.

**Effect on the product promise (interpretation):** the qualified-shortlist promise is not falsified, but the data path behind it is still unproven. The finding that most helps the promise is the concentration: in this area a few operator relationships would cover most cultural options.

## 2. Operator selection

The selection was fixed in advance (PROJECT_START_REVIEW §9).

- **Scitech (Al Khobar)** is the cultural operator. It has the richest first-party evidence in R02 (hours with a dated exception, per-offering prices, booking statement) and a high-confidence open record.
- **Escape The Room, Khobar branch,** is the repeatable indoor activity. It publishes group-size and duration fields, and it carried R02's branch-ambiguity failure.
- **Ithra** is used only as a desk contrast for restricted rights, and to evaluate cases C07 and C11.

Everything lies inside R02 rectangle E, within 12 km straight-line of the fixed synthetic origin (50.200, 26.300).

## 3. What was executed

| Step | Attempts | Outcome | Evidence |
|---|---:|---|---|
| robots.txt through the container proxy | 4 domains | All refused with `CONNECT 403` (environment egress policy). | [request_log.json](R02_1_evidence/request_log.json) |
| Page fetch tool, as the documented alternative | 4 URLs | All `EGRESS_BLOCKED`. | same |
| Domain-restricted web search, labeled as index evidence | 9 queries | Result links plus model-written summaries. Index dates unknown. | same; [source_observations.json](R02_1_evidence/source_observations.json) |
| Candidate pools for the locked cases | local | 104 culture, 38 activity and 545 local-stop records within 12 km. | [case_pools.py](R02_1_evidence/case_pools.py), [case_pools.json](R02_1_evidence/case_pools.json) |
| Plausibility judgments on the culture pool | 104 records | 9 plausible, 9 unclear, 86 implausible. | [culture_name_judgments.json](R02_1_evidence/culture_name_judgments.json) |
| Identity diagnostics for the anchor operators | local | See §6. | this report (reproducible from the R02 raw extract) |
| Case evaluation | 12 cases | See §7. | [case_outcomes.json](R02_1_evidence/case_outcomes.json) |

Per the prompt's network rule, I stopped after the failure and one documented alternative. I did not disable TLS, change proxies, or use third-party mirrors or caches of the operator pages. No accounts, messages, purchases or bookings were made. No raw page content was retained.

## 4. Five questions kept separate

| Question | Scitech | Escape The Room Khobar | Ithra (contrast) |
|---|---|---|---|
| **Technically accessible?** | Not from this environment. R02 read pages on 26 Sep, so the pages exist and render. | Not from this environment. R02 read a Riyadh room page. | Direct fetch returned 403 in R02. Blocked here. |
| **Permission to retrieve automatically?** | **Unknown.** robots.txt unreadable, no terms-of-use page found. | **Unknown.** Same. | **Restrictive.** Terms bar reproduction beyond personal non-commercial use (R01 §14). |
| **Permission to retain or display?** | **Unknown.** No licence, feed or agreement. | **Unknown.** | **Not without agreement.** |
| **Freshness** | Index date unknown. The results mix a current URL (`/en/p/22`) with a legacy one (`/en/page/About/81/...`), so the summarized hours may come from an old page. | Index date unknown. | Index date unknown. |
| **Factual reliability** | Hours consistent across two summaries. **IMAX price conflicts** between two summaries. The age band for the child price is undefined. | Group size varies by room (2–6, 4–6, "2–7"). Duration 60 or 75 min by room. | Accessibility provision documented at centre level, not per gallery. |

A visible booking path is not proof of availability. Escape The Room offers booking "online, by phone, or in person at the location". That does **not** establish walk-in availability tonight (case C04).

## 5. Field-level results for the two operators

States: **S** = supported (index evidence, weak provenance), **U** = unknown, **C** = conflict. Nothing is strongly supported, because no first-party retrieval succeeded.

| Field | Scitech | Escape The Room Khobar |
|---|---|---|
| Regular hours | S: Sat–Thu 09:00–12:00 and 16:00–22:00, Fri 16:00–22:00 | U |
| Date exceptions | U for 27 Sep–3 Oct. R02 saw only a 23–24 Sep National Day exception, which has expired. | U |
| Last entry | U | U (arrive 15 minutes before the game: S) |
| Visit or activity duration | U | S: 60 or 75 min by room |
| Price and unit | S: halls 23.00 adult / 17.25 child or group of 5+, incl. VAT. **C: IMAX 46.00 vs 28.75** | U. A summary mentions cash payment on site. |
| Age / group rule | Child price exists, age band U | S: recommended 12+, under-12s accompanied. Group 2–6 for most rooms, 4–6 for one. |
| Booking rule | S: no prior reservation needed for visits | S: online, phone or in person. Walk-in availability U. |
| Occurrences / sessions | A showtimes page exists; times U | An appointments page exists; slots U |
| Branch identity | Single site. Open-data location conflicts (§6). | **S: branch-specific URLs exist** (e.g. `/rooms/the-prison-khobar/`, `khobar.` subdomain) |
| Accessibility | U | U |

**This corrects R02 §9 and §11 (interpretation).** R02 read `/rooms/the-prison/`, the Riyadh variant, and found a Riyadh room above a Khobar footer. The operator also publishes **Khobar-specific room URLs**. The branch ambiguity is therefore partly an artefact of which URL was read. It is resolvable at URL level, provided the parser keys offerings to branch-specific URLs, not to the domain. R02's lesson, that a page-level address extractor is unsafe, still holds.

## 6. Candidate supply and identity: measured in the retained Eastern extract

**Culture pool precision.** 104 records within 12 km fall under R02's culture categories. By analyst judgment on name and category alone:
- 9 are plausibly visitor cultural venues, 9 are unclear, and 86 are implausible.
- Of the 85 `historic_site` records, 81 are implausible: residential compounds, furnished apartments, towers and companies.

Most of these are Meta-origin rows. This was a single annotator with no ground truth, and the Arabic names need a native-speaker check.

The 9 plausible records represent about **six distinct cultural destinations**: Scitech, the Ithra complex, the Tea Museum, Dawi Gallery, the Saudi Aramco Oil Exhibit (public access unclear) and Oil Well 7. R02's "154 culture/heritage" count for E, and any density claim based on it, **overstates cultural supply substantially**.

**Activity pool.** 38 records: cinemas, bowling, escape rooms, amusement and arcade. A few are obvious noise, such as a running track, a landscaping company and a football club. Activity supply is spread across roughly 25 operators.

**Anchor identity (measured distances).**

| Anchor | Records found | Spread | Implication for R03 |
|---|---|---|---|
| Scitech | `Scitech` (science_museum, 0.99), `Science Dome, Sultan Bin Abdulaziz S&T Center` (movie_theater, 0.65), `القبة العلمية` (movie_theater, 0.44) | Up to **3.99 km** apart | Several records for one complex are **up to 4 km apart**, so at least one is misplaced. The dome is a sub-offering typed as a cinema. Location needs verification before any travel claim. |
| Ithra | Cultural centre, Museum Galleries, Children's Museum and Theatre within about 100 m. A Foursquare `KACWC` record about 0.5 km away. An AllThePlaces `library` record about **3 km** away. An adjacent chocolatier named "Legend Ithra". | 0.02–3.1 km | Parent/child sub-venues and a displaced duplicate. The "Ithra" name also matches unrelated businesses. |
| Escape The Room | Meta record (0.99, operator URL) and Foursquare record (0.77, link aggregator) | **8.99 km** | Either a second site or a displaced or stale duplicate. The operator's index shows one Khobar address. Unresolved. |

**Interpretation.** In this area the cultural family is **operator-concentrated**: Ithra and Scitech account for most real cultural options. Two or three operator relationships could therefore cover most cultural decisions here. That makes R01.2's Model B much more plausible for culture than for activities, where the long tail of about 25 operators remains. It is also the most useful input for R01's partnership strategy (§30).

## 7. The 12 locked cases

Anchors: D0 is Sunday 27 Sep 2026, tonight is 18:00–23:00, the weekend is Fri–Sat 2–3 Oct, and Thursday is 1 Oct. Details and per-constraint states are in [case_outcomes.json](R02_1_evidence/case_outcomes.json).

| Case | Primary outcome | Best candidate: what is supported | Still unknown or what the user must check |
|---|---|---|---|
| C01 museum tonight ≤50 SAR | **Supported qualified shortlist** | Scitech: open Sun 16–22, halls 23 SAR (weak) | Tonight's special notice, last entry, travel |
| C02 four, active indoor tonight ≤150 each | Missing facts | Escape The Room: group 2–6 | Price, hours, a session for four |
| C03 90 min before 19:30, cultural | Missing facts | Scitech open (weak) | Duration, both travel legs, location conflict |
| C04 escape room tonight, no advance booking | Missing facts | Escape The Room: group | Walk-in availability (**must not pass**), hours |
| C05 kids 6 and 9, indoor weekend, ≤300 total | Missing user context | Scitech open weekend, child price exists | Number of adults; child age band |
| C06 weekend, not food, not mall | Missing facts | Scitech (weak hours) | "Inside a mall" has no data relation |
| C07 exhibition this weekend | Source-access failure | None | No occurrence inventory; Ithra blocked and restricted |
| C08 1 h quiet indoor after 21:00 | Missing facts | Scitech closes 22:00 (weak) | Last entry |
| C09 workshop Thursday evening | No candidates | None | No occurrence inventory |
| C10 new to me, not a café | Missing user context | Non-café candidates exist | Visit history must not be inferred |
| C11 wheelchair-accessible museum Saturday | Missing facts | Ithra access (weak, centre level) or Scitech Saturday hours (weak) | No single candidate supports both |
| C12 finish by 20:00, ≤15 min drive | Missing facts | None | No routing source |

**Distribution (denominator 12):** supported qualified shortlist 1 · missing facts 7 · missing user context 2 · source-access failure 1 · no candidates 1 · genuine constraint violation 0.
**Practical hard constraints** (excluding category-level ones): 24 in total. 8 weakly supported (33%), **0 strongly supported**, 0 contradicted, 16 unknown. Rights uncertainty applies to every supported fact.

No answer was presented as feasible. Unknown was never turned into a pass (C04, C11, C12) or into a failure.

**Does a shortlist plausibly reduce checking?** Interpretation only; this is untested with users.
- For C01, a card reading "Scitech · halls 23 SAR · open until 22:00 per operator (index) · check tonight's notice and travel" would leave about two checks instead of four.
- For C02 and C04, the most decision-critical facts (price, session) are exactly the unknown ones. A shortlist there mainly saves candidate generation, which R00 H2 suggests is not the painful step.
- Actual user benefit is **untested**.

## 8. Consequences

1. **Search-index enrichment is ruled out** as a product path. It has no provenance date, it introduced a price conflict, and it gives no rights.
2. **The decision-critical fields for activities (price, hours, sessions) were not found in any public index.** For this family, promise A needs an operator relationship or a booking-system integration. Culture is closer: hours, price and booking rule are published.
3. **Cultural discovery in this area rests on few operators.** An operator-first practical-data strategy (R01 §30) looks proportionate for culture: two to three agreements, not hundreds.
4. **Identity cleanup comes before practical enrichment.** Attaching Scitech's hours to the wrong one of three records 4 km apart would produce a wrong travel claim even with perfect hours.
5. **Occurrence cases (C07, C09) have no automated path at all** in this evidence. The "what's on" part of the product depends on Ithra-type programme access.

**Correction to PROJECT_START_REVIEW §7, falsifier (a).** As written, the falsifier is too weak: category-level constraints are trivially "supported". It should count **practical** hard constraints only. On that measure the current evidence is 8 of 24 weakly supported and 0 strongly supported. That is below the proposed "about half" threshold, but it cannot yet falsify the promise, because the shortfall is caused by blocked access and unknown rights, not by facts proven unavailable. The review has been annotated with a pointer here; its original text is kept.

### Reconciliation with R04 (added after R04 was drafted)

R02.1 labels index-derived facts "supported (weak)". [R04 §2](R04_Trust_and_Freshness_Policy.md#2-evidence-tiers) classifies index summaries as tier **E4**, which can never support a hard constraint. Applying R04 strictly:
- **0 of 24** practical hard constraints are supported.
- **C01 moves from "supported qualified shortlist" to "missing facts"**, with index hints and a link-out.
- The case distribution becomes: missing facts 8, missing user context 2, source-access failure 1, no candidates 1, supported 0.

The tables above are kept as recorded, since they describe what the index suggested. **R04's strict reading is the one to use for product claims.** The practical-data path is therefore not demonstrated at any level that could appear in a result.

## 9. What remains unresolved, and what would resolve it

| Dependency | Needed action | Who |
|---|---|---|
| Raw, timestamped first-party retrieval with hashes and repeat checks | Add `scitech.sa`, `escapetheroomsa.com`, `khobar.escapetheroomsa.com` and `www.ithra.com` to the environment's allowed domains (environment settings → Network access), then rerun this batch across two dates. | You, then agent |
| Permission to retrieve, retain and display | Send the requests below. | You |
| Location truth for the Scitech and Escape The Room records | One on-site or operator confirmation of each entrance. | Operator or field check |
| Routing | A keyed free-tier routing account (for example Mapbox) for C03 and C12. | You (account) |

### Permission request drafts (not sent)

**To Scitech (contact listed on scitech.sa):**
> We are researching a non-commercial prototype that helps residents choose a cultural outing. May we (1) read your published visiting hours, special-hours notices, ticket prices and show times automatically, at most a few times a day; (2) store those facts with the date we read them; and (3) display them with a link back to your page? We would not copy images or descriptive text. If you prefer, a simple feed (spreadsheet, ICS calendar or JSON) of hours, exceptions with dates, prices by ticket type, typical visit length and show times would be ideal. We would correct or remove any fact on request.

**To Escape The Room (info@escapetheroomgroup.com):**
> We are researching a prototype that helps small groups choose an indoor activity. For the Khobar branch, may we automatically read and display, with attribution and a booking link, each room's player range, duration, price per person, age guidance and opening hours? Could you tell us whether same-day availability can be checked through your booking system or an API? We would store only these facts with retrieval dates, and remove them on request.

## 10. Cost of this phase

Estimated at about $1.5–2.5 at list price, including 9 web searches at $0.01 each. The session's reported figure before this phase was $3.38. See [PROJECT_START_REVIEW §1](PROJECT_START_REVIEW.md#budget-table) for the running table.
