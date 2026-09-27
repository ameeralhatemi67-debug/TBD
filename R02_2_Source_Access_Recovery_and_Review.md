# R02.2: source-access recovery and review of Opus's findings

**Date:** 27 September 2026, Asia/Riyadh.

**Reviewed branch:** `claude/gifted-davinci-wv2qnj`, commit `ae983a809ebfdf6d92416eecb57492592fe998e2`.

**Follow-up branch:** `codex/source-access-followup`.

**Purpose:** perform the public-source checks blocked in Opus's environment, assess its conclusions, and provide evidence it can use to continue.

**Status:** several access blockers resolved in this environment; commercial reuse rights, longitudinal reliability, and user value remain unresolved.

## 1. What changed

The central technical conclusion is stronger than R02.1 could establish. We obtained current HTTP responses from Scitech, Sparky's, and Escape The Room's public website and its public data endpoints. We also obtained two route responses from the OSRM demonstration service.

Most importantly, Escape The Room publishes a branch-specific, machine-readable path to rooms and slot quotes. The public response for room 1, four players, and 27 September returned an available 18:15–19:15 slot with a displayed group total of SAR 384. The site's public client treats that amount as the selected booking total. An equal split is SAR 96 per person. This is a timestamped observation of the operator's response, not a reservation, confirmation of final charges, or permission to reuse its feed. [Public room endpoint](https://api.escapetheroomsa.com/api/rooms?branchId=1), [public availability request](https://api.escapetheroomsa.com/api/availability/slots?roomId=1&date=2026-09-27&players=4)

This changes the next question from whether such practical data is published at all to whether an appropriate reuse arrangement, reliable refresh process, and useful user experience can be established. It does not justify a production integration yet.

All numbers below are bounded research observations. The [evidence package](R02_2_evidence/README.md) includes request times, response hashes, failures, and small factual projections. Full operator pages, scripts, descriptions, images, and complete API bodies are kept out of the published repository.

## 2. Assessment of Opus's work

The intake, independent recount, provisional identity model, and distinction between unknown and contradicted constraints are useful. Stopping when its network policy blocked access was appropriate. Preserving uncertainty was preferable to claiming its search summaries were verified facts.

Several conclusions need revision:

| Claim or decision | Assessment and correction |
|---|---|
| All operator sources were blocked | Correct for Opus's recorded environment. It is not a general source-access finding. Three operators were accessible here; Ithra still timed out. |
| No usable activity price or slot path was found | Accurate as a description of its search results. Current public site responses now demonstrate a room/branch/party/date path to slot quotes. |
| Khobar-specific room URLs resolve branch ambiguity | Incomplete. The old room URL now returns the same app shell as the homepage. Its HTTP 200 response does not itself establish a room. Branch and room identifiers in the site's current data matter. |
| Scitech price disagreement comes from unreliable search summaries | The summaries are not adequate evidence. However, a directly retrieved Scitech page itself contains conflicting visible and metadata prices. Extraction channel and column interpretation are plausible causes, not just invented search text. |
| About six real cultural destinations, so two or three agreements cover most outings | Unsupported inference. A category-filtered, name-screened convenience sample cannot estimate all local cultural supply or the share of user decisions covered. Treat concentration as a hypothesis. |
| 81 of 85 historic-site records are wrong | The measured result is that one annotator marked 81 names implausible. This is useful triage, not independently validated classification precision. |
| Same-name proximity tests found no duplicates | Correct for that test. Nearby pairs do not prove duplicates. Distinct tenants, branches, and parent/child venues can be close. |
| Two distant Escape The Room records suggest a duplicate or relocation | Keep unresolved. The current operator lists two Khobar branches. One Overture record closely matches branch 1; the other still needs branch/history evidence. |
| R04 permits no hard constraints from any aggregator or social post | Too broad. A licensed authoritative booking provider or an operator's own cancellation post differs from an untraceable generated summary. Evidence authority, extraction fidelity, scope, freshness, and rights need separate treatment. |
| All phases completed | The documents were produced. The intended repeated practical-data experiment was not completed. Correct the status wording. |

Opus's clarification of the confidence-threshold loss is valuable: Foursquare explains 327 of the 941 excluded candidates; Meta accounts for the other 614. This refines R02's emphasis. It does not establish that all low-scoring Meta rows are bad, or that source-specific numerical cutoffs are already calibrated.

## 3. Method and actual access results

The formal collection contains 22 bounded HTTP requests across three manifests. Nineteen returned HTTP 200, one failed DNS resolution, and two timed out. A 200 response is not automatically a usable result: Scitech's robots URL returned the text `404`, and Escape The Room's old room URL returned an app shell.

The requests used PowerShell's normal TLS validation. No certificate checks were disabled. No proxy bypass, credentials, login, account creation, payment, booking, reservation hold, operator message, or administrative endpoint was used. The operator's public app identified the public GET paths used here. A browser attempt failed at local runtime startup, so no interactive-browser verification is claimed.

The formal manifests cover reproducible checks, not every exploratory tool call. Before recording them, we made small exploratory reads of Scitech's price page and Escape The Room's public app, branches, and rooms. Web text-reader observations were used separately and were not labeled as timestamped live HTTP retrievals.

| Source | Direct outcome | What it establishes |
|---|---|---|
| Scitech Arabic price, Arabic/English hours, privacy | HTTP 200 | Direct first-party content can be retrieved in this environment. |
| Scitech robots | HTTP 200, body `404` | No usable robots rules obtained. Do not interpret the status code as an actual robots policy. |
| Escape The Room homepage and old Khobar room URL | HTTP 200, identical content hashes | A modern client-rendered site; the old path alone is not a retrieved room description. |
| `khobar.escapetheroomsa.com` | DNS failure here | Do not rely on that old subdomain as a currently working source. It does not prove universal DNS failure. |
| Escape The Room public branches, rooms, FAQ, privacy, slots | HTTP 200 | Useful structured data exists in the public site's delivery path. No third-party API contract is established. |
| Escape The Room robots | HTTP 200, wildcard allow rule | A crawler preference for this host, not a data license or authorization for another host. |
| Sparky's branch directory | HTTP 200 | Branch names, locations, and displayed schedules are available; pricing/capacity were not established. |
| Ithra visit and terms pages | Two 20-second timeouts | This source remains unresolved here. No current rereading of its terms is claimed. |
| OSRM outbound and return routes | HTTP 200, `code: Ok` | A small no-account routing test succeeded. No production routing decision follows. |

## 4. Scitech: the page itself carries conflicting representations

The Arabic price page's visible table gives adult hall admission at SAR 20, IMAX at SAR 25, and combined admission at SAR 45. The child row gives 10, 25, and 35 respectively. The visible note says VAT is included. The same response's HTML description metadata instead contains adult prices 23, 28.75, and 46 and different child/group prices. [Price page](https://scitech.sa/p/24)

Therefore, both 28.75 and 46 can be traced to the page's metadata, but in different offering columns. We cannot prove exactly how Opus's search tool derived its summaries. We can demonstrate an upstream inconsistency and a potential column-mapping failure. Do not promote either extracted representation to current transaction truth without resolving the conflict. For a simple adult-hall threshold of SAR 50, both quoted amounts are below the ceiling, but fees, eligibility, date applicability, and hours still need their own evaluation.

The hours pages provide another conflict. Arabic shows a 23–24 September 2026 National Day exception ending at 22:00. English ends that exception at 23:00. Both show Friday 16:00–21:00 and a statement that visits do not require advance reservation. Neither observed body provides a clear ordinary Sunday schedule for 27 September. The Friday line's scope is ambiguous beside the holiday notice. [Arabic hours](https://scitech.sa/working-hours), [English hours](https://scitech.sa/en/p/22)

Do not import the old regular hours from the index, extend an expired exception, or assume the Friday line governs 2 October. A recently retrieved page can contain an expired notice. A no-reservation statement also does not confirm every IMAX showing's capacity.

The privacy policy concerns personal-data handling and lists a general centre contact. It supplies no express data-reuse grant in the reviewed text. It should not be presented as a scraping agreement or as proof that factual research is prohibited. [Scitech privacy policy](https://scitech.sa/privacy-policy)

**Test implications:** retain separate observations for page body, metadata, language, offering column, and valid interval. Do not silently combine them into one price or schedule.

## 5. Escape The Room: current public data resolves several gaps

### Branch identity

The public branch endpoint lists three branches: Al Khobar 1, Al Riyadh, and Al Khobar 2, branded Escape The Room+. Branch 1 has an operator-supplied map link containing longitude 50.1945561 and latitude 26.3055142. These coordinates were read from the operator's response; no Google Maps dataset was retrieved. [Branches](https://api.escapetheroomsa.com/api/branches)

The existing Overture record `b4fdc657-c04d-44df-a47c-8edd7a87cc53` is approximately 2.3 metres from that operator map point. This supports a candidate identity link to branch 1. It does not confirm an accessible entrance. The other named Overture record remains about 9 km away; its relationship to the second branch, an old branch, or a bad point is unresolved. Do not merge it or assign it to branch 2 from the name alone.

### Room details

The branch-1 room endpoint returns seven rooms. Room 1, The Prison, has branch ID 1, slug `the-prison-khobar`, 2–8 players, duration 60, and age-bound fields 8 and 80. Its static display-price field is null. The site's FAQ supports interpreting the duration as minutes. An age-bound field's operational meaning still needs care, especially before advising about children. [Rooms](https://api.escapetheroomsa.com/api/rooms?branchId=1), [FAQ](https://api.escapetheroomsa.com/api/faq)

These observed values supersede the index's 2–6-player or 12+-recommended assertions for this particular room as research evidence. They do not establish a brand-wide rule. A null room-price field means the quote may live at the slot level, not that the operator has no published price.

### Slot quote and price unit

The public site makes a GET request with `roomId`, `date`, and `players`. For room 1, 27 September, and four players, our response returned ten slots: one booked and nine available. An example was 18:15–19:15, SAR 384. Later returned slots cross midnight into the following date. Preserve their explicit `+03:00` timestamps and do not equate the query's business date with every slot's calendar date. [Exact request](https://api.escapetheroomsa.com/api/availability/slots?roomId=1&date=2026-09-27&players=4)

The public room-detail client takes the selected slot's amount into the total display without multiplying it by player count. This supports interpreting 384 as the displayed total for the selected party. Dividing it by four yields 96, a derived equal share. No promo code, hold, checkout, or payment was attempted. The final payable total and fee/tax conditions were not verified; the client has a tax-related translation key whose visible text merely says “Included,” which is not enough to establish a complete tax policy. [Public room client](https://www.escapetheroomsa.com/assets/RoomDetail-B3labSzF.js)

The FAQ recommends advance booking. That recommendation and an available online slot do not establish walk-in acceptance without advance booking. [FAQ](https://api.escapetheroomsa.com/api/faq)

**What is demonstrated:** a current technical path from branch to room to party/date-specific quote in this one operator's public site. **Still unproven:** third-party reuse terms, contracted access, stability across dates, refresh cost, admission completion, and generalized coverage.

## 6. Routing is now measured, within narrow limits

Using R02.1's synthetic origin at longitude 50.200, latitude 26.300 and branch 1's operator map point:

| Direction | Demo route distance | Demo duration |
|---|---:|---:|
| Origin to branch 1 | 1,077.4 m | 149 seconds |
| Branch 1 to origin | 1,753.1 m | 196.9 seconds |

The different directions illustrate why the return leg cannot simply copy the outbound leg. The service snapped the endpoints roughly 8.8 m and 15.1 m onto its network. These are model outputs from a public demo, not observed journeys or traffic-aware arrival guarantees. Parking, walking to the door, briefing, queues, and entrance suitability remain unmeasured.

The [OSRM demo policy](https://github.com/Project-OSRM/osrm-backend/wiki/Demo-server) restricts use to reasonable non-commercial requests and provides no service guarantees. The [server information](https://routing.openstreetmap.de/about.html) specifies a maximum of one request per second and no heavy usage. These two small requests do not select the demo as a production provider. Routing data attribution remains OpenStreetMap contributors, and these outputs remain separate from the owned place baseline.

This removes a no-account technical-access blocker for the present test. It does not close R08's practical travel-time validation gate or require the owner to open a paid account now.

## 7. How the 12 locked cases change

Do not replace the original R02.1 record. Treat this as a later evidence pass over the same cases and dates. Their denominator remains 12. Do not claim a new aggregate score until the individual practical requirements are explicitly reconciled with R04 and the machine-readable outcomes.

| Case | New research evidence | Remaining limitation |
|---|---|---|
| C01 museum tonight ≤50 each | Scitech's visible adult hall price is below the ceiling; metadata differs but is also below it | Ordinary Sunday hours still unsupported; exact current price conflict and reuse rights unresolved |
| C02 four, active indoor tonight ≤150 each | Branch 1 room fits four; 60-minute sessions; an 18:15 quote gives a displayed SAR 384 group total | Final charges, meaning of “active,” ages, admission, and commercial reuse remain separate. Availability was only a snapshot |
| C03 90 minutes before dinner, cultural | No new cultural-duration evidence | Escape-room travel data cannot answer a Scitech cultural query |
| C04 escape room without booking ahead | A same-day online slot was reported; advance booking is recommended | No proof of walk-in availability. Keep the clarification between no booking and same-day booking |
| C05 ages 6 and 9, weekend, total budget | Specific room age fields now exist; Scitech has a child-price row | Party count, child-price age band, correct date, and room-specific eligibility remain unresolved |
| C06 not food/not mall this weekend | No decisive new containment evidence | Do not infer absence of mall containment from a missing field |
| C07 exhibition this weekend | Ithra direct access still failed | Missing programme evidence, not evidence of no exhibition |
| C08 one quiet indoor hour after 21:00 | No valid ordinary Scitech schedule established | Quietness, last entry, and duration remain unknown |
| C09 workshop Thursday | No occurrence inventory recovered | Keep source/data coverage failure distinct from no real-world workshops |
| C10 new to me/not café | Unchanged | Requires user history or a visible clarification |
| C11 accessible museum Saturday | Unchanged | No specific access route or Saturday museum visit established |
| C12 depart 18:30, finish by 20:00, drive ≤15 min | Demo driving path exists to branch 1 | For room 1 on this fixed date, the 18:15 session is already underway and the next 19:30 session ends 20:30. It cannot satisfy this window. This is not a failure of every room or venue |

**Key distinction:** research support for a quoted fact, permission to publish it in a product, and a fully feasible outing are three different outcomes. A global “0 supported” figure that bundles them conceals where progress was made.

## 8. Required corrections to the provisional models

### R03

- Retain branch identity, room/offering identity, and dated sessions. Add the real two-Khobar-branch example and the close operator-point match as a provisional link.
- A URL returning a shared app shell does not identify an offering. Use observed operator IDs with provenance.
- Replace absolute statements that source records are never deleted. Preserve lineage and reversibility subject to retention rights, expiry, correction obligations, and applicable deletion requirements. A deletion may leave permitted tombstone metadata rather than retaining prohibited content forever.
- Treat containment as a relationship, not a general fact-inheritance rule. Each field needs its own scope rule. Parent opening hours and accessible assistance are not automatically child eligibility claims.

### R04

- Separate evidence authority from collection channel and rights. A licensed booking provider may be authoritative for inventory; an operator's own social account may be the direct source of a cancellation. A generated search summary is different.
- Add within-page conflicts, language conflicts, field-to-column mapping, and app-shell detection.
- Keep unknown lineage unknown. Decline a corroboration bonus when independence is unproven; do not assert that all unknown sources actually share one lineage.
- Remove universal legal statements such as “displaying a link is always allowed” and “all public facts require a negotiated agreement.” The project may choose conservative publication gates; those are project policy, not blanket legal findings.
- Keep hard constraints hard. Showing a separate unverified lead is an explicit relaxation, not a supported match. In particular, price-unit ambiguity or unknown duration cannot satisfy a strict budget or deadline just because a warning is shown.

### R05 and evidence files

- Reconcile the human-readable R04 correction with `R02_1_evidence/case_outcomes.json`, which still contains the earlier weakly supported C01 result. `check_phase_b.py` currently validates that historical structure, not the later policy. Create a versioned evidence pass instead of silently revising the original experiment.
- Define “under” versus “at most.” The seed currently maps “under 150” to `≤150`; boundary tests should preserve the distinction or record the chosen interpretation as ambiguity.
- Ground time and location defaults. A missing origin cannot be repaired by silently assuming one. The historical fixed synthetic origin is valid only within the fixed cases.
- Preserve the held-out set's stated limitation: it is unannotated, not unseen, because it was read during intake.

These changes can be made now. They do not require operator outreach or a production app.

## 9. Rights and remaining human dependencies

Escape The Room's robots file has a wildcard allow rule. [Robots file](https://www.escapetheroomsa.com/robots.txt). The Robots Exclusion Protocol explicitly does not grant access authorization. It is also not a reuse license, and one host's file does not define another host's terms. [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html)

The public privacy endpoint discusses handling booking information; it does not grant a third-party data license. [Privacy page data](https://api.escapetheroomsa.com/api/pages/privacy). We found no express reuse grant in the documents inspected. This bounded check cannot prove no agreement, terms page, or lawful alternative exists.

No operator messages were sent. The existing outreach drafts should be revised to request an approved read-only feed or partner access, desired fields, permitted retention/display, attribution, refresh limits, and cancellation/change handling. Do not describe the planned business as permanently non-commercial just to obtain permission for an eventual commercial product.

No setting in the user's Claude account was changed, and this audit does not establish a provider-enforced credit cap. The owner reports approximately $8 spent and $92 remaining. That is the next planning baseline, not a billing measurement by this agent.

Still requiring later evidence or owner action:

1. Source-specific legal/contract review or operator permission for ongoing reuse.
2. Observations on genuinely different dates. Today's reads cannot be relabeled a three-date reliability study.
3. Real-user observations of usefulness and remaining checks.
4. Physical entrance, access, and travel validation where a strict promise depends on them.
5. Claude network settings if Opus must make fresh external requests. It can use this repository's research observations for offline work without that change.

## 10. Recommended continuation

Proceed with corrections to R03–R05 and a bounded R06 retrieval/feasibility design grounded in these examples. A small offline research harness can test branch selection, source conflict, exact budget boundaries, date scope, and appointment timing. It must use clearly labeled research fixtures, not publish an unlicensed live feed or launch a product.

Do not spend the remaining balance rereading every report or producing a full platform design. Allocate the next batch at most $15 by conservative estimate, retain a $20 reserve, and report evidence gained at the next checkpoint. The remaining initial-work allowance is $72, based on the owner's $92 remaining balance; it is a ceiling, not a target.

The practical-data test is now **partially demonstrated technically**. Permission, repeat reliability, and user benefit remain open. That narrower conclusion supports further work without pretending the original blockers all disappeared.
