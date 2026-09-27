# Product & Technical Concept — Architecture Review & v0.2 Development Report

**Date:** 25 September 2026  
**Basis:** *Product & Technical Concept v0.1* (the project foundation)  
**Status:** Concept review and research agenda. This report proposes decisions to test; it does not specify a production schema or implementation roadmap.

## 1. Executive Assessment

The strongest idea in v0.1 is to answer a practical decision: **What can I realistically and enjoyably do in this area during my available time?** That requires one discovery experience across permanent venues, scheduled occurrences, and activities. The document correctly puts data quality, time, geography, retrieval, and ranking ahead of an AI planner.

The concept is still too broad to validate as written. "Places, events, activities, outdoors, shops, hidden gems, trips, planning, and assistance" describes an eventual platform, not a first user promise. A result can be relevant in meaning yet unusable because it is closed, cancelled, fully booked, too far by the available transport mode, or supported only by stale evidence. Such failures are likely to matter more than a small improvement in semantic similarity.

**Recommended product thesis:** help a person find a *feasible, appealing option* for a specific place and time, including options they would have missed in category search. The initial test should compare this promise against the way people currently search, in one dense geographic area and a deliberately narrow set of content with verifiable operating times.

**Major corrections to v0.1:**

1. Separate the user-facing discovery item from the underlying venue, offering, occurrence, and location. The eight proposed object types mix entities, subtypes, geometry, and editorial groupings.
2. Make eligibility and uncertainty explicit. "Open now" and "available tonight" are claims requiring different evidence; unknown must not silently mean yes.
3. Put source rights before source ingestion. A provider API response does not automatically grant permission to retain, merge, index, or enrich its content.
4. Treat "hidden gem" as an evidence-backed editorial or ranking judgment, not a category or a low-review filter.
5. Evaluate search against a fixed query and result set before deciding that LLM parsing, embeddings, or a separate search engine add value.
6. Define the MVP by **coverage and query success**, not by a checklist of map, smart search, saving, and categories.

**Evidence convention.** **Documented fact** refers to a cited product or technical document current at review time. **Engineering recommendation** is an architectural judgment. **Hypothesis** needs field research, an experiment, or a legal/commercial review. Provider terms, capabilities, and prices must be checked again at procurement and launch.

## 2. Product Reconstruction

### The job and the initial user

The user is making a small but consequential choice under constraints: limited time, an actual starting point, uncertain interests, and incomplete local knowledge. A visitor may ask the same question for a future date and unfamiliar neighborhood. The platform should turn a vague desire into a few credible options, with enough detail to decide and act. The likely first user is a person choosing a near-term outing in a known launch area; travelers are a second context for the same discovery engine. **Hypothesis:** this user has frequent enough unmet needs to return without a trip-planning feature.

Existing products already cover much of the surface. Google Maps documents local events, things to do, and saved places; AllTrails has detailed trail filters; Tripadvisor covers attractions and bookable experiences. The gap is therefore **not** "nobody offers discovery." The proposed gap is cross-domain choice under combined time, travel, preference, and trust constraints. That gap must be measured in user tests rather than asserted as a market fact. [Google Maps Help](https://support.google.com/maps/answer/144349?hl=en), [AllTrails filters](https://support.alltrails.com/hc/en-us/articles/37227964040852-How-to-use-filters-to-find-trails), [Tripadvisor](https://www.tripadvisor.com/)

### Core system versus features

The core system maintains a permitted, sufficiently current set of discoverable options; interprets the request; retrieves candidates; rejects infeasible candidates; ranks and diversifies the rest; and shows the evidence behind practical claims. Search, time reasoning, geographic reasoning, source governance, and evaluation are infrastructure. Natural-language entry, filters, list/map views, result details, and saving are product interfaces to it. Itinerary construction, monitoring, and notifications consume the same core but are separate products with additional reliability duties.

The v0.1 chain "Data → Understanding → Retrieval → Ranking → Discovery → Planning → Assistance" is a good dependency statement. In operation it is a loop: failures and user feedback must update data, labels, and ranking. It also needs a rights gate before data enters the canonical corpus and a feasibility gate between retrieval and ranking.

## 3. Core Thesis

"Spatiotemporal discovery engine" is accurate technical shorthand. It is too abstract as a user promise. A stronger external promise is **"find something worthwhile that actually fits your time and location."** It expresses the practical benefit and makes reliability testable.

| Layer | Capabilities | Why it belongs there |
|---|---|---|
| **Core** | Licensed local coverage; correct entity identity; location and time feasibility; useful mixed-type retrieval; trustworthy result details; evaluation | A failure in any one defeats the initial choice. |
| **Supporting** | Natural-language interpretation; semantic retrieval where it improves recall; saved items; light editorial curation; variety; concise explanations | These improve access to a working discovery corpus. |
| **Future / optional** | Full itineraries; schedule import; route detours; alerts; personalization models; booking; social contribution; business tools | Each needs additional data, consent, operational support, or evidence of demand. |

**What must be exceptional:** useful coverage in the chosen area, low false-positive rates for availability and location, and discovery beyond the obvious without sacrificing quality. A conversational interface is secondary. The platform should avoid becoming a general map, a broad directory with thin records, an event-ticket marketplace, or an autonomous itinerary agent. Those positions expand obligations faster than the proposed advantage.

## 4. User Modes

The three v0.1 modes overlap. "Explore Now" includes this weekend, while "Explore Destination" may include "tonight" from a different city. "Plan & Follow" combines deliberate planning with automated monitoring. **Engineering recommendation:** model one discovery task with independent context dimensions, and treat plan management as a later workflow:

- **Place context:** here, a selected area, a future destination, or a route corridor.
- **Time context:** now, a bounded free window, a named period, or dates not yet known.
- **Intent certainty:** specified activity, experiential preference, or open-ended exploration.
- **Commitment:** browse, save, compare, place in a schedule, or monitor for changes.

This avoids separate search logic for local and trip use. A future destination still needs temporal caution: a venue visible today is not proven open during a visit next month.

| User statement | Interpretation | Search behavior |
|---|---|---|
| "I have 90 minutes before dinner." | Fixed end time; total door-to-door budget. | Include outward travel, visit duration, return/onward travel, and buffer. |
| "I am bored tonight." | Broad intent, near-term time, unclear budget and transport. | Offer a varied set; infer only low-risk defaults and expose them. |
| "I'm visiting Tokyo next month." | Future destination, dates and neighborhoods missing. | Ask for or allow area/date refinement; show durable options with event uncertainty. |
| "Along tomorrow's route." | Route geometry and departure time are required. | Retrieve corridor candidates; validate detour, not point-to-line distance alone. |
| "What opened recently near me?" | Opening date, not publication date. | Use verified opening evidence; distinguish new listing from new business. |
| "What is happening this weekend?" | Occurrences within a local calendar window. | Resolve timezone/weekend convention; exclude ended or cancelled instances. |
| "Quiet but unusual." | Two soft experiential preferences. | Retrieve by attributes and descriptions; show why each matches. |
| "Surprise me." | Broad discovery request. | Ask for a minimal area/time boundary or use visible defaults; maximize useful variety. |

The missing scenario is **"compare a small set and decide"**. The unit of value is not opening a map; it is confidently choosing an option. Also distinguish **browse without a date** from **go now** so permanent places are not wrongly filtered by current hours.

## 5. Domain Model

The v0.1 object list mixes persistent identity ("Place"), scheduled occurrences ("Event"), an activity offered by an operator, route geometry, temporary duration, and curated lists. A stronger conceptual model is:

| Concept | Meaning and key relationships |
|---|---|
| **Site / venue** | A persistent physical destination or facility; may contain other sites and host many offerings or occurrences. A branch is its own site. |
| **Organization / operator** | Business, museum, guide, or event organizer; may operate many sites or offerings. A chain is an organization relationship, not a single place. |
| **Offering** | A repeatable thing a user can do: karting, guided tour, workshop, museum visit. It may have duration, price, requirements, and one or more sites. |
| **Occurrence / session** | A dated instance: concert, festival day, workshop slot, tour departure, exhibition run. It has status and potentially capacity. A series groups recurring occurrences. |
| **Location / geometry** | Point, area, path, remote/online, or changing meeting point attached to a site, offering, or occurrence. Geometry is not always a point. |
| **Availability rule / claim** | Opening pattern, occurrence interval, booking window, seasonal period, or capacity observation, each with source and uncertainty. |
| **Collection** | Editorial or user grouping of discoverable items; a content layer, not a real-world entity type. |
| **Discovery item** | Search presentation of a site, offering, or occurrence at a particular context; it prevents separate venue and its workshop from appearing as unhelpful duplicates. |

Relationships include **located at**, **operated by**, **hosts**, **part of series**, **instance of**, **occurs at**, **contained within**, **starts at/ends at**, and **replaces/supersedes**. The model must allow many-to-many relations and validity dates. It should preserve stable internal identities when a business changes its name or an event is rescheduled.

| Difficult case | Modeling decision |
|---|---|
| Museum and exhibition | Museum is a site; exhibition is an offering or dated series, with occurrences if admission windows matter. |
| Karting venue with several activities | One site, multiple offerings, separate sessions where booking requires them. |
| Multi-venue festival | Festival is a series/program; sessions occur at distinct sites. Do not collapse to a single point. |
| Seasonal market | Recurring series plus season-specific occurrences; a seasonal site only if its location/facility itself is temporary. |
| Online event | Occurrence with remote location; exclude from "near me" unless explicitly allowed. |
| Time-slot activity | Offering plus bookable sessions; "open venue" does not imply a free slot. |
| Hiking trail | Route geometry plus access points, duration/difficulty and condition claims; a route can be a discoverable offering. |
| Guided tour with changing meeting points | Offering and session-specific meeting location. |
| Pop-up inside a business | Temporary offering/site linked to host; preserve both identities. |
| Chain with branches | Organization plus distinct branch sites; branch-level hours and coordinates. |

"Outdoor Experience" and "Temporary Place" work better as attributes or subtypes. "Experience" is too broad to own a separate identity unless a concrete operator offers it. "Event" should distinguish a series from a particular occurrence. This is conceptual only; the physical schema can follow after source study.

## 6. Taxonomy

Use a **hybrid**: a small controlled hierarchy for stable "is-a" types, orthogonal facets for practical properties, evidence-backed experiential attributes, and explicit relations among entities. Free tags can capture emerging local language but should not become ungoverned filters. Embeddings can aid recall; they are not a taxonomy or evidence of facts.

| Dimension | Examples | Treatment |
|---|---|---|
| **What it is** | café, museum, live performance, trail, guided tour | Controlled, multilingual, multiple inheritance only where useful. |
| **What it offers** | coffee tasting, pottery class, exhibition, walk | Offering/occurrence relationship. |
| **Practical facets** | indoor, step-free, price, typical duration, reservation, exertion | Typed claims; unknown is distinct from false. |
| **How it may feel** | quiet, romantic, adventurous, unusual, contemplative | Contextual, graded, source-supported; time and crowd level can change it. |
| **Discovery status** | recently opened, locally distinctive, underexposed | Derived judgments with dated evidence; not permanent categories. |

"Romantic but not a restaurant" requires a restaurant exclusion and soft ambience matching. "Adventurous without exhausting" requires adventure plus low/moderate exertion, not an "outdoors" category. "Quiet for two hours" requires a plausible stay duration and a quietness claim conditioned on time of visit. Build a small labeled vocabulary from actual queries; avoid a large ontology until classification errors justify it. Any high-stakes facet, such as accessibility or safety, needs stronger evidence than a generated tag.

## 7. Search Architecture

The v0.1 hybrid approach is sound, but its diagram puts "quality/freshness" after diversification. That allows invalid candidates to be promoted. **Engineering recommendation:** use a staged pipeline with a hard feasibility gate before substantive ranking, plus a final verification step for volatile facts.

```text
Request + area/time/transport context
  → query understanding (deterministic parse, optional model)
  → typed intent with uncertainty and provenance
  → query plan (which indexes/sources, budgets, fallbacks)
  → parallel candidate generators: exact/name, text, category/facet,
      geo/temporal, optional semantic, curated or editorial
  → canonical-ID fusion and duplicate/parent-child suppression
  → eligibility and feasibility checks
  → relevance/quality/discovery ranking
  → diversity and source/coverage checks
  → volatile-fact recheck where needed
  → results with grounded reasons and uncertainty
  → interaction/accuracy feedback for evaluation
```

**Query planning** determines which retrieval channels are useful. An exact named venue should not depend on vector search; "quiet but unusual" benefits from semantic recall and evidence-backed attributes. Geo and time are often filters across all channels, not independent ranked result lists. The planner sets candidate budgets and decides whether to route-check a shortlist, because full route matrices for every database record are costly. Route duration is a separate service from straight-line proximity: PostGIS supports indexed geographic distance tests, while route matrices calculate network travel time. [PostGIS `ST_DWithin`](https://postgis.net/docs/ST_DWithin.html), [Google Routes matrix documentation](https://developers.google.com/maps/documentation/routes/compute_route_matrix)

**Candidate fusion** must deduplicate by canonical identity and keep retrieval evidence. Reciprocal-rank-style fusion is a possible baseline when channel scores cannot be compared directly; it is an experiment, not a prescribed formula. A result must never become eligible merely because several weak channels retrieve it.

**Hard constraints** include explicit exclusions, a required time window, transport mode, and a stated maximum journey. "Open now" requires a verified enough open-status policy; "bookable tonight" requires session/capacity evidence. **Soft preferences** include quiet, unusual, moderately priced, and close. Avoid transforming "preferably" into a hard SQL filter. Missing information should have three possible outcomes: exclude when the claim is essential, include with a clear caveat when acceptable, or ask the user when a decision cannot be made.

**Explanation** should refer to actual matched attributes and sources: "indoor pottery session at 19:00, 15 minutes by car, estimated 75 minutes," with any unresolved capacity shown as unknown. It must not generate new opening, safety, price, or availability facts. Empty results are a product response: state which constraint caused scarcity and offer one labeled relaxation at a time.

## 8. Intent Understanding

An LLM can extract likely goals, entities, negations, and preference strength from natural language, propose a clarification, and rewrite user language into a typed search intent. It should not decide venue eligibility, invent a price, infer consent to use private context, or turn its own interpretation into a fact. A deterministic parser should handle dates, numeric limits, and explicit negatives when possible; the model handles expressive language and context. Both write to the same validated representation.

**Conceptual search-intent representation** (illustrative, not production JSON):

```text
context: origin | selected_area | destination | route; timezone; transport_mode
time: interval; flexibility; arrival_deadline; assumed_timezone
party: size; ages/needs only if supplied; source=user|session
hard_constraints: field, operator, value, evidence_requirement
soft_preferences: concept, direction, strength, user_phrase
exclusions: entity/category/attribute; scope
activity_budget: total_minutes; visit_minutes; travel_and_buffer_policy
retrieval_hints: exact_terms; concepts; candidate_types
uncertainty: missing_fields; ambiguous_phrases; interpretation_confidence
context_policy: which prior preferences are allowed for this request
```

For "I have two hours before dinner and want something interesting nearby. Nothing outdoors because it's too hot, and I've already done most tourist things," the intent should contain: a **120-minute total window ending at dinner time** (dinner time missing); current origin (if permission exists); outdoor exclusion; soft novelty/unusualness; a soft downweight of mainstream tourist sites; known visited items only if the user supplied or previously consented to that history. The system should ask for the dinner time if needed to enforce the deadline, or state a visible assumption. It should not equate "most tourist things" with a complete visited list.

Ambiguity policy: preserve multiple interpretations where cheap, ask only when the answer changes results materially, and display defaults. Contradictions such as "free but premium" should trigger a short clarification or a labeled relaxation; neither side should silently win. Conversational refinements should modify a retained typed intent with an audit of what changed, while respecting explicit constraints from earlier turns. The typed representation needs versioning and regression examples so model changes do not alter query semantics unnoticed.

## 9. Ranking & Diversification

Avoid v0.1's single additive "FinalScore" as the conceptual model. Some dimensions are gates; others are incomparable or should impose a minimum standard. Use stages:

| Stage | Question | Candidate signals |
|---|---|---|
| **Eligibility** | Is it permissible, active, geographically and temporally feasible, and sufficiently supported? | status, cancellation, explicit negatives, travel ceiling, slot/open evidence, rights. |
| **Relevance** | Does it answer this request? | text/name match, semantic match, intent facets, time and duration fit. |
| **Quality** | Is there credible evidence it is worth the effort? | reliable firsthand/editorial assessments, sustained positive signals, operating reliability, evidence volume and bias. |
| **Discovery value** | Does surfacing it add something beyond the obvious? | local rarity, underexposure relative to credible quality, recency, geographic spread. |
| **Personal fit** | Does it suit this person, with permission? | explicit dislikes, saved/visited items, stated pace, recent exposure. |

Freshness and source confidence affect eligibility for critical claims and uncertainty for the rest; they should not merely add a few score points. Travel time has both a hard ceiling and a soft convenience gradient. Price has both explicit maxima and uncertain ranges. Weather can be a hard gate for safety-sensitive outdoors or a soft comfort factor otherwise. Popularity can be evidence of quality, but should saturate rather than dominate.

Start with transparent rules and calibrated thresholds, then consider learned ranking after collecting reliable judgments and outcomes. Offline judgments should score **feasibility, usefulness, novelty, evidence, and list quality separately**. Online saves alone are weak evidence: a save may mean "maybe," while a real visit, verified booking, or post-visit rating is closer to outcome. Measure result-level errors and whole-page success. Diversify over activity type, neighborhood, price, and known/familiar status, while protecting top relevance and not forcing irrelevant novelty. A small amount of exploration can reveal underrepresented candidates; label sponsored content and keep payment outside organic eligibility.

## 10. Hidden-Gem Framework

"Hidden gem" should mean **a credible, locally distinctive option that is underexposed relative to its likely value for this query and audience**. It is relational: a place may be unknown to a visitor yet familiar to locals, and it may stop being hidden after wide promotion.

Require three independent checks: (1) quality above a minimum evidence threshold; (2) distinctiveness or strong local fit; (3) exposure below what its quality/context would predict. Signals can include independent operation, rarity within a neighborhood, expert or community mentions with dates, saves converted to visits, return visits, newly opened status, and discovery velocity. Review count is only an exposure proxy. A low count alone says little; social spikes may be manipulated. Chains are not automatically poor, and independent ownership is not proof of quality.

Use **evidence tiers**: editor-verified, corroborated multi-source, promising but unverified. Only the first two should receive an assertive hidden-gem label. Suppress unsafe access, unverified opening status, poor quality, or stale recommendations. Rotate exposure to avoid making one location the repeated answer and monitor whether promotion causes crowding or harms fragile sites. For the MVP, a small manually audited "locally distinctive" set is a better test than a global hidden-gem score. **Hypothesis:** this set improves discovery success without raising bad-result rates.

## 11. Data Architecture

Data supply is the binding constraint. Each source has different coverage, identity keys, refresh behavior, fields, cost, and legal rights. Build a **source registry** before a unified data lake: what may be read, stored, transformed, indexed, embedded, displayed, attributed, exported, and retained; for how long; in which markets. A rights rule should travel with every fact and derived feature. The review must include map-display coupling, photo/review rights, and whether embedding provider text is permitted.

Conceptual flow: source approval → permitted ingest → immutable source observation with retrieval time → normalization → candidate identity matching → human/automated merge decision → field-level claim selection → enrichment with its own evidence → validation → canonical view → search projection → monitoring and correction. Preserve raw observations only where rights allow. Store source IDs and minimal operational metadata separately when permitted. User submissions need abuse controls and verification, not immediate authority.

Source families should be evaluated separately: commercial place APIs; OSM/open and municipal data; tourism bodies; event/ticketing feeds; venue/operator sites; partner feeds; local editorial work; social sources; and user reports. "Available on a website" does not imply a usable feed or redistribution right. Google Places documentation expressly allows retention of place IDs under a specific exception, while broader Maps content has separate restrictions, and Places results on maps have display rules. OSM is under ODbL with attribution and share-alike implications. These are examples of why a mixed canonical dataset needs legal design before ingestion. [Google Place IDs](https://developers.google.com/maps/documentation/places/web-service/place-id), [Google Maps service terms](https://cloud.google.com/maps-platform/terms/maps-service-terms), [Google Places policies](https://developers.google.com/maps/documentation/places/web-service/policies), [OpenStreetMap copyright](https://www.openstreetmap.org/copyright)

Eventually distinct subsystems may own ingestion connectors, identity resolution, claim/provenance management, verification scheduling, and search projection. For the MVP these can be logical modules and jobs in one application/database. Split them into services only when throughput, ownership, or failure isolation requires it. Track coverage by neighborhood and type, freshness by critical field, cost per **useful result**, and correction workload; raw record count is a poor metric.

## 12. Canonical Entity Resolution

Identity matching needs **candidate generation, evidence comparison, decision, and reversibility**. Candidate generation uses geospatial blocks and normalized names, phone, website/domain, address, provider identifiers, organization/branch names, and possibly photo fingerprints where rights allow. A classifier or ruleset compares these signals with type-aware thresholds. It should produce "same," "different," or "review," and retain the evidence. Coordinates are noisy; names change; a phone or website can be shared by several branches; provider IDs can change.

Use **cannot-merge constraints**: distinct branch identifiers, materially different street addresses or entrances, conflicting simultaneous operating locations, or two independently verified venues of the same chain. Two Starbucks 300 meters apart are two branch sites even if name, category, operator, and website match. A pop-up inside a café is linked by **contained within**, not merged. A festival and its component events remain related identities. Likewise, a listing that changes operator may need a successor relation rather than one timeless entity.

Canonical records should reference source records rather than erase them. Merges need audit history, versioned redirects, and a split procedure; otherwise a wrong merge contaminates hours, reviews, and search results. Review high-impact uncertain matches first. Measure false merges separately from missed merges because false merges can tell a user to go to the wrong site.

## 13. Provenance / Freshness / Confidence

These are distinct:

- **Provenance:** source, original claim, retrieval method, license/usage rights, and any transformation chain.
- **Freshness:** when the claim was observed and verified, plus the field-specific decay/expiry policy. A newly fetched stale website is not newly verified information.
- **Confidence:** estimated probability or ordinal trust that a particular claim is true in a particular context, based on source quality, corroboration, recency, and conflicts. Do not display invented decimal precision.

Use a field-level **claim ledger** behind each canonical item: `{subject, field, value, valid_time, observed_at, verified_at, source, method, rights, confidence/evidence tier, conflict_state}`. Entity-level health summarizes this ledger, but cannot replace it. A café can have high-confidence identity and low-confidence Friday hours. An event can have a confirmed date but unknown remaining capacity. Absence of a claim is **unknown**, not false.

Refresh schedules should follow volatility and impact: event cancellations and bookable slots need faster checks than coordinates; recently opened venues merit extra checks; critical claims near a user's requested time merit revalidation. Conflicts should not be silently resolved by "newest wins." Prefer the most authoritative source for that fact type, expose unresolved conflict where it affects the decision, and route high-impact conflicts to review. The system should support user-reported corrections with evidence and abuse protection.

## 14. Planner Architecture

The v0.1 direction is correct: a planner consumes discovery candidates and solves feasibility. Model fixed commitments, flexible options, opening intervals, session start/end, visit duration range, transit time by mode and departure time, setup/queue time, buffers, budget, reservations, and user pace. Hard constraints decide whether a schedule is valid. An optimizer can then trade off interest, travel, cost, and variety. A single gap-fit check is simpler than a full multi-day optimization and should precede it.

Constraint programming, scheduling, and routing techniques are appropriate once the data supports them. The exact solver should follow problem size and requirements; no solver is needed for the discovery MVP. AI can help interpret a preference ("slow morning," "avoid rushing"), explain tradeoffs, and propose candidate themes. It should not override a hard closing time, invent a booking slot, or make an infeasible route appear valid. A plan also needs rechecking when an event, route estimate, or opening hour changes.

## 15. Proactive Intelligence

The "A to B tomorrow" example is best understood as **event-driven contextual discovery** with a recommendation step. It requires permissioned user context, a reliable future route and schedule, change detection, candidate retrieval within a corridor, detour travel calculation, opening/session verification, ranking, and a notification policy. The trigger might be a newly published event, a changed schedule, a saved-place opening window, or a weather update.

The system must know *why now*, not merely *why relevant*. Avoid notifying on every ranking refresh. Deduplicate alerts, enforce quiet hours and frequency caps, show the time and evidence of the underlying fact, and allow the user to disable categories. A wrong proactive alert is more intrusive than a wrong search result. Defer this until discovery feasibility and change detection meet explicit reliability targets.

## 16. Technical Stack

**Documented capability:** PostgreSQL supports indexed full-text search and text ranking; PostGIS supports index-aware spatial proximity tests; pgvector supports exact and approximate vector search. Supabase documents PostGIS and vector extensions. These support an initial integrated corpus and moderate query volumes without a separate search cluster. [PostgreSQL full-text indexes](https://www.postgresql.org/docs/current/textsearch-indexes.html), [PostgreSQL text ranking](https://www.postgresql.org/docs/current/textsearch-controls.html), [PostGIS `ST_DWithin`](https://postgis.net/docs/ST_DWithin.html), [pgvector documentation](https://github.com/pgvector/pgvector), [Supabase PostGIS](https://supabase.com/docs/guides/database/extensions/postgis)

**Engineering recommendation:** Next.js/React/TypeScript for the eventual interface and PostgreSQL/PostGIS for canonical data are plausible defaults, but no framework choice determines product success now. Add full-text search early only if corpus and query tests warrant it. Add pgvector when a labeled benchmark shows semantic candidate recall improves materially. Approximate vector indexes can return too few matches under selective filters because filtering occurs after an index scan; use exact search, suitable partitioning, or tested scan settings as appropriate. [pgvector filtering notes](https://github.com/pgvector/pgvector#filtering)

**When to consider dedicated search:** measured latency or recall failures on the actual hybrid query mix; need for advanced lexical relevance, typo tolerance, multilingual analysis, or operational search features that PostgreSQL cannot meet at acceptable cost. Do not use record count alone as a trigger. A dedicated engine introduces synchronization and consistency duties, particularly painful for cancellations and closing times.

Keep provider adapters, geocoding, routing, embedding generation, intent parsing, search execution, and ranking behind replaceable interfaces. Keep canonical identity and rights metadata independent of a host platform. Evaluate Supabase on operational requirements and extension availability at implementation time; it can simplify setup but cannot solve data licensing or relevance. Route matrices add per-element cost and limits, so use them on a shortlisted set and measure budget. [Google Routes usage and billing](https://developers.google.com/maps/documentation/routes/usage-and-billing)

## 17. System Boundaries

These are **logical ownership boundaries**, not a microservice plan.

| Boundary | Owns and produces | Does not own |
|---|---|---|
| **Source governance and ingestion** | Approved source contracts, connectors, observations, ingestion health. | Canonical identity or final search rank. |
| **Identity and claim management** | Entity links, merge/split history, field claims, provenance, current canonical views. | User-facing search ordering. |
| **Availability and feasibility** | Time-window interpretation, open/session status, travel and duration feasibility, uncertainty outcome. | Source collection or preference learning. |
| **Discovery query** | Typed intent, query plan, candidate retrieval/fusion, search diagnostics. | Canonical factual authority. |
| **Ranking and list composition** | Relevance, quality thresholds, novelty/diversity, explanation evidence references. | Fabricating missing facts or changing eligibility. |
| **Evaluation and feedback** | Benchmark cases, human judgments, accuracy reports, error triage. | Production fact selection. |
| **User context** | Saved/visited items, explicit preferences, consent and retention policy. | Public venue facts. |
| **Planner** | Commitments, feasible schedules and tradeoffs. | Discoverable corpus or booking truth. |
| **Change and notification** | Change events, subscriptions, alert eligibility and delivery policy. | Search index as the sole source of truth. |

At MVP scale, these can reside in one deployable system with separate modules and jobs. The difficult-to-reverse boundaries are identity, claim provenance/rights, occurrence-versus-venue identity, and the typed search intent. Keep those conceptually clear even before implementation.

## 18. MVP Recommendation

**One city is a useful administrative boundary, but often a poor content boundary.** A city can be too large to verify well, too sparse in selected categories, or fragmented by travel patterns. Choose **one connected, dense activity area** within a city and its realistic travel catchment. Compare two or three candidate areas using source rights, content density, diversity, update burden, user access, and availability of local reviewers. The Saudi setting suggested in v0.1 is a plausible candidate, not yet a decision. A limited area is not a claim that all cities behave alike.

**Initial user promise:** "Find a worthwhile indoor, cultural, or active outing that fits today or this weekend within a realistic travel window." This tests cross-type discovery and time/geo fit. **Suggested corpus:** a curated, legally usable set of venues and repeatable offerings, plus a smaller set of dated occurrences from sources that can be refreshed. Include cafés only when they serve a real use case such as "quiet for two hours"; avoid a generic restaurant directory. Defer hikes/camping until trail access, conditions, seasonality, and safety can be represented credibly. Do not claim live ticket availability without a provider agreement and reliable feed.

**Minimum experience:** select area and time, enter a short query or choose a few intents, apply clear travel and price constraints, see a short diverse list with practical details, and open the original source for volatile facts. A map may help orientation but is not required to prove the core thesis. Saving can be a lightweight bookmark if it improves follow-up observation; accounts, personalization, full trip planning, alerts, and bookings are distractions for this test. A guided concierge or editorial prototype could precede software to learn which information people actually need.

**Data acceptance gate:** before inviting users, audit a representative sample for wrong identity, closed venue, incorrect hours, cancelled event, expired listing, duplicate, and missing source rights. Set explicit go/no-go thresholds after the audit baseline; no honest numeric target is available from v0.1. A sparse but correct corpus is preferable to false breadth, but it must contain enough variety to answer the benchmark rather than showing the same few items repeatedly.

**Learning design:** run moderated tasks with local users and visitors, then a small live test. Compare against each participant's usual search method on the same scenarios. Record whether they found a feasible option they would choose, time to a confident choice, novel useful finds, false-feasibility rate, variety, and reasons for abandonment. A save rate is diagnostic, not proof of a worthwhile outing. Review failures by stage: coverage, parse, retrieval, eligibility, ranking, explanation, or source accuracy. Expand geography only after success and refresh cost are repeatable in the first area.

**Hypotheses to falsify:** (H1) mixed-type results produce more useful choices than category-specific search; (H2) time and travel constraints reduce bad choices more than richer semantic matching; (H3) verified local curation adds enough value to justify its maintenance cost; (H4) a compact set of experiential attributes can support vague queries; (H5) data rights and update cost permit a sustainable corpus.

## 19. Benchmark Query Suite

This is an **initial evaluation set**, not a claim that the MVP can answer every row. For each case, record origin/area, local timezone, test date, transport mode, intended hard and soft constraints, a human-labeled set of eligible and useful results, and unacceptable results. Re-run after data and parser changes. Judge both top results and the whole list; include explicit "no good result" cases. The system abbreviations below are **I** intent, **D** data/coverage, **G** geography/routing, **T** time/availability, **F** facets/semantic retrieval, **R** ranking/diversity, **P** personalization/context, **X** explanation/trust.

| # | Realistic user query | Primary systems tested | Critical judgment |
|---:|---|---|---|
| 1 | "What can I do near me right now?" | I, G, T, D, R | Current location permission and verified open options. |
| 2 | "A good café open now within a 10-minute walk." | G, T, F, R | Walking travel, not radius alone. |
| 3 | "Something cultural tonight after 8." | I, T, D, R | Occurrence or venue genuinely usable after 20:00. |
| 4 | "Free things this weekend around downtown." | I, T, G, F | Local weekend, truly free rather than unknown price. |
| 5 | "I have 90 minutes before dinner at 7." | I, T, G, R | Door-to-door feasibility and buffer. |
| 6 | "An unusual place within 20 minutes by car." | I, G, F, R | Distinctiveness and route duration. |
| 7 | "Hidden gems that locals actually like." | D, F, R, X | Quality and evidence, not low review count. |
| 8 | "A newly opened independent coffee shop." | D, T, F, X | Verified opening date and ownership. |
| 9 | "An indoor activity for four friends tonight." | I, T, F, D | Group suitability and session availability. |
| 10 | "Something adventurous but not exhausting." | I, F, R | Adventure and exertion interpreted separately. |
| 11 | "An easy hike with shade tomorrow morning." | D, G, T, F, X | Trail condition, access, and shade evidence. |
| 12 | "A museum with an exhibition running this week." | D, T, F | Site–exhibition relation and dated run. |
| 13 | "A quiet place to spend two hours alone." | I, F, T, R | Likely quiet at chosen time; plausible stay. |
| 14 | "Something romantic but not a restaurant." | I, F, R | Hard negative plus graded ambience. |
| 15 | "Kid-friendly indoor options under 100 SAR." | I, F, D, R | Price unit and family suitability evidenced. |
| 16 | "A solo workshop I can join this Saturday." | D, T, F, X | Session and registration status. |
| 17 | "A date idea for two that isn't too formal." | I, F, R | Soft formality and couple suitability. |
| 18 | "A group activity that doesn't require booking." | F, D, T, X | Walk-in claim, not missing booking data. |
| 19 | "Show me something different from the usual tourist spots." | I, R, P | Tourist downweight; no invented visit history. |
| 20 | "Surprise me nearby." | I, G, R | Reasonable visible defaults and variety. |
| 21 | "Places open after 10 PM, no food or shisha." | I, T, F | Multiple explicit exclusions and late hours. |
| 22 | "A market this Friday, preferably local crafts." | I, T, F, D | Scheduled market versus permanent store. |
| 23 | "Something outdoors if the heat is manageable." | I, T, F, X | Conditional weather preference and uncertainty. |
| 24 | "A scenic stop along tomorrow's drive to the coast." | G, T, R | Route detour and stop duration. |
| 25 | "I'm visiting Tokyo next month; what should I save?" | I, D, T, R | Future context; avoid present-hours certainty. |
| 26 | "What's happening around my hotel on the 12th?" | I, G, T | Missing month/timezone clarification. |
| 27 | "Find paintball under 30 minutes, open now." | I, G, T, D | Venue open versus activity session available. |
| 28 | "A pop-up inside that bookstore I saw last week." | I, D, T, P | Host–pop-up relationship and uncertain reference. |
| 29 | "A wheelchair-accessible gallery open Sunday." | F, T, D, X | Accessibility evidence is essential; unknown cannot pass. |
| 30 | "Cheap or free things this evening, but no malls." | I, T, F, R | Price uncertainty and explicit mall exclusion. |

Add adversarial variants to each class: no location permission, DST or timezone crossing, a cancelled event, two same-chain branches nearby, a changed meeting point, and zero eligible results. Record top-k feasibility, useful choice rate, novel-useful rate, duplicate rate, source accuracy, clarification burden, and latency. Segment by query type and neighborhood; an average can hide failure in event or peripheral-area queries.

## 20. Failure Modes

| Failure | Likely cause / impact | Mitigation and detection |
|---|---|---|
| Permanently closed venue | Provider lag; wasted trip and trust loss. | Closure claim monitoring, site/operator checks, user report path, suppress on strong closure evidence. |
| Cancelled or moved event | Volatile organizer updates. | Occurrence status and source timestamp; near-time recheck; display cancellation/venue changes. |
| Wrong opening hours | Holidays, special hours, timezone, conflicting sources. | Field-level claims and holiday exceptions; label uncertainty; verify critical "open now" claims. |
| Venue open but session unavailable | Offering and venue conflated. | Separate site hours from session inventory; never infer slot availability from venue hours. |
| Duplicate results | Source duplicates or event/venue overlap. | Canonical IDs, parent-child suppression, list-level duplicate audit. |
| Dangerous false merge | Same-brand branches or co-located pop-up. | Branch-aware cannot-merge rules, human review, reversible merge history. |
| Wrong category or experiential tag | Weak auto-classification. | Evidence-backed typed facets, sampling, user feedback, remove unsupported attributes. |
| Semantic false positive | Similar wording, wrong practical fit. | Hard constraint validation after retrieval; benchmark negatives and counterexamples. |
| Famous venues dominate | Popularity proxy overwhelms relevance. | Saturate popularity, local-distinctiveness pool, list diversification, exposure audit. |
| Bad place promoted as "hidden" | Low reviews mistaken for quality. | Minimum quality/evidence gate and dated local review; audit complaints. |
| Travel time wrong | Straight-line proxy, mode mismatch, traffic or barriers. | Shortlist routing, mode and departure-time awareness, uncertainty margin. |
| Technically fits but impractical | No queue, setup, transit, or buffer allowance. | Door-to-door fit; duration ranges and conservative buffer; user pace. |
| Expired source record | Source refresh missed; invisible stale content. | Field-specific expiry, ingestion health alerts, suppress stale critical claims. |
| Provider conflict | Two values both plausible. | Preserve claims, source-specific authority, conflict flag and review. |
| Thin/missing coverage | Certain neighborhoods or types absent. | Coverage dashboard; honest empty states; choose launch area based on density. |
| AI-generated false description | Model extrapolates beyond evidence. | Ground explanations in stored claims; prohibit invented hours, prices, or safety. |
| Accessibility or safety overclaim | Critical attribute inferred from generic text. | Require direct credible evidence; show unknown; stricter eligibility for explicit need. |
| Too much personalization | Filter bubble or misread shared-device behavior. | Explicit controls, broad exploration, no hard exclusions from weak inferred preferences. |
| Repetitive recommendations | Same popular cluster shown repeatedly. | Session-level exposure memory, diversity over type/area, freshness of alternatives. |
| Sponsored result distorts discovery | Commercial incentive contaminates ranking. | Separate labeling and eligibility; audit organic list and conflict of interest. |
| Rights violation | Provider content retained or combined beyond license. | Source registry, field-level usage policy, deletion/expiry controls, legal review before ingest. |
| Proactive alert is wrong or excessive | Stale triggers, weak schedule consent, poor dedupe. | Defer alerts; change verification, quiet hours, rate caps, opt-in and audit trail. |

The highest-severity errors are false eligibility, dangerous merges, unlicensed use, and incorrect claims about accessibility/safety. Prioritize these over small ranking gains. Each mitigation needs an owner and a measurable check before release.

## 21. Open Questions

The priority labels describe **decision timing**, not certainty. "Critical before MVP" means the experiment cannot be interpreted or operated responsibly without an answer.

### Product questions

| Question | Priority |
|---|---|
| Which first audience has a repeated, unmet decision need: local residents, domestic visitors, or visitors from abroad? | **Critical before MVP** |
| What exact outing decision and time horizon will the first promise cover? | **Critical before MVP** |
| Which two or three launch areas offer dense, varied, verifiable options and reachable test users? | **Critical before MVP** |
| How will users define "worthwhile" and "novel" compared with their current workflow? | **Important during MVP** |
| Is a map needed for choice, or does a short evidence-rich list work better? | **Important during MVP** |
| When does saved-item use justify accounts and trip context? | **Can wait** |

### Data questions

| Question | Priority |
|---|---|
| Which source mix gives usable rights, coverage, and update frequency in the launch area? | **Critical before MVP** |
| How many independently verifiable options exist per neighborhood and time window? | **Critical before MVP** |
| What fraction of hours, event status, price, and duration claims are missing or wrong? | **Critical before MVP** |
| What false-merge rate is acceptable, and which cases need human review? | **Important during MVP** |
| Which field-specific refresh cycles and correction workflows are affordable? | **Important during MVP** |

### Search questions

| Question | Priority |
|---|---|
| Which benchmark queries can the actual corpus answer at all? | **Critical before MVP** |
| What typed intent fields and uncertainty policy cover the first query set? | **Critical before MVP** |
| Does semantic retrieval add relevant candidates beyond lexical/facet search? | **Important during MVP** |
| How often must a query ask for clarification versus use a visible default? | **Important during MVP** |
| What level of multilingual and colloquial query support is needed first? | **Important during MVP** |

### Ranking questions

| Question | Priority |
|---|---|
| What is the minimum evidence/quality threshold for a recommendation? | **Critical before MVP** |
| Which mistakes matter most to users: poor fit, stale fact, distance, sameness, or obviousness? | **Critical before MVP** |
| Does deliberate diversification improve useful choice without lowering relevance? | **Important during MVP** |
| Can "locally distinctive" be judged reliably at acceptable cost? | **Important during MVP** |
| Is behavior data rich and unbiased enough to learn rank weights? | **Can wait** |

### Architecture questions

| Question | Priority |
|---|---|
| What identity and occurrence boundaries must source adapters preserve? | **Critical before MVP** |
| How will field provenance and rights survive normalization and search projection? | **Critical before MVP** |
| Which travel-time provider or approximation meets the first scope and budget? | **Important during MVP** |
| At what measured latency/recall does PostgreSQL cease to be adequate? | **Can wait** |
| What planner solver and event infrastructure are appropriate? | **Can wait** |

### Business / economics questions

| Question | Priority |
|---|---|
| What is the acquisition, verification, routing, and editorial cost per useful decision in one area? | **Critical before MVP** |
| Can an initial content partnership or curator network improve coverage without compromising neutrality? | **Important during MVP** |
| What level of repeat use or willingness to pay could sustain the service? | **Important during MVP** |
| Which monetization model preserves ranking trust? | **Can wait** |

### Legal / licensing questions

| Question | Priority |
|---|---|
| For each first source, may its fields be retained, merged, indexed, embedded, displayed on the chosen map, and used commercially? | **Critical before MVP** |
| What attribution, deletion, and downstream redistribution rules apply to the combined corpus? | **Critical before MVP** |
| What permissions and retention rules govern location, saved places, visit history, and imported schedules? | **Important during MVP** |
| What rights apply to photos, descriptions, reviews, and user submissions? | **Important during MVP** |
| What terms would govern bookings, paid placement, and alerts? | **Can wait** |

## 22. Recommended Research Program

The v0.1 R01–R08 list identifies relevant subjects but places technology research before the product/evaluation contract and combines rights with late-stage economics. Reorder it so each study reduces a decision risk. These are research documents and experiments, **not implementation milestones**. R07 planner moves later; a new audience/task study and evaluation study come first.

| Sequence / relation to v0.1 | Goal and core questions | Expected output; why it matters | Dependencies |
|---|---|---|---|
| **R00  -  User decision study** (new) | Who is the first user? What decision fails today, how often, and what do they consider useful? | Interview/task findings, primary job, competitive baseline, launch-area shortlist. Stops an elegant system from solving a rare problem. | None. |
| **R01  -  Source rights and economics** (split R08, precedes old R01) | For candidate sources, what may be stored, combined, embedded, shown, attributed, and monetized? What are realistic per-query and refresh costs? | Rights matrix, cost scenarios, source exclusions, legal questions. Prevents an unusable canonical corpus. | R00 area and content needs. |
| **R02  -  Local coverage audit** (old R01) | Which sources cover the candidate areas, entities, events, and critical fields? How quickly do they change? | Sample corpus audit, coverage heatmap, error baseline, source mix decision. Tests data feasibility. | R00, R01. |
| **R03  -  Domain and identity model** (old R02) | What entities and relationships survive hard cases? How often do false merges occur? | Conceptual model, labeled match/nonmatch set, merge/split policy. Protects facts and search identity. | R02 sample records. |
| **R04  -  Trust and freshness policy** (old R05) | Which claims need source authority, how do they decay, when should the system abstain? | Field-level claim policy, conflict examples, verification priorities, accuracy targets. Enables defensible eligibility. | R02, R03. |
| **R05  -  Query/intent and evaluation set** (old R06 plus new evaluation topic) | Which real queries and negative constraints matter? When should the system clarify? | Versioned typed-intent specification, benchmark with judgments, baseline success measures. Defines what "better search" means. | R00, R02, R03. |
| **R06  -  Retrieval and search architecture** (old R03) | Which lexical/facet/geo/time methods recall eligible candidates? Does semantic search add value? What are latency and cost? | Comparative experiments and engine decision criteria, not a fixed engine purchase. | R04, R05. |
| **R07  -  Ranking, diversity, and local distinctiveness** (old R04) | Which results are useful, high quality, and genuinely discoverable? How much variety helps? | Human judgment rubric, rank baselines, hidden-gem evidence policy, list evaluation. | R04–R06. |
| **R08  -  Feasibility and travel-time study** (new) | Where does radius fail? What buffers and route calculations are necessary for first use cases? | Travel-mode policy, shortlist routing design, cost and error estimates. | R05–R06. |
| **R09  -  MVP field test** (new) | Does the selected area beat the user's current method on feasible, novel, worthwhile choices? | Usability and outcome evidence, failure breakdown, expand/adjust/stop recommendation. | R01–R08. |
| **R10  -  Planner and contextual assistance** (old R07; later) | Which saved-item and schedule cases justify constraint solving and alerts? | Planner problem definition, consent model, solver options, reliability bar. | Successful R09 and observed planning demand. |

Each study should report documented facts, observed local measurements, engineering recommendations, and remaining hypotheses separately. The sequence can overlap where evidence is independent; for example, interviews and preliminary rights review may run together. Do not let a technology comparison substitute for a coverage audit.

## 23. Proposed Changes for v0.2

### Keep

| v0.1 idea | Why keep it |
|---|---|
| Discovery before planning | A schedule made from weak candidate data cannot be trusted. |
| WHAT × WHERE × WHEN × WHO | A useful reminder that intent, geography, time, and context interact. Define WHO as consented context, not assumed personalization. |
| Time and travel feasibility as core dimensions | These distinguish actionable discovery from a generic list. |
| Hybrid retrieval and explicit diversity | Multiple retrieval methods and list-level variety are likely needed, subject to benchmark evidence. |
| Provenance, freshness, confidence | Correctly identifies trust as a product and data concern. |
| AI assists rather than supplies facts | Keeps model output subordinate to source evidence. |

### Modify

| Change | Why |
|---|---|
| Replace three hard product modes with one discovery context plus later planning workflow. | Local/future and now/later are independent dimensions; separate modes invite duplicated logic. |
| Replace eight peer object types with site, operator, offering, occurrence, geometry, and collection relationships. | Handles multi-venue, repeated, nested, and mobile cases without collapsing identities. |
| Move quality/freshness checks before ranking and diversify only eligible items. | Prevents a good score from laundering an unusable result. |
| Change category strategy to controlled types, typed facets, and graded experiential attributes. | "Quiet" and "romantic" depend on context and evidence; "hidden gem" is a derived judgment. |
| Replace one weighted score with staged eligibility, relevance, quality, discovery value, and personal fit. | Some conditions cannot be traded off against popularity or novelty. |
| Scope MVP by a dense area and answerable query set, then choose interface features. | One city and 6–10 categories do not guarantee useful coverage. |
| Treat Supabase/pgvector as options, not commitments. | Data rights and actual search errors should drive those choices. |

### Remove / Defer

| Idea | Why |
|---|---|
| Global "any selected area" promise at launch | Coverage and freshness will vary sharply by geography. |
| Separate "Temporary Place" and "Outdoor Experience" as universal peer entities | Temporariness and outdoors usually describe validity or geometry. |
| Automatic itineraries, route suggestions, weather alerts, recommendation ML, and booking | They depend on a reliable discovery corpus, permissions, and new operational guarantees. |
| Numeric confidence and discovery scores presented as if calibrated | Scores need labeled evidence and calibration before they mean anything. |
| A fixed version ladder beyond the MVP | Demand and data constraints may change the order. |

### Add

| Addition | Why |
|---|---|
| Source-rights registry and field-level usage rules | Some permitted API uses do not allow permanent indexing or combining. |
| Claim ledger with unknown/conflict states | Entity-level confidence cannot express uncertain hours or capacity. |
| Typed, versioned search intent with hard/soft distinctions | Makes interpretation inspectable and testable. |
| Explicit feasibility gate and abstention policy | Prevents closed, cancelled, too-far, and unsupported options from appearing actionable. |
| Canonical merge/split audit and cannot-merge rules | False merges can produce dangerous wrong-location or wrong-hours results. |
| Benchmark query suite and human relevance judgments | Gives the project a way to choose search methods by evidence. |
| Competitive baseline and user-decision study | Tests whether the proposed advantage is meaningful. |
| Empty-result and uncertainty behavior | Honest scarcity preserves trust and guides refinement. |
| Economics per useful decision and verification workload | A rich corpus may be unsustainable even if retrieval works. |

## 24. Recommended Next Actions

These are **ordered decisions and studies**, not a committed delivery schedule.

1. **Choose two or three candidate launch areas and one primary user group** for comparison. Document the repeated outing decision and the current tools people use.
2. **Run 12–20 observed discovery tasks** across local and visitor contexts, including vague, time-limited, and negative-constraint requests. Capture actual queries, decisions, failures, and willingness to travel; treat the sample as directional, not representative.
3. **Create a source-rights and cost matrix** for the first candidate data sources before retaining or merging content. Obtain legal review of any unclear commercial terms.
4. **Audit local content coverage and accuracy** in each area, sampling venues, offerings, and occurrences at different times and neighborhoods. Measure critical missing fields and manual verification effort.
5. **Finalize the conceptual entity and claim model** using the hard cases in Section 5 and real source records. Label a small merge/nonmerge set, including nearby chain branches and nested pop-ups.
6. **Turn the benchmark suite into an evaluation dataset** with area, date/time, transport mode, intent interpretation, eligible result judgments, and explicit false-positive cases.
7. **Specify the typed search intent and feasibility policy**: hard versus soft constraints, unknown status, clarification rules, and treatment of future dates and volatile availability.
8. **Compare simple retrieval and ranking baselines** on that dataset: editorial/facet/lexical/geo/time first, then add semantic retrieval only if it yields useful candidates without excess false positives.
9. **Run a small concierge or prototype field test** against participants' usual search method. Measure feasible useful choice, novel finds, false-feasibility rate, time to choice, and cost of keeping records accurate.
10. **Write v0.2 from the evidence**, deciding the actual MVP area/content promise and deferring stack components that did not improve the benchmark.

## Most Important Findings

1. The defensible promise is a **worthwhile option that fits the user's real time and location**, not broad local data coverage or an AI conversation.
2. The first risk is **rights-compliant, current local data**. An API record is not automatically a permanent indexable asset.
3. **Venue, offering, occurrence, and location need separate identities**; otherwise events, sessions, pop-ups, trails, and branches will break search and availability.
4. **Feasibility precedes ranking.** Closed, cancelled, too-far, and unsupported results should not be rescued by high semantic relevance.
5. **Unknown is a first-class state.** Freshness and confidence belong to specific claims, especially hours, sessions, prices, and accessibility.
6. "Hidden gem" needs credible quality and distinctiveness **relative to exposure**, with editorial checks before a broad score.
7. Local and destination exploration are the **same discovery task with different place/time context**; planning and alerts add separate reliability obligations.
8. A **dense launch area and benchmarked user decision** give a better MVP boundary than a whole city plus a feature checklist.
9. PostgreSQL/PostGIS is a reasonable initial technical direction; pgvector and a dedicated search engine should follow measured recall and latency needs.
10. The next work is **user, source-rights, coverage, and evaluation research**. The concept is not ready for a fixed implementation roadmap.
