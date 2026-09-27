# R05: Query intent and evaluation seed (provisional)

**Date:** 27 September 2026
**Inputs:** [R00 §8–9 and §25 corpus](R00_User_Decision_Study.md#25-100-query-corpus), [v0.2 §8 and §19](Product_Technical_Concept_Architecture_Review_v0.2.md#8-intent-understanding), [R02 §13–14](R02_Automated_Coverage_and_Feasibility_Audit.md#13-query-level-feasibility-diagnostics), [R02.1 §7](R02_1_Practical_Data_Feasibility_Followup.md#7-the-12-locked-cases), [R04 §3–4](R04_Trust_and_Freshness_Policy.md#3-constraint-states-and-how-results-use-them)
**Status:** Seed only (v0.2, revised 27 Sep 2026 after [R02.2](R02_2_Source_Access_Recovery_and_Review.md); see §6, change log).
- All annotations are **analyst judgments** by one annotator. They are not user data, and the queries are synthetic (R00 §3).
- Arabic renderings are **analyst drafts that need a native speaker's review**.
- **No engine exists, and nothing here claims any system passes these cases.**

## 1. Intent representation (conceptual)

This is a trimmed version of v0.2 §8, keeping only the fields the 24 seed queries actually need. It is not JSON and not an API.

| Field | Content | Why needed (example) |
|---|---|---|
| `origin` | Point or area, with source (user / device / explicit fixture) and precision. **Never invented:** if missing, it is recorded in `missing[]`, and travel constraints stay unknown or the user is asked. The fixed synthetic origin is valid **only** for F01–F12. *[Revised 27 Sep, R02.2]* | "near me" vs "near KAFD" vs "around my hotel" (hotel unknown) |
| `mode` | Car / walk / transit / unknown | "15 minutes driving" vs "half an hour walk" |
| `window` | Start, end or deadline, date anchor, timezone, and whether travel is included | "90 minutes before dinner at 19:30" is a **door-to-door** budget |
| `party` | Size, ages, needs, **only as stated** | "four of us", "kids 6 and 9", "my parents … without much walking" |
| `hard[]` | Field, operator, value, **blocking vs lead-eligible** (R04 §4), and the user's phrase | "under 150 each" gives price **< 150** (strict), unit per person. A value exactly 150 is a boundary ambiguity. "At most 150" would be ≤. *[Revised 27 Sep, R02.2]* |
| `soft[]` | Concept, direction, strength, and the user's phrase | quiet, romantic, not too expensive |
| `exclude[]` | Category, containment or entity, with scope | "not the mall" is a containment exclusion (R03 §4). "Not dinner" is a category. |
| `history` | Only user-supplied or consented visit history | "new to me" and "not the same five places" **cannot be inferred** |
| `missing[]` | Context required to evaluate a hard constraint | Number of adults for a total budget; dinner time |
| `ambiguous[]` | Phrases with competing readings, each with its candidate interpretations | "without booking" = walk-in vs same-day booking |
| `clarify` | Ask / default visibly / proceed, and which field | Ask only when the answer changes the result set |

**Interpretation rules (from R00 §9, v0.2 §8):**
- Preserve the user's phrase for every constraint.
- "Preferably" makes a constraint soft.
- An explicit "max" or "no X" is hard.
- Contradictions are clarified, never silently resolved.
- A model may propose the parse. Deterministic checks own dates, numbers and negations.

## 2. Seed set: 24 queries

**Area and time anchors.** The 12 fixed cases (F01–F12 = R02.1 C01–C12) use area E and the synthetic origin (50.200, 26.300). D0 is Sunday 27 Sep 2026, "tonight" is 18:00–23:00, the weekend is 2–3 Oct, and Thursday is 1 Oct. The 12 development queries (Dxx) keep R00's original place and time. Their areas outside E are marked, because no data audit exists there.

Abbreviations: **B** = blocking when unknown, **Q** = qualifiable (R04 §4).

### 2.1 Fixed feasibility cases (evidence-evaluated in R02.1)

| ID | Query (English) | Hard constraints | Soft | Missing or ambiguous | Clarify? | Acceptable uncertainty | Evaluation criteria |
|---|---|---|---|---|---|---|---|
| F01 | A museum near Khobar tonight, under 50 SAR each | museum (category); open in 18–23 window (B if no hours claim, else Q); price **< 50** per person (strict; lead-eligible if unknown) *[Revised 27 Sep, R02.2]* | near | Travel mode | No, default car and show it | Special-hours notice unchecked; travel unmeasured | Scitech-type candidate only with an E1–E3 hours claim. No exhibition claim invented. |
| F02 | Four of us, something active indoors tonight, under 150 SAR each | group of 4 (B); indoor (E5 allowed, disclosed); open tonight (B/Q); **< 150** per person (strict; lead-eligible if unknown, never satisfied) *[Revised 27 Sep, R02.2]* | active | "Active" breadth | No | None on price or group | Cinemas are not "active" (relevance). Price unknown must not pass. |
| F03 | Got 90 minutes before dinner at 19:30 back here, something cultural | total 18:00–19:30 door-to-door (B); cultural | — | Visit duration; mode | Default car, show it | None on the window | Needs duration plus both legs. A venue open 16–22 alone must not pass. |
| F04 | Four of us want an escape room tonight without booking ahead | escape room; group 4 (B); no advance booking (B); open tonight (B) | — | "Without booking" = walk-in or same-day | **Ask**, or show both readings | None on the booking rule | Expected answer: no supported result, plus "call for a same-night slot". Any "walk-in available" is a false-feasibility failure. |
| F05 | Family with kids aged 6 and 9, indoors this weekend, under 300 SAR total | ages 6 and 9 admitted (B); indoor; weekend open (Q); total ≤300 (B) | fun | **Number of adults** | **Ask** (it changes the total) | Price child-band unknown only with a caveat | An escape room (12+ recommended) must be flagged, not silently offered. |
| F06 | Something to do this weekend that isn't food and isn't the mall | not food (category); not inside a mall (containment, B); weekend open (Q) | — | "Mall" = inside a mall, or a mall itself | No, use containment | Containment unknown ⇒ not "not a mall" | Mall-contained cinemas and arcades excluded, or flagged "containment unknown". |
| F07 | Any exhibition still running this weekend around Dhahran? | exhibition occurrence overlapping 2–3 Oct (B) | — | "Still running" = run end ≥ date | No | None | With no occurrence data: an honest "no programme data" plus organiser link. A museum listing alone is a failure. |
| F08 | Solo, about an hour, a quiet indoor cultural stop after 21:00 tonight | open from 21:00 for ≈60 min, i.e. last entry (B/Q); indoor cultural | quiet | Last entry | No | Quietness unknown is fine | A venue closing at 22:00 with unknown last entry is "may fit, check last entry", never "fits". |
| F09 | Two of us, a workshop we can join this Thursday evening | workshop occurrence 1 Oct evening (B); registration open for 2 (B) | — | Topic | No | None on the occurrence | With no data: say so. Venues with "workshop" in the name ≠ a Thursday session. |
| F10 | Somewhere new to me in Khobar this weekend, not a café | not café; weekend open (Q) | **new to me** (needs history) | Visit history | Ask, or default to "not in your saved list" if one exists | Novelty unverifiable without history | Must not claim "new to you". May say "less commonly listed" only with evidence. |
| F11 | Wheelchair-accessible museum open this Saturday | wheelchair access at the specific site (B); open Saturday (Q) | — | Specific access needs | Optional | None on access | A centre-level statement must be shown as qualified. No accessibility claim from category. |
| F12 | Starting 18:30 tonight, something we can finish by 20:00 within a 15-minute drive | drive ≤15 min (B); start 18:30, finish 20:00 incl. travel (B) | — | Party | No | None on travel | With no routing: no supported result. A straight-line distance may not be expressed as minutes. |

### 2.2 Development queries (from R00 §25, not yet evaluated against data)

| ID | R00 # | Query | Area (audit status) | Hard | Soft | Missing / ambiguous | Clarify? | Evaluation criteria |
|---|---|---|---|---|---|---|---|---|
| D01 | 007 | anything open and interesting | origin | open now (B/Q) | interesting | Time = now; mode | Default now plus visible radius | Only E1–E3 open-now claims pass. Variety across types. |
| D02 | 022 | 90 mins near KAFD, no food | Riyadh KAFD (**not audited**) | total ≤90 min (B); not food | near | Start time; visit vs total | Ask if visit vs total changes results | Door-to-door budget, as F03. |
| D03 | 024 | don't send me across Riyadh, 20 min max | Riyadh (not audited) | travel ≤20 min (B) | — | Origin, mode, time | Default car and now, shown | Routing required. Radius ≠ minutes. |
| D04 | 037 | can we do pottery without booking weeks ahead | origin | pottery; short notice (B) | creative | "Weeks ahead" = same week OK? | Show the interpretation | Session and lead-time claim needed. A studio's existence alone fails. |
| D05 | 040 | something for a rainy evening, not cinema | origin | sheltered (B); not cinema | interesting | Date; the word "rainy" may be hypothetical | No | Cinemas excluded. Indoor by disclosed E5 acceptable. |
| D06 | 046 | is the art thing at Ithra still on | Ithra, Dhahran (E) | named programme run includes today (B) | — | **Which** exhibition | **Ask**, or list current Ithra programmes | Resolve the referent. Never answer "yes" from venue hours. |
| D07 | 055 | can a five-year-old do this workshop | referent | age 5 admitted (B) | — | Workshop identity | Ask for the referent | Only an E1–E3 age rule answers. Otherwise "not stated, check with organiser". |
| D08 | 057 | free place to go with family after Maghrib | origin | price = 0 (B); family access; open after Maghrib (B/Q) | — | Date; Maghrib time depends on date and location | Compute Maghrib for the date, show it | "Free" requires an explicit free claim; unknown price ≠ free (v0.2 §19 row 4). |
| D09 | 061 | date idea tonight that's not dinner | origin | not dinner/restaurant; tonight open (Q) | romantic, interesting | Budget, mode | No | Restaurants excluded. The mood match is explained from evidence, not invented. |
| D10 | 074 | good bookshop I can browse late | origin | bookstore; open late (B/Q) | good, browsable | "Late" cutoff | Default 22:00, shown | OSM had hours for 3 bookstores (R02 §10). Tests E3 open data with the ODbL boundary. |
| D11 | 087 | don't give me the same five places | origin | exclude the user's previously shown or visited set | novelty | Which five: needs session or history | Use session memory if consented, otherwise ask | Must not fabricate history. Diversity measured against the prior list. |
| D12 | 092 | in Jeddah for the weekend, things near Al Balad | Al-Balad J (audited in R02) | weekend dates; near Al-Balad | variety | Visitor vs resident; hotel | No | Mix of heritage, museum and activity. Heat and outdoor caveat for afternoon. teamLab duration disclosed. |

### 2.3 Arabic and mixed-language variants (analyst drafts, need native-speaker review)

| ID | Draft | Checks it adds |
|---|---|---|
| F02-ar | احنا أربعة نبي شي فيه حركة داخلي الليلة، بأقل من ١٥٠ للشخص | Arabic-Indic numerals; "للشخص" = per person; dialect "نبي" |
| F04-ar | نبي غرفة هروب الليلة لأربعة بدون حجز | "بدون حجز" = without booking (same walk-in ambiguity) |
| F04-mix | فيه escape room فاضي الليلة لأربعة؟ | Code-switching; "فاضي" (available) is a **capacity** claim, so blocking |
| F05-ar | طلعة عائلية داخلية هالويكند، عيالي ٦ و٩ سنين، الميزانية ٣٠٠ ريال كلها | "كلها" = total; "هالويكند" loanword |
| F06-ar | شي نسويه الويكند غير الأكل وغير المول | Two negations |
| D08-ar | مكان مجاني نروح له مع العايلة بعد المغرب | Prayer-time anchor; "مجاني" = free |
| D09-ar | فكرة طلعة الليلة غير العشا | "غير العشا" = other than dinner |
| F10-ar | عايش في الخبر من زمان، فاجئني بشي جديد، مو كوفي | "مو كوفي" = not a café; novelty relative to a long-term resident |

A native speaker should judge whether these sound natural, and add real variants from observed sessions (R00 §25 "How to use the corpus later").

## 3. Held-out cases

The following R00 queries are **held out, not inspected for annotation, and not used for development**: every R00 query whose number ends in **3 or 9**. That is 003, 009, 013, 019, 023, 029, 033, 039, 043, 049, 053, 059, 063, 069, 073, 079, 083, 089, 093 and 099.

None of them was used in F01–F12 or D01–D12. Caveat: this annotator read the whole R00 corpus during intake, so the held-out set is unannotated, not unseen. They should be annotated **by someone other than the developer of any future parser**, and only after that parser's first version is frozen. Consented real queries from R00 sessions should replace or extend them.

## 4. Evaluation criteria (for future systems; none applied yet)

Report these separately, never as one score:

| Measure | Denominator | Rule |
|---|---|---|
| **Parse fidelity** | All seed queries | Hard/soft split, exclusions, window and party match the annotation. Every missing field is flagged. |
| **Clarification appropriateness** | Queries marked Ask vs No | Asks when marked Ask (F04, F05, D06, D07). Does not ask when a visible default suffices. |
| **False feasibility** | All results claiming a hard constraint is satisfied | **Target zero** for blocking constraints (R04 §4). Every case is reviewed individually. |
| **Outcome class correctness** | All cases | Matches the R02.1 classes, or the class re-evaluated with new evidence: supported / missing facts / missing context / access failure / no candidates / violation. |
| **Honest empty answers** | Cases whose correct outcome has no supported result (F04, F07, F09, F12 today) | States which constraint caused scarcity. Offers one labeled relaxation. |
| **Residual checks per result** | Results shown | Lists what the user must still verify. Fewer is better **only if** false feasibility stays at zero. |
| **Useful-candidate presence** | Cases with any supported or qualifiable candidate | Requires human judgment of usefulness: a separate annotator, with ratings recorded. |
| **Three separate outcomes per case** *[added 27 Sep, R02.2]* | All cases | Research support per hard constraint, publication eligibility (rights), and **complete-query satisfaction** are reported in separate columns and never combined into one rate. |
| **Language robustness** | Arabic and mixed variants | The same intent as the English version, once native-speaker-validated. |

User benefit (fewer checks, faster confident choice) can only be measured in R00/R09 sessions. It is not a property of this seed.

## 5. What is missing from this seed

- Real user phrasing. All queries are synthetic.
- Ground-truth eligible-result labels. These need E1–E3 evidence per candidate (R04), which R02.1 could not obtain.
- A native-speaker review of the Arabic drafts.
- Coverage of D02, D03 and D12 areas with data. Only E and, partly, J have audited extracts.

## 6. Change log

**v0.2, 27 Sep 2026 (after R02.2):**
- "Under X" is strict (< X), with equality recorded as a boundary ambiguity. "At most X" is ≤ X. Applied to F01, F02 and the `hard[]` definition. Other rows using "≤" for "under" (F05 "under 300 total") follow the same rule.
- Origins are never invented. The fixed synthetic origin applies only to F01–F12.
- "Qualifiable" is replaced by "lead-eligible". An unknown hard constraint is never satisfied (R04 v0.2 §4).
- Evaluation criteria (§4) now score **research support, publication eligibility and query satisfaction separately** (see the [v2 case pass](R02_1_evidence/case_outcomes_v2_2026-09-27.json)).
- The held-out caveat is unchanged: those queries are unannotated, not unseen.

**v0.1 (same day):** see git history (`ae983a8`).
