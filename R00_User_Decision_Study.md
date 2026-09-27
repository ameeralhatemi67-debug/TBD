# R00 — User Decision Study

**Project:** Location-aware discovery platform  
**Date:** 26 September 2026  
**Research type:** Project-document review and current desk research; preparation for later observed user research.  
**Decision sought:** Which user's which outing decision should the product solve first?

## 1. Executive Summary

**Recommended first hypothesis.** Test local residents who organize short-notice outings for themselves and one to four others in a connected Saudi urban area. Their decision is: **Given where we will start, when we can go, our total time and budget, and what the group feels like doing, which two or three credible options can we actually choose now?** A secondary hypothesis is a domestic visitor making the same decision from a hotel or host's neighborhood. These are hypotheses, not validated audiences.

The desk evidence shows an active category, not an empty market. Google Maps already offers conversational things-to-do ideas and collaborative lists; Google Search accepts compound local prompts; TikTok, Instagram, and Snapchat support place discovery; event platforms show dated bookable inventory; trip planners combine maps and schedules. [Google Maps, 2025](https://blog.google/products-and-platforms/products/maps/20-years-google-maps-20-features/), [Google Search AI Mode, 2025](https://blog.google/products-and-platforms/products/search/ai-mode-development/), [TikTok Nearby](https://newsroom.tiktok.com/tiktok-nearby-discover-whats-happening-around-you?lang=en-GB), [Wanderlog](https://wanderlog.com/)

**Product interpretation:** the possible gap is the *last mile of decision*: combining ideas from different content types, checking date and hours, estimating practical travel, establishing price/booking/group fit, and reducing the set to a choice. Product pages confirm that many competing tools handle parts of this task. They do **not** establish that their users experience a severe unsolved problem. R00's next study must observe the workflow and compare it with the current best tools, especially Google Maps and local Saudi event products.

Saudi evidence supports a large pool of cultural and leisure activity but cannot establish how often an individual needs help deciding. GASTAT's 2024 household survey reports that 81.6% of respondents aged 15+ visited at least one cultural event/activity venue and 85.3% visited at least one entertainment event/activity. Those are participation measures, not weekly discovery rates or evidence of product demand. [GASTAT 2024 survey](https://www.stats.gov.sa/documents/20117/2435273/Household%2BCulture%2Band%2BEntertainment%2BStatistics%2BPublication%2B2024%2BEN.pdf/591d6f59-c7ae-5ef4-0190-56643b41f4e7)

**Decision:** proceed to R01 source rights now and R02 coverage audit conditionally, using four candidate test environments and the narrow content scope below. Run observed user tasks before selecting a final launch area or product promise. No interview, survey, or usage result is represented as having been collected for this project.

## 2. Research Scope

R00 examines the human choice before implementation: triggering situation, language, tools opened, candidate comparison, rejection, confidence, and repeat need. It considers near-term local discovery and a future-destination contrast. It excludes itinerary solving, proactive alerts, personalization systems, booking integration, database design, and interface design.

The [v0.1 concept](<Product & Technical Concept v0.1.md>) supplies the broad product, WHAT × WHERE × WHEN × WHO, and a discovery-before-planning principle. The [architecture review](Product_Technical_Concept_Architecture_Review_v0.2.md) narrows the working promise to feasible, worthwhile choices and orders the R00–R10 research ladder. R00 tests that narrowing rather than treating it as a fact.

## 3. Evidence Method & Limitations

This report uses four explicit labels. **Documented evidence** means a cited source directly supports a product capability, market participation figure, place/program example, or research finding. **Product interpretation** is a reasoned implication that has not been observed in this project's users. **Hypothesis** is a claim the later study should try to disprove. **Requires primary research** identifies a question no desk source can answer for the first audience.

The source set includes 2023–2026 official product pages, GASTAT and Saudi tourism/entertainment sources, and selected academic research. Product-owned pages establish what a service advertises, not how well it performs for a particular Saudi query. Government participation counts establish activity, not discovery difficulty. Studies of tourists or restaurants can inform a decision framework but cannot be transferred automatically to Saudi residents choosing an outing. Any workflow below is **illustrative reconstruction**, not a recorded participant journey. The 100 queries are **synthetic prompts**, not search-log samples or user quotations.

| Evidence with direct relevance | What it supports | Important limit |
|---|---|---|
| [Google Maps discovery and collaborative lists](https://blog.google/products-and-platforms/products/maps/20-years-google-maps-20-features/), [2025 Explore update](https://blog.google/products-and-platforms/products/maps/holiday-gemini-tips-new-explore-tab/) | The leading map already attempts vague, social, and nearby discovery. | Some features are region-specific; this does not prove Saudi performance. |
| [Google Search AI Mode example](https://blog.google/products-and-platforms/products/search/ai-mode-development/) | Compound prompts such as weekend/friends/food/chill/offbeat are already an explicit search use case. | Marketing example, not measured success. |
| [GASTAT culture and entertainment survey](https://www.stats.gov.sa/documents/20117/2435273/Household%2BCulture%2Band%2BEntertainment%2BStatistics%2BPublication%2B2024%2BEN.pdf/591d6f59-c7ae-5ef4-0190-56643b41f4e7) | People in Saudi Arabia participate across malls, parks, beaches/desert, heritage, museums and events. | No individual decision frequency, tool use, or unmet-need measure. |
| [GASTAT Livability in Saudi Cities 2025](https://www.stats.gov.sa/documents/20117/2435245/GASTAT_LISC%2Breport_2025_EN.pdf/80b46893-12e0-2b26-2a54-70a1553169c1) | 2024 city tourism totals and commute-time context for Riyadh, Jeddah and Dammam. | Tourism total means overnight visitors; commute is not leisure travel time. |
| [Tourist restaurant information-search study, 2023](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/Tourists-Online-Information-Search-Behavior-Combined/99818303302346) | Photos, written content and positive/negative reviews can reduce perceived choice risk. | International tourist restaurant choices, not all local activities. |
| [Recreation travel-time choice study](https://www.sciencedirect.com/science/article/pii/S0095069613000880), [2026 perceived leisure travel-time study](https://www.sciencedirect.com/science/article/pii/S2214367X25001747) | Travel time and destination attractiveness are both part of leisure choice. | Different geography and trip scale; do not import numeric weights. |
| [FTC review rule](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers) | Review manipulation is a real trust concern. | US rule, not Saudi law or a measure of fake-review prevalence here. |

**Evidence gaps:** no representative Saudi study located that measures the exact cross-source outing-decision process, app switching, time to choice, rejected options, or weekly repeat need. No local availability/coverage audit has been done. No primary research with prospective users has been done. These limits should shape the decision gate, not be filled with invented estimates.

## 4. Product Problem Restatement

A map helps locate and assess a known place. An event directory lists occurrences and may sell tickets. A travel planner organizes things already selected. This product would help earlier, when the user has a vague or mixed intent and must discover a feasible choice across venues, activities and dated occurrences. It only earns that role if its answers are more actionable or less laborious than existing products.

**Strongest problem statement to test:** "When people want to go out within a specific time window, they often find ideas in one source and must verify whether those ideas suit their starting point, group, budget, duration and current availability in other sources. The effort or uncertainty may make them choose the familiar option, abandon the outing, or make a poor choice." The words "often" and "may" remain **hypotheses**. Their frequency and severity require observed tasks.

Location, time and intent matter jointly. A museum is not a useful "tonight" option if its exhibition has ended. A nearby karting venue is not a usable four-person option if no session fits. A scenic outdoor place can be a poor midday summer result. A highly rated destination can still exceed the available total time. These examples are logical feasibility cases; the research task is to learn which happen frequently enough to support a product.

## 5. Jobs-to-be-Done

The scenarios contain a shared decision process but different triggers. Treat them as **three related jobs** rather than one undifferentiated "discover things" job.

| Job | Examples | Desired progress | Distinct difficulty |
|---|---|---|---|
| **Choose an outing soon** | "I'm bored"; "tonight"; "90 minutes before dinner"; "four of us, no booking" | Turn a loose intention into a feasible group choice with little lead time. | Live hours, session, duration, travel and group fit. |
| **Find a worthwhile new option** | "Unusual nearby"; "I've lived here for years"; "quiet but not boring" | Escape known or generic options without losing quality. | Novelty, mood and trusted local evidence. |
| **Build a future possibility set** | "Tokyo next month"; "what's on this weekend?" when plans are fluid | Save credible choices before committing to a schedule. | Date uncertainty and coverage across an unfamiliar area. |

"Something active but indoors" and "quiet but not boring" are preference descriptions inside any of these jobs. "What's happening this weekend?" can be an occurrence search or a broader outing choice depending on the user's purpose. The first job is the **strongest initial hypothesis** because its feasibility constraints are concrete and observable, and locals may face it repeatedly. That frequency advantage is unproven. The second job supplies a differentiating preference, "not the usual option," but should not become an unsupported hidden-gem promise. The third job is a useful contrast cohort, not the initial product's center.

## 6. Candidate Users

The table is a **hypothesis comparison**, not segment sizing. "High/medium/unknown" is a research priority judgment, not measured behavior.

| Candidate | Plausible trigger and repeat need | Existing tools / difficulty | Data and study burden | Test priority |
|---|---|---|---|---|
| Local resident who coordinates friends | Evenings/weekends; mixed tastes and vetoes. Repeat need may be high. | Maps, social media, messages and event sites; coordination may multiply checks. | Need current hours, price, group/booking fit; easy to recruit locally. | **Primary** |
| Local resident choosing solo or with partner | Short windows and preference for novelty or atmosphere. Potential repeat use. | Existing local search is strong; fewer group constraints. | Easier initial tasks; risk that Maps already suffices. | **Primary comparator** |
| Domestic visitor to another Saudi city | Wants orientation and a feasible nearby choice during a short stay. | Tourism sites plus maps and ticketing. | More multilingual/date needs; recruit through visitor networks. | **Secondary** |
| International traveler | High unfamiliarity and trust needs, but less frequent personal reuse. | Strong guide/travel tools; language and payments add complexity. | More translation, transport, cultural context and rights needs. | Later |
| Family organizer | Strong age, accessibility, price and duration constraints. | Often needs facility-level detail unavailable in feeds. | Higher risk of false suitability; recruit for contrast, not first promise. | Contrast cohort |
| Couple/date organizer | Atmosphere and novelty can matter. | Social and map discovery strong; "romantic" is subjective. | Need mood evidence and privacy-sensitive interpretation. | Contrast cohort |

**Recommend testing 1–2 audience hypotheses first:** (A) local residents, particularly the person proposing a same-day or weekend outing for two to four people; (B) domestic visitors making a near-term choice from a selected neighborhood. Within A, include solo and couple tasks to see whether "group coordination" is actually the hard part. **Requires primary research:** frequency, frustration, willingness to use a new tool, and whether the organizer role is stable enough to target.

## 7. Existing Discovery Workflow

**Illustrative reconstruction A, short-notice resident outing.** A friend messages "what are we doing tonight?" The organizer asks about budget and timing, searches TikTok/Instagram/Snap Map or a group chat for ideas, checks Maps for route and reviews, looks at an event or venue site for exact hours and tickets, sends links, receives vetoes, then settles on an option. TikTok Nearby and Snap Map explicitly support nearby/local content; Instagram Map supports viewing location-tagged content from friends and creators in some markets. This makes social discovery plausible, but the sequence and Saudi use need observation. [TikTok Nearby](https://newsroom.tiktok.com/tiktok-nearby-discover-whats-happening-around-you?lang=en-GB), [Snap Map places](https://newsroom.snap.com/launching-sponsored-snaps-and-promoted-places?lang=en-GB), [Instagram Map](https://about.fb.com/news/2025/10/now-in-india-instagram-rolls-out-map-feature-to-help-people-connect-with-friends/)

**Illustrative reconstruction B, known event.** The user hears about a concert or workshop from a friend/creator, searches the name, lands on webook, Fever or another organizer's page, checks a date, price and tickets, then opens Maps for travel. The product may add little value here unless it surfaces relevant *other* options or reduces failure at the final decision. webook advertises "Today," "Weekend," sports, concerts and experiences; Fever presents curated city experiences; Eventbrite supports event search by location and type. [webook](https://webook.com/en), [Fever](https://feverup.com/en?c=1), [Eventbrite](https://eventbrite.com/)

**Illustrative reconstruction C, traveler.** A visitor starts with a guide, Google Search or Tripadvisor to learn an area, saves several places in Maps or Wanderlog, and then checks official sites and transit or drive times as dates approach. Wanderlog already offers itinerary, travel times, reservations and collaboration; Google Maps offers lists. The opportunity is therefore early mixed-domain choice or trustworthy local timing, not basic save-and-plan functionality. [Wanderlog](https://wanderlog.com/), [Google Maps lists](https://blog.google/products-and-platforms/products/maps/google-maps-updates-summer-travel-2024/)

**Likely breakpoints to test:** (1) an appealing idea lacks a clear date, booking or price; (2) a result is reachable in kilometers but not in the available minutes; (3) social media content is old or promotional; (4) friends reject otherwise attractive options for different reasons; (5) a list repeats famous venues while overlooking relevant small offerings; (6) the person cannot compare venue, workshop and event on the same practical terms. These are **product interpretations**, not observed failure rates. The study must record every switch and veto before deciding which breakpoint is costly.

## 8. Discovery Search Behavior

People can express a category ("museums"), a purpose ("date idea"), a constraint ("open after 10"), an experiential quality ("somewhere calm"), or an exploration aim ("what's new"). Google itself uses a compound Search AI Mode example combining weekend, friends, food, chill and offbeat. That documents support for this query style, not its prevalence. [Google AI Mode example](https://blog.google/products-and-platforms/products/search/ai-mode-development/)

| Dimension | Natural language examples | Research implication |
|---|---|---|
| **WHAT** | "karting," "culture," "something fun," "not just coffee" | Exact type and open-ended intent coexist. |
| **WHERE** | "near me," "around the hotel," "not across town" | Origin and acceptable journey are contextual. |
| **WHEN** | "now," "after work," "this Friday," "before dinner" | The calendar window can be harder than the category. |
| **WHO** | "with my parents," "four of us," "alone," "date" | Group fit can be an eligibility issue. |
| **Cost/duration** | "free," "under 150 each," "got two hours" | Need to distinguish per-person from total and travel from visit time. |
| **Transport/environment** | "walking," "no driving," "indoors, too hot" | Distance and weather comfort depend on mode and time. |
| **Discovery value** | "somewhere new," "local," "not touristy" | Requires familiarity and source evidence, not a category token. |

Compound queries matter because one ignored part can invalidate a good-looking result. The query corpus in Section 25 deliberately includes unfinished, messy and contradictory language. **Requires primary research:** capture verbatim queries from observed tasks and compare the synthetic distribution with real phrasing in Arabic and English.

## 9. Hard Constraints vs Soft Preferences

The distinction is **context-dependent**. "Indoors" is a hard exclusion when a user says "nothing outdoors because of heat," but a soft preference when they say "preferably indoors." "Under 100 SAR" may be a strict cap or a rough budget. Preserve the user's wording and ask when the difference changes the answer.

| Usually hard when explicitly stated | Usually soft unless explicitly stated |
|---|---|
| Correct date and usable interval; not closed/cancelled; maximum travel time; accessibility/age need; group capacity; reservation or slot required; explicit "no X"; strict budget; fixed end commitment. | Quiet, romantic, adventurous, scenic, unusual, independent, less touristy, less crowded, relaxing, creative, preferably close, "not too expensive." |

**Product interpretation:** false eligibility is generally more damaging than an imperfect mood match because the user may travel or buy on that claim. The exact severity order may differ by scenario. A wheelchair-accessibility error can be decisive; an uncertain quietness claim may only disappoint. The observed study should ask participants to rank *actual rejection reasons* and note which claims they verify. Do not force all missing facts into "false"; unknown availability or accessibility can require abstention.

## 10. Result Rejection Taxonomy

Record the **first disqualifying reason** and secondary reasons. Rejection is not evidence of a bad place; it may be a bad fit for this occasion.

| Rejection reason | Primary class | What to observe |
|---|---|---|
| Too far by selected mode; parking or access difficult | Eligibility/feasibility | Did the user inspect a route or infer distance? |
| Closed, wrong day/time, event ended/cancelled | Eligibility/freshness | Which source corrected the first listing? |
| No slot, ticket, walk-in access or capacity | Eligibility/information | Was "venue open" mistaken for available activity? |
| Over budget or price unclear | Eligibility or trust | Strict cap, total versus per-person, hidden fees. |
| Too long/short for the available window | Feasibility | Whether travel and buffer were included. |
| Wrong age, group, accessibility or weather fit | Eligibility | Which practical detail made the choice impossible? |
| Wrong activity or atmosphere | Relevance/preference | What phrase in the query was ignored? |
| Too generic, touristy, familiar, already visited | Discovery failure | Is novelty worth extra effort or cost? |
| Low perceived quality, crowding, weak photos | Quality | What evidence drives the judgment? |
| Contradictory hours, stale post, promotional-only proof | Trust/freshness | Did the person seek an official page or call? |
| Five near-identical options or no clear comparison | Diversity/comparison | Did sameness slow the decision? |

The study should distinguish a user veto from a source omission. A participant may reject a place because it *looks* crowded even if actual crowd levels are unknown. Record the participant's reasoning, not the researcher's assumption that the venue is crowded.

## 11. What Makes an Option Worthwhile

"Worthwhile" is a **situated tradeoff**, not a universal rating. The person compares expected enjoyment or meaning with money, travel, waiting, coordination and risk. Likely components are expected quality, novelty, atmosphere, local significance, social fit, convenient timing, duration, price and confidence that the facts are true. A "worthwhile" experience for a two-hour solo gap can differ from a planned family day.

Reviews and photos help people assess a candidate: a 2023 tourist restaurant study specifically analyzes pictorial and written information and positive/negative reviews in risk reduction. Yet a rating does not encode tonight's hours, the group's interests, travel effort or whether the user has already been there. Review manipulation is also a recognized risk, as shown by the FTC's 2024 rule, though that rule is not Saudi evidence. [Surrey study](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/Tourists-Online-Information-Search-Behavior-Combined/99818303302346), [FTC rule](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers)

**Requires primary research:** ask for a recent excellent outing and a regretted one, then reconstruct the choice. Test whether participants value a novel option that needs 25 minutes of driving over a familiar option 10 minutes away. Do not choose a ranking formula in R00.

## 12. Search-Type Analysis

| Search family | Example | Existing-tool position | Possible product opening |
|---|---|---|---|
| Known item | "Where is Ithra?" | Maps and official sites are strong. | Little differentiation; serve only as utility. |
| Category | "Coffee shops in Al Khobar" | Maps, Search and social platforms have abundant results. | Differentiate only if special attributes or recency matter. |
| Attribute | "Quiet café with parking" | Maps reviews and Search can help; judgment may take work. | Grounded experiential and practical fit. |
| Open discovery | "Somewhere interesting tonight" | Maps AI, Search AI, TikTok Nearby and local guides are direct competitors. | Mixed types and practical feasibility, if demonstrably better. |
| Constraint-heavy discovery | "Unusual indoor activity for four tonight, no booking, under 150 each, 20 minutes away" | Some tools accept the words; data and joint verification are demanding. | Strongest differentiation hypothesis, but perhaps too rare. |

This is a hypothesis about comparative *performance*. Google explicitly supports complex local prompts, so the product must win on accuracy, breadth of relevant types, decision effort, or local coverage rather than on "natural language" alone. [Google Maps](https://blog.google/products-and-platforms/products/maps/20-years-google-maps-20-features/), [Google Search](https://blog.google/products-and-platforms/products/search/ai-mode-development/)

## 13. Decision Confidence

Confidence requires enough proof to act. The essentials change by request; the table is a proposed observation rubric.

| Use case | Essential to decide | Important | Often optional |
|---|---|---|---|
| Go now to a permanent venue | Current operating status, address, travel time, relevant price/entry rule | Photos, recent reviews, parking/access | Editorial backstory |
| Attend a dated event | Exact date/start/end, location, status, ticket/entry availability, total price | Seating, language, age suitability, cancellation terms | Broad neighborhood guide |
| Join an activity with four people | Session/booking, group capacity, duration, cost per person, requirements | Setup time, parking, photos, reviews | Historic significance |
| Quiet solo stop | Open interval, atmosphere evidence, plausible dwell time, distance | Seating, noise/time-of-day, Wi-Fi if work-related | Ticketing details |
| Save for a future trip | Durable identity, area, seasonal relevance | Indicative price, opening pattern, reason to visit | Live "open now" or current slot |

People may still call a venue or check an official account when evidence is thin. The R00 study should record both *which fact was checked* and *which source satisfied the person*. Images and reviews can help form expectations, but high confidence about "open tonight" needs current operational evidence. The Ithra event site, for example, separately presents dated museum sessions, last-entry guidance and general visiting hours; these are different facts a user must reconcile. [Ithra museum schedule](https://www.ithra.com/en/programme/2026/ithra-museum)

## 14. Local vs Traveler

Both can share the same core decision representation: area, time, activity intent, practical limits and trust. Their default context differs. **Product interpretation:** locals likely recognize headline attractions and may demand novelty; visitors need orientation and may welcome famous sites. Locals can make more repeated short-notice choices; a traveler may have a more intense but episodic trip need. Neither claim is proven for the project's first audience.

| Dimension | Local-resident hypothesis | Traveler hypothesis |
|---|---|---|
| Familiarity | Knows obvious options; "new to me" matters. | May need landmarks and neighborhood context. |
| Timing | Same day or weekend; last-minute availability. | Plans days or weeks ahead; future hours uncertain. |
| Geography | Home, workplace, friends' origins, recurring routes. | Hotel, attractions, transit access and clustered areas. |
| Trust | May know local accounts or friends to verify. | May rely more on official sites, reviews and maps. |
| Repeat use | Potential weekly/seasonal, unmeasured. | Per-trip, unless frequent domestic travel. |

The 2023 tourist information-search study supports the role of photos and reviews for international restaurant decisions; it does not establish the behavior of Saudi residents. [Surrey study](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/Tourists-Online-Information-Search-Behavior-Combined/99818303302346) **Recommendation:** keep one discovery core and test separate defaults. Do not create two products before observing distinct workflows.

## 15. Hidden / Local Discovery

The phrases "hidden gem," "local favorite," "under the radar," "independent," "unusual," and "newly opened" express different requests. Hidden/under-the-radar concerns *exposure*; local favorite concerns *whose endorsement*; independent concerns *ownership*; unusual concerns *distinctiveness*; newly opened concerns *time*. A user may mean "new to me" rather than objectively obscure. Ask them to clarify through examples in the later study.

Google Maps already publishes "Gems" and "Trending" lists in some cities, and Atlas Obscura curates unusual places worldwide. Thus neither a hidden-gem label nor a quirky-place directory is unique. [Google Maps lists](https://blog.google/products-and-platforms/products/maps/google-maps-updates-summer-travel-2024/), [Atlas Obscura app](https://app.atlasobscura.com/)

**Product interpretation:** assess potential local discoveries through credible quality relative to exposure, geographic/category uniqueness, dated community or expert mentions, recent opening, and evidence that the place is actually usable. Low review volume alone can mean new, neglected, inaccessible or poor. A viral video can make a place fashionable but crowded; copied listicles can make an old recommendation appear freshly endorsed. Do not call a venue "hidden" until its quality and practical information have been checked. R07 should later design ranking; R00 asks whether people value such results and what would convince them to try one.

## 16. Temporal Discovery

Time expressions describe different decisions: "now" requires current opening and enough remaining time; "tonight" requires a local window and possibly an activity session; "this weekend" needs correct dates; "before dinner" needs a deadline and travel buffer; "newly opened" needs a business-opening date rather than a listing's publication date. Temporary events have cancellation and sold-out risk. Future trips need a warning that today's hours do not prove next month's schedule.

Saudi timing adds material context. Visit Saudi describes summer heat and the value of early/late outdoor activity; its Ramadan guide describes a shift toward after-sunset activity. Riyadh and Jeddah seasons create temporary programs with defined dates. These sources support treating weather and calendar as context, but not assuming every resident follows one pattern. [Visit Saudi climate](https://www.visitsaudi.com/en/stories/climate-and-seasons), [Ramadan guide](https://www.visitsaudi.com/en/campaigns/discover-ramadan), [Saudi seasons calendar](https://www.visitsaudi.com/en/calendar.html)

**Hypothesis:** reliable temporal feasibility may improve near-term decisions more than a sophisticated semantic description. Test it by observing which facts cause rejection and by comparing plain-category search with verified time-aware choices. Do not claim the hypothesis is proven by the mere existence of event listings.

## 17. Geographic / Travel-Time Discovery

Users may refer to a neighborhood, hotel, mall, another planned stop, "around here," a 15-minute drive, or a walk they are willing to take. A radius measures geometric proximity, while a journey depends on road layout, mode, departure time, congestion, crossings and parking. Recreation research models travel time as part of destination choice; it does not provide a Saudi-specific weight. [Recreation travel-time study](https://www.sciencedirect.com/science/article/pii/S0095069613000880)

Saudi geography should not be flattened into "car only." An official Riyadh city review says car travel dominates there, while Riyadh Metro opened in late 2024 and government trip planning now covers metro and bus. The correct mode is a user-context question, especially in district-scale tests. GASTAT reports 2024 average daily round-trip commute times of 67 minutes in Riyadh, 55 in Jeddah and 51 for Dammam city; these are **commute context**, not leisure-trip times. [Riyadh city review](https://www.rcrc.gov.sa/wp-content/uploads/2025/11/Riyadh-Citys-Voluntary-Local-Review-VLR-2024.pdf), [Riyadh Metro](https://alriyadh.gov.sa/en/new/projects/metro-alriyadh), [GASTAT city report](https://www.stats.gov.sa/documents/20117/2435245/GASTAT_LISC%2Breport_2025_EN.pdf/80b46893-12e0-2b26-2a54-70a1553169c1)

**Requires primary research:** ask people to show the journey they actually considered and what "nearby" meant for this outing. R00 should not choose a routing provider or algorithm.

## 18. Competitive Workflow Analysis

These products are not interchangeable. The question is which step a person gives each product and what still requires checking. "Residual decision" below is a **product interpretation to observe**, not a proven product defect. Capabilities and regional rollout can change; the cited pages were checked in September 2026.

| Product / source | Job it serves and how discovery happens | Time, location, trust and planning strengths | Residual decision to observe |
|---|---|---|---|
| **Google Search and AI Mode** | Broad web research; accepts detailed local prompts and follow-ups. | Place cards can show ratings, reviews and hours; Search can combine sources. [Google Search](https://blog.google/products-and-platforms/products/search/ai-mode-development/), [place cards](https://blog.google/products-and-platforms/products/search/ai-mode-updates-may-2025/) | Does the user still verify dates, slots, travel and group fit elsewhere? Search AI availability and behavior in Saudi Arabia need direct testing. |
| **Google Maps** | Known places, nearby options, reviews, navigation, saved/collaborative lists; Gemini ideas in supported markets. | Strong location context, route, operating-hours and social choice tools; 2025 Explore updates show trends and curated lists. [Maps discovery](https://blog.google/products-and-platforms/products/maps/20-years-google-maps-20-features/), [Explore update](https://blog.google/products-and-platforms/products/maps/holiday-gemini-tips-new-explore-tab/) | The main competitor. Does a mixed venue/event/activity query with strict time and availability still require cross-checking? Do not assume it does. |
| **TikTok** | Video-led inspiration, creator suggestions and local feed discovery. | Nearby content can include travel, events and food; rich visual atmosphere. [TikTok Nearby](https://newsroom.tiktok.com/tiktok-nearby-discover-whats-happening-around-you?lang=en-GB) | An attractive clip may require checking date, location, price and current status elsewhere. Rollout varies by market. |
| **Instagram** | Creator/friend posts, venue accounts, location-tagged content and social proof. | Visual atmosphere and direct venue updates; Instagram Map shows tagged content in supported markets. [Instagram Map](https://about.fb.com/news/2025/10/now-in-india-instagram-rolls-out-map-feature-to-help-people-connect-with-friends/) | Is the relevant post current, and can the group use the place at the planned time? Saudi usage for this decision is unmeasured here. |
| **Snapchat / Snap Map** | Friends' activity, nearby places and local trends. | Snap describes Snap Map as a place to see what is happening nearby and popular local places. [Snap Map](https://newsroom.snap.com/launching-sponsored-snaps-and-promoted-places?lang=en-GB), [Place Loyalty](https://newsroom.snap.com/place-loyalty?lang=en-GB&useContentAccordionItems=%27%22efx) | Social/trending signals may inspire but not prove booking, price or group suitability. |
| **Reddit, blogs, messaging and word of mouth** | Local opinion, unusual suggestions and backstories; messages coordinate a group. | Human context and candid tradeoffs may be useful; Reddit now integrates AI-assisted answers with its conversations. [Reddit Answers](https://redditinc.com/news/introducing-reddit-answers) | Advice can age; a trusted friend's suggestion still needs schedule and route checking. Ask participants how much they trust each source. |
| **Tripadvisor** | Destination-oriented attractions, reviews and bookable experiences. | Good comparative traveler content and review volume. [Tripadvisor Things to Do](https://www.tripadvisor.com/Attractions) | Does it help with short-notice local mood and real travel window, or mainly with destination shortlist? Test rather than assume. |
| **Eventbrite** | Discover dated events by place and interest; ticketing. | Event and category entry points. [Eventbrite](https://eventbrite.com/) | A permanent venue, open-ended activity or local shop may sit outside the event search. Actual local coverage varies. |
| **Fever** | Curated city entertainment and bookable experiences. | Specific cities, event/experience presentation and checkout. [Fever](https://feverup.com/en?c=1) | Does the person want ticketed curated experiences or broader, less commercial choices? |
| **Wanderlog** | Organize a known trip: destinations, reservations, collaborative itinerary, routes. | Check distances/travel times and attraction hours; optimize route. [Wanderlog](https://wanderlog.com/) | If the user has no candidate set yet, does planning impose work before discovery? |
| **Atlas Obscura** | Discover unusual places and read their stories. | Curated oddities, map, lists and community tips. [Atlas Obscura app](https://app.atlasobscura.com/) | Does an unusual place actually fit today's hours, journey and group? |
| **AllTrails** | Find a specific outdoor route with difficulty, length and suitability filters. | Specialized trail geometry and practical trail attributes. [AllTrails filters](https://support.alltrails.com/hc/en-us/articles/37227964040852-How-to-use-filters-to-find-trails) | Strong inside outdoors; the cross-domain decision between a hike and an indoor activity remains elsewhere. |
| **webook** | Saudi event, sport, experience and booking discovery, including "Today" and "Weekend." | Strong regional dated/paid inventory and transaction path. [webook](https://webook.com/en) | Does it cover independent unticketed options and vague experience moods with enough practical comparison? Audit actual listings. |
| **Visit Saudi / Enjoy** | Official destination and entertainment calendars, guides and attractions. | Visit Saudi joins attractions, experiences and events; Enjoy is a GEA event discovery initiative with nearby events and sharing. [Visit Saudi things to do](https://www.visitsaudi.com/en/things-to-do?sortBy=manual_order), [GEA Enjoy](https://www.gea.gov.sa/en/media-center/news/enjoy-platform-2) | Can people find a short, mixed, feasible option from their exact starting point, or must they verify across pages? Test on live tasks. |

The competitive bar is higher than v0.1 implied. Google, TikTok and Snapchat are moving toward contextual local discovery, and webook/Visit Saudi hold strong local content. A new product should **not** claim "one place for everything" without first demonstrating a narrower win: fewer false options, quicker confident choice, or locally distinctive options missed by the participant's normal process. A tool-switch count alone is not pain if each tool provides valuable verification.

## 19. Saudi Arabia Context

**Documented evidence.** GASTAT's 2024 survey shows broad participation but an uneven mix: 65.8% reported visiting parks/gardens, 61.9% shopping malls, 60.2% spending time in desert or at a beach, 24.9% cinemas, 13.4% museums and 6.5% art exhibitions. These are participation proportions for people aged 15+, not a ranking of desired recommendations or a statement that one area has those options nearby. [GASTAT 2024 survey](https://www.stats.gov.sa/documents/20117/2435273/Household%2BCulture%2Band%2BEntertainment%2BStatistics%2BPublication%2B2024%2BEN.pdf/591d6f59-c7ae-5ef4-0190-56643b41f4e7)

**Documented evidence.** The General Entertainment Authority reported 5,406 approved entertainment events and more than 72 million event/recreation visits in 2023. These are sector totals and visits, not unique users or evidence that the project's chosen neighborhoods have live feeds. Official calendars now span seasonal and temporary programs; Riyadh Season 2025–26 and Jeddah Season pages illustrate the importance of date-specific content. [GEA 2023 release](https://www.gea.gov.sa/en/media-center/news/72-million-visitors), [Riyadh Season](https://www.visitsaudi.com/en/seasons/riyadh-season), [Jeddah Season](https://www.visitsaudi.com/en/seasons/jeddah-season)

**Documented evidence.** Visit Saudi describes strong summer heat, coastal humidity in Jeddah and Dammam, and seasonal differences in outdoor suitability. Its Ramadan material describes more active evenings after sunset. These justify asking about time and indoor/outdoor preference; they do not justify assuming that "outdoors" is always wrong in Saudi Arabia. [Climate and seasons](https://www.visitsaudi.com/en/stories/climate-and-seasons), [Ramadan](https://www.visitsaudi.com/en/campaigns/discover-ramadan)

**Documented evidence.** Riyadh's official local review describes car-dominated mobility, while the Metro has opened. GASTAT's city tourism figures for 2024 list about 15.4 million overnight tourists in Riyadh, 11.3 million in Jeddah and 9.1 million in the Dammam metropolitan area. These indicate sizeable visitor contexts, not local discovery demand or equally dense supply. [Riyadh review](https://www.rcrc.gov.sa/wp-content/uploads/2025/11/Riyadh-Citys-Voluntary-Local-Review-VLR-2024.pdf), [GASTAT city report](https://www.stats.gov.sa/documents/20117/2435245/GASTAT_LISC%2Breport_2025_EN.pdf/80b46893-12e0-2b26-2a54-70a1553169c1)

**Product interpretation by area.** Riyadh offers a large seasonal entertainment program and areas such as Diriyah/JAX with cultural offerings; its size and traffic increase travel-fit risk. Jeddah's Al-Balad combines heritage, markets, cafés and a major immersive museum within a recognizable district; its tourist and resident mixes may differ. Dammam–Al Khobar–Dhahran is a connected urban cluster with a waterfront, café/retail areas and Ithra's museum, exhibitions and workshops. These are **candidate environments**, not audited content inventories. [JAX District](https://www.visitsaudi.com/en/diriyah/attractions/jax-in-diriyah), [Historic Jeddah](https://www.visitsaudi.com/en/jeddah/attractions/summer-night-adventures-in-al-balad), [Khobar seafront](https://www.visitsaudi.com/en/eastern-province/attractions/khobar-seafront), [Ithra programme](https://www.ithra.com/en/programme/2026/ithra-museum)

Saudi social-media use for *this exact choice* remains insufficiently documented. A 2024 Saudi dissertation examines how TikTok, Snapchat and Instagram affect travel destination choices among younger cohorts, but destination choice is different from choosing an outing tonight. Platform statements describe nearby-place discovery globally, not actual first-app use in Al Khobar or Jeddah. Observe Arabic, English and mixed-language search and WhatsApp/Snap sharing instead of importing US/European assumptions. [Saudi dissertation record](https://drepo.sdl.edu.sa/items/e563f79b-9141-4106-ba3b-d083b59ff4b5), [Snap Map description](https://newsroom.snap.com/launching-sponsored-snaps-and-promoted-places?lang=en-GB)

## 20. Candidate Test Environments

These are **four audit candidates**, not a launch ranking. "Promising" means source-backed anchors exist; option density, correction cost, travel-time distribution and recruiting access remain unknown. R02 should sample connected catchments rather than every address in a city.

| Candidate catchment | Why it could test the thesis | Main uncertainty to resolve in R01/R02 |
|---|---|---|
| **Al Khobar waterfront–Dhahran/Ithra–nearby Dammam cluster** | Resident repeat context; waterfront, independent café and cultural/activity mix. Ithra publishes dated sessions, ticket and age details, giving a concrete temporal test. [Khobar seafront](https://www.visitsaudi.com/en/eastern-province/attractions/khobar-seafront), [Ithra](https://www.ithra.com/en/programme/2026/ithra-museum) | Is the practical travel catchment compact enough? How many independent options and sources can be verified each week? Access to participant groups is unknown. |
| **Riyadh Diriyah–JAX–Bujairi/At-Turaif area** | Cultural, heritage, art, dining and seasonal discovery in a recognizable destination area. [JAX](https://www.visitsaudi.com/en/diriyah/attractions/jax-in-diriyah), [Visit Saudi Riyadh](https://www.visitsaudi.com/en/riyadh/riyadh-season) | Event rights, seasonal variation, traffic/parking and whether the mix answers weekday as well as weekend queries. |
| **Historic Jeddah / Al-Balad catchment** | Dense heritage, markets, cafés and immersive culture; useful resident-versus-visitor contrast. [Historic Jeddah](https://www.visitsaudi.com/en/jeddah/attractions/summer-night-adventures-in-al-balad) | Exact walking/access conditions, operating hours by venue, whether most choices are already obvious and whether daytime heat changes use. |
| **Riyadh Boulevard City–Hittin entertainment catchment** | Dated events, activity zones and ticketing give a strong "tonight with friends" test. [Riyadh Season](https://www.visitsaudi.com/en/seasons/riyadh-season), [webook](https://webook.com/en) | Seasonal concentration, ticket-provider dependence and a risk of testing one mega-destination rather than cross-domain local discovery. |

R01 should assess rights before ingesting any listing. R02 should measure coverage by *time window and choice type*, not simply count pins. A feasible candidate may win because it is easier to verify, even if another has more raw listings. No final launch decision is justified now.

## 21. Problem Frequency

**Documented evidence:** Saudi population-level participation in cultural and entertainment venues is high on an annual measure; official city tourism totals and GEA event visits show significant activity. None of those sources tells us how frequently a particular resident faces an unresolved "what shall we do tonight?" choice. Event-page traffic and annual tourist counts are likewise not individual repeat-use measures. [GASTAT participation](https://www.stats.gov.sa/documents/20117/2435273/Household%2BCulture%2Band%2BEntertainment%2BStatistics%2BPublication%2B2024%2BEN.pdf/591d6f59-c7ae-5ef4-0190-56643b41f4e7), [GASTAT city tourism](https://www.stats.gov.sa/documents/20117/2435245/GASTAT_LISC%2Breport_2025_EN.pdf/80b46893-12e0-2b26-2a54-70a1553169c1), [GEA event visits](https://www.gea.gov.sa/en/media-center/news/72-million-visitors)

**Hypothesis:** a local organizer encounters a meaningful version of the choice on some evenings or weekends and when friends/family visit. A traveler encounters it intensely during a trip but may not return between trips. A person seeking only a once-a-year festival is a weaker basis for a frequently used standalone product. **Requires primary research:** use a 4-week recall calendar of actual attempted outings, including plans cancelled or defaulted to a familiar place. Ask how often the decision was genuinely hard, who initiated it, and how much time they spent; avoid asking "would you use an app weekly?"

## 22. Repeat-Usage Potential

Repeat use could come from recurring choices with changing inputs: group composition, mood, new openings, temporary exhibitions, weekends, weather and neighborhood. It could fail if the product repeatedly shows the same few options, if Google/Maps becomes good enough, or if only rare high-effort outings justify a specialist service.

Measure **repeatable decision occasions**, not app-open intention. In the user study, reconstruct the last three outings and the next plausible one. Later, measure whether a person returns for a *new decision*, whether they select a new-to-them option, and whether the choice was actually carried out. A saved-item count alone does not establish repeat utility. **Requires primary research:** how often do people seek novelty rather than deliberately repeat trusted favorites?

## 23. Candidate Product Promises

These are alternatives to test, not positioning statements to lock in. Supporting evidence establishes adjacent behavior or available content; it does not validate unmet demand.

| Promise | First-user and decision | Include / exclude | Why it might win; evidence | Major uncertainty and risk |
|---|---|---|---|---|
| **A. "Choose a feasible outing tonight."** | Local resident organizing one to four people; pick an option within a defined time/travel/budget window. | Include selected activities, cultural venues, exhibitions and verifiable events. Exclude broad restaurants, unverified live capacity, remote outdoor trips. | Strong practical contrast with inspiration feeds; official calendars and venue pages expose dated detail. [webook](https://webook.com/en), [Ithra](https://www.ithra.com/en/programme/2026/ithra-museum) | Does it occur often and hurt enough? Google Maps and Search may already solve it. Booking evidence may be inaccessible. |
| **B. "Find something new to do in your own area this weekend."** | Resident who knows the obvious places; select a fresh but credible option. | Include local exhibitions, workshops, independent cultural/retail spots and selected events. Exclude generic directories and unverified "hidden gems." | GASTAT confirms varied participation; Google itself offers Gems/Trending, proving demand is being pursued. [GASTAT](https://www.stats.gov.sa/documents/20117/2435273/Household%2BCulture%2Band%2BEntertainment%2BStatistics%2BPublication%2B2024%2BEN.pdf/591d6f59-c7ae-5ef4-0190-56643b41f4e7), [Maps lists](https://blog.google/products-and-platforms/products/maps/google-maps-updates-summer-travel-2024/) | Local novelty requires continuous sourcing; copycat recommendations would fail. |
| **C. "Pick a low-friction group activity."** | Friend-group organizer; choose an activity that fits size, cost and booking notice. | Include activity venues, walk-in experiences, workshops with confirmed group access. Exclude events with unclear capacity. | Coordination creates several potential vetoes; bookable experiences exist in local platforms. [webook](https://webook.com/en) | Group capacity/walk-in truth may be unavailable; groups may simply message and settle quickly. |
| **D. "Know what fits around your hotel today."** | Domestic visitor; choose a worthwhile near-term stop in one district. | Include cultural venues, markets, activities, selected cafés and dated events. Exclude full itineraries. | Official tourism and map sources provide orientation; visitors face lower familiarity. [Visit Saudi things to do](https://www.visitsaudi.com/en/things-to-do?sortBy=manual_order) | Episodic personal use and strong existing travel tools. |
| **E. "Discover a quiet or unusual local stop."** | Solo/couple resident; decide where to spend a spare hour or two. | Include quiet cultural/retail/café stops with atmosphere evidence. Exclude unsupported mood tags. | Tests experiential intent beyond category search; Atlas Obscura and Maps Gems show competition for unusual finds. [Atlas Obscura](https://app.atlasobscura.com/), [Maps Gems](https://blog.google/products-and-platforms/products/maps/google-maps-updates-summer-travel-2024/) | Quietness changes with time; user mood is subjective and evidence may be weak. |

**Recommend testing A and B first.** A has clear feasibility outcomes; B tests the discovery value that could distinguish the product after basic filtering. C is a task variant within A. D is the secondary-user contrast. E can be a query and interview probe. If A is easy with Google Maps/Search or if verified data is too costly, do not force the thesis; consider B or another narrower job.

## 24. Recommended Initial Scope

For a first **discovery experiment**, use a legally reviewable set of four content families: (1) cultural venues and their current exhibitions; (2) repeatable indoor activities with stated duration, price and booking policy; (3) selected dated events/workshops from organizers with current schedules; (4) a small curated set of locally distinctive, independently verifiable stops such as a bookstore, specialty café or market. These create meaningful cross-domain alternatives without turning the product into a generic places index.

Choose items only when the experiment can verify identity, exact access point, relevant operating/occurrence time, price or price range, and booking requirement. "Unknown" must remain visible. The first set should cover the test's key time windows: weekday evening, Thursday/Friday or local weekend, short pre-commitment window, and a future visit date. R02 determines whether these families contain enough options in any candidate area.

**Defer:** hiking/camping and remote outdoors (route, condition and safety burden); broad restaurant and mall coverage (strong incumbents and volume); automatic booking or capacity claims without a direct source; every pop-up/social post; full itinerary, alerts and personalization. A coastal walk or accessible park can be included as a simple permanent outdoor contrast only when heat/time/access are handled honestly. The precise inclusion set is conditional on R01 rights and R02 accuracy.

## 25. 100-Query Corpus

These **100 synthetic, realistic prompts** are working examples for R05, not user quotes, search logs or prevalence evidence. Keep their informal wording. "Place" is the expressed origin/destination, not a geocoded location; "time" is the expressed window; "hard" contains only explicit or logically required conditions; "soft" contains preferences; "ambiguous" records wording with competing interpretations; "missing" identifies information a search may need. `none` means none stated. Each family's code in the Family column is an annotation: **V** vague/immediate, **G** group/evening, **W** bounded window, **A** active/indoor, **E** events/culture, **F** family/access, **C** couples/social, **S** solo/quiet, **N** novelty/local, **T** destination/future. Queries mix resident and visitor contexts deliberately. Do not impose the same defaults on all of them.

### V. Vague and immediate discovery

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 001 | bored what can I do | Current area | Now? | none | Interesting | Whether to leave now | Origin, time, mode | V |
| 002 | anything fun around here | Current area | Unstated | none | Fun | "Fun" and radius | Origin, time, party | V |
| 003 | what can we do rn | Current area | Now | none | — | "We" size | Origin, group, mode | V |
| 004 | somewhere to go after work | Work area? | After work | none | Low effort | Work end and origin | Time, transport | V |
| 005 | show me stuff nearby that's not food | Current area | Unstated | No food | Variety | "Stuff," radius | Origin, time | V |
| 006 | don't know what I want, surprise me | Current area? | Unstated | none | Novelty | All intent and place | Origin, time, transport | V |
| 007 | anything open and interesting | Current area? | Now | Open now | Interesting | "Interesting" | Origin, mode | V |
| 008 | where should I go tonight | Current area? | Tonight | none | — | Venue or activity | Origin, party, budget | V |
| 009 | something chill to do later | Current area? | Later today? | none | Chill | Time and "chill" | Origin, exact window | V |
| 010 | ideas for this afternoon, not the mall again | Current area? | This afternoon | No mall | Novelty | Length of outing | Origin, mode, budget | V |

### G. Friends and group evenings

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 011 | anything going on tonight? | Current city | Tonight | none | Events? | Event versus activity | Origin, budget | G |
| 012 | four of us need something fun tonight | Current area | Tonight | Group of 4 | Fun | Meaning of fun | Origin, mode, budget | G |
| 013 | no restaurants, just something to do with friends | Current area | Unstated | No restaurants | Social | Group size, activity | Time, origin | G |
| 014 | we can leave at 9 and don't want to book | Current area | Tonight after 9 | No advance booking | Spontaneous | "Leave" versus arrive | Origin, group, travel cap | G |
| 015 | bowling or something like that for six | Current area | Unstated | Group of 6 | Bowling-like | Alternative breadth | Time, booking, origin | G |
| 016 | guys are bored, under 100 each | Current area | Now? | ≤100 SAR/person | Social, fun | "Guys," currency assumption | Origin, group, time | G |
| 017 | is there paintball tonight without a reservation | Current area | Tonight | Paintball; no reservation | none | Walk-in versus same-day booking | Origin, group, price | G |
| 018 | somewhere for friends that's not loud | Current area | Unstated | none | Quiet, social | How quiet | Origin, time, group | G |
| 019 | make it different, we've done every escape room | Current area | Unstated | No escape rooms | Novel | What else visited | Origin, time, group | G |
| 020 | can we do anything after the match ends | Match venue? | After match | none | Convenient | Match end time, "anything" | Venue, end time, group | G |

### W. Bounded windows and travel limits

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 021 | got like two hours before dinner | Current area | Before dinner | Total ≈2h | Interesting? | Whether travel included | Dinner place/time, mode | W |
| 022 | 90 mins near KAFD, no food | KAFD, Riyadh | Current window? | ≤90m; no food | Nearby | Visit versus total time | Start time, mode | W |
| 023 | something under an hour from my hotel | Hotel | Unstated | Duration <1h? | none | Travel or visit duration | Hotel, date, mode | W |
| 024 | don't send me across Riyadh, 20 min max | Current Riyadh origin | Unstated | ≤20m travel | none | Mode/traffic | Origin, time, mode | W |
| 025 | quick stop before I pick up the kids | Current route? | Before pickup | Deadline | Quick | Pickup location/time | Origin, destination, time | W |
| 026 | between 5 and 7 near the corniche | Khobar or Jeddah corniche? | 17:00–19:00 | Window | Nearby | Which corniche | City, date, mode | W |
| 027 | half an hour walk from here max | Current area | Unstated | ≤30m walking | none | One-way or total | Origin, time | W |
| 028 | something we can actually finish before 8 | Current area | Before 20:00 | End deadline | none | Includes return? | Start, origin, mode | W |
| 029 | I'm in Al Balad for only 45 minutes | Jeddah Al-Balad | Current visit | ≤45m total | Local | Start point | Exact origin, mobility | W |
| 030 | cheap activity within 15 minutes driving | Current area | Unstated | ≤15m drive | Cheap, active | "Cheap" threshold | Origin, time, budget | W |

### A. Activity, exertion and environment

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 031 | something active indoors, it's too hot | Current area | Soon? | Indoor | Active | Exertion level | Origin, time, party | A |
| 032 | karting near me open tonight | Current area | Tonight | Karting; operating tonight | Nearby | Venue open versus slots | Origin, group, booking | A |
| 033 | adventurous but I don't want to get sweaty | Current area | Unstated | none | Adventurous, low exertion | Degree of activity | Origin, time, budget | A |
| 034 | paintball for beginners tomorrow | Current area | Tomorrow | Paintball; beginner-suitable | none | Ages/equipment | Origin, group, time | A |
| 035 | something physical but no gym | Current area | Unstated | No gym | Physical | Required intensity | Origin, time, party | A |
| 036 | indoor things for adults near Dhahran | Dhahran | Unstated | Indoor; adult-suitable | Nearby | "Adult" age threshold | Date/time, mode | A |
| 037 | can we do pottery without booking weeks ahead | Current area | Near-term | Pottery; short notice | Creative | Walk-in versus same-day | Origin, date, group | A |
| 038 | an easy outdoor walk after sunset | Current area | After sunset | Easy walk | Outdoors, scenic | Exact sunset/day | Origin, date, duration | A |
| 039 | no hiking, just a nice view we can drive to | Current area | Unstated | No hike; car access | Scenic | Walking tolerance | Origin, time | A |
| 040 | something for a rainy evening, not cinema | Current area | Rainy evening | No cinema; weather-sheltered | Interesting | Rain date | Origin, date, party | A |

### E. Events, culture and temporary opportunities

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 041 | what's happening this weekend | Current area | Weekend | Dated occurrence? | Variety | Event-only or broader | Origin, budget | E |
| 042 | any exhibitions still running tonight | Current area | Tonight | Exhibition; running tonight | none | Entry cutoff | Origin, mode | E |
| 043 | live music in Riyadh Friday under 200 | Riyadh | Friday | Live music; ≤200 SAR | none | Per ticket, which Friday | Date, group | E |
| 044 | market near me tomorrow morning | Current area | Tomorrow morning | Market; open then | Nearby | Food versus craft | Origin, mode | E |
| 045 | a workshop I can join solo this Thursday | Current area | Thursday | Workshop; solo admission | Creative? | Which Thursday, topic | Origin, time, budget | E |
| 046 | is the art thing at Ithra still on | Ithra, Dhahran | Now/future? | Named program? | Art | Which exhibition | Event title, date | E |
| 047 | any pop-ups that end soon | Current area | Before ending | Temporary | Novel | "Soon" horizon | Origin, time, type | E |
| 048 | free cultural events during Eid | Selected area? | Eid | Free; cultural | none | Which Eid/year | Area, year, group | E |
| 049 | theatre tonight but not too late | Current area | Tonight | Theatre | Earlier finish | "Too late" | Origin, cutoff, budget | E |
| 050 | any museum with something new, not the permanent collection | Current area | Unstated | Museum; non-permanent exhibit | New | New since when | Origin, date | E |

### F. Families, age and accessibility

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 051 | where can I take two kids tonight indoors | Current area | Tonight | Indoor; child-suitable | Fun | Ages and bedtime | Origin, ages, budget | F |
| 052 | family thing this weekend under 300 total | Current area | Weekend | Family fit; ≤300 SAR total | none | Family size/ages | Origin, ages, transport | F |
| 053 | something my parents can enjoy without much walking | Current area | Unstated | Low walking | Cultural? | Mobility needs | Origin, time, access needs | F |
| 054 | wheelchair accessible gallery open Saturday | Current area | Saturday | Verified wheelchair access; open | Art | Which Saturday | Origin, specific access needs | F |
| 055 | can a five-year-old do this workshop | Referenced workshop | Unstated | Age 5 permitted | none | Referent | Workshop identity, date | F |
| 056 | not loud, toddler will be with us | Current area | Unstated | Toddler-suitable | Quiet | Noise tolerance | Origin, time, party | F |
| 057 | free place to go with family after Maghrib | Current area | After Maghrib | Free; family access | none | Date and prayer time | Origin, ages, date | F |
| 058 | somewhere stroller friendly near the waterfront | Waterfront? | Unstated | Stroller access | Scenic | Which waterfront | City, time, route | F |
| 059 | activity for teens that isn't just a mall | Current area | Unstated | Teen-suitable; no mall | Active | Teen ages | Origin, time, budget | F |
| 060 | three generations, easy evening out | Current area | Evening | Mixed-age suitability | Low effort | Access/pace | Origin, date, ages | F |

### C. Couples and social mood

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 061 | date idea tonight that's not dinner | Current area | Tonight | No dinner | Romantic, interesting | Indoor/outdoor | Origin, budget, mode | C |
| 062 | somewhere romantic but not a restaurant | Current area | Unstated | No restaurant | Romantic | Meaning of romance | Origin, time | C |
| 063 | anniversary plan, nothing too expensive | Current area | Anniversary date? | none | Special, affordable | Price ceiling | Date, origin, budget | C |
| 064 | somewhere to talk without shouting | Current area | Unstated | none | Quiet, social | Noise tolerance | Origin, time, party | C |
| 065 | sunset place for two with easy parking | Current area | Sunset | Parking required | Scenic | Parking standard | Origin, date, mode | C |
| 066 | first date activity, not awkward and no food | Current area | Unstated | No food | Easy conversation | "Not awkward" | Origin, date, budget | C |
| 067 | anything cute near our hotel tonight | Hotel | Tonight | none | Cute, nearby | Meaning of cute | Hotel, transport, budget | C |
| 068 | quiet cultural thing for us on Friday | Current area | Friday | Cultural | Quiet | Which Friday | Origin, time, budget | C |
| 069 | want to surprise her with something local | Current area | Unstated | none | Local, special | Preferences, "local" | Origin, date, budget | C |
| 070 | dessert then something different nearby | Dessert venue? | After dessert | none | Different, close | Which first stop | Venue, time, mode | C |

### S. Solo, calm and short stays

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 071 | somewhere quiet but not boring | Current area | Unstated | none | Quiet, interesting | "Boring" | Origin, time, duration | S |
| 072 | solo thing to do for an hour | Current area | Unstated | Solo-suitable; ≈1h | none | Total or visit time | Origin, time, mode | S |
| 073 | I want to be around people but not talk to anyone | Current area | Unstated | none | Ambient social, low interaction | Crowd tolerance | Origin, time | S |
| 074 | good bookshop I can browse late | Current area | Late evening | Bookshop; open late | Browse-friendly | "Late" cutoff | Origin, date | S |
| 075 | somewhere to think near me, no café | Current area | Unstated | No café | Quiet, reflective | Indoor/outdoor | Origin, time | S |
| 076 | alone tonight, not another movie | Current area | Tonight | No cinema | Engaging | "Alone" as party or mood | Origin, budget | S |
| 077 | can I spend two hours at this museum | Referenced museum | Unstated | Visit ≈2h | none | Suitable dwell time | Museum identity, date | S |
| 078 | peaceful indoor place after 9 | Current area | After 21:00 | Indoor; open after 21:00 | Peaceful | End time | Origin, date, mode | S |
| 079 | quick art stop before heading home | Current route | Before home | Short duration | Art | Route/end point | Origin, home, time | S |
| 080 | somewhere with a view I can just sit | Current area | Unstated | Seating? | Scenic, calm | Public access/seating | Origin, time, mode | S |

### N. Local novelty and underexposed places

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 081 | what's new around here | Current area | Recent? | none | Newly opened | New since when | Origin, time, type | N |
| 082 | lived in Khobar forever, surprise me | Al Khobar | Unstated | none | New-to-me | Visit history unknown | Time, mode, history | N |
| 083 | local favourites not the tourist list | Current area | Unstated | none | Local, less touristy | Local to whom | Origin, time, interest | N |
| 084 | hidden gem coffee but actually good | Current area | Unstated | Coffee | Quality, underexposed | Hidden/quality criteria | Origin, time, budget | N |
| 085 | newly opened independent shops near Al Balad | Jeddah Al-Balad | Unstated | Independent shop | Newly opened | Opening recency | Date, shop type | N |
| 086 | weird little places in Riyadh | Riyadh | Unstated | none | Unusual, small | "Weird" | Area, time, mode | N |
| 087 | don't give me the same five places | Current area | Unstated | Exclude familiar set? | Novelty | Which five | Origin, history, time | N |
| 088 | something locals do on a Thursday night | Current area | Thursday night | none | Local, social | Which locals, which Thursday | Origin, budget | N |
| 089 | place I wouldn't find on Google Maps | Current area | Unstated | none | Underexposed | Literal exclusion impossible? | Origin, time, intent | N |
| 090 | an old market that's still worth going to | Current area | Unstated | Market; operating | Authentic, worthwhile | "Old" age vs historic | Origin, date, mode | N |

### T. Destination and future exploration

| # | Query | Place | Time | Hard | Soft | Ambiguous | Missing | Family |
|---:|---|---|---|---|---|---|---|---|
| 091 | visiting Tokyo next month, what should I save | Tokyo | Next month | none | Worth saving | Neighborhood and dates | Dates, interests, transport | T |
| 092 | in Jeddah for the weekend, things near Al Balad | Jeddah Al-Balad | Weekend | Nearby | Variety | Resident/visitor context | Dates, hotel, mode | T |
| 093 | what can I do near my hotel tomorrow night | Hotel unknown | Tomorrow night | none | Nearby | Hotel location | Hotel, budget, party | T |
| 094 | first time in Riyadh, not only tourist stuff | Riyadh | Trip dates unknown | none | Mix iconic/local | "Not only" strength | Dates, area, transport | T |
| 095 | two days in the Eastern Province, no itinerary yet | Eastern Province | Two future days | none | Exploration | Very broad region | Dates, base, interests | T |
| 096 | save events during our October trip to Saudi | Saudi destination unknown | October | Occurs during trip | Events | Year and cities | Dates, cities, party | T |
| 097 | anything interesting near Ithra after the museum | Ithra, Dhahran | After visit | Nearby | Interesting | Museum exit time | Date, mode, duration | T |
| 098 | travelling with friends, places we can do without tickets | Destination unknown | Future trip | No tickets | Flexible | Free versus walk-in | Destination, dates, group | T |
| 099 | easy things to do in Jeddah if we land late | Jeddah airport/hotel | Arrival night | Late usable; low effort | Nearby | "Late" arrival | Flight arrival, hotel, mode | T |
| 100 | what should we keep open for our trip, not lock a schedule | Destination unknown | Future trip | No fixed itinerary | Options, variety | "Keep open" action | Destination, dates, interests | T |

**How to use the corpus later:** R05 should replace and supplement synthetic prompts with consented verbatim task language, record Arabic variants and code-switching, label constraint strength, and add human judgments of eligible results and "no satisfactory answer" cases. Do not use these 100 as proof of query frequency.

## 26. Failure / Friction Taxonomy

This taxonomy follows the user's journey and the point where a problem becomes visible. A single attempted choice can receive multiple codes. Record **source of evidence** (observed behavior, participant explanation, or researcher inference) for each code. Rejection reasons in Section 10 describe a candidate; these codes describe the broader workflow.

| Code | Failure / friction | Observable example | Main downstream risk |
|---|---|---|---|
| COV | **Coverage failure** | No result for a nearby workshop or small exhibition the participant already knows. | Product cannot answer the job. |
| INF | **Information failure** | Candidate has no price, duration, age or booking rule. | Extra verification or abandonment. |
| FRS | **Freshness failure** | Old social post, expired market or changed hours. | Wrong choice and trust loss. |
| FEA | **Feasibility failure** | Result is 25 minutes by car, closes before arrival, or has no group slot. | User cannot actually do it. |
| REL | **Relevance failure** | "Active indoors" returns a gym or restaurant. | Query rework and wasted attention. |
| DIS | **Discovery failure** | Results contain only familiar mega-venues and chains. | Product offers no reason to return. |
| DIV | **Diversity failure** | First page contains six escape rooms and little else. | User cannot compare meaningful alternatives. |
| CMP | **Comparison failure** | Price is per person for one option and total for another; travel effort omitted. | Decision remains unresolved. |
| TRU | **Trust failure** | Hours conflict between Maps and operator page; source of claim unclear. | User rechecks or avoids the result. |
| FRG | **Workflow fragmentation** | Idea in TikTok, route in Maps, price in booking site, coordination in WhatsApp. | Decision time and cognitive load. |
| SOC | **Social coordination failure** | One friend rejects cost, another vetoes travel, candidate links get lost. | Group defaults to familiar option. |
| CTX | **Context loss** | Search loses date, language, transport or prior exclusion after a refinement. | Repeated queries and wrong candidates. |
| UNC | **Uncertainty handling failure** | "Walk-in available" inferred from missing booking data. | False confidence. |
| ACT | **Actionability failure** | User finds a suitable activity but cannot determine how to enter, reserve or contact it. | No completed outing. |

The study should identify the first point of friction and its cost. Four app switches are not necessarily a failure if the person makes a confident decision quickly; one inaccurate "open now" claim can be severe even with no switching.

## 27. Key Hypotheses

| Hypothesis to test | Supporting desk evidence | What would weaken or falsify it | Primary-research observation |
|---|---|---|---|
| **H1. Same-day group outings are the strongest first job.** | Local event/experience supply and common group tools exist. [webook](https://webook.com/en), [Google collaborative lists](https://blog.google/products-and-platforms/products/maps/20-years-google-maps-20-features/) | Participants rarely face it, decide in minutes, or repeatedly choose known defaults by preference. | Frequency diary/recall plus observed group-choice task. |
| **H2. The painful step is practical verification, not generating ideas.** | Product workflows separate inspiration, routing and booking information; research links information search to risk reduction. [Surrey study](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/Tourists-Online-Information-Search-Behavior-Combined/99818303302346) | Most tasks end confidently within one tool; false information is rare for chosen categories. | Source switches, fact checks, rejections, confidence by stage. |
| **H3. Mixed-domain choice creates value beyond a specialized event feed.** | Current tools organize different kinds of supply differently. [Eventbrite](https://eventbrite.com/), [AllTrails](https://support.alltrails.com/hc/en-us/articles/37227964040852-How-to-use-filters-to-find-trails), [Visit Saudi](https://www.visitsaudi.com/en/things-to-do?sortBy=manual_order) | Participants decide the category before searching and never compare events with permanent venues or activities. | Count genuine cross-type comparisons and switches. |
| **H4. Reliable time/travel fit matters more initially than rich semantic matching.** | Leisure travel-time research and dated event inventory support feasibility as a factor. [Travel-time study](https://www.sciencedirect.com/science/article/pii/S0095069613000880), [Ithra schedule](https://www.ithra.com/en/programme/2026/ithra-museum) | Most rejected options fail on taste/quality, while time and journey are easy to verify. | Code first veto and secondary veto for each considered option. |
| **H5. Locally distinctive options cause repeat use.** | Maps/Atlas already invest in gems and unusual places. [Maps lists](https://blog.google/products-and-platforms/products/maps/google-maps-updates-summer-travel-2024/), [Atlas Obscura](https://app.atlasobscura.com/) | Users mainly want reliable familiar venues, or new options lack trusted evidence. | Compare selected new-to-person versus familiar options and reasons. |
| **H6. A Saudi connected district is a better test unit than a whole city.** | Riyadh mobility context and source-backed district anchors exist. [Riyadh city report](https://www.rcrc.gov.sa/wp-content/uploads/2025/11/Riyadh-Citys-Voluntary-Local-Review-VLR-2024.pdf), [Historic Jeddah](https://www.visitsaudi.com/en/jeddah/attractions/summer-night-adventures-in-al-balad) | Participants willingly cross large areas, or a district lacks enough varied choices. | Travel tolerance in tasks plus R02 coverage sample. |

The research should seek **negative cases**: a participant who succeeds immediately with Google Maps, someone who never checks hours, a group that already knows its choice, and a visitor who values famous sites over novelty. These cases can change the product thesis.

## 28. Proposed User Study

Conduct a **12–20 participant directional study**, not a representative survey. Recruit from at least two candidate geographic contexts and include both Arabic- and English-dominant participants where feasible. Do not describe the proposed product before tasks. Ask participants to use their own device, accounts and normal tools; avoid collecting passwords or private chats. Obtain consent for screen/voice recording if used, and allow redaction of messages and location. A researcher should observe, not help search unless the task is blocked by a technical issue.

**Session shape (about 45–70 minutes):** 8–10 minutes of recent-outing history; 25–40 minutes across two to three observed tasks (one recent/real, one constrained scenario, optionally one contrasting task); 10–15 minutes of reflection. Use participants' real starting area where safe, then compare with a standardized vignette so sessions share some constraints. Have them make a choice or explicitly decline. Do not require them to purchase a ticket or travel.

**Capture:** first tool; exact search strings; sources opened; location/time defaults; number and type of candidate options; all checks made; tab/app switches; messages or calls only if participant volunteers to show them; vetoes; chosen or abandoned option; elapsed time; confidence before and after verification. Distinguish visible actions from post-hoc accounts. Record what the participant *did*, not only what they say they usually do.

**Analysis:** code candidate-level rejections with Section 10, workflow friction with Section 26, and compare by user context. Report counts as descriptive "of these participants/tasks," with the small, nonrandom sample clearly stated. Do not publish percentages implying population prevalence. The result should choose, revise or reject the first-user and first-decision hypotheses and identify the few facts R01/R02 must provide.

## 29. Participant Profiles

Recruit for variation in decision role and constraints, not age alone. A suggested allocation for **16** participants is below; adjust within 12–20 based on availability. One person may fit more than one row. This is a recruitment target, not a claim of completed recruitment.

| Profile | Suggested count | Why include |
|---|---:|---|
| Residents who regularly suggest outings for friends | 4 | Tests group coordination and same-day choice. |
| Residents who usually choose solo or with a partner | 3 | Tests whether the job exists without group friction. |
| Parents or family outing organizers | 2 | Exposes age, access and budget constraints. |
| Residents who say they often choose a familiar default | 2 | Negative case for novelty demand. |
| Domestic visitors in the city being studied | 3 | Contrasts familiarity and future/near-term context. |
| People with a specific access, transport or budget constraint | 2 | Tests hard-constraint consequences; recruit respectfully and avoid assuming disability from appearance. |

Recruit across the Al Khobar/Dhahran/Dammam, Riyadh or Jeddah candidate areas only where a researcher can observe a real or realistic task. Screen for recent outing decisions in the past month, tool use, language preference and comfort sharing a screen. Do not recruit only event enthusiasts or only people who already follow local discovery accounts; that would bias the study toward the concept.

## 30. Observational Tasks

Use **8–12 task cards** across the study. A participant completes only two or three to avoid fatigue. Personalize origin and clock time while preserving the task's constraint structure; give a clear "none of these" option. Start with the participant's own recent decision before prompted tasks where possible.

| Card | Neutral task presented to participant | What it reveals |
|---|---|---|
| 1. Recent real choice | "Show me how you decided on your last outing with others. If you still have the links or searches, walk through them." | Actual trigger, memory of tools and vetoes. |
| 2. Thursday with friends | "Two friends can meet Thursday evening. Find one thing you would genuinely suggest." | Open discovery and coordination. |
| 3. Ninety-minute gap | "You have 90 minutes before a dinner reservation in this area. Decide whether to do anything beforehand." | Door-to-door time feasibility. |
| 4. Unusual indoors | "It's a hot afternoon. Find a non-food option you would actually try indoors." | Experiential intent, environment and evidence. |
| 5. Weekend visitor | "A friend is visiting this district for the weekend. Suggest one stop you would stand behind." | Local knowledge versus tourist defaults. |
| 6. Date or pair | "Find an outing for two that allows conversation and is not dinner." | Mood interpretation and negative constraint. |
| 7. Family fit | "A family with a child needs a two-hour afternoon option within its budget." Give actual ages/budget on card. | Age, price and duration evidence. |
| 8. Low budget | "Find a worthwhile evening option under a stated per-person budget." | Free versus unknown price and value. |
| 9. New opening | "Find something genuinely new in this area that you would visit." | Opening-date verification and novelty. |
| 10. Non-touristy | "A resident wants to avoid the obvious attraction. Find a local alternative." | Definition of local and distinctiveness. |
| 11. Bookable activity | "Four people want to do an activity tonight without booking days in advance." | Venue hours versus session/capacity. |
| 12. No good option | "Given these constraints, decide whether any option is worth going to." Use a deliberately tight but plausible window. | Willingness to say no, relaxation and confidence. |

Observe the participant's own searches. Do not require them to use Maps, TikTok, webook or any other named tool. A task is successful only if they can explain why they would choose the result and what remains unverified. Record when they stop because the decision is "good enough."

## 31. Interview Guide

### Pre-task questions

1. "Tell me about the last time you decided what to do outside your home. What started the decision?"
2. "Who usually suggests the first option when you go out with other people?"
3. "Think of the last month. Which outings took planning, and which were decided the same day?"
4. "What tools or people do you normally turn to first? You can show me rather than describe them."
5. "What kinds of outings do you usually repeat, and when do you want somewhere new?"

### Neutral think-aloud prompts

- "What are you looking for on this screen?"
- "What would you check next?"
- "What makes this option a possibility?"
- "What is still uncertain?"
- "Why did you open that source?"
- "What would make you stop searching?"

Avoid "Wouldn't it help if one app combined these?" or "Isn't this too far?" Such prompts teach the concept or suggest a problem.

### Post-task questions

1. "Which options did you consider and why did you rule them out?"
2. "What information made you comfortable with the final option?"
3. "What would you verify before leaving or paying?"
4. "If none worked, what would you do instead?"
5. "On a scale you choose, how confident are you that this outing would work? What would change that confidence?"
6. "Was this similar to a real decision you've made? What was different?"

### Final questions

1. "How often has a decision like this come up in the last four weeks? Walk me through the occasions."
2. "Which part took the most effort today, if any?"
3. "When do you ask another person instead of searching?"
4. "Can you recall a choice that failed after you arrived? What was wrong in the information?"
5. "Which result would you have been most disappointed to miss?"
6. "Would you expect to solve the next similar occasion the same way? Why?"

Questions are prompts, not a script requiring every item. Follow the participant's actual behavior, especially unexpectedly easy decisions. Record spontaneous phrasing separately from researcher-led answers.

## 32. Observation Template

Copy this template for each participant-task pair. Use local time and protect identifiable location/chat data.

| Field | Entry |
|---|---|
| Participant ID / consent scope | `P__`; screen/voice permission, redactions |
| Profile | Resident/visitor; solo/group organizer; language; transport/access constraints supplied voluntarily |
| Scenario / whether real or prompted | Task card number and exact customized wording |
| Session date, local start time, timezone |  |
| Starting area and intended destination/next commitment | Broad area unless precise coordinates are necessary and consented |
| Initial stated goal and exact wording |  |
| First tool opened and reason |  |
| Tool/application timeline | Time; app/site; action; tab/app switch; researcher observation |
| Exact query text and edits | Verbatim, including spelling and Arabic/English mix |
| Sources visited | Maps, social post, official venue, ticketing, friend/message, etc. |
| Filters and defaults used | Date, open, price, radius, sort, mode |
| Candidate considered | Name, type, URL/reference, discovered in which tool, timestamp |
| Candidate rejected | First reason, secondary reasons, code from Sections 10/26, participant-stated or inferred |
| Information checked | Hours, event date, price, duration, route, age, booking, photos, reviews, atmosphere, parking, accessibility |
| Missing or conflicting information | Field, competing sources, whether resolved |
| Final choice or no-choice | What was chosen, why, practical next step, any remaining caveat |
| Decision time | Start, final decision and any pauses in minutes |
| Confidence | Participant's own scale and explanation; before/after verification if offered |
| Participant quotations | Verbatim only; mark source/time and obtain quote consent |
| Researcher notes | Visible behavior, context, possible observer effect, unanswered questions |
| Failure categories | COV/INF/FRS/FEA/REL/DIS/DIV/CMP/TRU/FRG/SOC/CTX/UNC/ACT; evidence type |

The template captures observed behavior and participant interpretation separately. It should never be prefilled with hypothetical quotes or decisions.

## 33. Implications for R01 — Source Rights & Economics

R01 can start now, **before provider content is ingested**. Investigate rights and cost for the source types needed by promises A and B: (1) place identity, coordinates and opening hours; (2) event/exhibition/workshop schedules and cancellation updates; (3) activity duration, price, booking and group rules; (4) photos/descriptions and experiential evidence; (5) road/public-transport travel-time services; (6) local editorial, community and venue-owned updates. Examine commercial maps/places providers, Google Maps Platform, OpenStreetMap and local open data, Visit Saudi/GEA calendars, webook and other ticketing partners, operator/Ithra sites, and licensed social or editorial sources. **This is an investigation list, not permission to scrape or combine them.**

For each candidate provider, R01 must answer: Can we retrieve, retain, refresh, merge, index, embed, summarize, show on another map, attribute and commercially display each field? How long may it be cached? Who owns photos/reviews? Can event status and availability be rechecked affordably? What are costs per useful candidate, verification cycle and active search, rather than per raw API call alone? Google Places' place-ID storage exception and broader Maps content rules illustrate why the answer is field-specific. [Google Place IDs](https://developers.google.com/maps/documentation/places/web-service/place-id), [Google Maps service terms](https://cloud.google.com/maps-platform/terms/maps-service-terms)

**Exact R01 assumptions to carry forward:** the first user is a local near-term outing organizer (unvalidated); the first promises under test are A and B; the first content families are cultural venues/exhibitions, indoor activities, dated events/workshops and a small curated local set; the four candidate catchments are in Section 20; no provider is presumed licensed for a canonical dataset; group capacity and "available tonight" require direct evidence or an unknown label. R01 should return a rights matrix and cost scenarios **for all four catchments**, with a recommendation on which content types are legally and economically testable.

## 34. Implications for R02 — Local Coverage Audit

R02 should compare the four catchments in Section 20, with the Eastern cluster, Diriyah/JAX, Al-Balad and the Boulevard/Hittin corridor as separate samples. Audit the four content families from Section 24. Stratify by weekday evening, Thursday/Friday or local weekend, a 90-minute pre-commitment window, and a future date; include summer/heat and seasonal-event periods where the source permits. Count **usable choices** after identity, time, travel, price, booking and group-fit checks, not raw pins.

For a sampled record, capture: entity and exact access point; source and permitted use; category/experience type; permanent versus dated; operating hours and exceptions; occurrence date/status; price unit/range; typical duration; booking/walk-in rule; group/age/accessibility claim if present; last-verified time; actual transport mode and estimated travel from a few representative origins; duplicate/branch risk; independent source for confirmation. Record "unknown" and contradictory claims. Check whether small independent options appear alongside headline attractions.

**Exact R02 assumptions to carry forward:** a shortlist of 2–3 credible options is the provisional decision output, not a promise; "nearby" must be tested in travel minutes and by mode; a source listing does not equal a feasible outing; the user may compare permanent venues with time-bound opportunities; no catchment is preselected; the audit must identify at least one negative case where no good option exists. R02 should report coverage by query family and time window, false-feasibility risks, verification labor, and the area/content pair best suited to a controlled field test. Perform only manual public-page assessment until R01 resolves retention and automated-use rights.

## 35. Open Questions

### Requires primary user research

- How often does a local resident actually face a difficult near-term outing decision, and who initiates it?
- Which veto happens first in real tasks: timing, travel, price, availability, group fit, mood, quality or familiarity?
- Do people truly compare events, workshops and permanent venues in one decision, or do they choose a category first?
- Does cross-app checking feel costly, or is it a quick and trusted routine?
- What does "worthwhile," "local," "hidden," "quiet" and "nearby" mean to different participants?
- When is an empty answer preferable to an uncertain suggestion?
- How well do Google Maps/Search and Saudi event tools already answer these exact tasks in Arabic and English?
- Does the organizer need a new tool, or would a better message/share artifact inside existing tools suffice?

### Requires R01/R02 evidence

- Which local feeds can legally support a retained, searchable mixed corpus and at what recurring cost?
- Where do legally usable records have enough field completeness for "tonight" or "this weekend" decisions?
- How many relevant options remain after eligibility checks by neighborhood and time window?
- Are independent places and short-run events verifiable frequently enough to support a novelty promise?
- Which candidate district allows a fair comparison rather than an artificially sparse or mega-event-only test?

## 36. Recommended Next Actions

1. Recruit the 12–20 directional participants across two candidate contexts and a mix of organizer, solo, visitor and constraint profiles.
2. Run and code real or realistic outing decisions using Sections 30–32 without demonstrating a proposed product.
3. Compare the participant's outcome with their normal tools, including Google Maps/Search and relevant Saudi event sources; preserve easy-success cases.
4. Complete R01's rights and economics matrix for the four content families before any automated collection or canonical storage.
5. Begin a manual R02 pilot in all four catchments using the same time windows and field checklist; narrow to two after the first sample.
6. Revise the synthetic query corpus with verbatim consented language, including Arabic and mixed-language prompts; pass the labeled set to R05.
7. Hold a decision review: keep promise A, move toward B or another job, or stop if the need is infrequent or already solved well enough.

# Most Important Findings

1. **The core decision remains a hypothesis:** choosing a feasible, worthwhile outing may be a repeat pain, but no desk source measures it for the proposed first users.
2. **Competition is substantial.** Google Maps/Search and Saudi platforms already offer contextual discovery, lists, event inventory and booking. The project needs an observed outcome advantage.
3. **The possible product gap is practical verification and comparison** across venue, activity and occurrence, especially under time, travel, booking and group constraints.
4. **Local organizers are the strongest first audience to test**, with domestic visitors as a contrast; neither is a validated market.
5. **False feasibility is likely more damaging than an imperfect mood match**, but the ordering of actual rejection reasons must be observed.
6. **Saudi time and place context matters:** heat, Ramadan, seasons, car travel and new transit make "nearby" and "open" situational rather than fixed.
7. **A connected catchment is a better audit unit than a whole city.** Four candidates have identifiable anchors, but none has been coverage-audited.
8. **A narrow mixed corpus can test cross-domain choice** without claiming exhaustive local coverage.
9. **Annual activity and tourism figures do not prove weekly product demand.** Repeat-use frequency is a central primary-research question.

# What We Know

- The existing project defines a discovery-before-planning concept across places, activities and occurrences; the architecture review calls for R00 before source, search and planner decisions.
- Current large and regional products already offer local ideas, dated events, maps, social discovery or trip organization, though their fit for the selected Saudi tasks is unmeasured. [Google Maps](https://blog.google/products-and-platforms/products/maps/20-years-google-maps-20-features/), [webook](https://webook.com/en), [Visit Saudi](https://www.visitsaudi.com/en/things-to-do?sortBy=manual_order), [Wanderlog](https://wanderlog.com/)
- GASTAT documents widespread annual cultural/entertainment participation in Saudi Arabia, but not individual decision frequency. [GASTAT 2024 survey](https://www.stats.gov.sa/documents/20117/2435273/Household%2BCulture%2Band%2BEntertainment%2BStatistics%2BPublication%2B2024%2BEN.pdf/591d6f59-c7ae-5ef4-0190-56643b41f4e7)
- Saudi official sources document seasonal weather, Ramadan evening patterns and time-bound entertainment programming; these make timing a real data dimension. [Climate](https://www.visitsaudi.com/en/stories/climate-and-seasons), [Ramadan](https://www.visitsaudi.com/en/campaigns/discover-ramadan), [Saudi calendar](https://www.visitsaudi.com/en/calendar.html)

# What We Think

- The first useful job may be helping a local organizer choose among two or three feasible near-term outings.
- Fact verification, travel time and group/booking fit may be more valuable initially than richer prose or a conversational layer.
- A resident novelty variant could support repeat use if it finds high-quality options that normal tools miss.
- One discovery core can serve residents and visitors with different defaults, provided actual behavior confirms overlap.

# What We Still Need to Observe

- Verbatim searches, first tools, app switches, source checks, candidate vetoes, final choice and confidence in 12–20 real task sessions.
- Frequency of hard outing decisions and cases where people happily reuse a familiar venue.
- The exact threshold at which uncertainty about time, price, access or booking stops a decision.
- Comparative outcomes against Google Maps/Search, webook, Visit Saudi and participants' preferred social sources in candidate Saudi areas.

# Assumptions We Should Not Lock In Yet

- Saudi Arabia, any specific city, or any catchment as the launch market.
- Local residents as the validated first market; group organizing as the dominant job.
- A need for a map, chatbot, LLM parsing, global hidden-gem score, live booking or planning.
- That app switching is painful, that ratings are unhelpful, or that current competitors fail the compound queries.
- That source pages can be copied, indexed, merged or refreshed at acceptable cost.
- Any numeric frequency, willingness-to-pay or useful-result target before observation and coverage audit.

# Recommended First User Hypothesis

**Primary:** a resident of a connected Saudi urban area who initiates same-day or weekend plans for themselves and one to four others and needs to choose a feasible activity beyond an obvious default. **Secondary:** a domestic visitor who must make a near-term choice around a hotel or host's neighborhood. Both need observation; no demographic or city has been validated.

# Recommended First Decision Problem

"We can go out within this real time window. From our starting point, budget and group constraints, what are two or three different, credible things we can actually do, and which should we choose?" The initial study must measure whether this is harder than the participant's current method and whether a cross-domain answer helps.

# Candidate Geographic Test Environments

1. Al Khobar waterfront–Dhahran/Ithra–nearby Dammam connected cluster.
2. Riyadh Diriyah–JAX–Bujairi/At-Turaif cultural area.
3. Historic Jeddah / Al-Balad catchment.
4. Riyadh Boulevard City–Hittin entertainment catchment.

These are R02 audit candidates, not a ranked launch decision. Each must be assessed for legally usable data, feasible choice density, travel-time shape, seasonality and participant access.

# Recommended Initial Content Scope

Include a controlled mix of cultural venues and current exhibitions, repeatable indoor activities, selected dated workshops/events, and a small verified set of locally distinctive stops. Require usable time, access, price and booking facts or label them unknown. Defer broad restaurants/malls, remote hiking/camping, unverified live availability and planning features. A simple outdoor option can be a contrast when weather and access are clear.

# R00 Decision Gate

### Proceed to R01 — Source Rights & Economics? **YES**

R01 can investigate terms, prices and field rights without deciding the target market. It must carry the **unvalidated** local-organizer and domestic-visitor hypotheses, the A/B product promises, all four candidate catchments and the four narrow content families. It must not assume that API retrieval permits storage, merging, embeddings or display.

### Proceed to R02 — Local Coverage Audit? **CONDITIONAL**

Begin a **manual public-source scoping audit** of all four catchments now. Do not build an automated retained corpus until R01 resolves rights. R02 must use the same weekday-evening, weekend, 90-minute-gap and future-date windows; assess venue/activity/occurrence identity, hours, price, duration, group and booking fit; record unknowns and contradictions; and report feasible options rather than raw listing counts. Final R02 scope should incorporate actual query and rejection evidence from the user study. Neither gate means the MVP or launch market is validated.
