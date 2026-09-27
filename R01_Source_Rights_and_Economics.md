# R01 — Source Rights & Economics

**Project:** Location-aware discovery platform  
**Research date:** 26 September 2026 (Asia/Riyadh)  
**Status:** Desk research and decision guidance; not legal advice, a signed license, a Saudi coverage audit, or a procurement quote.  
**Decision:** Whether a rights-defensible, economically testable corpus can support R00's first outing decision.

## 1. Executive Summary

**Finding.** A persistent test corpus is possible, but it should begin with explicitly reusable place data and records obtained directly from operators or under specific agreements. The most consequential new source distinction is between **FSQ OS Places**, an Apache 2.0 open dataset with a documented download route and core place fields, and **Foursquare Places API**, whose self-service terms and acceptable-use policy restrict derivative works, blending, bulk extraction, and database creation. They are not interchangeable licenses. [FSQ OS license and notice](https://opensource.foursquare.com/places-notice-txt/), [FSQ OS schema](https://docs.foursquare.com/data-products/docs/places-os-data-schema), [Foursquare API EULA](https://foursquare.com/legal/terms/apilicenseagreement/), [Foursquare acceptable-use policy](https://foursquare.com/legal/terms/aup/)

**Recommended initial strategy — RECOMMENDATION:** use FSQ OS Places and a source-aware sample of Overture Places as candidate *place identity* layers; use Wikidata and carefully selected Saudi open datasets for specific cultural facts; obtain time, price, booking, age, and cancellation facts from directly authorized operators or feeds; maintain a small editorial verification process. Use commercial places and route APIs only in use cases their contracts permit. Do not seed the canonical index from Google Places, Foursquare paid API, Yelp, webook pages, social posts, or Tripadvisor reviews. This is a test strategy, not proof of Saudi field coverage.

**Key constraint.** R00's promise A (“feasible outing tonight”) depends on current operating and event facts that open POI datasets generally do not contain. FSQ OS Places includes identity, coordinates, categories, contacts, a `date_refreshed`, and some quality flags; its documented open schema does **not** provide bookable sessions, live availability, prices, special hours, or cancellation streams. Its `date_created` is explicitly **not** a business opening date, and `date_refreshed` means any one reference was refreshed, not that every field is current. [FSQ OS schema](https://docs.foursquare.com/data-products/docs/places-os-data-schema)

**Gate.** A narrow corpus and R02 controlled audit can proceed **conditionally** using the open sources and permissioned first-party records below. R02 may query an authorized API within its own terms, but must not turn restricted responses into a retained or merged corpus. A broad, automatically current Saudi event layer is **not established**; event feed partnerships or a bounded first-party network may become necessary if R02 finds inadequate dated choice coverage.

## 2. R00 Inputs

The immediate input is [R00 — User Decision Study](R00_User_Decision_Study.md), not a generic tourism brief. Its **unvalidated** primary user is a resident arranging a same-day or weekend outing for themselves and roughly one to four others. The secondary user is a domestic visitor making a near-term choice near a hotel or host. The candidate promises are **A: choose a feasible outing tonight** and **B: find something worthwhile and new locally this weekend**. An answer should offer two or three credible, different choices with location, time, price, booking and group fit.

R00's first content families are (1) cultural venues and current exhibitions; (2) repeatable indoor activities; (3) selected dated events and workshops; (4) a small independently verifiable set of locally distinctive stops. The four **audit candidates**, with no launch decision implied, are Al Khobar–Dhahran/Ithra–nearby Dammam, Diriyah–JAX–Bujairi/At-Turaif, Historic Jeddah/Al-Balad, and Boulevard City–Hittin. The [v0.1 concept](<Product & Technical Concept v0.1.md>) and [architecture review](Product_Technical_Concept_Architecture_Review_v0.2.md) call for source rights, provenance, and feasible rather than merely relevant results.

The minimum useful record in this study is not a map pin. It is a distinct venue, offering, or dated occurrence for which a person could decide whether to go. A venue may be open while its workshop is full; an exhibition may be running while admission has a separate schedule. R02 must measure **usable options by query and time window**, not raw POI count.

## 3. Research Scope

This report tests the rights and cost of **retrieval, retention, normalization, matching, indexing, embeddings, transformation, display, refresh, and commercial use** for sources plausibly relevant to R00. It covers place identity, time-bound opportunities, practical decision facts, media, review signals, and travel-time services. It does not measure actual POI completeness in the four catchments; that belongs to R02. It does not make a final legal determination or negotiate rights.

**Meaning of labels used below:**

- **DOCUMENTED:** directly stated by linked primary documentation, terms, or a license.
- **INTERPRETATION:** a defensible product/technical reading, but not an express permission.
- **UNCLEAR:** documentation reviewed did not establish the right or local availability.
- **LEGAL / COMMERCIAL REVIEW REQUIRED:** uncertainty could change what we may store, combine, display, or sell.
- **RECOMMENDATION:** proposed action. A recommended workflow does not itself create a legal right.

“No public API found” means this review did not locate a published API or feed for the specific use. It does not mean a negotiated partner feed is impossible. Likewise, a documented worldwide product claim is not evidence of usable results in a Saudi neighborhood. Prices below are public list prices checked on the research date, excluding tax, negotiated rates, hosting, and payment effects unless stated.

## 4. Evidence Standard & Legal Caveat

Contractual conclusions rely on provider terms, license text, platform policies, product documentation, and official pricing. Product marketing can establish an offer or public positioning but **not** a permission beyond the actual agreement. Saudi government open-data policy applies to **datasets actually published under that license**; it does not license all text, photos, event pages, or logos on a government site. The [National Portal](https://my.gov.sa/content/open-Data) expressly distinguishes dataset rights from rights in individual media and other protected interests. **LEGAL / COMMERCIAL REVIEW REQUIRED** before a production ingest involving OSM-derived/proprietary blends, commercial feeds, third-party media, or systematic extraction from first-party websites.

This is technical and product due diligence, **not formal legal advice**. Recheck the applicable agreement, plan, geography, and price at procurement and before public release. Keep a dated copy of the governing source terms and license for each ingested release.

## 5. Required Data Fields

| Decision layer | Required or highly useful fields | Where a single source is insufficient |
|---|---|---|
| Identity | Internal ID; name/aliases; branch/site; operator; provider IDs | A chain and its branch cannot be collapsed; an event is not its host venue. |
| Geography | Entrance coordinate, address, neighborhood, multi-site or route geometry | POI coordinates may be rooftop; venue pages may describe an access gate. |
| Classification | Venue, offering, occurrence type; indoor/outdoor; stable facets | Open POI categories rarely encode experiential fit. |
| Time | Standard/special hours; occurrence interval; timezone; status; last check | “Exists” does not mean “usable tonight.” |
| Feasibility | Price and unit; duration; booking/walk-in; available session; age/group/access rules | Most open place layers omit these; unknown must not become “yes.” |
| Trust and display | Official URL; source and retrieval time; permitted photo/description; correction path | Reviews/photos have separate rights from place facts. |
| Geography in practice | Mode-specific travel minutes, departure time, route uncertainty | Straight-line radius is a poor substitute for trip effort. |

**RECOMMENDATION:** distinguish facts verified by a direct operator from facts copied from a commercial provider and from editorial judgments. The same field may have a different rights status for each claim.

## 6. Source-Landscape Overview

Four layers matter for the first experiment: **(a)** reusable place identity, **(b)** current actionable facts, **(c)** permitted media and experiential evidence, **(d)** route estimates. Open POI data can plausibly cover (a), and open cultural data can fill a few stable attributes. R00's differentiation lives mainly in (b). No reviewed general-purpose source establishes all four layers in Saudi Arabia. [FSQ OS schema](https://docs.foursquare.com/data-products/docs/places-os-data-schema), [Overture Places guide](https://docs.overturemaps.org/guides/places/), [GEA Enjoy description](https://www.gea.gov.sa/en/media-center/news/enjoy-platform-2)

The preferred hierarchy of evidence for a volatile outing fact is **operator-authored feed or signed submission → permissioned ticket/venue integration → explicitly licensed open dataset with suitable timestamp → direct human verification with lawful notes → third-party restricted live display**, subject to demonstrated accuracy. That order is an engineering recommendation, not a universal legal or quality ranking. A source can be authoritative about an event yet provide an old, unmaintained page.

## 7. Google Maps Platform / Places

**DOCUMENTED.** Places API (New) provides Text Search, Nearby Search, Place Details, photos, and fields including identifiers, addresses, locations, hours, ratings and reviews depending on field mask and SKU. Billing uses the highest applicable requested field tier for a call. Current global list prices include Nearby/Text Search Pro **$32/1,000 after 5,000 free monthly events**, Place Details Pro **$17/1,000 after 5,000 free**, Place Details Essentials **$5/1,000 after 10,000 free**, Place Details Photos **$7/1,000 after 1,000 free**, and Routes Matrix Essentials **$5/1,000 elements after 10,000 free**; Pro routing is a different SKU. [Places billing](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing), [global price list](https://developers.google.com/maps/billing-and-pricing/pricing)

**DOCUMENTED rights.** Google's terms prohibit prefetching, indexing, storing, resharing, or rehosting Google Maps Content outside services except express exceptions. They specifically give copying business names, addresses, and reviews as prohibited examples and restrict creating content from Maps Content, including using it to improve ML/AI models. Place IDs may be stored indefinitely; Google advises refreshing old IDs. Places content may be shown without a map with Google Maps attribution, but Places content used **with a map** must be on a Google map; service-specific terms also prohibit use in conjunction with a non-Google map. Places latitude/longitude may be temporarily cached for up to **30 days**, not promoted to an owned coordinate layer. [Maps terms §3.2.3](https://cloud.google.com/maps-platform/terms), [service-specific terms §14](https://cloud.google.com/maps-platform/terms/maps-service-terms), [Places policies](https://developers.google.com/maps/documentation/places/web-service/policies), [Place IDs](https://developers.google.com/maps/documentation/places/web-service/place-id)

**DOCUMENTED media.** Place photo names cannot be cached; photos and reviews carry author attribution and source-link requirements. [Place Photos](https://developers.google.com/maps/documentation/places/web-service/place-photos), [Places policies](https://developers.google.com/maps/documentation/places/web-service/policies)

**INTERPRETATION:** Google is useful as a live, attributed end-user reference or a stored ID crosswalk, but the normal terms do **not** support constructing our permanent cross-provider place/event index from its names, coordinates, descriptions, hours, review text, photo content, or embeddings. A separate bespoke license, if offered, would require review. Do not use a Google response to “verify” and silently overwrite an independently sourced canonical field; that risks turning restricted content into retained derived content. Google Places UI Kit has a particular non-Google-map exception, but still forbids exporting or caching its content; it does not solve corpus ownership. [Service-specific terms §15](https://cloud.google.com/maps-platform/terms/maps-service-terms)

**RECOMMENDATION:** exclude Google Places from canonical seeding, entity-resolution training, embeddings, and audit spreadsheets of copied provider fields. If tested, isolate a small live-display workflow with attribution and no retained content other than allowed IDs and operational billing counts. Route results have their own non-Google-map and caching constraints; do not assume a Google drive-time annotation can be plotted on an OSM/Mapbox map without review. [Service-specific terms §19](https://cloud.google.com/maps-platform/terms/maps-service-terms)

## 8. Foursquare

### 8.1 FSQ OS Places — open dataset

**DOCUMENTED.** FSQ OS Places is licensed under **Apache License 2.0**, with a Foursquare NOTICE file that calls for preserving attribution, a license copy for recipients, and change notices where applicable. The open dataset is accessed through the Places Portal/Iceberg catalog, with Places, Categories, and Deltas available; the former public S3 distribution no longer receives new releases. The documented schema includes FSQ ID, name, coordinates, address/locality, contact/website/social handles, category IDs, `date_created`, `date_refreshed`, `date_closed`, and unresolved quality flags. [FSQ notice](https://opensource.foursquare.com/places-notice-txt/), [access guide](https://docs.foursquare.com/data-products/docs/access-fsq-os-places), [schema](https://docs.foursquare.com/data-products/docs/places-os-data-schema), [distribution change](https://foursquare.com/resources/blog/data/evolving-fsq-open-source-places/)

**INTERPRETATION:** this is a strong candidate for a persistent rights-defensible base layer, including commercial use under license obligations. It does not guarantee Saudi completeness or current schedules. The global count and monthly release cadence cannot substitute for R02's catchment sample. A branch ID should remain separate. `date_created` cannot be used as a “newly opened” signal. Open data may be stored and indexed subject to the license; per-file photos/reviews are **not** part of this open place license unless separately documented. [FSQ schema](https://docs.foursquare.com/data-products/docs/places-os-data-schema)

### 8.2 Foursquare paid Places API and commercial flat files

**DOCUMENTED.** The paid Places API can return richer search, hours, tastes, ratings, photos, tips, and related-place information by tier. Its self-service EULA disallows derivative works, restricts material bulk exposure, requires “Powered by Foursquare” where data appear, and defers caching/rate limits to usage guidance. The applicable acceptable-use policy restricts blending and extraction/storage to create or enhance a location database unless the agreement permits it. Enterprise data authorizations can differ, so product and contract must be matched precisely. The published pay-as-you-go page lists **500 free Pro calls/month**, then **$15/1,000 through 100,000** and lower volume tiers; Premium is **$18.75/1,000** for the first listed tier. The API documentation lists global places, but does not establish Saudi field completeness. [API response fields](https://docs.foursquare.com/fsq-developers-places/reference/response-fields), [EULA](https://foursquare.com/legal/terms/apilicenseagreement/), [acceptable-use policy](https://foursquare.com/legal/terms/aup/), [pricing](https://foursquare.com/pricing/), [2026 change notice](https://docs.foursquare.com/developer/reference/upcoming-changes)

**RECOMMENDATION:** compare the open dataset to actual local options in R02 before paying for richer API fields. If a missing field materially improves a test query, seek written terms covering storage, joins, embeddings, display, deletion, and Saudi territory. Commercial flat-file documents show regional MEA packaging and separate rich attributes, but price and rights require a negotiated subscription. Do not assume flat-file delivery grants indefinite ownership. [Flat-file overview](https://docs.foursquare.com/data-products/docs/places-flat-file-overview), [enterprise data authorization](https://foursquare.com/legal/terms/eula/)

## 9. Yelp

**DOCUMENTED.** Yelp's current Places API documentation allows a maximum **24-hour cache** of content and indefinite storage of business IDs for back-end matching; it says commercial analysis is not permitted for Places integrations. The current supported-locale list does **not** include Saudi Arabia or Arabic. That absence is not proof the API returns zero Saudi businesses, but it weakens its fit. Yelp has photos, reviews, ratings, hours, and some event endpoints, all subject to separate terms and coverage. [Yelp Places FAQ](https://docs.developer.yelp.com/docs/places-faq), [rate limits](https://docs.developer.yelp.com/docs/places-rate-limiting), [supported locales](https://docs.developer.yelp.com/docs/resources-supported-locales), [developer overview](https://docs.developer.yelp.com/docs/getting-started)

**INTERPRETATION / RECOMMENDATION:** defer Yelp from the Saudi MVP source stack. R02 may record that it exists as a competitor/reference source, but a paid Yelp integration should require evidence of local coverage and a specific use not already served. Its cache and analytic limits rule out treating it as an owned discovery corpus. Public plan terms were not sufficient here for a reliable Saudi cost estimate; mark pricing **UNCLEAR** rather than inventing it.

## 10. OpenStreetMap

**DOCUMENTED license.** OSM data are open under **ODbL 1.0** with attribution. Publicly used derivative databases can trigger share-alike; produced works and collective databases have different treatment. OSM Foundation's collective-database guideline describes cases where an independently sourced layer remains separate, but warns that supplementing a proprietary restaurant list with matching OSM records and removing duplicates is outside that safe example. The precise effect of joining OSM POIs to our privately curated records is **LEGAL REVIEW REQUIRED** before calling the resulting index proprietary. [OSM copyright](https://www.openstreetmap.org/copyright), [OSMF collective-database guideline](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline), [produced-work guideline](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Produced_Work_-_Guideline)

**DOCUMENTED infrastructure distinction.** The public Nominatim endpoint has an absolute **1 request/second** ceiling and special limits on recurring bulk tasks; its policy is separate from ODbL. Public OSM tile servers forbid bulk prefetch/offline downloads, require visible attribution and cache handling, and have no SLA. Overpass public instances are community services with their own limits; they are not an unlimited production data pipeline. [Nominatim policy](https://operations.osmfoundation.org/policies/nominatim/), [tile policy](https://operations.osmfoundation.org/policies/tiles/), [Overpass overview](https://wiki.openstreetmap.org/wiki/Overpass_API)

**RECOMMENDATION:** use OSM as a source-aware comparison and possible routing/map base, with licensed hosting/self-hosting if needed. Do not blend OSM and Apache/CDLA/private place fields indiscriminately. Preserve OSM-derived geometry and claims in a separately governed layer until a lawyer confirms the intended database model. Sample Saudi POI accuracy in R02 rather than relying on global OSM reputation.

## 11. Commercial Map / POI Providers

| Provider | Documented capability and rights | R01 assessment |
|---|---|---|
| **Overture Places** (open data, not a paid API) | September 2026 Places guide says the theme is openly available, excludes OSM POIs, and contains records under **CDLA-Permissive 2.0 or Apache 2.0 by source**. The Foursquare-sourced subset retains its Apache notice. [Places guide](https://docs.overturemaps.org/guides/places/), [attribution](https://docs.overturemaps.org/attribution/) | Strong second open identity candidate. Preserve **row/source-level license** and version. Overture conflates providers, so audit duplication and source quality; do not infer all rows share one license. |
| **Mapbox** | Geocoding v6 has **temporary (default; no storage)** and **permanent (storage permitted)** modes; Search Box POI results are only for temporary use. Geocoding v6 is **not** a POI API. Matrix supports driving/walking/cycling and driving-traffic profiles, billed by elements. [Geocoding](https://docs.mapbox.com/api/search/geocoding/), [Search Box](https://docs.mapbox.com/api/search/search-box/), [Matrix](https://docs.mapbox.com/api/navigation/matrix/) | Useful routing or address tool, not a permanent POI corpus via Search Box. Permanent geocoding is for address results only; review distribution limits. |
| **Geoapify** | Places API is mainly OSM-derived. Public site says cache/store/redistribute results according to terms; formal terms require OSM attribution and Geoapify attribution on free plan. Free tier is **3,000 credits/day**; paid plans start at **$59/month for 10,000 credits/day**. [Places](https://www.geoapify.com/places-api/), [terms](https://www.geoapify.com/terms-and-conditions/), [pricing](https://www.geoapify.com/pricing/) | A practical hosted OSM/routing comparator. ODbL still matters. Exact permanent-store and redistribution language for each API needs written confirmation before using it in a proprietary merged corpus. |
| **HERE** | Search/geocoding and traffic-aware Matrix Routing exist; matrix docs distinguish region/traffic modes. Coverage is product-specific and can change. Public limited plan has daily/RPS limits. [Matrix docs](https://docs.here.com/routing/docs/matrix-v8-intro), [coverage](https://docs.here.com/coverage/docs/here-coverage-information), [limited-plan limits](https://www.here.com/get-started/pricing/rps-limits-excluded-use-cases) | Good travel-time candidate for a Saudi comparison, but contract, storage, and plan price need a quote/terms review. Do not assume HERE POIs are a reusable corpus. |
| **TomTom / MapTiler / Stadia** | Plausible maps/routing or hosted OSM alternatives, but this review found no sufficiently clear **Saudi-specific POI rights-and-cost case** to justify deeper matrix treatment before R02. | Keep as routing/hosting alternatives only if the first two tested providers fail. No rights inferred. |

**Important distinction:** an OSM-based commercial service can sell access and hosting while underlying OSM data remain ODbL. Buying an API plan does not erase attribution or share-alike obligations.

## 12. Saudi Official / Open Sources

**DOCUMENTED.** Saudi Arabia's National Portal says datasets actually published on official open-data platforms may be shared, used, modified and reused under the Open Data License, with attribution, license disclosure, and preservation of notices. It explicitly says the dataset license does not automatically cover media in the dataset, trademarks, privacy rights, or special contracts. Riyadh Municipality describes a similar open-data mechanism. GEA has an open-data page and datasets/policy entry, but an events webpage is not itself shown to be an open event feed. [National Portal](https://my.gov.sa/content/open-Data), [Riyadh Municipality](https://www.alriyadh.gov.sa/en/content/government-open-data), [GEA open data](https://www.gea.gov.sa/open-data)

**INTERPRETATION:** government/open-data portals may provide authoritative baseline entities, licensing counts, facilities, or aggregate cultural statistics, but public dataset descriptions viewed here do not establish a maintained live calendar with sessions, cancellations, and prices for all four catchments. Some cultural open datasets are historical rather than outing inventory; for example, RCU's displayed eMuseum archaeology dataset lists a 2021 update and yearly cadence. [RCU dataset](https://www.rcu.gov.sa/open-data-library/emuseum-archaeology)

**RECOMMENDATION:** R02 may examine catalog metadata and explicitly open downloadable datasets, retaining only fields covered by the specific dataset license plus required notices. Record each dataset's publisher, version, license URL, last update, field definitions, and exclusion of photos unless separately cleared. Treat Visit Saudi, Ministry of Culture, commissions, municipalities, and institutions as **different legal sources**, not one “Saudi official” permission. Visit Saudi's site describes protected intellectual property, and publication on its pages alone does not grant corpus rights. [Visit Saudi secure-use principles](https://www.visitsaudi.com/en/principles-secure-use)

## 13. Saudi Event / Experience Platforms

**webook.** Its June 2026 terms reserve platform data and intellectual property, forbid unauthorized mining/collection and automated use, and require written permission for copying platform content. The wording on private/personal data collection is not the only restriction; separate clauses cover any platform content and databases. webook PRO advertises a selective affiliate program with event referral links, but an affiliate link is **not** a data feed or storage license. No public event-feed API for our use was verified in this review. [webook terms](https://webook.com/business/en/legal/terms), [affiliate program](https://webook.com/business/en/solutions/affiliate-program)

**GEA/Enjoy.** GEA describes Enjoy as a Saudi entertainment-event reference and calendar, including locations and organizer contact/bookings. That confirms relevance to R00, not data reuse rights. Its open-data page and Enjoy event pages must be evaluated separately. No documented general-purpose public event ingest API or commercial reuse permission for Enjoy listings was verified. [GEA Enjoy](https://www.gea.gov.sa/en/media-center/news/enjoy-platform-2), [GEA open data](https://www.gea.gov.sa/open-data)

**RECOMMENDATION:** manually inspect public pages during R02 to assess whether the sources cover the catchments and the fields people need; keep source URL, timestamp and **researcher-authored coverage/rejection codes**, not copied listing text, media or a machine-extracted event database. Seek a signed feed/affiliate/content agreement if the dated-event family proves indispensable. Ask specifically about event IDs, occurrence/status deltas, cancellation latency, price/fees, deep links, photos, attribution, retention and termination deletion.

## 14. First-Party Venue & Operator Sources

Operators are likely best placed to confirm hours, exhibition runs, admission fees, age rules, booking policies and cancellations. **But public first-party does not mean reusable.** Ithra's general website terms, for example, bar reproduction and distribution of site materials except personal non-commercial use without permission. Its ticketing terms note that admission can depend on advance purchase and capacity. [Ithra site terms](https://www.ithra.com/en/terms-conditions), [ticketing terms](https://www.ithra.com/en/ticketing-terms-conditions)

**RECOMMENDATION:** seek direct, small-scope written permission from a handful of museums, galleries, workshops and indoor-activity operators. A lightweight agreement should cover the exact fields (name/site/offer/session, hours, price, availability status), format (CSV/ICS/API/email submission), update duty and cadence, photos separately, public display, embedding/translation/summarization, search indexing, correction and termination. A venue operator may own some descriptions/photos but not all performer or visitor media; the contract should require rights warranties for supplied assets. ICS, RSS, Schema.org/JSON-LD and APIs are **formats**, not grants. Direct editorial notes from a phone/email verification should capture facts and permission to publish them; do not copy protected prose.

## 15. Social Media Sources

**DOCUMENTED scope.** TikTok Display API exposes an authenticated user's own profile/video-list/query integration; its Research API has eligibility tied to independent, non-commercial public-interest research. Snapchat Public Profile API is allowlist-only and oriented to creator/profile functions. Meta's Instagram API documentation describes professional-account management and cannot access consumer Instagram accounts through the Facebook Login variant. YouTube's developer policies restrict downloading/caching audiovisual content, aggregation, and retention of much metadata. None of these establishes a licensed general Saudi place/event discovery firehose. [TikTok Display API](https://developers.tiktok.com/docs/en/display-api-overview), [TikTok Research API](https://developers.tiktok.com/products/research-api), [Snap Public Profile API](https://developers.snap.com/marketing-api/Public-Profile-API/GetStarted), [Meta Instagram API documentation](https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api), [YouTube policies](https://developers.google.com/youtube/terms/developer-policies)

**RECOMMENDATION:** use social pages only as **manually reviewed leads** at first. Confirm an event/opening through an operator or permissioned feed before adding a factual claim. Store a lead URL and internal verification result if lawful; do not store captions, imagery, thumbnails, sentiment embeddings, or “quiet/local” scores derived from platform content without explicit rights. Embedding a post in its official player or obtaining creator permission is a different use case; review it separately. Platform popularity should not be treated as reliable availability or quality.

## 16. Review / Rating Rights

Google reviews and ratings are Maps Content with no general permanent-index right; displaying them has author, source-link and attribution rules. Yelp Places content has a 24-hour cache cap and no commercial analysis permission in its FAQ. Foursquare paid Premium fields include tips, ratings and rich attributes, but its EULA/acceptable-use restrictions apply. Tripadvisor offers a licensed Content API/Terra tiers with reviews/photos, attribution and commercial plans, yet package rights differ. No source here grants a blanket right to store review text, summarize it into persistent descriptors, embed it, train ranking models, or republish it independent of provider terms. [Google Places policies](https://developers.google.com/maps/documentation/places/web-service/policies), [Yelp FAQ](https://docs.developer.yelp.com/docs/places-faq), [Foursquare fields](https://docs.foursquare.com/fsq-developers-places/reference/response-fields), [Tripadvisor Terra](https://docs.terra.tripadvisor.com/docs/overview)

**RECOMMENDATION:** omit third-party review text from the canonical first corpus. Use direct links where allowed, permissioned display only if it improves the decision, and independently documented editorial/user observations. Do not translate or AI-summarize restricted reviews into a stored “atmosphere” field without licensed derivative rights. A rating alone would also poorly establish whether a group can attend tonight.

## 17. Photos / Media Rights

Photos have a distinct provenance and permission chain. Google prohibits caching photo resource names and requires author attribution/source access. Foursquare API Premium photos are not part of FSQ OS Places open core fields. Ithra and webook reserve site content rights. Wikimedia Commons permits reuse **per file** under the file's license, which may require author attribution, a license link and share-alike; a Commons file's presence does not prove that it accurately depicts today's venue. Operator-supplied photos need a written warranty or permission specific to our display and derivative thumbnails. [Google photo rules](https://developers.google.com/maps/documentation/places/web-service/place-photos), [FSQ OS schema](https://docs.foursquare.com/data-products/docs/places-os-data-schema), [Commons reuse](https://commons.wikimedia.org/wiki/Commons%3AREUSE), [Ithra terms](https://www.ithra.com/en/terms-conditions), [webook terms](https://webook.com/business/en/legal/terms)

**RECOMMENDATION:** image records need owner, source URL, exact license/consent, attribution text, permitted transformations, expiry/withdrawal, subject/date, and confidence that the image represents the current experience. Start with operator-permissioned images, a small number of individually checked Commons files, or our own photography. If none exists, show no image rather than copying a search thumbnail. Photo quality is a product issue, but an unlicensed image is not a viable solution.

## 18. Event Data Providers

| Provider | Current documented position | Saudi/R00 implication |
|---|---|
| **Ticketmaster Discovery** | Search/lookup API has event, venue, date and status structures; its country-code list includes `SA`. Terms limit storage to reasonable service periods and require prompt removal upon owner request. The separate **Discovery Feed's supported-country list omits SA**. [Discovery API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-manual/v2/), [feed](https://developer.ticketmaster.com/products-and-docs/apis/discovery-feed/), [terms](https://developer.ticketmaster.com/support/terms-of-use/partner/) | An API parameter is not proof of Saudi event inventory. Audit actual authorized results; no assumption of a Saudi bulk feed. |
| **Eventbrite** | Public global event-search endpoint is explicitly marked shut down since 2019. API terms allow limited storage of **future** event content, prohibit past-event storage absent user permission, require title plus direct link when displaying event listings, and set deletion obligations. Organizer/venue-specific endpoints exist. [API docs](https://www.eventbrite.com/platform/new/api), [API terms](https://www.eventbrite.com/help/en-us/articles/833731/eventbrite-api-terms-of-use/) | Do not plan on public category/location search. Consider only an organizer-authorized integration if R02 identifies a relevant operator. |
| **PredictHQ** | Global event API is sold by plan and location/category; documentation defines a **24-hour cache** when caching is permitted. Public pricing is largely plan/quote oriented. Its search docs warn that out-of-subscription locations can look like missing data. [API search](https://docs.predicthq.com/api/events/search-events), [cache definition](https://docs.predicthq.com/webapp-support/api-plans-pricing-and-billing/what-are-the-definitions-for-storing-and-caching), [pricing](https://cf-origin.predicthq.com/pricing) | Potential licensed supplement, but rights, Saudi coverage and cost need a paid-plan sample. Its demand-intelligence focus may not align with small workshops. |

**RECOMMENDATION:** none should be the assumed Saudi event backbone. First test whether direct institution/organizer relationships and selected open datasets produce enough dated options. If not, R01's partner questions become an MVP gate, not a later optimization.

**Outdoor/route content (deferred):** OSM supplies open trails/roads with ODbL conditions; AllTrails, Komoot and Wikiloc are consumer products, not demonstrated reusable trail feeds here. OSRM/Valhalla can route on OSM data but do not solve trail safety, access, weather or permissions. Keep remote hiking/camping outside the first content set. [OSM copyright](https://www.openstreetmap.org/copyright), [OSRM](https://project-osrm.org/), [Valhalla](https://valhalla.github.io/valhalla/)

## 19. Open Cultural Data

**DOCUMENTED.** Wikidata structured entity data are **CC0**, making identifiers and stable claims a low-friction cultural baseline; data accuracy still requires checking. Wikipedia article text generally carries CC BY-SA 4.0/GFDL attribution and share-alike obligations, so it should not be silently copied into proprietary descriptions. Wikimedia Commons files each have their own license and attribution. Overture Places has source-specific permissive licenses; OSM is ODbL. Saudi open cultural datasets need their actual dataset license and update date inspected. [Wikidata licensing](https://www.wikidata.org/wiki/Wikidata%3ALicensing), [Wikimedia terms](https://foundation.wikimedia.org/wiki/Terms_of_Use), [Commons reuse](https://commons.wikimedia.org/wiki/Commons%3AREUSE), [Overture attribution](https://docs.overturemaps.org/attribution/)

**RECOMMENDATION:** Wikidata for museum/landmark identity and alternate names; separately checked Commons imagery; no Wikipedia prose in the owned descriptions by default. These sources are weak for tonight's hours, session capacity, or ticket price.

## 20. Structured Web Data

Schema.org/JSON-LD can expose event date, location, organizer, offers, event status, LocalBusiness hours and other machine-readable fields. Google's event-structured-data guidance requires one event per leaf page and discusses date/time semantics; its general guidance warns that markup may be inaccurate or misleading. **Structured markup is a parsing aid, not a content license.** [Google Event markup](https://developers.google.com/search/docs/appearance/structured-data/event), [structured-data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

**RECOMMENDATION:** during R02, record whether a first-party site offers ICS/RSS/JSON-LD and whether the operator would grant reuse. Do not systematically crawl/index event markup merely because it is visible. If authorized, preserve occurrence IDs, timezone, status and update timestamp; mark absent cancellation or price information unknown.

## 21. Source Rights Matrix

The table is deliberately conservative. **L** = limited by documented terms or source-specific conditions; **?** = unclear, do not treat as permission; **LR** = legal/commercial review before use; **Y** = permitted under the cited open license/consent and its obligations; **N** = prohibited or unsuitable under the reviewed ordinary terms. “Index/Embed” means **persistent** search index/vectorization, not transient response rendering. “Merge” means a persistent canonical join that retains source-derived fields. “Commercial” means commercial product use, not onward sale of a provider dataset. Sources for each row are linked in Sections 7–20.

| Source / fields | Retrieve | Cache | Store | Merge | Index / embed | Transform | Independent display | Attribution | Commercial | Redistribute | Refresh / cost | Saudi evidence / risk |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **FSQ OS Places core** | Y, portal | Y | Y | Y, license notices | Y | Y | Y | License + NOTICE | Y | Y, license | Monthly release/deltas; dataset free, processing cost | Global; local completeness unknown; no live feasibility. |
| **Foursquare paid API POI fields** | Y, account | L | N/L | N/L | N/L | N/L | L, branded | “Powered by FSQ” | L | N | 500 free Pro then $15/1k tier | Richer fields; canonical rights blocked without negotiated license. |
| **Foursquare paid tips/photos/ratings** | Y, Premium | L | N/L | N/L | N/L | N/L | L | FSQ and content rules | L | N | Premium $18.75/1k first tier | Distinct media/UGC risk. |
| **Google Place ID only** | Y | Y | Y | L, ID crosswalk only | L, identifier | N/A | L | Depends on display | Y, API terms | N | IDs-only details listed free | ID does not transfer place-content rights. |
| **Google place metadata/hours/ratings** | Y | N, except defined exceptions | N | N | N | N | L, logo; Google map if mapped | Required | L | N | Field/SKU priced | Strong apparent coverage untested here; incompatible with owned corpus. |
| **Google photos/reviews** | Y | N | N | N | N | N | L, author/source link | Required | L | N | Enterprise/photo SKU | High rights and UI burden. |
| **Yelp Places content** | Y, key | L, 24h | N; ID Y | N | N | N | L | Required | L | N | Paid plan unclear | Saudi locale absent; low priority. |
| **OSM POI/roads** | Y | Y | Y | LR, ODbL boundary | Y with ODbL | Y with ODbL | Y | © OSM + license | Y | Y with ODbL | Data free; host/refresh cost | Saudi quality unmeasured; share-alike review. |
| **OSMF public Nominatim/tiles** | L, usage policy | L | L, data rights separate | LR | LR | LR | L | OSM | L | N as service | Rate limits/no SLA | Do not build production dependency on public infra. |
| **Overture Places rows** | Y | Y | Y | Y/L by row license | Y/L | Y/L | Y/L | Per-source notice | Y/L | Y/L | Open release; compute cost | Source-specific license and conflation quality. |
| **Wikidata structured data** | Y | Y | Y | Y | Y | Y | Y | CC0 (credit good practice) | Y | Y | API/dump limits | Cultural scope; freshness weak. |
| **Commons photo, individually checked** | Y | Y/L | Y/L | L | L | L, file license | Y/L | Per file | Y/L | Y/L | Download/hosting | Depiction currency and rights vary. |
| **Saudi licensed open dataset** | Y | Y | Y | Y/L | Y/L | Y/L | Y/L | License/source | Y/L | Y/L | Dataset release | Must verify exact dataset and media exclusion. |
| **GEA/Enjoy, Visit Saudi pages** | Y, public viewing | ? | N/? | N/? | N/? | N/? | L, link | Source link | ? | N/? | Manual; no public feed found | Public page ≠ open dataset. |
| **webook pages / event media** | Y, public viewing | N/? | N | N | N | N | Link only without agreement | Agreement | N/? | N | Partner quote | Written permission required for feed/content. |
| **Direct operator-authorized fields** | Y, agreement | Y, agreement | Y, agreement | Y, agreement | Y, agreement | Y, agreement | Y, agreement | As agreed | As agreed | As agreed | Staff/partner cost | Strong on time; operationally fragmented. |
| **Social public posts/content** | L | L/N | N/? | N | N | N | Official embed only if allowed | Platform/creator | L | N | Access-dependent | Lead/reference only in first experiment. |
| **Ticketmaster API events** | Y, key | L, reasonable | L | LR | LR | LR | L | Terms/content | L | N | API/affiliate terms | SA code listed; SA feed absent. |
| **Eventbrite organizer-authorized future events** | L | L | L, future only | LR | LR | LR | L, title/link | Direct link | L | N | API limits | Global search shut down; operator route only. |
| **PredictHQ plan events** | Y, plan | L, 24h if allowed | ?/plan | LR | LR | LR | L/plan | Plan-dependent | L/plan | N/? | Quote | Saudi/category completeness unknown. |
| **Mapbox Search Box POIs** | Y | N | N | N | N | N | L | Terms | L | N | API price | Temporary only. |
| **Mapbox permanent geocodes** | Y, paid mode | Y | Y | L | L | L | L | Mapbox | Y | N (own use only) | Per-call price | Address, not POI feed. |
| **Geoapify OSM-derived POIs** | Y, plan | L | LR | LR | LR | LR | Y/L | OSM; Geoapify if free | Y | LR | Credits/day | Hosted alternative; ODbL remains. |

**Legal review priorities:** (1) whether our exact OSM/FSQ/Overture joined tables form an ODbL derivative database; (2) Foursquare paid API enrichment and post-termination retention; (3) permissions from event/ticketing partners, especially availability and photos; (4) live Google content alongside an independent map; (5) field-level rights of any Saudi dataset containing third-party media.

## 22. Field-Level Rights Matrix

“Safe storage” below assumes the field comes from the **named open/authorized source**, never from a restricted lookalike field in a commercial API. “Cost” is a driver, not a quote. R02 must measure fill rate and correctness.

| Field | Best candidate and backup | Safe persistent storage / merge? | Refresh and trust rule | Cost or hole |
|---|---|---|---|---|
| Internal place/branch identity | Our ID from FSQ OS; Overture/Wikidata crosswalk | Yes with per-source license | Separate branches and contained venues; confirm ambiguous matches | Entity-resolution labor. |
| Name and aliases | FSQ OS; permissioned operator | Yes, source-aware | Operator check for spelling/transliteration | Moderate; avoid Google-derived overwrite. |
| Coordinates / entrance | FSQ OS or Overture; operator correction | Yes if rights retained | Verify entrance for destination use | Moderate local verification. |
| Address / neighborhood | FSQ OS, open government; operator | Yes if source license applies | Normalize, keep source original | Geocoding if missing; rights-sensitive. |
| Category/type | FSQ OS / Overture; editorial | Yes | Human check nested offerings | Moderate classification effort. |
| Standard hours | Operator permission; OSM only with ODbL review | Yes if permissioned/open | Recheck weekly/monthly by volatility; holiday exceptions | **Major gap** in open POI layer. |
| Special/holiday hours | Operator feed or direct authorized update | Yes if permissioned | Recheck near date; unknown is not open | High labor and missed-change risk. |
| Exhibition run / event occurrence | Operator/organizer feed; specific open dataset | Yes if licensed | Date, timezone, venue, occurrence ID | **Major gap** without partner network. |
| Cancellation / reschedule | Operator/ticket feed | Yes if licensed | Event-driven or same-day confirmation | High trust impact; no broad source established. |
| Price and price unit | Operator feed or authorized editorial fact | Yes if permissioned | Distinguish entry, per person, package, fees | Often absent/variable. |
| Duration | Operator/first-party verified; editorial estimate clearly labeled | Yes if authored/permitted | Range and activity vs total outing time | Verification labor. |
| Booking and walk-in rule | Operator feed/direct confirmation | Yes if permissioned | Never infer from open hours | Critical for promise A. |
| Session availability | Booking partner/venue only | Only under explicit agreement | Query-time/status TTL; no inference | Likely unavailable initially. |
| Group/age rules | Operator/organizer | Yes if permissioned | Recheck on program change | High consequence when wrong. |
| Accessibility / parking | Operator statement or verified observation | Yes if authorized | Never infer unsupported accessibility | High verification bar. |
| Indoor/outdoor | Open category plus editorial verification | Yes for independent observation | Season/context still matters | Low to moderate. |
| Photo | Operator license, own image, individually licensed Commons | Only with asset-specific license | Removal and attribution path | Rights and production cost. |
| Description / mood | Original editorial wording grounded in permissioned facts | Yes if original | Update when experience changes; avoid review paraphrase | Editorial cost. |
| Rating / review | Licensed live display only; direct link fallback | Generally **no** for owned corpus | Respect author/link/TTL terms | Deferred; not essential to first decision. |
| Official URL / contact | FSQ OS, operator submission | Yes for source-aware identity; test link | Link health checks; phone may change | Low API, recurring QA. |
| Travel time | Route API at user decision time | Cache/store per specific service terms; not a permanent place attribute | Recompute with mode/departure | Element-based; quality must be audited. |

## 23. Canonical Database Feasibility

| Model | Rights position | Decision quality / cost | Verdict |
|---|---|---|---|
| **A. Open/owned canonical corpus** | FSQ OS (Apache), selected Overture rows (CDLA/Apache), Wikidata (CC0), individually licensed Saudi datasets, direct operator records. OSM only with ODbL-aware partitioning/review. | Low recurring API spend; substantial manual coverage and freshness work. | **Viable for a narrow controlled test**, contingent on local coverage and operator permissions. |
| **B. Federated dynamic discovery** | Minimal internal IDs; query commercial providers live under their own display/caching rules. | Faster broad reach, but difficult cross-source ranking, dedupe and repeatable evaluation; per-search API and lock-in costs. | Useful supplement, weak sole foundation for the proposed product. |
| **C. Licensed commercial canonical corpus** | Requires explicit contract for retention, joins, indexing, embeddings, onward display and exit rights. Ordinary self-service plans do not establish all of these. | Could raise completeness, but cost/rights/termination risk unknown until quotes. | Investigate if R02 proves open/first-party baseline inadequate. |
| **D. Hybrid rights-segregated corpus** | Persist only fields with explicit open/owned/contractual rights; restricted providers remain live, attributed and separately governed. | Supports R00's cross-domain decision while preserving a lawful internal evaluation set. | **Preferred hypothesis for R02**, provided the application never launders restricted fields into owned records. |

**Answer:** **conditionally yes** to a persistent canonical database for *independently licensed facts*, **no** to one automatically assembled from all accessible APIs/pages. Legal defensibility depends on license notices, source-specific field provenance, ODbL treatment, operator agreements, and deletion controls. The database's practical value depends on coverage and refresh effort, which R02 must measure.

## 24. Provider Lock-In

Google Places can create ID and map-display dependency even when no content is retained. Foursquare's open dataset is less rights restrictive than its API, but an FSQ ID should not become the only canonical identity. Overture has per-row source licenses and conflation history that can change. A single ticketing partner may dominate dates in one catchment and miss small workshops. Route providers differ in traffic and Saudi coverage; switching can change travel-time feasibility. Providers can revise prices, terms, quotas and release channels—Foursquare already shifted the FSQ OS download route from public S3 to a portal while retaining the open license. [FSQ access](https://docs.foursquare.com/data-products/docs/access-fsq-os-places), [FSQ transition](https://foursquare.com/resources/blog/data/evolving-fsq-open-source-places/)

**RECOMMENDATION:** own internal venue/offering/occurrence IDs; maintain provider IDs as crosswalks; retain each fact's lawful source; keep route results separate from entity records; test a second geospatial/route provider on a small sample. Export/termination rights belong in every commercial negotiation.

## 25. Provenance / Rights Metadata

For every retained claim, record conceptually: **source organization and exact product/dataset; provider ID; source URL or release ID; license/agreement version; field-specific right to store/merge/index/embed/transform/display; attribution text; retrieval and last-confirmed times; valid-from/to; expiry/deletion trigger; actor/consent where first-party; confidence and conflict status**. For photos, add author and per-asset license. For open datasets, preserve release/version and upstream source license (especially Overture). For editorial verification, record what was observed and who confirmed it, not a copy of protected prose.

**RECOMMENDATION:** R03 should model claims as source-bound; an entity-level label such as “Google/Foursquare/OSM verified” is inadequate. A result may have an open identity, operator-confirmed hours, uncertain price, and no licensed image. Rights filtering must apply before search indexing and embeddings, and source deletion must remove downstream search projections. Do not use a restricted provider's content as training labels or generated-description input without permission.

## 26. Refresh Economics

| Volatility | Examples | Test cadence **hypothesis**, not a source guarantee | Primary cost |
|---|---|---|---|
| Slow | Name, stable address, entrance, operator | Open release updates plus targeted operator correction | Match/review labor. |
| Medium | Normal hours, category, phone, repeatable offering | Weekly/monthly sample; verify before surfacing “open tonight” | Operator follow-up. |
| Fast | Special hours, exhibition run, price, booking policy | At publication and near the user's date; explicit unknown if stale | Human monitoring or contracted feed. |
| Very fast | Cancellation, sellout, session availability, pop-up move | Event-driven partner update or query-time confirmation | Feed/license cost; failure risk. |

FSQ OS monthly releases and an entity `date_refreshed` do not certify current hours, because one refreshed reference can change the timestamp. Eventbrite's future-event storage permission, PredictHQ's plan-dependent 24-hour cache, Yelp's 24-hour cache, and Google Places' no-caching rule are **rights limits**, not suggested freshness intervals. [FSQ schema](https://docs.foursquare.com/data-products/docs/places-os-data-schema), [Eventbrite terms](https://www.eventbrite.com/help/en-us/articles/833731/eventbrite-api-terms-of-use/), [PredictHQ cache](https://docs.predicthq.com/webapp-support/api-plans-pricing-and-billing/what-are-the-definitions-for-storing-and-caching), [Yelp FAQ](https://docs.developer.yelp.com/docs/places-faq), [Google Places policies](https://developers.google.com/maps/documentation/places/web-service/policies)

**Economic rule:** refresh only fields that change the decision or safety/trust level. A stale opening-hour claim can make a good option unusable; an old category label often does not. Count manual minutes per verified fact and per correction, not merely records checked.

## 27. Routing / Travel-Time Economics

R00's “nearby” is plausibly travel minutes rather than radius, but actual mode and tolerance require user observation. **RECOMMENDATION:** use rough geographic pruning, then request travel times for a shortlist of perhaps 5–10 candidates at decision time. A one-origin/8-destination matrix is 8 billed elements on providers that meter by element; an all-pairs 8×8 matrix is 64, with little value for the first outing decision. Google Routes Matrix and Mapbox Matrix both meter elements; HERE Matrix supports traffic-aware options; OSRM/Valhalla can run on OSM data but require hosting, data maintenance and local accuracy testing. [Google price list](https://developers.google.com/maps/billing-and-pricing/pricing), [Mapbox Matrix](https://docs.mapbox.com/api/navigation/matrix/), [HERE Matrix](https://docs.here.com/routing/docs/matrix-v8-intro), [OSRM Table service](https://project-osrm.org/docs/), [Valhalla](https://valhalla.github.io/valhalla/)

| Option | Modes/traffic | Published economic signal | Rights/fit caveat |
|---|---|---|---|
| Google Routes Matrix | Driving/walking/transit details depend on mode/SKU; traffic features can trigger Pro | Essentials 10,000 elements free/month then $5/1k; Pro 5,000 free then $10/1k first tier. [Prices](https://developers.google.com/maps/billing-and-pricing/pricing) | Non-Google map restriction; cache only express exceptions. [Terms](https://cloud.google.com/maps-platform/terms/maps-service-terms) |
| Mapbox Matrix | Driving, walking, cycling, driving-traffic profiles; traffic profile has smaller request limit | **100,000 elements free/month**, next 400,000 at $2/1k on public page. [Matrix](https://docs.mapbox.com/api/navigation/matrix/), [pricing](https://www.mapbox.com/pricing) | Terms/traffic behavior and Saudi accuracy need testing; no guarantee free tier remains. |
| HERE Matrix | Car/pedestrian/bicycle plus traffic modes in defined regional requests | Public pricing needs account/plan confirmation; do not invent per-element figure. [Matrix](https://docs.here.com/routing/docs/matrix-v8-intro) | Product coverage and rights need plan review. |
| Geoapify routing/matrix | OSM-based driving/walking options | Free 3,000 credits/day; paid $59/month for 10,000/day; matrix credit formula must be checked. [Prices](https://www.geoapify.com/pricing/), [details](https://www.geoapify.com/pricing-details/) | OSM attribution/quality; daily, not monthly allowance. |
| Self-hosted OSRM/Valhalla | Road/walk/bike profiles; no proprietary live traffic by default | No per-call vendor fee, but servers, updates, observability and operations are **unpriced here**. [OSRM](https://project-osrm.org/), [Valhalla](https://valhalla.github.io/valhalla/) | ODbL data and accuracy/ops burden; do not use public demo servers as production dependency. |

**R02 task:** compare predicted drive/walk minutes from two lawful providers for a small set of real origin–destination pairs in each catchment at relevant hours. Do not declare a winner based on free-tier price alone. Transit support and Saudi network coverage need explicit confirmation; car travel is a test hypothesis, not a hard assumption.

## 28. Cost Model

The scenarios are **illustrative workloads, not forecasts**. Currency conversion uses **USD 1 = SAR 3.75**, the long-standing Saudi riyal peg documented by the Saudi Central Bank; actual billing conversion/fees may differ. [SAMA annual report](https://www.sama.gov.sa/en-US/EconomicReports/AnnualReport/Fifty_Eighth_Annual_Report-EN.pdf)

**Public unit prices used:** FSQ OS Places and Wikidata dataset licenses have no data-access fee, though processing/hosting are not free. Mapbox Matrix: first 100,000 elements/month free, next tier $2/1,000. Google Routes Matrix Pro sensitivity: first 5,000 free, 5,001–100,000 at $10/1,000, 100,001–500,000 at $8/1,000. Foursquare API sensitivity: 500 free Pro calls, then $15/1,000 in first tier. [Mapbox pricing](https://www.mapbox.com/pricing), [Google pricing](https://developers.google.com/maps/billing-and-pricing/pricing), [Foursquare pricing](https://foursquare.com/pricing/)

**Editorial labor sensitivity assumption, explicitly *not a documented wage or quote*:** SAR **50–150 per hour** of all-in researcher/curator time. This bracket is chosen only to show sensitivity. It excludes hiring overhead, legal review, vendor minimums, cloud hosting, product development and marketing. Actual Saudi staffing cost must be obtained separately.

| Scenario / assumptions per month unless noted | Dataset/API and routing calculation | Illustrative human verification | What is **not priced** |
|---|---|---|---|
| **1. Manual research prototype:** 150 candidate records; 100 observed/test searches; 8 route elements/search; one-time 8 min/record + 40 monthly rechecks × 4 min. | Open dataset license $0; Mapbox 800 elements = **$0/SAR 0** under published free cap. Google Routes Pro also $0 at this volume if eligible. | Initial **20 h** = **SAR 1,000–3,000 / USD 267–800**; monthly 2.7 h = **SAR 133–400 / USD 36–107**. | Workspace/cloud, travel to sites, photo permissions. |
| **2. Controlled MVP:** one catchment; 500 records; 3,000 searches; 8 route elements/search; one-time 8 min/record + monthly 500 routine checks × 4 min + 100 event/status checks × 8 min. | Open dataset $0; Mapbox 24,000 elements = **$0/SAR 0** under published cap. If Google Routes Pro is selected, `(24,000−5,000)/1,000×$10 = $190 / SAR 713`. If 1,000 Foursquare Pro API calls are actually added, `500/1,000×$15 = $7.50 / SAR 28` under listed tier, but API rights remain restricted. | Initial **66.7 h** = **SAR 3,333–10,000 / USD 889–2,667**; monthly **46.7 h** = **SAR 2,333–7,000 / USD 622–1,867**. | Event-feed license, cloud/maps, any paid media. |
| **3. Early production stress case:** several areas; 3,000 records; 50,000 searches; 8 route elements/search; monthly 3,000 routine checks × 6 min + 600 event/status checks × 8 min. | Mapbox 400,000 elements = `300,000/1,000×$2` = **$600 / SAR 2,250**. Google Routes Pro sensitivity = `95,000/1,000×$10 + 300,000/1,000×$8` = **$3,350 / SAR 12,563**. 10,000 FSQ Pro calls would be **$142.50 / SAR 534** after 500 free, if rights and use fit. | Monthly **380 h** = **SAR 19,000–57,000 / USD 5,067–15,200**. | Headcount management, provider subscriptions, venue SLAs, failed/retried calls, taxes and hosting. |

**Interpretation:** free API allowance does not mean the corpus is cheap. The illustrative monthly verification expense is already far larger than matrix cost in scenario 2. Conversely, manual workload can be reduced if operators supply machine-readable, rights-cleared updates; whether they will is unknown. Map display, geocoding, paid event feeds, media hosting, embeddings and database/compute are **not priced as zero**—their prices depend on the chosen product architecture and contracts. If a provider minimum or licensed feed quote is material, insert it before calculating cost per decision. Avoid bundling a Google Places enrichment cost into this owned-corpus model; that would imply rights we do not have.

## 29. Unit Economics

Track separately by catchment, source and content family: **cost per rights-cleared item**, cost per item passing identity/time/price/booking checks, manual minutes per item and update, % with unknown critical facts, correction latency, cost per route matrix element, API spend per search, cost per *feasible* result, cost per user decision, and cost per catchment/month. Also track partner onboarding and recurring maintenance time. A raw API request can return many irrelevant/duplicate/stale candidates and say nothing about whether a user can act on them. The unit of value is a credible outing decision, not a retrieved record.

## 30. Partnership Strategy

The first outreach should target **few high-yield operators** spanning several offerings or recurring events, not hundreds of one-off businesses. Candidate classes are cultural institutions/exhibition operators, indoor-activity chains or independent venues, workshop organizers, and area/district managers; selection must follow R02 coverage, not assumed prestige. A source can improve *information rights* without necessarily improving *discovery diversity*.

Minimum deal checklist: exact licensed fields and territory; whether historical and future occurrences may be retained; schedule/status/availability update mechanism; permitted indexing/embeddings/translation; images and author rights; attribution and outbound ticket links; price/fee semantics; correction/cancellation SLA; display on any map; sublicense/export restrictions; termination deletion; ability to preserve first-party user decisions; and whether supplied operator data can be merged with open identities. A ticketing affiliate agreement addresses referrals, not automatically content rights. [webook affiliate offer](https://webook.com/business/en/solutions/affiliate-program)

**Commercial dependency:** if promise A requires “available tonight” rather than merely “open tonight,” a bookable-session feed or operator confirmation becomes an actual product dependency. R02 should quantify how many otherwise relevant choices fail for lack of that field before we negotiate broad inventory access.

## 31. Editorial Curation

Human curation can create the differentiating “worthwhile” layer: identify a distinctive workshop or exhibition, check why it is relevant, confirm its practical facts, and explain uncertainty. It is lawful only if researchers record their own observations/facts or have permission to use protected content; it is not a loophole for copying a provider database by hand. For a pilot, use a standard fact checklist, direct source URLs, a review timestamp, a consent/permission status, and a correction mechanism. Author original descriptions and prohibit unsupported “hidden gem,” “quiet,” “wheelchair accessible,” or “no booking needed” assertions.

**Economic test:** measure minutes for first verification, repeat check, event change, photo clearance and correction. Stop expanding content if cost per verified viable choice rises faster than query coverage. Record missing data as an outcome, not a reason to invent it.

## 32. User / Business Contributions

**User submissions:** potentially useful for new openings, closure reports and experiential language. They need original-content terms granting this product the rights to store, display, adapt and remove submissions; privacy rules; moderation; spam/abuse controls; and evidence thresholds. A user-uploaded screenshot of Google Maps or a copied Instagram caption does not become user-owned content. Defer open submissions until a correction/verification loop is operational.

**Business claims:** allow a verified operator to assert hours, prices, sessions and media only after proving control of the entity and rights to supplied assets. Treat claims as source-specific, dated and reversible. A business has an incentive to overstate availability or quality; verify high-impact claims and separate paid placement from editorial eligibility. This is a future acquisition channel, not a reason to bypass direct agreements in the first experiment.

## 33. Source Scorecard

Qualitative, deliberately **not** collapsed into a universal score. “Rights” refers to the proposed persistent corpus use; “Saudi quality” remains an R02 unknown unless explicitly documented.

| Candidate | Saudi/catchment completeness | Time and feasibility fields | Persistent rights | Cost shape | Main burden |
|---|---|---|---|---|---|
| FSQ OS Places | **Unknown locally**; global open dataset | Weak for hours/session/price | **Strong** Apache 2.0 plus NOTICE | Free dataset; import/QA | Refresh, false/duplicate POIs. |
| Overture Places | **Unknown locally**; multi-source | Weak for near-term decisions | Strong but **row-specific** CDLA/Apache | Free dataset; processing | Source-license and conflation tracking. |
| Wikidata / Saudi licensed open datasets | Narrow cultural/administrative coverage | Usually weak for tonight | Strong only for exact licensed dataset | Free access, QA | Incompleteness and old publication. |
| OSM data | **Unknown locally** | Some hours/tags, no sessions | Usable with ODbL share-alike duties | Hosting/QA | Derivative-database boundary. |
| Direct operators | Highly local if recruited | **Potentially strongest** | Strong if explicit agreement | Human/partner effort | Fragmented onboarding and updates. |
| Google Places | Saudi claim not audited | Broad place fields; no live booking guarantee | **Poor for canonical use** | Per-SKU calls | No indexing/storage; map display. |
| Foursquare paid API | Global claim, local fill unknown | Some hours/ratings/tips | Poor under self-service for merged corpus | Pro/Premium calls | Restrictions and branded display. |
| Local ticket platform or signed event feed | Potentially high for dated events | Best potential status/booking | **Contract-dependent** | Quote/affiliate | Partner concentration and outages. |
| Yelp | Saudi locale absent | Some business hours/reviews | Poor for canonical use | Plan unclear | Low apparent fit. |
| Social content | Saudi user relevance plausible, unmeasured | Often announcements but unreliable | Poor without creator/platform rights | Manual lead review | Rights, virality bias, stale posts. |

## 34. Candidate Source Stacks

| Strategy | Composition | Strength | Failure / cost | R02 role |
|---|---|---|---|---|
| **A. Open and operator-first** | FSQ OS/Overture/Wikidata, selective Saudi open datasets, 10–30 permissioned operators, original editorial checks, limited routing | Owned test corpus; lowest restricted-content risk | Events and special hours may be sparse; manual labor | **Primary baseline** for all four catchments. |
| **B. Commercial-provider-heavy federation** | Live Google/Foursquare/Tripadvisor/ticket APIs and routed display | Fast apparent breadth where products cover area | Weak corpus rights, map/attribution complexity, volatile cost, hard cross-source ranking | **Not the primary candidate**; use as external benchmark only, no retained content. |
| **C. Rights-segregated hybrid** | Stack A plus contracted event/venue feed where it fills measured gaps, separate live commercial displays when lawful | Balances ownership with current data | Source-specific rights governance and partner minimums | **Preferred development hypothesis** after baseline gap measurement. |

The preferred strategy is **C, starting operationally with A**. This avoids a premature paid-feed commitment while preserving a path if R02 shows promise A cannot be answered reliably from open and first-party sources. A large open identity layer is not a product until the time/price/booking fields work.

## 35. Catchment-Specific Implications

These are source hypotheses, **not R02 coverage findings**.

| R00 catchment | Source families to inspect first | Specific rights/economics question |
|---|---|---|
| **Al Khobar waterfront–Dhahran/Ithra–nearby Dammam** | FSQ OS/Overture identity; direct Ithra and activity operators; municipal/open datasets; local organizers | Ithra pages are protected, so can an operator permission/first-party feed supply exhibition and session facts? What portion of trips need car vs walk route time? |
| **Diriyah–JAX–Bujairi/At-Turaif** | District/heritage authority, galleries/workshops, operator feeds, FSQ OS/Overture, permitted open cultural data | Are programs and site-access rules centralized under a rights-granting partner or scattered across protected pages? |
| **Historic Jeddah/Al-Balad** | Heritage/tourism institutions, local galleries/markets, open cultural/OSM place data, direct operators | Can temporary cultural opportunities be verified without reusing protected tourism imagery or articles? Which entrances/parking facts matter? |
| **Boulevard City–Hittin** | GEA/Enjoy, webook and venue operators, FSQ OS identity, route provider | High event/ticket dependency may make this the most partner-dependent area; can a direct license expose status and price affordably? |

All four need the same **weekday evening, Thursday/Friday or local weekend, 90-minute gap and future-date** checks from R00. Do not count a source's national event calendar as evidence of options in a given catchment/time window.

## 36. Risk Register

| Risk | Severity / likelihood now | Mitigation and MVP effect |
|---|---|---|
| Restricted provider forbids canonical storage/indexing | High / **known** for ordinary Google use; high uncertainty for other plans | Exclude from persistent corpus; obtain explicit license if essential. **Blocks that source**, not all MVP. |
| OSM share-alike contaminates proprietary join | High / unresolved | Partition provenance, review exact join and ODbL obligations. **Blocks OSM-based merged corpus until reviewed.** |
| Foursquare open vs paid rights confused | High / plausible | Separate source IDs, licenses and fields; test imports from open release only. **Blocks paid enrichment ingest.** |
| Photos/reviews copied without rights | High / plausible | Asset-specific rights and no default review storage. **Blocks copied media.** |
| Saudi open dataset mistaken for all official site content | High / plausible | License-check each dataset; no page content/media copied. **Blocks affected source.** |
| Event source lacks cancellation/status deltas | High / unknown | Direct operator confirmation, suppress or label uncertain near-time events. **May block promise A** if common. |
| webook/GEA partnership unavailable or too costly | High / unknown | Test direct operators; narrow dated content. **May narrow content/promise.** |
| Open POI layer incomplete/stale in catchment | High / unknown | R02 ground truth sample, compare FSQ/Overture/OSM. **May change area.** |
| Social platform API/search inaccessible | Medium / likely for bulk discovery | Manual lead-only workflow; do not make source critical. **No MVP block.** |
| Map/routing provider inaccurate or incompatible | Medium/high / unknown | Compare at real times; rights-screen display and cache. **May affect travel-time promise.** |
| Editorial verification cost overwhelms API savings | High / unknown | Time every verification/correction and cap initial scope. **Potential economic gate.** |
| Provider changes prices, access path, terms | Medium / ongoing | Dated terms register, independent IDs, supplier exit plan. **Manageable if decoupled.** |

## 37. Architecture Consequences

R03 should preserve these logical rules, not implement microservices now:

1. **Source/claim segregation:** a canonical entity links to claims, each with license, source, validity, expiry and attribution. Restricted live fields do not enter the owned search projection.
2. **Identity independent of providers:** one internal site/offering/occurrence ID; FSQ/Overture/Wikidata/Google IDs as qualified crosswalks. Never infer a new opening from FSQ `date_created`.
3. **Rights-aware transforms:** indexing, embeddings, summaries, comparisons, training labels, image thumbnails and redisplay count as distinct uses. A generic “API allowed” flag is inadequate.
4. **Deletion and correction lineage:** source expiry or withdrawal removes downstream projections and media; operator correction supersedes a claim with history, not silent overwriting.
5. **Time-specific trust:** “open venue,” “active event,” “available session,” and “price known” are separate claims with separate TTLs and abstention behavior.
6. **Provider-neutral route interface:** route results carry provider, mode, departure time, element count and permitted caching/display scope; they are not permanent venue properties.
7. **Attribution ledger:** result display can present the right notice for OSM, FSQ open data, Commons, Saudi datasets and any live restricted provider.

## 38. Inputs for R02 — Permitted Source Plan

**R02 may start beyond simple public-page reading, but only within these lanes:**

| Lane | Allowed next step | Retain in R02 audit | Do **not** retain or do |
|---|---|---|---|
| **Open datasets** | Obtain FSQ OS Places from official portal, Overture Places release, Wikidata; inspect specifically licensed Saudi datasets. | A bounded catchment sample of licensed fields; license/release/source/attribution; researcher QA judgments. | Do not merge OSM into a private corpus without legal review; do not assume media shares dataset license. |
| **OSM** | Manually inspect data and/or use a compliant limited extract; track ODbL and public endpoint policy. | OSM IDs/tags in a separately governed sample with OSM attribution. | No public Nominatim/Overpass/tile service bulk production; no unreviewed proprietary blend. |
| **First-party operators** | Ask for explicit pilot permission or a feed; manually verify facts with venue/organizer. | Agreed fields and original researcher notes, agreement/consent record, timestamps. | Do not copy protected descriptions/images from public sites without permission. |
| **Public restricted event/venue pages** | Human coverage reconnaissance: source exists? what fields are visible? how current? | URL, source name, date checked, field-presence flags, original coverage/rejection notes, uncertainty. | No automated scraping, copied descriptions/photos, bulk event rows or provider-derived canonical fields without rights. |
| **Commercial APIs** | Only after developer account, current terms and allowed audit method are documented; use a bounded lawful query sample if plan permits. | Provider ID or aggregated **non-content** audit counts where terms permit; billing log. | No lasting response table, embeddings, cross-source merged index, or display outside terms. Google Places examples require special care. |
| **Routing** | Bounded Mapbox/Google/HERE/Geoapify comparison under applicable terms using a fixed set of operator/open-data coordinates. | Measurement results only if provider terms permit; otherwise aggregate error/latency and cost. | No permanent cache or non-compliant map combination. |

**R02 sampling inputs:** all four catchments; four R00 content families; weekday evening, Thursday/Friday or local weekend, 90-minute pre-commitment and future-date windows. Count **eligible, rights-clearable choices** with identity, entrance, time, duration, price or honest unknown, booking/group rule, and confirmation time. Include “no good result” cases and closure/cancellation contradictions. Measure source-specific fill rates, false matches, verified option density, verification minutes and price per useful item. Compare strategy A against C only if a narrow licensed pilot feed becomes available. R02 should log the published prices in Section 28 as assumptions and replace them with actual account quotes before committing spend.

**Specific partnership/legal questions to carry into R02:** Does one direct operator or district partner provide enough time-bound inventory to test promise A? Does an event partner provide occurrence-level cancellation/status and fee-inclusive price? Can OSM be used as an independent map/routing layer without triggering share-alike for our place facts? Are FSQ OS/Overture Saudi branch coordinates and category labels reliable enough to seed a 500-item pilot? Is a commercial route estimate materially better than OSM-based estimates at relevant hours?

## 39. Open Questions

| Priority | Question | Decision affected |
|---|---|---|
| **Critical before MVP** | Which open/permissioned source yields enough verified options in each catchment/time window? | Area and content scope; R02. |
| **Critical before MVP** | Can operators or a signed feed provide current exhibition/workshop/event status, price and booking? | Promise A vs B. |
| **Critical before MVP** | What are the exact ODbL consequences of the intended POI joins and map/routing layers? | Canonical architecture; legal review. |
| **Critical before MVP** | What written rights cover first-party photos, copied descriptions and event media? | Presentation and index. |
| **Critical before MVP** | How many minutes and SAR does a verified item and change cost in each area? | Sustainable scope. |
| **Important during MVP** | Is FSQ OS or Overture better on Saudi branch accuracy, openings/closures, and cultural categories? | Base-source choice. |
| **Important during MVP** | Which travel-time service best matches real Saudi trips at useful times and legal display conditions? | Feasibility. |
| **Important during MVP** | Do commercial review/rating displays improve decisions enough to justify rights/cost complexity? | Later enrichment. |
| **Can wait** | Does live ticket inventory or personalization pay for its contractual and operational burden? | Future product. |

## 40. Recommended Next Actions

1. **Create a dated rights register** for FSQ OS, Overture, Wikidata, chosen Saudi datasets, OSM and any pilot operators, with exact license/NOTICE copies and field-level allowed uses.
2. **Obtain legal review** of the intended OSM/FSQ/Overture join and of any restricted source proposed for persistent indexing or embeddings.
3. **Run R02's bounded open-data sample** in all four catchments. Measure usable options by R00 time window and content family; preserve row-source licenses.
4. **Request pilot data rights from a small set of operators** likely to supply multiple exhibitions, workshops or indoor activities; ask for occurrence/status updates and image rights separately.
5. **Ask webook/GEA or other event operators for a concrete feed/affiliate-content proposal** only if R02 shows the dated-event family is otherwise too thin. Get written price and data-rights answers.
6. **Compare 20–40 representative travel-time pairs** across lawful route providers and relevant times, with rights and element costs noted.
7. **Time every manual verification and correction** during R02. Replace the assumed SAR/hour bracket with actual staffing or contractor quotes.
8. **Revise promise A/B after observed users and R02 evidence.** If cancellation/booking facts cannot be kept current, narrow “available tonight” claims instead of masking unknowns.

# Most Important Findings

1. **FSQ OS Places is materially different from Foursquare's paid API.** The open Apache 2.0 dataset is a realistic persistent place baseline; the self-service API is not an automatic canonical-data license.
2. **Overture Places is a second plausible open baseline**, but its rows can carry different CDLA/Apache licenses and need source-level tracking.
3. **The hardest first-product data are temporal and practical**—special hours, occurrence status, price, duration and booking—not generic place identity.
4. **Google Places can support live, attributed functions and stored Place IDs, but its ordinary terms do not permit seeding our permanent merged search corpus.**
5. **OSM is commercially usable with ODbL duties; public OSM servers are a separate, limited infrastructure resource.** Mixing OSM POIs with proprietary records needs legal review.
6. **Saudi official pages and ticketing pages are not automatically open data.** webook requires written permission for content extraction/reuse; only specifically licensed government datasets carry open-data rights.
7. **No reviewed provider establishes a complete, licensed Saudi near-term event layer.** Ticketmaster lists SA for API country codes but not in its bulk feed list; Eventbrite public search is deprecated; PredictHQ needs plan/coverage review.
8. **A narrow owned/open plus permissioned-operator corpus is feasible to test;** usefulness and correction cost remain unproved until R02 and observed users.
9. **Illustrative verification labor can dominate route/API fees.** A controlled 500-record case yields roughly SAR 2,333–7,000 monthly verification labor under explicit assumed rates, before partner, hosting and staff overhead.

# What We Can Safely Use

- **FSQ OS Places** core fields under Apache 2.0 with its NOTICE, license copy and change notices, from the official release channel. [License/notice](https://opensource.foursquare.com/places-notice-txt/)
- **Overture Places** with each record's source license and attribution retained. [Licensing](https://docs.overturemaps.org/attribution/)
- **Wikidata structured data** under CC0, with accuracy checks. [License](https://www.wikidata.org/wiki/Wikidata%3ALicensing)
- **Specific Saudi government datasets published under the Open Data License**, with attribution and media exclusions honored. [National Portal](https://my.gov.sa/content/open-Data)
- **Our original factual verification and operator-supplied records/media** only to the extent direct permission and asset rights are documented.

“Safely” here means **relatively clear rights under the stated conditions**, not guaranteed correctness or no need for legal review of combinations.

# What We Can Use Only Under Restrictions

- **OSM data:** ODbL attribution/share-alike and careful derivative-vs-collective database handling. Public Nominatim/tiles/Overpass have separate usage policies. [OSM license](https://www.openstreetmap.org/copyright)
- **Google Places/Routes:** permitted live uses, ID exceptions, map/attribution rules and narrow caching exceptions; no persistent canonical content index under ordinary terms. [Terms](https://cloud.google.com/maps-platform/terms)
- **Mapbox Geocoding:** permanent mode can store address geocodes; default temporary and Search Box POI results cannot become our corpus. [Geocoding](https://docs.mapbox.com/api/search/geocoding/), [Search Box](https://docs.mapbox.com/api/search/search-box/)
- **Ticketmaster/Eventbrite/PredictHQ:** API-specific plan, retention, link, deletion and territorial conditions; Saudi relevance unproven. [Ticketmaster terms](https://developer.ticketmaster.com/support/terms-of-use/partner/), [Eventbrite terms](https://www.eventbrite.com/help/en-us/articles/833731/eventbrite-api-terms-of-use/), [PredictHQ cache](https://docs.predicthq.com/webapp-support/api-plans-pricing-and-billing/what-are-the-definitions-for-storing-and-caching)
- **Commons images:** only the individual file's license and attribution, with actual depiction checked. [Commons reuse](https://commons.wikimedia.org/wiki/Commons%3AREUSE)

# What Requires Partnership or Licensing

- webook/Enjoy or other ticketing content for systematic event rows, images, status and availability; affiliate access alone is insufficient. [webook terms](https://webook.com/business/en/legal/terms)
- Ithra and other operator program pages/media for repeated use beyond ordinary public viewing; direct structured feeds are preferred. [Ithra terms](https://www.ithra.com/en/terms-conditions)
- Foursquare API rich fields/flat files or Tripadvisor reviews/photos if those become critical to ranking or display; inspect the actual negotiated agreement. [FSQ enterprise data terms](https://foursquare.com/legal/terms/eula/), [Tripadvisor Terra](https://docs.terra.tripadvisor.com/docs/overview)
- Any social creator/post content used as a persistent discovery signal beyond link/lead review.

# What We Should Avoid

- Scraping Google Maps, webook, Enjoy, social platforms or venue pages into a permanent index because the pages are public.
- Copying third-party reviews, photos, descriptions or thumbnails into editorial text or embeddings without derivative rights.
- Treating an API key, affiliate link, JSON-LD, or government website as a reuse license.
- Using FSQ `date_created` as “newly opened,” or `date_refreshed` as proof that hours are current. [FSQ schema](https://docs.foursquare.com/data-products/docs/places-os-data-schema)
- Making a production service depend on public OSM infrastructure or a single paid places/event supplier without an exit path.

# Preferred Initial Source Strategy

**Rights-segregated hybrid, beginning with open/first-party:** FSQ OS and Overture as separately licensed candidate place layers; Wikidata and selected Saudi licensed datasets for stable cultural facts; a small set of permissioned operators and original editorial verification for actionable time/price/booking facts; limited, legally compatible route calls for shortlists. Add an event feed or paid POI enrichment only after R02 demonstrates a specific gap and a contract grants the necessary rights. This strategy is an R02 hypothesis, not a permanent architecture decision.

# Approximate MVP Data Economics

For the **illustrative one-catchment, 500-record, 3,000-search/month** controlled MVP, open-dataset license cost is $0; 24,000 Mapbox matrix elements fall under the published free allowance, while a Google Routes Pro alternative would be about **$190 / SAR 713** before taxes if that SKU and use apply. Initial verification is **66.7 hours**, and illustrative monthly checking is **46.7 hours**, or **SAR 2,333–7,000 / USD 622–1,867** monthly at the explicitly assumed SAR 50–150/hour. These are **not total product costs**: event/feed licenses, photo rights, cloud, maps, staff overhead, legal work and acquisition remain unpriced. Actual cost per feasible choice is an R02/R09 measurement. [Mapbox prices](https://www.mapbox.com/pricing), [Google prices](https://developers.google.com/maps/billing-and-pricing/pricing), [SAMA peg](https://www.sama.gov.sa/en-US/EconomicReports/AnnualReport/Fifty_Eighth_Annual_Report-EN.pdf)

# R01 Decision Gate

### Can we construct a legally defensible test corpus for the R00 content scope? **CONDITIONAL**

**Yes for a bounded corpus of open and explicitly authorized fields** with license notices, field provenance and conservative handling of OSM combinations. The four content families are testable only where direct time/price/booking facts exist; a broad event or availability corpus is not yet licensed or verified. Professional legal review is required for material combination and commercial-display ambiguities.

### Can R02 proceed beyond manual public-page analysis? **CONDITIONAL**

**Yes:** download/query the named open datasets under their licenses, sample OSM within its service policies, obtain explicit operator permission, and run bounded commercial API tests only under the current plan terms. **No** automated retained corpus from restricted pages/APIs. The exact R02 lanes, retention limits and required fields are in Section 38.

### Is a commercial places provider required for the MVP? **NO**

Not on present evidence. FSQ OS/Overture plus operator verification can support a first test. R02 may overturn this if local coverage or identity quality is too poor; a paid API still needs the correct data rights.

### Is a licensed event/feed partner likely required? **UNCLEAR**

Likely **if** promise A includes broad dated events and near-live booking/cancellation status. It may be unnecessary for a narrow operator-led cultural/indoor test. R02 must measure answerable queries and missing status/availability before this becomes a commercial dependency.

**Exact assumptions for R02:** the local near-term outing organizer and domestic visitor remain unvalidated; promises A/B remain tests; all four R00 catchments and four content families remain candidates; “2–3 choices” is provisional; unknown booking/availability is not a positive claim; FSQ OS/Overture rights are distinct from paid APIs; OSM joins remain a legal-review item; no event provider has proven Saudi catchment coverage; route prices are list-price assumptions; editorial time must be measured. R02 should recommend an area/content/promise combination only after counting **rights-clearable, verifiable, feasible options** across the specified time windows.
