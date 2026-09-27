**Working Title:** TBD  
**Document Version:** 0.1  
**Status:** Early Concept / Foundation  
**Primary Purpose:** Define the product vision, underlying discovery system, technical model, MVP boundaries, and major areas requiring further research.

---

# 1. Executive Summary

The proposed product is a **location-aware discovery platform** designed to help users understand what they can do, visit, experience, or discover within a selected geographical area.

The platform combines several types of discovery that are usually fragmented across separate services:

- permanent places;
    
- temporary events;
    
- local businesses;
    
- cultural attractions;
    
- physical activities;
    
- controlled activities and entertainment;
    
- outdoor experiences;
    
- exhibitions;
    
- markets;
    
- openings;
    
- pop-ups;
    
- workshops;
    
- hidden gems;
    
- unusual points of interest;
    
- and eventually user-specific recommendations.
    

The central concept is not merely:

> “What places are near me?”

Instead, the system attempts to answer:

> **“Given where I am, when I am available, what I am interested in, and what is actually available, what could I meaningfully do?”**

The platform therefore combines:

**WHAT × WHERE × WHEN × WHO**

Where:

- **WHAT** = desired experience or intent;
    
- **WHERE** = geographical constraints and travel feasibility;
    
- **WHEN** = opening times, event times, availability, and schedule;
    
- **WHO** = user preferences and context.
    

The long-term product becomes a form of **local intelligence assistant** rather than merely a map or directory.

---

# 2. Problem Statement

Current discovery systems are highly fragmented.

A user looking for something to do may need to search separately through:

- Google Maps;
    
- event platforms;
    
- tourism websites;
    
- social media;
    
- hiking applications;
    
- local guides;
    
- museum websites;
    
- venue websites;
    
- Instagram accounts;
    
- activity-booking platforms;
    
- Reddit;
    
- blogs;
    
- and word-of-mouth recommendations.
    

These systems are generally strong within their individual domains but often weak when the user does not already know **what category of activity they want**.

For example:

> “I have three hours free this afternoon. I want something interesting within 20 minutes of me, preferably indoors, not food, and something I haven't done before.”

This query spans:

- location;
    
- travel time;
    
- schedule;
    
- activity type;
    
- preference;
    
- novelty;
    
- opening hours;
    
- possibly weather;
    
- and potentially ticket availability.
    

Traditional search engines and directory applications are poorly optimized for this kind of request.

---

# 3. Product Vision

Create a system where the user can select any geographical area and quickly answer:

> **What is worth discovering here?**

The user should be able to interact using either:

1. traditional filters; or
    
2. natural-language smart search.
    

The platform should support both spontaneous local discovery and future travel planning.

Over time, it should move from:

**Search → Discovery → Planning → Assistance**

---

# 4. Core Product Principles

## 4.1 Discovery before planning

The system should first help users understand what exists.

Planning should be built on top of high-quality discovery rather than asking AI to create itineraries from incomplete or generic recommendations.

---

## 4.2 Intent before category

Users should not need to know the platform's taxonomy.

A user can search:

> “Something exciting to do with three friends tonight.”

The system translates the intent into structured search parameters.

---

## 4.3 Time is a first-class dimension

An excellent place that is closed is not currently an excellent result.

The system must treat:

- current time;
    
- opening hours;
    
- event dates;
    
- booking windows;
    
- duration;
    
- travel time;
    
- schedule compatibility;
    

as central search dimensions.

---

## 4.4 Geography means more than distance

Five kilometers can mean:

- 6 minutes;
    
- 25 minutes;
    
- inaccessible without a car;
    
- an easy walk;
    
- or geographically nearby but practically inconvenient.
    

Where possible, the platform should evolve from simple radius filtering toward **travel-time awareness**.

---

## 4.5 Popularity should not dominate discovery

The system should avoid continuously recommending only:

- major chains;
    
- famous landmarks;
    
- highly reviewed tourist destinations;
    
- and already-popular venues.
    

Popularity is one ranking signal, not the ranking objective.

---

## 4.6 Freshness must be measurable

Local information becomes stale quickly.

The platform should know:

- when information was last verified;
    
- which source supplied it;
    
- how trustworthy the source is;
    
- whether conflicting data exists;
    
- and how likely the information is to have expired.
    

---

## 4.7 AI assists the system; it does not replace it

LLMs should interpret intent, enrich information, and explain results.

They should not become the primary database or source of truth.

---

# 5. Primary User Modes

The product initially revolves around three major modes.

---

# 5.1 Explore Now

The user is currently located somewhere and wants to discover nearby opportunities.

Example searches:

- What can I do tonight?
    
- Show me interesting things within 15 minutes.
    
- Coffee places worth visiting nearby.
    
- Something active but indoors.
    
- Free activities this weekend.
    
- Anything unusual around me?
    
- Interesting places open after 10 PM.
    
- Things I can do alone.
    
- Somewhere quiet for two hours.
    
- Newly opened businesses nearby.
    

Primary variables:

- location;
    
- time;
    
- available duration;
    
- travel distance/time;
    
- activity intent;
    
- environment;
    
- price.
    

---

# 5.2 Explore Destination

The user is researching another city or country before arriving.

Example:

> “I'm visiting Istanbul for five days. Show me interesting places around the neighborhoods I'm staying in.”

The user may browse:

- permanent attractions;
    
- restaurants;
    
- coffee;
    
- markets;
    
- shops;
    
- activities;
    
- exhibitions;
    
- upcoming events;
    
- seasonal opportunities;
    
- outdoor experiences.
    

Interesting results can be saved before an itinerary exists.

The system therefore supports **discovery-led trip planning**.

---

# 5.3 Plan & Follow

The user has saved places, events, reservations, or destinations.

The system helps organize them into a practical schedule.

Eventually it can identify gaps and opportunities.

Example:

> You are travelling from Location A to Location B tomorrow morning.

The platform may determine:

- the user has 90 free minutes;
    
- a saved place opens at 10:30;
    
- it lies near the planned route;
    
- the average visit duration is approximately 45 minutes;
    
- visiting it will not interfere with the next scheduled activity.
    

The system can suggest inserting the visit.

---

# 6. Core Domain Model

The system should not model everything as a generic “place.”

Several primary object types are required.

---

## 6.1 Place

A persistent physical location.

Examples:

- café;
    
- restaurant;
    
- museum;
    
- gallery;
    
- shop;
    
- landmark;
    
- park;
    
- cultural center;
    
- bookstore.
    

---

## 6.2 Event

A time-bound occurrence.

Examples:

- concert;
    
- exhibition opening;
    
- festival;
    
- market;
    
- conference;
    
- performance;
    
- community gathering.
    

Events contain:

- start time;
    
- end time;
    
- recurrence;
    
- venue;
    
- ticket information;
    
- availability;
    
- event status.
    

---

## 6.3 Activity

An experience performed at a location.

Examples:

- karting;
    
- paintball;
    
- bowling;
    
- escape room;
    
- pottery workshop;
    
- cooking class;
    
- horse riding.
    

A venue may contain multiple activities.

---

## 6.4 Outdoor Experience

A location or route-based activity.

Examples:

- hiking;
    
- climbing;
    
- camping;
    
- cycling;
    
- beach activities;
    
- viewpoints;
    
- nature walks.
    

These may require additional metadata such as:

- difficulty;
    
- distance;
    
- duration;
    
- elevation;
    
- weather suitability;
    
- equipment;
    
- accessibility.
    

---

## 6.5 Route

A geographical path.

Examples:

- hiking trail;
    
- walking tour;
    
- cycling route;
    
- scenic drive.
    

---

## 6.6 Temporary Place

A location that operates for a limited period.

Examples:

- pop-up shop;
    
- seasonal market;
    
- Ramadan market;
    
- temporary exhibition space;
    
- festival village.
    

---

## 6.7 Experience

A broader bookable or curated experience.

Examples:

- guided city tour;
    
- food tasting;
    
- photography walk;
    
- cultural experience;
    
- desert tour.
    

---

## 6.8 Collection

A curated set of discovery objects.

Examples:

- Best independent coffee shops in Al Khobar.
    
- Interesting architecture in Riyadh.
    
- Quiet places for studying.
    
- Unusual museums in Tokyo.
    
- Family activities for the weekend.
    

Collections may eventually be created by:

- the platform;
    
- users;
    
- local experts;
    
- organizations;
    
- businesses.
    

---

# 7. Taxonomy

The platform requires a controlled internal taxonomy while still allowing flexible natural-language search.

Initial top-level taxonomy:

## Food & Drink

- Coffee
    
- Restaurants
    
- Bakeries
    
- Desserts
    
- Specialty food
    
- Markets
    
- Food experiences
    

## Culture

- Museums
    
- Galleries
    
- Exhibitions
    
- Heritage
    
- Historical locations
    
- Architecture
    
- Cultural centers
    

## Entertainment

- Cinema
    
- Theatre
    
- Concerts
    
- Comedy
    
- Festivals
    
- Live performances
    
- Gaming
    

## Activities

- Karting
    
- Paintball
    
- Escape rooms
    
- Bowling
    
- Workshops
    
- Horse riding
    
- Diving
    
- Sports facilities
    

## Outdoors

- Hiking
    
- Camping
    
- Beaches
    
- Parks
    
- Cycling
    
- Climbing
    
- Viewpoints
    
- Nature
    

## Shopping & Local

- Independent shops
    
- Crafts
    
- Bookstores
    
- Markets
    
- Vintage
    
- Specialty shops
    
- Pop-ups
    

## Interesting Places

- Hidden gems
    
- Unusual architecture
    
- Scenic locations
    
- Photography locations
    
- Curiosities
    
- Local discoveries
    

The taxonomy should eventually support hierarchical and multi-category classification.

A location can therefore be:

```
Coffee
Specialty Coffee
Independent
Quiet
Work Friendly
Architecture
Hidden Gem
```

simultaneously.

---

# 8. Discovery Filters

The filtering system should go considerably beyond standard price/rating filters.

Possible filters include:

### Time

- Open now
    
- Today
    
- Tonight
    
- Tomorrow
    
- This weekend
    
- Custom dates
    
- Starts soon
    

### Geography

- Radius
    
- Travel time
    
- Walking time
    
- Driving time
    
- Along route
    
- Near destination
    

### Cost

- Free
    
- Budget
    
- Moderate
    
- Premium
    
- Custom price
    

### Environment

- Indoor
    
- Outdoor
    
- Mixed
    
- Weather-dependent
    

### Duration

- Under 30 minutes
    
- Under 1 hour
    
- 1–2 hours
    
- Half-day
    
- Full-day
    

### Social context

- Solo
    
- Couple
    
- Friends
    
- Family
    
- Large group
    

### Experience properties

- Relaxing
    
- Physical
    
- Educational
    
- Cultural
    
- Social
    
- Adventurous
    
- Quiet
    
- Scenic
    
- Creative
    

### Discovery

- Famous
    
- Balanced
    
- Local
    
- Hidden
    
- Newly opened
    
- Trending
    

### Practical

- Reservation required
    
- Walk-in available
    
- Accessible
    
- Parking available
    
- Family suitable
    

---

# 9. Smart Search

Smart search should convert natural-language intent into structured search constraints.

Example input:

> “I have about two hours tonight and want something fun with my brother, no restaurants, within 20 minutes.”

Possible interpretation:

```
{
  "location": "current",
  "date_range": "tonight",
  "max_duration_minutes": 120,
  "max_travel_minutes": 20,
  "party_size": 2,
  "exclude_categories": ["restaurant", "food"],
  "intent": ["fun", "activity", "entertainment"]
}
```

The LLM's role is primarily **query interpretation**.

The structured query is then processed by the discovery engine.

---

# 10. Search Architecture

The discovery engine should use **hybrid retrieval**.

Four primary search mechanisms:

## 10.1 Structured Search

For deterministic constraints:

- opening hours;
    
- event dates;
    
- price;
    
- categories;
    
- accessibility;
    
- indoor/outdoor.
    

---

## 10.2 Geographic Search

For:

- radius;
    
- bounding areas;
    
- travel distance;
    
- near-route searches;
    
- neighborhood searches.
    

PostGIS is a likely early technical foundation.

---

## 10.3 Keyword Search

For exact information such as:

- names;
    
- categories;
    
- venue descriptions;
    
- event titles.
    

---

## 10.4 Semantic Search

Used when users express meaning rather than exact keywords.

Examples:

> “Romantic but not too formal.”

> “Something unusual.”

> “Good place to think.”

> “Activity that feels adventurous without being extreme.”

Vector embeddings can help retrieve relevant candidates.

---

# 11. Search Pipeline

```
User Query
     │
     ▼
Intent Interpreter
     │
     ▼
Structured Search Request
     │
     ├── Geo constraints
     ├── Time constraints
     ├── Category constraints
     ├── Semantic intent
     ├── Price constraints
     └── User context
     │
     ▼
Candidate Retrieval
     │
     ├── SQL filters
     ├── Full-text retrieval
     ├── Vector retrieval
     └── Geographic retrieval
     │
     ▼
Candidate Pool
     │
     ▼
Ranking Engine
     │
     ▼
Diversity Layer
     │
     ▼
Quality / Freshness Layer
     │
     ▼
Final Results
```

---

# 12. Ranking Engine

Retrieving valid results is not sufficient.

The system must determine which ones deserve to appear first.

Initial conceptual ranking inputs:

```
Query relevance
Semantic relevance
Geographic convenience
Travel time
Opening-hour compatibility
Event timing
Quality
Freshness
Data confidence
Uniqueness
Popularity
Personal preferences
Novelty
Schedule compatibility
```

A conceptual score could eventually resemble:

```
FinalScore =
    relevance
  + time_fit
  + geo_fit
  + quality
  + freshness
  + uniqueness
  + preference_fit
  - inconvenience
```

The actual model should eventually be learned and tested rather than permanently hand-coded.

---

# 13. Discovery / Hidden-Gem Logic

Traditional discovery systems often reward popularity so strongly that the same famous locations repeatedly dominate results.

This platform should explicitly model **discoverability** separately from quality.

Possible internal signals:

- number of reviews;
    
- rate of review growth;
    
- independence vs chain;
    
- uniqueness of category;
    
- uniqueness within geographic area;
    
- local mentions;
    
- recent opening;
    
- editorial curation;
    
- user saves;
    
- repeat recommendations;
    
- novelty relative to user history.
    

This can produce a conceptual:

**Discovery Score**

which may be separate from:

**Quality Score**

A place may therefore have:

```
Quality:       High
Popularity:    Low
Uniqueness:    High
Confidence:    High
Discovery:     Very High
```

This could make it an excellent recommendation despite modest public visibility.

---

# 14. Diversity Layer

Without a diversity mechanism, the top 20 search results may all be nearly identical.

Example:

> “Things to do tonight.”

Raw ranking may return:

1. escape room
    
2. escape room
    
3. escape room
    
4. bowling
    
5. escape room
    
6. escape room
    

The diversity layer can intentionally provide broader discovery:

- karting;
    
- gallery;
    
- escape room;
    
- live performance;
    
- workshop;
    
- bowling;
    
- unusual café;
    
- local market.
    

Diversity therefore becomes an explicit system objective.

---

# 15. Data Platform

The platform's largest long-term technical challenge is likely to be its data system rather than the AI model.

The product may ultimately consume information from:

- commercial places APIs;
    
- map data;
    
- tourism sources;
    
- ticketing systems;
    
- event aggregators;
    
- municipal/open data;
    
- venue websites;
    
- business websites;
    
- social media;
    
- partners;
    
- local organizations;
    
- user submissions;
    
- community contributors;
    
- internal editorial research.
    

Conceptual pipeline:

```
External Sources
       │
       ▼
Data Connectors
       │
       ▼
Raw Ingestion
       │
       ▼
Normalization
       │
       ▼
Entity Resolution
       │
       ▼
Deduplication
       │
       ▼
Enrichment
       │
       ▼
Validation
       │
       ▼
Canonical Database
       │
       ▼
Search Index
```

---

# 16. Canonical Entity Model

Different sources may describe the same entity differently.

Example:

```
Google:
ABC Coffee Roasters

Source B:
ABC Roastery

Source C:
ABC Coffee - Downtown
```

The system should create one canonical internal identity:

```
place_id: plc_001827

canonical_name
aliases[]

coordinates
address

categories[]
tags[]

opening_hours

phone
website

price_range

source_ids {
    google
    foursquare
    osm
    internal
}

photos[]

quality_score
discovery_score

source_confidence
last_verified_at
```

This entity-resolution layer will become an important long-term asset.

---

# 17. Provenance

The system should know **where every important fact came from**.

Example:

```
Opening Hours

Google       → 09:00–23:00
Website      → 09:00–00:00
User report  → closes at 23:30
```

The platform can then reason about:

- source authority;
    
- update recency;
    
- conflicts;
    
- confidence.
    

AI-generated information should never silently overwrite source data.

---

# 18. Freshness Model

Every dynamic fact should carry metadata.

Example:

```
value:
source:
retrieved_at:
verified_at:
confidence:
expected_expiry:
```

Different data types decay differently.

Examples:

### Geographic coordinates

Very slow decay.

### Phone number

Moderate decay.

### Opening hours

Moderate/high decay.

### Event availability

Extremely high decay.

### Pop-up location

Extremely high decay.

Freshness policy should eventually depend on the field type.

---

# 19. Confidence Model

The platform should internally assign confidence to information.

For example:

```
Place exists          0.99
Coordinates           0.99
Category              0.94
Opening hours         0.78
Price range           0.65
Currently operating   0.86
```

Confidence can influence:

- ranking;
    
- UI warnings;
    
- refresh priority;
    
- verification jobs.
    

---

# 20. Planner

The planner should be treated as a separate system consuming the Discovery Engine.

It should not simply ask an LLM to write an itinerary.

Inputs include:

- user schedule;
    
- saved places;
    
- travel times;
    
- reservations;
    
- event start/end times;
    
- opening hours;
    
- expected activity duration;
    
- preferred pace;
    
- geographical routing;
    
- buffer times.
    

Example:

```
Hotel
09:00

Lunch
12:30

Available Window:
09:00–12:30
```

Possible candidate:

```
Travel to museum      18 min
Visit museum          60 min
Travel to lunch       22 min
Buffer                 20 min
```

The planner can determine mathematically whether the activity fits.

---

# 21. Flexible vs Fixed Schedule Items

Planner objects should distinguish between:

## Fixed

- flight;
    
- reservation;
    
- concert;
    
- appointment;
    
- scheduled event.
    

## Flexible

- coffee;
    
- museum;
    
- shopping;
    
- viewpoint;
    
- walk.
    

The planner should schedule flexible activities around fixed commitments.

---

# 22. Smart Suggestions

Once discovery and scheduling systems exist, proactive recommendations become possible.

Examples:

## Schedule opportunity

> You have 90 minutes available tomorrow near this museum.

## Route opportunity

> One of your saved shops is only five minutes from tomorrow's route.

## New event

> A temporary exhibition was announced during the dates of your trip.

## Limited availability

> The workshop you saved has only two sessions during your visit.

## Opening-hours optimization

> This market is only open Thursday–Saturday.

## Weather response

> Tomorrow's outdoor plan may be affected by the weather. These indoor alternatives are nearby.

---

# 23. Notifications

Notifications should be highly controlled.

Potential notification categories:

- saved event reminder;
    
- event changes;
    
- new event matching interests;
    
- newly opened nearby place;
    
- availability alert;
    
- route opportunity;
    
- trip suggestion;
    
- closure warning;
    
- weather conflict.
    

Users should control:

- categories;
    
- frequency;
    
- geographical zones;
    
- quiet hours;
    
- trip-specific notifications.
    

Avoid notification spam.

---

# 24. Personalization

Personalization should initially rely more on explicit signals than opaque behavioral profiling.

Possible explicit signals:

- likes;
    
- dislikes;
    
- saved places;
    
- visited places;
    
- selected categories;
    
- preferred price range;
    
- travel tolerance;
    
- indoor/outdoor preference.
    

Later behavioral signals may include:

- searches;
    
- clicks;
    
- saves;
    
- dismissals;
    
- dwell time;
    
- repeated categories.
    

The recommendation system should distinguish:

> “This user likes coffee”

from:

> “This user wants coffee right now.”

Short-term intent should often override long-term preference.

---

# 25. User Context

Possible future context object:

```
Current location
Trip location

Current date/time

Available duration

Transportation:
- walking
- car
- transit

Party:
- solo
- couple
- friends
- family

Preferences

Saved items

Schedule

Weather

Budget
```

Context should only be used where appropriate and with clear privacy controls.

---

# 26. High-Level System Architecture

```
                 CLIENT APPLICATION
                        │
                        ▼
                   API GATEWAY
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
     DISCOVERY SERVICE        USER SERVICE
            │
     ┌──────┼────────┐
     │      │        │
     ▼      ▼        ▼
   Search  Ranking  Intent
                  Interpreter
     │
     ▼
CANONICAL DATA PLATFORM
     │
     ├── Places
     ├── Events
     ├── Activities
     ├── Routes
     ├── Experiences
     └── Collections
     │
     ▼
PostgreSQL / PostGIS
     │
     ├── Full Text
     ├── Vector Search
     └── Geo Search


DATA PIPELINE

Sources
   │
   ▼
Connectors
   │
   ▼
Ingestion
   │
   ▼
Normalization
   │
   ▼
Entity Resolution
   │
   ▼
Validation
   │
   ▼
Canonical Database


LATER SYSTEMS

Planner
Recommendation Engine
Notification Engine
Personalization
User Contributions
Moderation
Analytics
```

---

# 27. Early Technical Direction

A practical early stack could be:

## Frontend

Potentially:

- Next.js;
    
- React;
    
- TypeScript.
    

---

## Backend / Database

Potentially:

- PostgreSQL;
    
- PostGIS;
    
- pgvector;
    
- PostgreSQL Full Text Search.
    

A platform such as Supabase could simplify the initial implementation while preserving PostgreSQL underneath.

---

## Search

Initial:

```
PostgreSQL
+ PostGIS
+ Full Text Search
+ pgvector
```

Later, depending on scale:

- Elasticsearch;
    
- OpenSearch;
    
- Typesense;
    
- another dedicated retrieval platform.
    

A dedicated search engine should only be introduced when justified by scale or product needs.

---

## AI

Possible responsibilities:

- natural-language query parsing;
    
- taxonomy classification;
    
- tag generation;
    
- entity-description enrichment;
    
- duplicate assistance;
    
- recommendation explanation;
    
- trip-planning interface.
    

AI should not be the authority for:

- opening hours;
    
- event dates;
    
- prices;
    
- addresses;
    
- availability;
    
- existence of locations.
    

---

# 28. API / Source Strategy

The platform should not become dependent on one external data provider.

An abstraction layer should separate:

```
Provider Data
```

from:

```
Internal Canonical Data
```

Therefore:

```
Source Adapter
      ↓
Internal Schema
```

rather than letting provider-specific structures leak throughout the application.

This allows providers to be:

- replaced;
    
- combined;
    
- disabled;
    
- reprioritized.
    

---

# 29. Source Rights and Licensing

Every data source should eventually be documented with:

- permitted usage;
    
- storage limitations;
    
- caching rules;
    
- attribution requirements;
    
- redistribution restrictions;
    
- API cost;
    
- request limits;
    
- commercial-use rules.
    

This is an architectural concern, not merely a legal task.

Some providers may allow retrieval but prohibit permanently rebuilding their database.

The internal data strategy must account for this from the beginning.

---

# 30. MVP Philosophy

The MVP should not attempt to prove every part of the long-term vision.

Its primary question should be:

> **Can we provide meaningfully better local discovery than existing generic search methods?**

Everything else depends on that.

---

# 31. MVP v0 — Discovery Prototype

Recommended initial scope:

### Geographic scope

One city or limited geographic region.

### Content

- places;
    
- events;
    
- activities;
    
- selected outdoor experiences.
    

### Interface

- map;
    
- results list;
    
- filters;
    
- search bar;
    
- smart natural-language search.
    

### Initial categories

Approximately 6–10 primary categories.

### Features

- location selection;
    
- nearby search;
    
- date/time filtering;
    
- category filtering;
    
- open-now filtering;
    
- basic semantic search;
    
- save item;
    
- result details.
    

---

# 32. MVP Smart Queries

The prototype should be capable of handling realistic queries such as:

> Something interesting tonight.

> Good coffee within 15 minutes.

> Physical activities indoors.

> Free things this weekend.

> Hidden places around here.

> Something for three friends.

> Interesting cultural places open now.

> Something unusual that takes less than two hours.

These queries should become benchmark tests.

---

# 33. MVP Non-Goals

Do NOT initially build:

- complete global coverage;
    
- automatic itinerary generation;
    
- complex personalization;
    
- social network;
    
- full user contribution system;
    
- automatic booking;
    
- AI travel concierge;
    
- advanced route optimization;
    
- every possible category;
    
- business owner dashboards;
    
- complex notification system.
    

These belong to later phases.

---

# 34. Success Metrics

Early metrics should measure discovery quality rather than raw traffic.

Potential measurements:

## Search success

Percentage of searches where the user finds at least one useful result.

## Save rate

How often results are saved.

## Discovery depth

How often users view results beyond already-famous locations.

## Query reformulation

How often the user must repeatedly change the query.

## Result diversity

How varied useful recommendations are.

## Data accuracy

Frequency of:

- closed venues;
    
- incorrect hours;
    
- expired events;
    
- duplicates.
    

## Search latency

Discovery should feel immediate even when ranking is sophisticated.

---

# 35. Core Technical Risks

## Risk 1 — Data quality

Bad data creates bad recommendations regardless of AI quality.

---

## Risk 2 — Data coverage

Some cities may have excellent structured data.

Others may have extremely fragmented information.

---

## Risk 3 — Duplicate entities

Multiple sources may represent the same physical place differently.

---

## Risk 4 — Stale information

Local data changes constantly.

---

## Risk 5 — API dependence

External pricing, limits, or terms can change.

---

## Risk 6 — Search quality

Semantic search may produce conceptually related but practically incorrect results.

---

## Risk 7 — Recommendation homogenization

Popularity signals can cause famous locations to dominate.

---

## Risk 8 — AI hallucination

The AI interface may describe facts not supported by verified sources.

---

## Risk 9 — Cost

Large-scale:

- APIs;
    
- embeddings;
    
- maps;
    
- geocoding;
    
- routing;
    
- search infrastructure;
    

can become expensive.

---

# 36. Product Risks

## Cold-start problem

A discovery platform with poor geographic coverage feels empty.

A focused launch geography may therefore be preferable to broad but shallow coverage.

---

## User trust

One recommendation sending the user to a permanently closed venue can damage trust significantly.

---

## Information overload

The objective is not to expose every possible location.

The objective is to surface a manageable set of good possibilities.

---

# 37. Potential Competitive Advantage

The primary moat should not initially be considered the UI or the AI chatbot.

Potential long-term defensibility comes from:

1. **canonical local dataset;**
    
2. **entity-resolution system;**
    
3. **freshness intelligence;**
    
4. **discovery taxonomy;**
    
5. **ranking system;**
    
6. **hidden-gem identification;**
    
7. **user preference data;**
    
8. **schedule-aware recommendations;**
    
9. **local partnerships and unique sources.**
    

The product becomes stronger as its understanding of a geographic area improves.

---

# 38. Long-Term Product Evolution

Possible evolution:

## Version 0

Discovery prototype.

## Version 1

Reliable local discovery engine.

## Version 2

Accounts, saving, collections, preferences.

## Version 3

Trip planning.

## Version 4

Schedule-aware recommendations.

## Version 5

Notifications and monitoring.

## Version 6

Personalized discovery engine.

## Version 7+

Community contributions, local experts, booking, partnerships, business tools, deeper local intelligence.

Exact version boundaries should remain flexible.

---

# 39. Research Areas Required Before Architecture Lock-In

Several topics deserve dedicated research.

## R01 — Local Discovery Data Sources

Research:

- places providers;
    
- events providers;
    
- outdoor data;
    
- municipal data;
    
- tourism APIs;
    
- social/local sources;
    
- costs;
    
- rights;
    
- coverage.
    

---

## R02 — Canonical Data & Entity Resolution

Research:

- duplicate detection;
    
- entity matching;
    
- source provenance;
    
- merge strategies;
    
- conflict resolution.
    

---

## R03 — Search Architecture

Research:

- PostgreSQL hybrid search;
    
- pgvector;
    
- PostGIS;
    
- Elasticsearch/OpenSearch;
    
- Typesense;
    
- ranking pipelines;
    
- latency.
    

---

## R04 — Discovery Ranking

Research:

- recommendation ranking;
    
- diversity;
    
- novelty;
    
- popularity bias;
    
- hidden-gem identification.
    

---

## R05 — Freshness & Verification

Research:

- data decay;
    
- stale-record detection;
    
- verification systems;
    
- confidence models;
    
- source authority.
    

---

## R06 — Smart Query Understanding

Research:

- intent extraction;
    
- structured-output schemas;
    
- LLM query parsing;
    
- deterministic fallback;
    
- ambiguous queries.
    

---

## R07 — Planner & Constraint Solver

Research:

- temporal scheduling;
    
- travel-time matrices;
    
- route planning;
    
- constraint optimization;
    
- flexible itinerary generation.
    

---

## R08 — Data Licensing & Economics

Research:

- API pricing;
    
- storage rights;
    
- redistribution rights;
    
- caching;
    
- commercial terms;
    
- cost per active user.
    

---

# 40. Major Open Product Decisions

These should not be rushed.

### Geographic starting point

Do we begin with:

- one Saudi city;
    
- several Saudi cities;
    
- Saudi Arabia;
    
- another test market?
    

---

### Target user

Do we initially optimize for:

- locals;
    
- domestic tourists;
    
- international tourists;
    
- everyone?
    

---

### Primary use case

Which initially receives highest priority?

- spontaneous nearby discovery;
    
- event discovery;
    
- travel research;
    
- hidden gems;
    
- planning.
    

---

### Initial data strategy

Do we:

- aggregate APIs;
    
- curate ourselves;
    
- combine both?
    

---

### Business model

Future possibilities include:

- subscriptions;
    
- affiliate bookings;
    
- promoted discovery;
    
- tourism partnerships;
    
- business tools;
    
- premium trip planning.
    

No model needs to be selected yet.

---

# 41. Working Product Statement

> **A location-aware discovery platform that helps people understand what they can do, visit, and experience around any selected area by combining places, events, activities, time, geography, and personal intent into a single intelligent search system.**

Longer-term:

> **The platform evolves from helping users discover what exists into helping them decide what fits, plan around it, and discover relevant opportunities as their location and schedule change.**

---

# 42. Core System Thesis

The product should not be designed primarily as:

> a map application with AI.

Nor as:

> an AI travel planner.

The stronger technical model is:

> **A spatiotemporal discovery engine with planning and intelligent assistance built on top.**

Its foundation is therefore:

```
DATA
  ↓
UNDERSTANDING
  ↓
RETRIEVAL
  ↓
RANKING
  ↓
DISCOVERY
  ↓
PLANNING
  ↓
ASSISTANCE
```

If the first five layers are strong, AI can substantially improve the experience.

If those layers are weak, AI will merely provide a polished interface over unreliable recommendations.

---

# 43. v0.1 Conclusion

The strongest part of this concept is not any single feature.

It is the decision to create a common intelligence layer across types of local experiences that currently live in different ecosystems.

The project's most important early problems are therefore:

1. acquiring useful local data;
    
2. converting that data into a canonical model;
    
3. understanding natural-language intent;
    
4. performing geographical and temporal retrieval;
    
5. ranking for usefulness rather than popularity alone;
    
6. maintaining freshness and trust;
    
7. proving that users can genuinely discover things they would otherwise have missed.
    

The planner, proactive suggestions, notifications, and personalization should then be constructed on top of this foundation.

**End of Product & Technical Concept v0.1**