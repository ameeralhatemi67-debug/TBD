# R02 — Automated Coverage & Feasibility Audit

**Project:** Location-aware discovery platform  
**Audit date:** 26 September 2026, Asia/Riyadh  
**Inputs:** Product & Technical Concept v0.1, architecture review, R00, R01, and R01.2  
**Status:** Completed bounded source audit with retained measurements. Several architecture gates remain unproven.  
**Primary question:** How much useful discovery coverage can we obtain automatically, and what prevents those candidates from becoming credible outing choices?

## 1. Executive assessment

R01.2's automation-first direction remains worth pursuing. This audit demonstrates automatic retrieval of a substantial place baseline, but **does not demonstrate automatic production of a reliable, constraint-complete shortlist**.

We retrieved **13,764 Overture Places records** across four explicit Saudi sample rectangles. A deliberately narrow category rule selected **1,379 potential discovery records**. These are source records, not verified distinct venues. Most selected records are cafés or similar stops. The retrieved schema contains **no opening hours, price, visit duration, booking rule, event occurrence, age rule, or live availability**. Those missing fields prevent the baseline alone from supporting R00's promise of a feasible outing tonight. The counts and exact extraction parameters are retained in [the evidence package](R02_evidence/README.md).

The most consequential finding concerns confidence. All **1,916 Foursquare-sourced records** in the full Overture sample have confidence **0.77**. A simple cutoff at 0.8 removes every one of them, including teamLab Borderless and the Red Sea Museum. A source confidence number cannot be treated as a universal ranking-quality or eligibility score.

Public operator pages contain useful practical information, but also reveal conflicts, expired exceptions, ambiguous branch context, and incomplete booking information. These pages were inspected as research evidence. They were not converted into a licensed automated feed. Automated extraction, even if technically possible, would not resolve source permissions or the meaning of conflicting facts.

The separate OSM experiment retrieved **353 elements for the Eastern rectangle**, including **26 with an opening-hours tag**. Its server-reported database timestamp was **31 May 2026**, almost four months before this audit. Requests for the other three rectangles failed. Routing requests also failed certificate validation in this environment. These are observed access limitations, not evidence that the missing venues or routes do not exist.

**Recommendation:** continue concept development with a place-based, feasibility-aware discovery hypothesis, and treat dynamic enrichment as the next specific dependency to prove. Do not commit to broad events, guaranteed availability, a staffing operation, or a global confidence threshold. R03 can begin from the actual records. The operational feasibility and low-human-maintenance gates remain open.

## 2. What this audit carried forward

[R00](R00_User_Decision_Study.md) proposed a local resident arranging a near-term outing for themselves and approximately one to four others, with domestic visitors as a secondary hypothesis. Neither has been validated through the proposed observed user study. Its candidate promises remain:

- A: choose a feasible outing tonight.
- B: discover something worthwhile and new locally this weekend.

[R01](R01_Source_Rights_and_Economics.md) established that accessible data and reusable data are different. [R01.2](R01.2_Automation_First_Data_Strategy_and_Architecture_Correction.md) corrected the implied operating model toward an open or owned baseline, permitted automated refresh, query-time enrichment, explicit uncertainty, and selective curation.

This audit preserves that correction. Missing fields were left missing in the measured baseline. Researcher observations were kept separate. We did not repair all records by hand and then describe the result as automated coverage.

The current product remains a discovery engine for a location and time. Planning, proactive notifications, personalization, interface design, and implementation are outside this audit.

## 3. Evidence levels and limits

| Label | Meaning in this report |
|---|---|
| **Measured** | Calculated from a retained source response or recorded request outcome during this audit. |
| **Observed page evidence** | Read from a linked public page or search-index representation. It is not a retained production feed or proof of current capacity. |
| **Documented** | Stated in current provider documentation or source terms. |
| **Interpretation** | A reasoned implication of those observations. |
| **Hypothesis** | A proposed direction or test condition still requiring evidence. |
| **Not measured** | No defensible numeric result is available. |

The evidence is deliberately bounded:

- Four rectangles, one Overture release, one audit date. This is not a Saudi or international coverage census.
- Categories were selected by an explicit rule. We did not classify every business, establish an independent venue inventory, or validate entrances in person.
- Named anchors were examined after retrieval. Their examples diagnose failure mechanisms; they cannot establish unbiased recall or overall location accuracy.
- We made one small set of endpoint attempts. Request success rates are descriptive outcomes of those attempts, not service reliability estimates.
- Official-page evidence was purposively selected for the product's difficult fields. The frequency of conflicts in those pages is not a population conflict rate.
- No accounts, paid feeds, partner agreements, live inventory credentials, completed bookings, venue contacts, or user observations were obtained.
- Search results can expose indexed content when direct opening fails. Such content is labeled separately and does not count as successful live refresh.

The supporting evidence is about 20 MB of Overture JSON plus a small OSM extract, manifests, measurements, and license notices. Collection and analysis helpers are research utilities, not application code.

## 4. Scope, sample geography, and time windows

### Geographic sample

Coordinates use WGS84 longitude and latitude. The rectangles are analyst-selected audit boundaries, not administrative boundaries or travel-time catchments.

| ID | Sample area | West, south, east, north | Main purpose |
|---|---|---|---|
| E | Al Khobar, Dhahran/Ithra, and part of Dammam | 50.070, 26.280, 50.240, 26.470 | Test an extensive urban cluster with culture, indoor activities, and local stops. |
| D | Diriyah, JAX, Bujairi, At-Turaif | 46.550, 24.710, 46.585, 24.765 | Test a compact cultural district and shared operator information. |
| J | Historic Jeddah/Al-Balad | 39.170, 21.475, 39.200, 21.505 | Test heritage, museums, and a walking-oriented discovery context. |
| B | Boulevard/Hittin sample | 46.585, 24.755, 46.635, 24.800 | Test indoor entertainment and time-sensitive attractions. Includes adjacent content that still needs geographic classification. |

E is much larger than J or D. Its larger record count cannot establish better density, better relevance, or shorter journeys. These bounds do not cover all of the named cities. The four extracts contain **13,764 unique Overture IDs**, so their totals do not double-count identical IDs across files.

### Time scenarios

The diagnostic cases use Saturday **26 September 2026** for tonight, Tuesday **29 September** for a weekday, Friday/Saturday **2–3 October** for the next weekend, and **24 October** for a future outing. A 90-minute interval and a late-night interval test duration and midnight handling. These are audit scenarios, not outing recommendations.

The audit fell immediately after Saudi National Day. A Scitech page still showed a specific 23–24 September hours exception. That observation is useful precisely because the dates do not cover the audit's Saturday scenario. [Scitech hours](https://scitech.sa/working-hours)

### Content boundaries

The first-pass selection covers cultural/heritage venues, selected repeatable activities, and candidate local stops. Dated events and workshops are tested through source feasibility, because the retrieved place schema has no occurrence objects. Cafés and bookstores are candidates for local discovery; category membership does not establish independent ownership, novelty, or quality.

## 5. What was actually executed

| Experiment | Actual execution | Outcome | What the outcome supports |
|---|---|---|---|
| Overture baseline | Four bounding-box extracts, release `2026-09-23.1`, through the official Python reader with direct GeoParquet access | Four completed extracts; 13,764 records | Automated geographic candidate acquisition works in these areas. |
| Initial Overture catalog filter | Same four boxes with the reader's catalog-filter option | Returned no files; direct access then succeeded | An ingestion failure must not be reported as zero local coverage. Cause not isolated. |
| Category/field audit | Exact category sets, all extracted records, no manual backfill | 1,379 selected records and field counts below | Reproducible baseline composition and missingness. |
| Confidence sensitivity | Cutoffs at 0, 0.7, 0.8, 0.9 on selected records | Large provider-sensitive coverage changes | A global threshold is unsafe without calibration. |
| OSM comparison | Four bounded queries at the first endpoint, then four at a documented mirror | First endpoint TLS failures; mirror returned E, with D failing HTTP 504 and J/B timing out | One separate, dated comparison sample; no other-area coverage result. |
| First-party information check | Targeted pages for culture, indoor activities, ticketing, and districts | Useful practical fields, conflicts, branch ambiguity, and access limitations | Specific enrichment requirements and failure cases. |
| Routing | Eight small car/walking matrix requests through the documented demo endpoint | All failed client TLS validation; alternate car endpoint also failed | No travel times, accuracy, or route latency measured. |
| Human/curation value | No participants or ongoing operating cycle | Not measured | No claim about low exception rate, retention, or incremental user value. |

The public catalog identified `2026-09-23.1` as the latest release. It was pinned rather than allowed to change during collection. The official reader supports geographic extracts. [Overture catalog](https://stac.overturemaps.org/catalog.json), [data access documentation](https://docs.overturemaps.org/getting-data/)

Direct Overture extraction took approximately **14.4 seconds for E, 10.0 for D, 22.7 for J, and 12.5 for B** in this environment, excluding installation and the failed first attempt. These are single batch-extraction timings. They do not measure search latency, refresh service-level performance, or global ingestion cost.

## 6. Automatic baseline coverage

### Counts before any confidence cutoff

| Area | All place records | Selected discovery candidates | Culture/heritage | Activity | Candidate local stop | Rows without taxonomy in the full extract |
|---|---:|---:|---:|---:|---:|---:|
| E | 10,466 | 1,056 | 154 | 61 | 841 | 341 |
| D | 255 | 44 | 9 | 4 | 31 | 6 |
| J | 1,796 | 84 | 44 | 2 | 38 | 178 |
| B | 1,247 | 195 | 17 | 16 | 162 | 46 |
| **Total** | **13,764** | **1,379** | **224** | **83** | **1,072** | **571** |

Measured from [Overture summary](R02_evidence/overture_summary.json). The selected pool is **10.0%** of all returned rows. Candidate local stops make up **77.7%** of the selected pool. A general nearby search will not automatically become a varied activity-discovery product simply by using this database.

The category rules are retained in [category_rules.json](R02_evidence/category_rules.json). Culture includes exact labels such as `museum`, `art_gallery`, `historic_site` and `monument`. Activity includes `movie_theater`, `escape_room`, `go_kart_club`, `bowling_alley` and related explicit labels. Local stops include cafés, tea rooms, bookstores, gift shops, and selected art/craft shops.

This rule intentionally omits generic shopping, generic arts/entertainment, gyms, restaurants, and event-planning businesses. It is a first-pass measurement rule, not a final taxonomy. We found relevant entities outside it, including Bujairi Terrace under `shopping` and a muvi cinema record under `shopping_mall`. Broader retrieval followed by classification is likely necessary. Expanding the filter also increases false positives and must be evaluated.

**Coverage is not recall.** We do not know how many real eligible venues are missing from these rectangles. High record volume can coexist with missing anchor venues, duplicates, closed businesses, and no usable event sessions.

## 7. Field completeness

### Stable fields in the selected Overture pool

| Area | Candidate denominator | Name | Any website value | Phone | Social link | Nonempty freeform address | Operating status value |
|---|---:|---:|---:|---:|---:|---:|---:|
| E | 1,056 | 1,056 | 509 | 638 | 866 | 842 | 0 |
| D | 44 | 44 | 21 | 21 | 34 | 31 | 0 |
| J | 84 | 84 | 32 | 37 | 79 | 59 | 0 |
| B | 195 | 195 | 100 | 122 | 156 | 157 | 0 |
| **Total** | **1,379** | **1,379** | **662** | **818** | **1,135** | **1,089** | **0** |

All selected records have point geometry and source metadata. A point does not establish an entrance or correct branch. A nonempty website field, present for **48.0%**, does not establish an official, reachable, useful, or reusable website.

Among website URL occurrences in the selected pool, 82 point to `locations.starbucks.sa`, 69 to `www.dunkinksa.com`, and 25 to `www.starbucks.com`. There are also 25 `linktr.ee` URLs, Instagram links, Google Maps links, and five URL strings without a parsed host. These are descriptive URL counts, not independently verified website outcomes. They suggest that measured contact completeness may favor chains and link aggregators.

### Practical fields

| Field needed by the product | Overture selected pool | Separate Eastern OSM sample | Interpretation |
|---|---|---|---|
| Opening hours | No column in retrieved schema | 26/353 have `opening_hours` | OSM can add some schedule leads, with syntax/freshness checks. |
| Price | No column | No `fee` or `charge` tags | A hard budget limit remains unresolved. |
| Expected visit duration | No column | 0 `duration` tags | A 90-minute outing cannot be certified from these extracts. |
| Booking rule | No column | 0 `reservation` tags | Absence is not permission to walk in. |
| Dated occurrence | No column | Not an event inventory in this query | Venue existence cannot answer what is happening this weekend. |
| Age rule | No column | Not measured systematically | Family and karting eligibility need offering-level evidence. |
| Indoor status | No column | 0 `indoor` tags | Some category-based inference is possible; confidence must be explicit. |
| Wheelchair access | No column | 0 `wheelchair` tags | Do not infer access from a generic venue category. |
| Live capacity | No column | Not provided | Requires an authorized inventory source or an honest handoff. |

OSM denominators differ from Overture. The OSM query includes parks and attraction geometries; it is not a matched venue sample. The comparison shows field availability in two retrieved datasets, not that one source has a higher overall coverage rate.

## 8. Confidence thresholds can destroy useful coverage

| Area | No confidence cutoff | At least 0.7 | At least 0.8 | At least 0.9 |
|---|---:|---:|---:|---:|
| E | 1,056 | 718 | 347 | 184 |
| D | 44 | 29 | 14 | 9 |
| J | 84 | 38 | 15 | 3 |
| B | 195 | 139 | 62 | 24 |
| **Total** | **1,379** | **924** | **438** | **220** |

The experiment also excluded records explicitly marked permanently closed, but every selected record had missing operating status. The actual reduction therefore came from confidence screening.

At 0.8, **68.2% of the selected pool disappears**. Every Foursquare-sourced record in the full extract has 0.77; 327 of those records were in the selected pool. Examples removed include teamLab Borderless, the Red Sea Museum, and the English At-Turaif district record. This is a measured property of this release and these rectangles, not a claim about every Foursquare dataset.

Overture documents that its confidence concerns existence and is not strictly calibrated across providers. That supports the observed need for source-aware interpretation. [Overture Places guide](https://docs.overturemaps.org/guides/places/)

**Recommendation:** retain source confidence as evidence. Do not interpret 0.77 as a 77% chance of a good visit, and do not adopt 0.8 as a global eligibility boundary. R03/R07 should evaluate identity plausibility, source agreement, freshness, and query-specific practical facts separately. The 438-row CSV is a diagnostic artifact, not the preferred corpus.

## 9. Identity, category, and location diagnostics

These examples are traceable to [anchor_matches.json](R02_evidence/anchor_matches.json) and the raw extracts. They are purposive checks, not a randomized error study.

| Anchor or record | Actual observation | Implication |
|---|---|---|
| Ithra Museum Galleries | Museum record found with confidence about 0.847; no website. A separate Ithra Theatre record also exists. | One complex has multiple usable sub-entities. Shared parent information needs explicit scope. |
| Scitech | Science-museum record found, confidence about 0.987, with a website path. | Identity is a useful starting point; it does not supply Saturday admission facts. |
| Escape the Room, Khobar | A high-confidence Khobar record links to the operator domain. A room page read later names a Riyadh branch above a Khobar footer. | Same domain is insufficient for attaching an offering to a branch. |
| At-Turaif | English district, Arabic district, and welcome-center records exist. The English record's website is a third-party tour-guide URL with an unrelated-looking path. | A website field cannot be accepted as official. Parent/entrance/duplicate ambiguity remains. |
| Bujairi Terrace | Found under generic `shopping`, outside the narrow selection rule. | Category-only retrieval misses relevant districts. |
| SAMoCA/JAX | No match in the initial `jax`, `samoca`, and selected Arabic name-pattern scan, while the district site lists SAMoCA. | Name-matching failure or missing baseline record requires investigation. This is not proof of dataset-wide absence. |
| teamLab Borderless | Found as an art museum, confidence 0.77, with the operator URL. | The 0.8 filter removes a useful enrichment lead. |
| Red Sea Museum | Found as a history museum with operator-domain URL and confidence 0.77. | Similar threshold issue; domain access failed in the research browser. |
| Nassif/Nasseef House | Several spelling/language variants occur, including nearby Arabic/English records and another museum record several hundred metres away. | A multilingual entity-resolution test is needed. These were not automatically merged. |
| Doos Karting | Found as `go_kart_club`, with a booking-domain link. | Indoor activity retrieval has a concrete candidate, but no session or price proof. |
| muvi Cinemas | Name indicates a cinema; taxonomy says `shopping_mall`. | Conflict between name and classification should trigger alternative retrieval, not unquestioned exclusion. |
| Boulevard district | Broad and ambiguous Arabic district-like records appear, including an event-planning classification. | A district is not the same entity as a show, attraction, or ticketed session. |

An exact normalized-name test for pairs within 100 metres found **zero pairs among the 438 confidence-screened candidates**. This weak test missed the language and threshold examples above. Reporting that result as “no duplicates” would be wrong. It also cannot decide whether two nearby records are branches, parent/child entities, or duplicates.

No entrance accuracy, geographic error rate, branch precision, closure rate, or deduplicated venue total is reported. Those require independent checks. The current samples are sufficient to design R03's difficult cases without inventing a production schema.

## 10. OSM comparison and freshness

The first Overpass endpoint failed TLS validation. A documented public mirror returned the Eastern query in **43.56 seconds**, with 353 elements and no response error remark. Its `timestamp_osm_base` was **2026-05-31T22:37:44Z**. The other rectangles produced an HTTP 504 or a 90-second client read timeout. We stopped after the bounded attempts. [OSM request manifest](R02_evidence/osm_manifest.json), [public instance documentation](https://wiki.openstreetmap.org/wiki/Overpass_API)

Of the 353 Eastern elements:

- 196 have a name.
- 26 have opening hours, approximately 7.4%.
- 14 have `website`, and one has `contact:website`. These tag counts are not asserted to be disjoint.
- 13 have a phone and three have `check_date`.
- None has the measured price, duration, reservation, wheelchair, or indoor tags.

The 26 hours-bearing elements comprise **16 cafés, three bookstores, six parks, and one coffee-shop-tagged retail record**. None of those 26 is a museum or a ticketed indoor activity. Several hours strings deserve review, including `Not-So 06:00-23:00`, a Friday 04:00 opening, and schedules with ambiguous missing separators. A syntax-valid schedule would still not prove current correctness.

**Interpretation:** this sample does not establish OSM as the automatic feasibility solution for the proposed cultural/indoor scope. It may help specific categories or stable geographic facts. The mirror timestamp means we must not treat successful retrieval as a fresh venue check. The failed other-area requests leave their OSM coverage unknown.

The OSM extract remains separate under ODbL. It was not joined into the Overture candidate database. Public Overpass service availability is also separate from OSM's data license; it should not become the production backend by accident. [OSM license](https://www.openstreetmap.org/copyright), [Overpass public-service guidance](https://dev.overpass-api.de/overpass-doc/en/preface/commons.html)

## 11. First-party enrichment evidence

The following are **research observations of public pages**, not measured production feed completeness. “Readable” means the research tool returned useful text. It does not establish a permitted extractor, stable API, cache right, or service guarantee. No practical fields from these pages were silently added to the open samples.

| Source / page | Fields or issue observed | What it would enable if rights and access were established | Remaining blocker |
|---|---|---|---|
| [Ithra museum programme](https://www.ithra.com/en/programme/2026/ithra-museum) | Search-index representation exposes dated September sessions, age/language and starting price. Direct page opening returned 403. | Occurrence-level discovery and parent/child programme modelling. | Indexed content is not live refresh; session capacity and reuse permission untested. |
| [Ithra Open Art Space](https://www.ithra.com/en/programme/2026/art-studio1/open-artistic-space) | Indexed page exposes a dated workshop-like opportunity, age threshold and box-office ticket wording. Direct opening returned 403. | More distinctive content than a venue pin. | No current machine feed, capacity result, or extraction permission established. |
| [Scitech hours](https://scitech.sa/working-hours) | Arabic text gives National Day dates and a no-advance-booking statement. | Special-hours and booking-rule interpretation. | The date exception does not establish normal Saturday hours. |
| [Scitech ticket prices](https://scitech.sa/p/24) | Different prices for scientific halls, IMAX, and a combined ticket; VAT statement. | Budget checking by offering. | A venue-wide scalar price would lose the distinction; no duration or live show inventory measured. |
| [Sparky's branch directory](https://sa.sparkysme.com/Home/Locations) | Individual branch names, locations, and hours are readable. | Branch-specific recurring hours, if authorized. | Pricing, attraction suitability, and live availability are absent from this page; generic shorthand requires interpretation. |
| [Escape The Room: The Prison](https://escapetheroomsa.com/rooms/the-prison/) | Player count and 60-minute duration appear, but the room says Riyadh while the footer says Khobar. | Duration/group fit after branch resolution. | A naïve extractor would attach a Riyadh room to the Khobar address. |
| [Diriyah visit page](https://www.diriyah.sa/en/plan-your-visit) | Landmark hours, last entry, date-bounded free access, parking and diversions. | Rich practical context at district scale. | Conflicts with FAQ; expired offers and road notices need their own validity intervals. |
| [Diriyah FAQ](https://www.diriyah.sa/en/faq) | At-Turaif hours and last entry differ from visit page. | A second first-party assertion. | Conflict is unresolved; “official” alone cannot select a winner. |
| [JAX FAQ](https://jaxdistrict.com/faq/) | District access differs from business/exhibition access. Studios generally do not accept casual visits outside announced sessions. | Prevents recommending private studios as walk-in attractions. | Specific activity dates and bookability remain separate. |
| [JAX what's on](https://jaxdistrict.com/whats-on/) | Recurring residents and hours appear alongside empty current/upcoming event messages. | Reusable operator relationships could cover several entities. | Resident listings are not dated occurrences; no events shown is not proof no events exist. |
| [teamLab FAQ](https://teamlab-jeddah.com/en/faqs) | Day-specific hours, last entry, approximate two-hour visit, ticket rules and accessibility statements. | Several feasibility fields from one operator. | Age wording needs reconciliation; capacity for the user's party is not established. |
| [teamLab booking page](https://teamlab-jeddah.com/en) | Next available date appears; group request explicitly does not guarantee booking. | A possible booking handoff. | A date label is not confirmation of four seats at 19:00. No booking API tested. |
| [Boulevard City](https://www.blvdcity.com/en/aboutus) | District operating interval is readable. | District-level orientation. | District open status says nothing about individual attractions or shows. |
| [Doos Hittin](https://www.dooskarting.com/hitten) | The text retrieval returned only image/tracking references. | A venue-specific source worth testing through permitted access. | No machine-readable practical fields demonstrated by this method. |
| [Riyadh Season](https://riyadhseason.com/) | The direct text open returned no content. | Potential seasonal inventory source. | Empty extraction must not become a zero-events claim. |
| [Red Sea Museum](https://redseamuseum.moc.gov.sa/) | Research tool could not access the domain. | A candidate first-party cultural source. | No current practical fields measured. |

These 16 source checks cover different pages, some belonging to the same operator. They are not 16 independent providers or 16 independent samples of user demand.

## 12. What the difficult examples teach us

### Official-source conflicts survive automation

The Diriyah visit page says At-Turaif starts at 17:00 with last entry at 23:00. The FAQ gives an earlier start and last entry at 23:30; its Friday closing text also contains an apparent AM/PM inconsistency. We did not decide which is correct. A system can automatically detect the disagreement and downgrade or omit the affected claim. It cannot turn two conflicting first-party statements into verified truth by averaging them. [Visit page](https://www.diriyah.sa/en/plan-your-visit), [FAQ](https://www.diriyah.sa/en/faq)

### Time exceptions need end dates

Scitech's hours page specifies National Day on 23–24 September 2026. Carrying that interval into Saturday 26 September would be an unsupported inference. Similarly, Diriyah's free-access announcement ends on 30 September. The next-weekend scenario on 2–3 October crosses that boundary. These are concrete reasons to store fact validity separately from retrieval time. [Scitech](https://scitech.sa/working-hours), [Diriyah](https://www.diriyah.sa/en/plan-your-visit)

### An operator page can mix branches

The Escape The Room page combines room-specific Riyadh text with a Khobar footer. A page-level “address” extractor would be unsafe. The relationship must be between the offering and its branch, not merely between a website and a brand. [Room page](https://escapetheroomsa.com/rooms/the-prison/)

### Access and duration can reject attractive candidates

A two-hour typical teamLab visit cannot fit comfortably inside a 90-minute total outing once arrival and onward travel are included. It could still be offered as an explicitly abbreviated visit if the user accepts that tradeoff and entry rules permit it. JAX studios cannot be assumed open simply because the district is accessible. [teamLab FAQ](https://teamlab-jeddah.com/en/faqs), [JAX FAQ](https://jaxdistrict.com/faq/)

**Interpretation:** the strongest first automation is often a reliable rejection or uncertainty decision. These cases do not establish that an LLM is needed for every query. They establish that entity scope, date scope, provenance, and unresolved conflicts must survive any parser.

## 13. Query-level feasibility diagnostics

We applied simple category selections to the retained Overture records to inspect the candidate supply for the following cases. This is a **data-sufficiency exercise**, not a benchmark of an implemented search engine. No parser, ranking model, route engine result, or user preference model is being claimed.

The category-pool counts below are measured before confidence filtering and deduplication. They are upper bounds on candidates to investigate, not counts of suitable answers. Museum pools include museums and art galleries. Active pools include selected gaming, karting, bowling and similar categories, but their indoor status is not assumed. The exact sets and counts are retained in [additional_metrics.json](R02_evidence/additional_metrics.json).

| Case | Query and explicit audit context | Initial pool | What prevents a confident answer | Allowed conclusion from this audit |
|---|---|---:|---|---|
| Q01 | “A museum near Khobar tonight, under 50 SAR.” E, 26 Sept, 18:00–22:00 | 19 museum records | Hours, offering price, journey, and current admission not in baseline. | Named cultural candidates exist; tonight's feasibility unproved. |
| Q02 | “Four of us, active indoors, under 150 each.” E, 26 Sept evening | 27 active records | Indoor status, group restrictions, price, sessions. | Relevant types exist; do not label them eligible for four. |
| Q03 | “Got 90 minutes before dinner, something cultural.” E, 26 Sept, 18:00–19:30 | 19 museum records | Duration, last entry, both travel legs, buffers. | No full time-fit proof. A venue's opening interval is insufficient. |
| Q04 | “Somewhere new and quiet around Khobar this weekend.” E, 2–3 Oct | 818 café records | New-to-user, atmosphere, quality, hours. | Raw abundance does not establish distinctiveness. |
| Q05 | “At-Turaif at 10 on Tuesday?” D, 29 Sept, 10:00 | Named district records | First-party hours conflict. | Explicit uncertainty; no confident “open.” |
| Q06 | “Can I drop into an artist's studio in JAX today?” D, 26 Sept | No occurrence inventory | Studio public-access rules and open-studio dates. | District access cannot satisfy this request. |
| Q07 | “Free workshop in Diriyah next weekend.” D, 2–3 Oct | No occurrence inventory | Date, price, age, registration/capacity. | No supported answer from audited automation; not evidence of no workshop. |
| Q08 | “Coffee around Bujairi before dinner, no long drive.” D, 26 Sept, 18:00–19:30 | 28 café records | Opening hours, precise origin/dinner point, routing. | Category retrieval works; time fit remains unresolved. |
| Q09 | “A museum around Al-Balad for us and two children.” J, 26 Sept evening | 8 museum records | Ages, child pricing, admission time and capacity. | Several named leads; party fit unproved. |
| Q10 | “teamLab with 90 minutes total.” J, 26 Sept | Named museum record | Typical visit alone is approximately two hours; travel also needed. | A complete visit is a poor fit under this duration evidence. |
| Q11 | “Interesting old places to explore around Al-Balad, no indoor booking.” J, 26 Sept afternoon | 38 heritage records | Public access, exterior/interior distinction, heat and walking route. | Plausible discovery direction, with narrower exterior-only claims needing evidence. |
| Q12 | “Which exhibitions will be on here next month?” J, 24 Oct | 8 museum records, no exhibition occurrences | Exhibition dates and admission. | Museum presence cannot answer programme dates. |
| Q13 | “Something active indoors near Hittin tonight.” B, 26 Sept evening | 8 active records | Indoor status, operating hours, offering eligibility. | Doos is a useful lead, not an automatic feasible recommendation. |
| Q14 | “Karting for four without booking, max 150 each.” B, 26 Sept evening | Active pool 8; named Doos lead | Walk-in rule, total price, session capacity, age/height. | Unknown booking status must not pass a no-booking constraint. |
| Q15 | “Somewhere to sit after midnight near Boulevard.” B, night of 26–27 Sept | 161 café records | Cross-midnight hours, branch access, district versus venue timing. | District hours cannot validate café hours. |
| Q16 | “What's happening in Boulevard on 24 October?” B, future date | No occurrence inventory | Programme publication, dates, cancellation and ticketing. | No automated event answer demonstrated. |

**Measured limitation:** none of the 1,379 selected Overture records contains the complete practical field bundle required for a strict time-, budget-, duration- and booking-constrained outing. That is a **0/1,379 baseline completeness result under this demanding definition**. It is not a 0% usefulness score, a global source-coverage result, or a measured end-to-end search success rate.

For the 16 diagnostics, no complete automated shortlist was demonstrated. Several cases could become useful discovery responses with explicit uncertainty and a source handoff. Whether users find those responses valuable enough is an R00/R09 observation question.

## 14. Revise the automation coverage metric

R01.2 proposed dividing automatically produced decision-ready candidates by all decision-ready candidates. On its own, this can reward a system that shows three easy choices and silently excludes everything else. It also becomes undefined when there are no established decision-ready candidates.

Use a fixed query set and report these measures together:

| Measure | Denominator | Current result |
|---|---|---|
| Baseline retrieval completion | Four defined Overture extraction tasks | 4/4 by direct access after the first method failed. |
| Category candidate supply | All 13,764 extracted records | 1,379 selected by the stated rules. |
| Baseline practical completeness | 1,379 selected records, strict practical bundle | 0 complete; schema omits critical fields. |
| Answer coverage | All predeclared user cases, including no-answer cases | Not established end to end. Sixteen data-sufficiency diagnostics are retained. |
| Automatic feasibility precision | Recommendations claiming to satisfy hard constraints, checked independently | Not measured; no such recommendations were issued. |
| Automatic decision-ready yield | Fixed candidate/query pairs, not only surfaced survivors | Not measured for the combined baseline/enrichment system. |
| User handoff burden | Completed user decisions | Not measured. Clicking through should not be counted as zero human work. |
| Human exception rate | Candidates or queries actually attempted by the combined automated workflow | Not measured. Missing data is not evidence that human checking is the only remedy. |
| Curation benefit | Comparable user choices with and without curated additions | Not measured. |

Maintain three distinct outcomes for each hard constraint: **supported**, **contradicted**, and **unknown**. Add a separate **conflict** state when credible assertions disagree. Do not turn unknown into false during coverage analysis or into true during recommendation.

For product claims, distinguish:

1. **Discovery lead:** a plausible entity with enough identity and context to inspect.
2. **Feasibility-supported candidate:** the required practical facts for this query are supported, with any permitted estimate disclosed.
3. **Booking-confirmed option:** the required date, session, party and inventory have been confirmed through an appropriate source.

The audit establishes a path to the first level. It has not established broad automatic coverage at the second or third level.

## 15. Query-time refresh: what is real and what remains hypothetical

### Demonstrated

The open baseline can be retrieved by geography without downloading the entire global dataset. Some records contain operator URLs. Public pages sometimes expose the missing practical fields. These are useful pieces of a future enrichment workflow.

### Not demonstrated

We did not obtain an authorized, repeatable machine feed for the practical fields, measure its latency or per-request cost, establish branch matching precision, or confirm available inventory. Research-tool page readability is not evidence that our future service may fetch and reuse that page at scale. Several pages were incomplete or unavailable through the text reader.

FSQ OS direct access now calls for a Places Portal account and token. We did not create an account. The Foursquare-origin rows received through Overture do **not** constitute an independent test of the full current FSQ OS dataset. [FSQ access documentation](https://docs.foursquare.com/data-products/docs/access-fsq-os-places)

The audit also did not call a commercial Places, routing, or event API. No relevant keyed integration was provisioned for this study. R01's rights restrictions remain in force. In particular, changing a restricted provider lookup to query time does not automatically create retention, transformation, or display rights. [R01](R01_Source_Rights_and_Economics.md)

### The next specific enrichment proof

Test one cultural operator and one repeatable activity operator with an explicitly permitted source. For each, require the following evidence before making it a dependency:

| Question | Evidence required |
|---|---|
| Is reuse allowed? | Named product/feed and permission covering the proposed fields, display, retention and refresh. |
| Is the target the correct venue/branch? | Stable operator ID, branch ID, address and offering relationship. |
| Does a response resolve this query? | Date-specific hours/last entry, price unit, duration, booking rule; capacity only where available. |
| Does the source behave repeatedly? | A small repeat sample across ordinary hours, a weekend and one exception/change. |
| Is a missing response survivable? | Degrade to a clearly qualified lead or omit the unsupported claim. |
| Is it economical? | Actual calls, retries, latency, cache policy, cost and user handoffs per answered case. |

This is an integration feasibility experiment, not a request to maintain hundreds of venues manually. If no permitted practical source can be secured for even these cases, the product promise should change before coverage expands.

## 16. Travel-time audit

We selected synthetic public-area origins and three Overture landmark coordinates in each rectangle. These are test points, not the user's location. Targets included Ithra/Scitech, At-Turaif/Bujairi, teamLab/Nasseef, and Doos/muvi. We attempted four driving and four walking matrices, each with one origin and three destinations.

The client reported an expired-certificate validation failure for every request to the FOSSGIS endpoint. An alternate official OSRM car endpoint produced the same class of failure. Certificate validation was not disabled. A research-browser attempt also did not return route data. [Recorded route attempts](R02_evidence/route_results.json)

**Result:** no route duration, route accuracy, routing success rate in normal service, or provider comparison was measured. The subsecond failure times are connection-failure timings, not route computation latency. This cannot be used to claim that routes are unavailable in Saudi Arabia or that OSRM itself is unsuitable.

The documented demo service is rate-limited and provides no production guarantee. Its use here was a small research test, not a chosen product dependency. [OSRM demo documentation](https://github.com/Project-OSRM/osrm-backend/wiki/Demo-server), [routing service details](https://routing.openstreetmap.de/about.html)

The architecture implication is still concrete. A maximum-travel-time constraint cannot pass on a radius alone. Query-time routing also needs correct entrances, mode, departure time, last-entry time, and any onward commitment. The Diriyah page's road-diversion notices show why endpoint geometry and local access matter. R08 should compare an authorized traffic-aware service with a maintained open-routing baseline, then validate a small number of journeys. [Diriyah visit information](https://www.diriyah.sa/en/plan-your-visit)

No route provider should be selected from R01's list-price estimates or these failed demo requests.

## 17. Human exceptions and user handoffs

The audit identifies likely exception types, but does not measure their production frequency.

| Situation observed | First automated response to test | When human intervention may be justified |
|---|---|---|
| Missing duration | Leave unknown; prefer another candidate for a tight interval | Repeated high-demand offering with no alternative source. |
| Conflicting operator hours | Preserve both assertions; avoid an unconditional open claim | A recurring, important source conflict that blocks many queries. |
| Expired date exception | Stop applying it after its validity interval | No ordinary schedule exists and the venue is repeatedly requested. |
| Branch ambiguity | Avoid attaching the offering until identifiers agree | Entity split/merge or operator confirmation. |
| Missing capacity | Link to authorized booking flow and label capacity unconfirmed | Usually a booking-system issue, not editorial maintenance. |
| Suspect category | Retrieve through alternate evidence and flag for classification | Repeated false positives/negatives in important categories. |
| Unavailable source | Use cached data only if rights and freshness allow; otherwise qualify or abstain | Persistent provider issue, not every failed user request. |
| Low novelty evidence | Offer neutral description; avoid “hidden gem” claim | Selective editorial addition with demonstrated user value. |

Some unknowns should lead to a narrower claim. Some should lead to another candidate. Others may be resolved through an operator-maintained source. None of these automatically requires a human to recheck the whole geography.

Equally, pushing every uncertainty to a user is not free automation. If the user still checks hours, pricing, route, and booking on four other sites, the product may have reproduced the workflow R00 intended to improve. Measure **remaining checks per chosen outing**, not merely back-office labor.

## 18. Curation and local distinctiveness

The candidate mix is a warning for the local-discovery promise. Cafés and similar stops account for 1,072 of 1,379 selected records. Some of the most frequent website domains belong to large chains. A high field-completeness threshold could further concentrate results around those businesses.

This is a hypothesis about selection bias, not a measured recommendation outcome. We did not assess taste, quality, ownership, local importance, or whether a participant had visited a place. No venue was awarded a hidden-gem score.

For the next observed experiment, add a small, permissioned set of distinctive offerings rather than a general manual-verification backlog. Examples worth investigating include a current exhibition, a public art session, or a documented local studio opening. Compare those additions against the uncurated baseline on:

- whether they enter participants' serious shortlists;
- whether participants had already heard of them;
- whether they add a different type of outing;
- whether the information eliminates practical checks;
- how often their facts need exceptional attention.

Keep added value and maintenance effort separate. A distinctive item may be worth one editorial investigation without needing a recurring city-wide operations team. That remains unvalidated until actual choice behavior is observed.

## 19. Candidate geography assessment

| Environment | What this audit actually found | Main risk for the first promise | Recommended role |
|---|---|---|---|
| Eastern sample | Largest and broadest raw sample; concrete Ithra, Scitech and indoor-activity leads; some first-party practical information. | Broad rectangle, travel burden unmeasured, operator/branch and special-hours problems. | Strong candidate for the next source experiment, narrowed to a specific user origin and a few operators. |
| Diriyah/JAX | Smaller baseline; Bujairi/At-Turaif records; district site contains practical information and explicit studio-access rules. | Open data misses or misclassifies important district entities; official hours conflict. | Valuable compact stress case for parent/child identity and source conflict, and a possible operator-led pilot. |
| Al-Balad | Named teamLab, Red Sea Museum and Nasseef records; rich teamLab FAQ. | Sparse activity categories, multilingual identity variants, source access and booking uncertainty. | Good second context for cultural discovery and walking/entry tests. |
| Boulevard/Hittin | Concrete karting/cinema candidates and many café records. | Attraction/session information differs from district hours; time-sensitive inventory is not established. | Keep as the entertainment stress case; defer a broad first-promise commitment without a permitted practical source. |

**No final launch winner is justified.** The rectangles differ in size, there is no independent denominator, routing was not measured, and participant access has not been established. The Eastern sample's higher count is not a reason to launch across the entire urban cluster.

For the next bounded experiment, prioritize **one Eastern cultural/indoor subcatchment**, with a fixed origin selected during participant recruitment, and **one compact contrast case in Diriyah/JAX or Al-Balad**. Choose the contrast according to which operator can provide permitted practical data and where users can be observed. This preserves a geographical choice instead of locking one from map-pin counts.

Hayy Jameel surfaced during source research, but it is outside the Al-Balad rectangle. It was not added to improve Al-Balad's measured supply. Its visitor page demonstrates useful first-party information but is not part of the quantified catchment sample. [Hayy Jameel visit page](https://hayyjameel.org/visit/)

## 20. Recommended content and promise adjustment

The strongest testable direction is:

> Help me discover a small set of plausible cultural or indoor outings around my chosen area, make their practical fit clear where supported, and tell me exactly what still needs confirmation.

This is a hypothesis for testing user value, not permanent positioning. It retains location, intent and time, while avoiding a promise that the current data cannot support.

### Include in the next experiment

- Cultural venues and stable repeatable offerings with an identifiable operator.
- A few indoor activities whose duration and group rules can be obtained through an authorized source.
- A small selection of current exhibitions or workshops only where occurrence dates and access rules are available under suitable rights.
- A limited number of distinctive local stops, with editorial novelty claims separated from basic place facts.

### Defer or qualify

- Comprehensive “everything happening tonight” coverage.
- Guaranteed walk-in access or live availability.
- Entire-city independent-shop and café coverage presented as hidden gems.
- Camping, hiking, paintball safety/access assurance, or remote outdoor feasibility.
- Global quality promises based on these Saudi rectangles.
- Automatic itineraries and proactive suggestions before feasibility evidence exists.

The audit does **not** justify abandoning cross-domain discovery and becoming a café finder because cafés are easier to retrieve. It justifies limiting the number of domains whose practical facts we promise to resolve at first.

## 21. Economics after the measured audit

### What was incurred and measured

No provider subscription, paid source request, or account purchase was initiated. The retained Overture payload totals **20,090,266 bytes**, approximately 20.1 MB in decimal units. The successful OSM response is approximately 73 KB. These are local retained payload sizes, not measured total network transfer. Dataset license access cost for these open extracts was zero; compute, bandwidth, tooling, and researcher time are not economically free.

This audit did not measure a maintained operating cycle. It therefore cannot replace R01's illustrative labor scenario with a new reliable monthly cost estimate. It also cannot claim that the product will operate at zero recurring data cost.

### A better cost model to carry forward

Separate:

1. baseline acquisition, processing and periodic release refresh;
2. candidate-level query-time calls allowed by the source contract;
3. routing calls after rough geographic selection;
4. exceptional source/identity review;
5. user effort left after the recommendation.

The useful denominator is an **answered outing decision at a stated confidence level**. An inexpensive API call that leaves every critical fact unknown is not an inexpensive completed decision.

**Illustrative workload only:** 1,000 searches, six enriched candidates per search, two field-source calls per candidate, and a 20% lawful cache-hit rate would generate 9,600 enrichment calls before retries. Actual price is unknown until the provider, permitted caching and required fields are chosen. This scenario is not a traffic forecast or a cost quote.

Human-exception sensitivity also changes the economics. At an assumed five minutes per escalated query, exception rates of 1%, 5% and 20% across 1,000 queries would require about **0.8, 4.2 and 16.7 hours**, respectively. Those rates and minutes are hypotheses, not audit measurements. A single source correction may fix many queries, so deduplicate exception work rather than multiplying by every affected result.

The next economic question is whether a small number of permitted, operator-maintained integrations resolve many high-value decisions. R02 does not support routinely paying people to update every retrieved venue.

## 22. Logical architecture implications

These are boundaries and requirements for later research, not a production design.

| Evidence from this audit | Implication |
|---|---|
| Baseline schema lacks practical fields | Keep identity/discovery acquisition separate from practical-fact acquisition. |
| Same source confidence value across FSQ rows | Treat confidence according to source and meaning; do not use one universal cutoff. |
| Categories miss Bujairi and muvi | Candidate generation needs alternate labels/name evidence; evaluate false positives when broadening. |
| Venue, room, exhibition and district scopes differ | Preserve entity type and parent/child/host relationships. |
| Khobar footer on Riyadh offering page | Resolve branch before attaching practical facts. |
| Official hours conflict | Retain field-level assertions, validity, provenance and unresolved conflict. |
| OSM mirror timestamp is old | Track dataset snapshot time separately from request time and fact-check time. |
| Initial catalog filter returned no files | Distinguish source failure, empty result and missing coverage. |
| Entry deadline differs from closing | Temporal feasibility needs last-entry and duration, not just open/closed. |
| No capacity feed tested | Keep bookability separate from existence, schedule and general admission rules. |
| Source licensing differs by row/product | Rights checks apply before indexing, enrichment, caching and display. |
| No route response obtained | Hard travel constraints cannot silently fall back to confident radius claims. |

A conceptual sequence remains sensible: identify candidates, attach only permitted evidence, resolve query-specific feasibility, rank what remains, and expose uncertainty. The audit provides no reason to choose microservices, a vector database, agents, or a specific frontend.

The current Overture release uses `taxonomy` and `basic_category`. Our actual extracts have no old `categories` column. R03 must inspect real release schemas and keep provider adapters versioned instead of inheriting a stale schema from an earlier concept. [Retrieval manifest](R02_evidence/retrieval_manifest.json)

## 23. Rights boundaries and retained evidence

The Overture source metadata in the selected pool identifies **1,035 CDLA-Permissive-2.0 records, 327 Apache-2.0 records, and 17 CC0-1.0 records**. The Apache records originate from Foursquare, and the CC0 records from AllThePlaces. The license is retained on each raw claim rather than assigned from a generic “open data” label. License texts and notices are saved with the evidence. [Overture attribution](https://docs.overturemaps.org/attribution/), [Foursquare notice](https://opensource.foursquare.com/places-notice-txt/)

The separate OSM extract is credited to OpenStreetMap contributors and governed by ODbL. This audit does not resolve the legal implications of a production merged database. It avoids using the OSM sample to overwrite the Overture sample. [OSM copyright and license](https://www.openstreetmap.org/copyright)

Reading a first-party page to understand source capabilities did not create a right to repeatedly collect it into the product. No webook listings, commercial Places responses, reviews, photos, or social posts were imported into a persistent candidate index. Current webook terms include restrictions on automated collection and content reuse; the report does not treat a booking link as permission for an inventory feed. [webook terms](https://webook.com/business/en/legal/terms)

For future enrichment, retain the distinction between an open place record that contains a URL and the separate rights in the content at that URL. Public contact links do not license the linked text, media or booking data.

## 24. International scaling implications

This audit is compatible with international ambition, but it does not validate international execution.

The reusable part is the mechanism: geographic baseline acquisition, source-aware identity, query-specific facts, explicit uncertainty, and a bounded exception queue. The non-uniform part is practical coverage: local operator websites, language, calendars, holiday rules, transport, booking systems and legal rights.

A credible expansion rule should require evidence at the **area × content family × promise level** combination. A city may support museum discovery but not workshop availability. One country may have a useful event feed while another requires a narrower source strategy. The same website can offer different confidence levels in different places, provided those differences are visible and useful to users.

Before claiming global scalability, repeat the same fixed query and field checks in at least one non-Saudi context using permitted data. Compare automatic answer coverage, source concentration, unresolved hard constraints, and remaining user checks. Do not extrapolate local Saudi operator-page failures into a global impossibility, or global open-data counts into universal usefulness.

## 25. R02 decision gates

The five gates below follow R01.2. “Unproven” means the audit does not have sufficient evidence; it is not a prediction that the gate will fail.

| Gate | Decision | Evidence and consequence |
|---|---|---|
| **A. Enough automatic baseline discovery density?** | **Conditional** | Automatic raw supply is demonstrated in all four areas. Usable distinct-venue density, missing anchors, category precision, travel reach and user value are not established. |
| **B. Automatic refresh of volatile shortlist facts?** | **Unproven** | Public-page evidence identifies useful fields, but no permitted practical feed was integrated and measured. The open baseline lacks those fields. |
| **C. Useful top results with some unknowns?** | **Unproven** | Plausible leads and specific rejection cases exist. No user study shows whether qualified leads reduce decision effort enough. |
| **D. Low enough human exception rate for scaling?** | **Unproven** | No repeated enrichment/decision workflow ran. Missingness cannot be translated directly into a labor rate. |
| **E. Curation adds enough value?** | **Unproven** | Source mix makes the question relevant; no controlled user comparison was performed. |

### Can R03 proceed?

**Yes, conditionally.** Use these actual records to define places, branches, districts, offerings, occurrences, claims and rights. Include the identified failure cases. Keep the model adaptable while practical feed access remains unresolved.

### Can R04 and R05 proceed?

**Yes as provisional research.** R04 can formalize unknown/conflict/expiry handling from real examples. R05 can turn the 16 cases into annotated evaluation fixtures, alongside the R00 corpus. Positive “feasible” labels require additional evidence; do not label missing information as confirmed failure.

### Can we lock the MVP, choose the final geography, or begin major implementation?

**Not yet.** The immediate unresolved issue is one lawful, repeatable practical-data path and whether its output improves a real user's decision. Expanding the baseline or adding sophisticated semantics would not settle that question.

## 26. What this changes in the research sequence

Keep the research ladder, with a short practical-data experiment before the project treats R06/R07 as settled architecture.

1. **R02 follow-through: permitted enrichment proof.** One cultural operator and one repeatable activity operator, a small fixed candidate set, actual date/group constraints, and repeated checks. This is completion of the unproven gate, not a new broad research programme.
2. **R00 observation sessions.** Use ordinary tools first, then compare a small evidence-backed discovery output. Measure remaining checks and willingness to choose despite stated uncertainty.
3. **R03 domain and identity.** Work from the raw samples and anchor problems. Do not start with a universal “Experience” table that erases branch/occurrence distinctions.
4. **R04 trust and freshness.** Define validity intervals, exceptional hours, conflict handling, source refresh and claim levels.
5. **R05 intent and evaluation.** Combine R00's natural-language cases with measured data limitations and a fixed denominator.
6. **R06/R07 retrieval and ranking.** Evaluate category expansion and provider-aware evidence only after the test set has credible labels.
7. **R08 travel feasibility.** Rerun through an authorized maintained routing path and validate representative entrances/journeys.

These are dependencies and experiments, not a locked delivery roadmap.

## 27. Prioritized next actions

| Order | Concrete action | Required result | Why it matters |
|---:|---|---|---|
| 1 | Discuss the claim level: supported feasibility versus qualified discovery leads. | Agree which unknowns users may reasonably accept and which must block a result. | Otherwise the audit's success criterion remains ambiguous. |
| 2 | Obtain a permitted practical-data route for one cultural and one indoor-activity source. | Written/source-documented rights and a retrievable field sample. | This is the largest unproven technical/business dependency. |
| 3 | Run a small repeat enrichment experiment against fixed cases. | Actual retrieval success, response time, correct branch/occurrence, resolved fields, and failures across at least two relevant time windows. | Tests automation rather than theoretical extractability. |
| 4 | Observe initial R00 participants making the same kind of outing decision. | Exact tool checks, rejected candidates, remaining uncertainty and chosen option. | Determines whether the narrower promise creates value. |
| 5 | Produce R03 using the retained examples. | Conceptual entities/relationships and identity-review rules; no full production schema. | Prevents costly errors around branches, districts and sessions. |
| 6 | Add a maintained route source to the same small cases. | Measured route results and entrance checks, with no live-traffic claim unless supported. | Required for genuine 90-minute/max-travel-time tests. |
| 7 | Reassess content/geography with query-level answer coverage. | A justified pilot combination or a documented promise change. | Avoids choosing the area with the largest raw pin count. |

## 28. Open questions we should discuss

1. If we can give an appealing shortlist but require one final operator check, is that still enough improvement over the current workflow?
2. Which fields must be resolved for the first promise: ordinary hours only, or also duration, price and booking rules?
3. Can a small number of source relationships cover enough varied outings without creating a permanently partner-dependent product?
4. Do users prefer a distinctive but partly uncertain option, or a familiar option with stronger practical information? This cannot be decided from source coverage alone.
5. Can we support explicit “no advance booking” queries at all without a permitted inventory/rules source?
6. Is repeatable cultural/indoor discovery useful often enough for residents, or does it need dated events sooner than the data supports?
7. Where can actual participants be recruited and source evidence checked with the least friction?
8. What degree of source-specific licensing and display complexity is acceptable before a provider's benefit stops justifying it?

## 29. Reproducibility and evidence inventory

The raw samples, exact rectangles, release, request outcomes and calculation helpers are in [R02_evidence](R02_evidence/README.md). The important files are:

- [retrieval_manifest.json](R02_evidence/retrieval_manifest.json), including payload hashes and source schema.
- [overture_summary.json](R02_evidence/overture_summary.json), including category and confidence sensitivity counts.
- [category_rules.json](R02_evidence/category_rules.json), the exact initial category rule.
- [additional_metrics.json](R02_evidence/additional_metrics.json), the diagnostic query pools and OSM tag counts.
- [screened_candidates.csv](R02_evidence/screened_candidates.csv), the diagnostic 0.8 subset, not an endorsed shortlist.
- [anchor_matches.json](R02_evidence/anchor_matches.json), post-hoc name-pattern matches including false positives.
- [osm_manifest.json](R02_evidence/osm_manifest.json), with server snapshot date and failed request outcomes.
- [route_results.json](R02_evidence/route_results.json), recording failed routing attempts rather than fabricated travel times.

Licenses and source notices accompany the extracts. Web citations point to the inspected pages; those pages can change after this date. No confidential account data, real-user locations or participant data were collected.

# Most important findings

1. **Automated place acquisition works in the sampled areas.** We retrieved 13,764 records and selected 1,379 discovery candidates without manual venue backfill.
2. **The baseline does not establish practical feasibility.** It lacks the fields that would answer hours, budget, duration, booking and capacity constraints.
3. **A global confidence cutoff is dangerous.** Every Foursquare-origin record in the full sample had 0.77, so a 0.8 cutoff removed useful attractions wholesale.
4. **Category-only retrieval misses real discovery targets.** Bujairi and muvi illustrate category/intent mismatch, while cafés dominate the selected pool.
5. **Official information can be ambiguous or contradictory.** Date exceptions, conflicting hours, and mixed branch context need explicit handling.
6. **Successful retrieval is not freshness.** The OSM response had a database timestamp almost four months before the audit; other source requests failed.
7. **Query-time enrichment is still an unproven dependency.** A readable page, a booking button, and a permitted reliable feed are different things.
8. **Human-maintenance cost remains unknown.** The audit supports neither a city-wide verification team nor a claim of effortless automation.
9. **The next decision is about practical data and user value.** More raw records or an advanced ranking model will not answer it.

# What we know

The open baseline supplies relevant types of places in all four rectangles. Its field omissions, source-confidence distribution, and category problems are measured and reproducible. Specific first-party pages contain useful practical information and specific failure cases. The audit did not establish reliable automated live feasibility, low human exceptions, or a launch geography.

# What we think

A narrow cultural/indoor discovery product with source-aware practical information may be viable without routine manual maintenance of an entire city. A few permitted operator sources could be more valuable initially than another broad POI subscription. Qualified uncertainty may be acceptable when the shortlist is distinctive and reduces user effort. These are hypotheses.

# What we still need to observe

An authorized practical feed resolving real queries repeatedly; route and entrance accuracy; actual booking-rule and price correctness; users choosing from uncertain versus fully supported options; repeated usage; and the exceptional human work needed after automation runs over time.

# Assumptions not to lock in

Saudi Arabia as the permanent launch market, the Eastern cluster as a single travel catchment, 0.8 as a universal confidence threshold, cafés as the easiest first product, scraped public pages as an enrichment strategy, missing availability as walk-in permission, all official pages as equally authoritative, and a fixed monthly verification-labor budget.

# R02 conclusion

**Proceed with the project, but keep the feasibility claim conditional.** R02 has supplied actual source records and concrete failure mechanisms that can guide R03–R05. It has not passed the automation, user-value, or operating-cost gates needed to lock an MVP.

The next evidence to seek is small and specific: **one lawful practical-data path, applied repeatedly to a fixed set of outing decisions, followed by observation of how much checking the user still has to do.** If that fails, adjust the promise or scope before expanding the dataset or adding a manual operations team.
