# R03: Domain and identity model (provisional, conceptual)

**Date:** 27 September 2026
**Inputs:** [v0.2 §5 and §12](Product_Technical_Concept_Architecture_Review_v0.2.md#5-domain-model), [R01 §25 and §37](R01_Source_Rights_and_Economics.md#37-architecture-consequences), [R01.2 §17](R01.2_Automation_First_Data_Strategy_and_Architecture_Correction.md), [R02 §9](R02_Automated_Coverage_and_Feasibility_Audit.md#9-identity-category-and-location-diagnostics), [R02.1 §5–6](R02_1_Practical_Data_Feasibility_Followup.md#6-candidate-supply-and-identity-measured-in-the-retained-eastern-extract)
**Status:** Provisional. This is a conceptual model built from the actual cases. **It is not a database schema, migration or API.** The practical-data source dependency is still unresolved (R02.1), so the model must not assume any particular feed shape.

## 1. Design goals, derived from observed failures

| Observed failure | Goal |
|---|---|
| Three Scitech records up to 4 km apart, including the dome typed as a cinema (R02.1 §6) | One real destination may have several source records, and a sub-offering is not a separate venue. Location disagreement must be visible. |
| A Riyadh room page with a Khobar footer, and Khobar-specific room URLs for the same room name (R02 §12, R02.1 §5) | The same offering name at two branches is two offerings. Facts attach to the branch-specific offering. |
| Ithra: four sub-venues within 100 m, a copy 0.5 km away, an AllThePlaces record 3 km away, and a chocolatier named "Legend Ithra" (R02.1 §6) | Parent/child containment. Name similarity is never sufficient on its own. |
| Two Escape The Room Khobar records 9 km apart (R02.1 §6) | "Same brand, same city" must stay undecided without branch evidence. |
| Nasseef House: Arabic/English variants and another museum record several hundred metres away (R02 §9) | Multilingual names as sets. No merge on translation alone. |
| At-Turaif English record carries a third-party tour-guide URL (R02 §9) | A website on a source record is a claim with provenance, not an identity key. |
| JAX: district access ≠ studio access (R02 §11) | Access rules attach to the specific site or offering, not to the container. |
| Bujairi under `shopping`, muvi under `shopping_mall` (R02 §9) | Category is a claim that can conflict with the name. It must not hide an entity. |
| "Not the mall" had no data relation (R02.1 case C06) | Containment ("inside a mall") must be representable. |

## 2. Concepts

Only concepts required by the actual cases are included.

| Concept | Meaning | Needed by |
|---|---|---|
| **Site** | A physical destination a person can go to: a branch, a museum building, a gallery, a park, a district. A branch is its own site. A site may be **contained in** another site. | All place cases. Scitech, Ithra sub-venues, Escape The Room branch. |
| **Access point** | A specific entrance, gate or meeting point used for travel and arrival. A site may have several. It is **not** the source record's point. | C03 and C12 travel. Ithra's two entrances (index evidence). Diriyah diversions (R02 §16). |
| **Operator** | The organisation that runs sites or offerings: a museum authority, a chain, an organiser. A chain is an operator with many branch sites. | Escape The Room group, Ithra, Scitech's operating body. |
| **Offering** | A repeatable thing to do, with its own practical facts: gallery admission, IMAX film admission, an escape room at a branch, a workshop type. It is offered **at** one site (per-branch instance) or at a series of meeting points. | Scitech halls/dome/IMAX prices. "The Prison" at Khobar vs Riyadh. |
| **Programme / series** | A named, dated grouping: an exhibition run, a festival, a season, a recurring market. It has a validity interval. It can span several sites. | C07, C09. Riyadh Season, Ithra programme. |
| **Occurrence / session** | One dated instance with a start and end, a status, and possibly capacity: a show time, a workshop slot, a market day, a tour departure. It happens **at** a site or access point. | IMAX show times, escape-room slots, workshop sessions. |
| **Source record** | One provider's record as received: an Overture ID, an FSQ ID, an OSM element, an operator page URL, a feed item. **It is never edited or deleted by identity decisions.** | All 13,764 R02 records. |
| **Claim** | One assertion about one field of one concept, with provenance, observation time, valid time, rights and state. See [R04](R04_Trust_and_Freshness_Policy.md). | Hours, prices, age rules, accessibility, category, website, location. |
| **Identity link** | A reversible, evidenced decision relating source records to a concept: *describes*, *same as*, *different from*, *contained in*, *branch of*, *successor of*, *undecided*. | Merge/split handling. |
| **Discovery item** | What a result shows: a site, offering or occurrence in a query context. It is not stored identity; it is derived. | Prevents a venue and its workshop appearing as unhelpful duplicates. |

Deliberately **not** separate concepts: "outdoor experience" (an attribute and a geometry), "temporary place" (a site with a validity interval), "experience" (too broad), and "collection" (a content layer). These follow v0.2 §5.

## 3. Relationships

```text
Operator ──operates──▶ Site ──contained_in──▶ Site (complex / district / mall)
   │                     │
   └──offers──▶ Offering ─offered_at─▶ Site | Access point
                   │
Programme ─includes─▶ Offering / Occurrence
                   │
Occurrence ─instance_of─▶ Offering | Programme ; ─occurs_at─▶ Site | Access point
Source record ─describes (identity link)─▶ Site | Offering | Occurrence | Operator
Claim ─about─▶ (any concept, field) ; ─from─▶ Source record | Source page | Agreement
```

All relationships carry validity intervals. A pop-up can be `contained_in` a café from date A to date B. An operator change is recorded as `successor_of`.

## 4. Hard cases resolved conceptually

| Case | Model |
|---|---|
| **Museum and exhibition** | The museum is a site. Each exhibition is a programme with a run interval, offered at that site. Timed admissions are occurrences. "Museum open" does not imply "exhibition running" (C07). |
| **Several activities in one venue** (Scitech halls, dome, IMAX) | One site with several offerings, each with its own price and schedule claims. The two "Science Dome" records **describe the dome offering or a contained site**. They are not separate destinations and never supply the complex's location. |
| **Complex with sub-venues** (Ithra) | Complex site → contained sites (Museum Galleries, Children's Museum, Theatre). Centre-level claims such as "wheelchair assistance at information desks" attach to the complex and are **inherited only as qualified claims** by contained sites (R04 §6). |
| **Chain with branches** (Escape The Room) | Operator → branch sites (Khobar, Riyadh). Offering "The Prison" exists **per branch**. Facts from `/rooms/the-prison-khobar/` attach only to the Khobar offering. A page mixing branch cues creates a **conflict claim**, not a Khobar fact. |
| **Separate nearby branches** (two cafés of one chain 300 m apart) | Two sites. Cannot-merge (§5). They share operator-level claims (brand, website) but not hours or location. |
| **District vs tenant** (Boulevard, JAX, Bujairi) | The district is a site with its own access hours. Tenants are contained sites with their own hours and access rules. District hours never validate tenant hours (R02 Q15). |
| **Festival** (Riyadh Season) | A programme with a season interval, including many occurrences at several sites and zones. Not a point. Not a single venue. |
| **Seasonal market** | A recurring programme with occurrences (market days) at a site or area. Create a separate site only if the market has its own temporary facility. |
| **Pop-up** | An offering (or temporary site) `contained_in` a host site, with a validity interval. Never merged with the host. |
| **Changing meeting points** (guided tours) | Offering with occurrences, each having its own access point. The offering has no fixed location. |
| **Mall containment** (C06 "not the mall") | Cinema, arcade or play centre `contained_in` a mall site. The exclusion evaluates containment. A missing containment link means **unknown**, not "not in a mall". |
| **Multilingual names** (Nasseef/Nassif/بيت آل نصيف) | A name set of (text, language, script, source) entries. Transliteration variants are **candidate evidence** for "same as", never the decision on their own. |

## 5. Identity decisions

### Principles

1. **Source records are immutable.** Identity is a separate, versioned layer of links. Splitting a wrong merge restores the prior links; no source data is lost.
2. **Every link records** its type, evidence (signals and values), decider (rule or person), time, and confidence tier. Links can be superseded, never silently edited.
3. **Default to undecided.** An undecided pair is shown as separate candidates with a duplicate warning suppressed only in presentation. Facts never flow across an undecided link.
4. **Facts flow only across `same as` and, in qualified form, across `contained_in`** (R04 §6). They never flow across `branch of`, `different from` or `undecided`.

### Signals (evidence, not rules)

Useful signals: distance between points; normalised and transliterated name similarity; category agreement; shared operator-specific URL path (not just the domain); phone; branch identifiers on operator pages; containment evidence such as a mall name in the address; provider cross-references (Overture sources, Wikidata IDs).

Weak or misleading signals, shown by R02 and R02.1:
- **Website domain.** Chains share it, and link aggregators appear (`linktr.ee`, `reach.link`).
- **Source confidence.** It is constant per source (Foursquare 0.77).
- **Category.** The dome is typed as a cinema, and 81 of 85 nearby `historic_site` records are not heritage sites.
- **Exact same name.** There were zero exact-name pairs among 1,387 close pairs, so real duplicates differ in name.

### Dangerous merges: cannot-merge without explicit branch evidence

| Pattern | Why dangerous | Example |
|---|---|---|
| Same brand, different locations | Wrong-branch hours or travel | Escape The Room records 9 km apart. Chain cafés. |
| Parent complex and contained venue | Children's Museum hours differ from the centre (closes two hours earlier per index evidence) | Ithra complex vs Children's Museum |
| District and tenant | District open ≠ tenant open | Boulevard district vs café inside |
| Host and pop-up | The pop-up expires, the host does not | Any pop-up in a café or bookstore |
| Offering and site | Price and schedule differ | Scitech dome vs Scitech halls |
| Name collision on a landmark | A different business borrowing a landmark name | "Legend Ithra" chocolatier, "Dunkin … ithra Knowledge Program" |
| Same offering name at two branches | A room page's duration or price attached to the wrong city | "The Prison" at Riyadh vs Khobar |

### Reversible actions

| Action | Effect | Reverse |
|---|---|---|
| Link `describes` record → concept | The record's claims become candidate claims for that concept | Unlink. Claims revert to the record only. |
| Mark `same as` (two records, one concept) | Claims pooled, conflicts surfaced (R04) | Split. Each record's claims return to separate concepts. |
| Mark `contained_in` | Qualified inheritance of parent claims | Remove. Inherited claims disappear. |
| Mark `different from` | Blocks future automated merges | Remove, with review |
| Mark location conflict | Travel claims for the concept become unknown until an access point is confirmed | Resolve by selecting or confirming an access point |

**Location conflict trigger (provisional):** records linked to one concept whose points are farther apart than the concept type plausibly spans. For a single building a few hundred metres is suspect; Scitech's 1.4–4.0 km spread is clearly suspect. No universal threshold is set here; it should be calibrated on labeled pairs.

## 6. Source cross-references

- Every concept keeps a list of source-record IDs: Overture ID and its upstream IDs (Meta, Foursquare, Microsoft, AllThePlaces), OSM element, Wikidata ID, and operator page URLs. Each carries a release or retrieval date.
- Provider IDs are **crosswalks**, never the internal identity (R01 §24, §37).
- Copies of one fact on several websites share a **lineage**. Corroboration counts independent lineages, not pages (R04 §5).
- Rights travel with the source record. A concept can mix Apache-licensed identity, an operator-permitted hours claim, and an ODbL-governed OSM tag only if the layers stay separable (R01 §21, §25).

## 7. What this model does not settle

- The physical schema, identifiers, storage or indexing. That comes after the Phase B data path is known.
- Automatic merge thresholds. These need a labeled match/non-match set. Proposed seed: the Scitech, Ithra, Escape The Room, Nasseef and At-Turaif groups, plus a random sample of close pairs from the 1,387 found within 100 m.
- Whether culture-family candidate generation should drop `historic_site` (81 of 85 implausible nearby) or reclassify it. That is an R06 retrieval decision, pending labeled data.
- Offering-level taxonomy (v0.2 §6). Deferred until R05 labels show which facets matter.
