# R06: Retrieval and feasibility design (bounded, provisional)

**Date:** 27 September 2026 (evening)
**Inputs:** [R02](R02_Automated_Coverage_and_Feasibility_Audit.md), [R02.1](R02_1_Practical_Data_Feasibility_Followup.md), [R02.2](R02_2_Source_Access_Recovery_and_Review.md), [R03 v0.2](R03_Domain_and_Identity_Model.md), [R04 v0.2](R04_Trust_and_Freshness_Policy.md), [R05 v0.2](R05_Query_Intent_and_Evaluation_Seed.md)
**Status:** A logical design, only as deep as the evidence supports, plus an offline research harness ([`R06_research_harness/`](R06_research_harness/)).
- It is **not** a search platform, crawler, database, API, UI or ingestion pipeline.
- Engine, index and vector choices remain open: nothing measured yet would decide them.

## 1. The simplest flow the evidence supports

```text
1 Parse intent          → typed constraints; missing context recorded, never invented (R05 §1)
2 Candidate discovery   → open baseline by area + category, with name rescue for misclassified venues
3 Identity resolution   → record → site / branch / offering via operator IDs where available (R03)
4 Evidence selection    → per constraint: admissible observations only (authority × channel × scope × valid time; R04 §2)
5 Constraint evaluation → supported / contradicted / unknown / conflict / boundary ambiguity (harness)
6 Partition             → fits · unverified leads (explicit relaxation) · excluded
7 Small diverse list    → 2–3 fits across different offering types if possible; else honest scarcity + one labeled relaxation
8 Publication gate      → show only publication-eligible facts; otherwise link out (R04 §9 project policy)
```

| Step | What the evidence says | Design decision | Still open |
|---|---|---|---|
| 2 Discovery | Culture categories are noisy: 81 of 85 nearby `historic_site` names were judged implausible (single annotator). Real venues sit under other labels (Bujairi as `shopping`, muvi as `shopping_mall`). | Category filter plus a name/alias rescue list. **Excluding `historic_site` is a retrieval experiment, not a settled rule.** It carries a recall risk: real heritage places such as Oil Well 7 fall under that label. Compare runs with and without it on a labeled sample, measuring false positives and negatives. *[Revised 27 Sep night]* | Recall is unknown: no independent venue inventory exists. |
| 3 Identity | Escape The Room has **two Khobar branches**. One Overture record is 2.3 m from branch 1's operator point; another is 9 km away. Scitech has 3 records up to 4 km apart. | Distance only proposes candidates. A provisional link needs exactly one located operator branch within a small radius **and** corroborating identity evidence (name or operator domain). Distance alone gives `candidate_only_no_corroboration`; branches without coordinates keep brand-matching distant records **undecided** (R03 §5). *[Revised 27 Sep night]* Operator branch and room IDs, not URLs, identify offerings (app shell). | Entrances; branch 3 has no resolved point. |
| 4 Evidence | Operator API (C1) supplies room, party size, duration and slot quotes. Scitech's page body and metadata disagree, and its AR and EN pages disagree. | Keep each channel as a separate observation. Conflicts decide nothing. Search summaries are never evidence. | Refresh cadence per source (needs observations on different dates). |
| 5 Evaluation | Room 1 fits four; SAR 384 party total gives a derived SAR 96 each; the 18:15 slot is a quote. For C12 the room's sessions miss the window. | Deterministic rules in the harness: strict "under", unit reconciliation, exception intervals, session timing, quote age. | Duration and last entry for cultural venues. |
| 6–7 Shortlist | The fixed cases produce at most one research-supported fit, and only as a historical quote (C02). | Never pad the list with leads presented as fits. Report which constraint caused scarcity. | Whether users accept a separate "unverified leads" section (R00 sessions). |
| 8 Publication | No reuse grant found for either operator. Robots rules are not a licence (RFC 9309). | Research support ≠ publication eligibility. Until permission or legal review, link out. | Operator responses (drafts in PROJECT_START_REVIEW §12). |

**Travel.** Use a routing call per shortlisted candidate and direction. Outbound (149 s) and return (196.9 s) legs differ, and both are OSRM demo model outputs (non-commercial, no SLA). A straight-line radius is never expressed as minutes. Parking, walk-in time and briefing buffers stay explicit unknowns until measured.

## 2. Offline research harness

[`R06_research_harness/check_harness.py`](R06_research_harness/check_harness.py) runs **45 checks** (v2, 27 Sep night; see §6) with the standard library only.

- **13 REAL checks** use observations **transferred from R02.2**, collected by Sol, not this agent: branch linking, the C02 derived price, C12 session failure, quote ageing, the Scitech body/metadata and AR/EN conflicts, and app-shell detection from manifest hashes.
- **32 SYNTH checks** use clearly labeled invented fixtures ([`fixtures_synthetic.json`](R06_research_harness/fixtures_synthetic.json)): nearby same-brand branches, the strict "under" boundary vs inclusive "at most", unit mismatch with unknown party, straddling conflicts, exception date scope, ambiguous-scope hours, booked slots, midnight-crossing slots, and leads ≠ matches.
- Mutation sanity check (scratch copy, not committed): disabling the boundary rule or the quote-age rule each produces exactly one failing check.

**What passing does not prove:**
- that real users benefit;
- that any quote is currently available;
- that Sol's observations are still true;
- that publication is permitted;
- that a licensed live integration works;
- that retrieval recall is adequate.

The harness tests decision rules on fixed inputs, nothing more.

## 3. Compared with ordinary Maps/Search plus operator links

| Step of the user's task | Maps / Search + operator site (current workflow) | Specialized product (this design) | What the product must still prove |
|---|---|---|---|
| Find candidates | Strong: broad POI coverage, reviews, "things to do" | Weaker today: open baseline has noisy categories; no reviews in the owned corpus | Comparable or better candidate recall for the target categories (labeled sample) |
| Check hours | Maps shows hours of unknown provenance; the operator page may conflict | Shows only admissible hours with valid time; flags conflicts | That surfacing conflicts helps users rather than confusing them |
| Party-specific price and slot | User must open the operator site and enter date and party | Evaluates the party/date quote in one step **if** the operator path is permitted | **Permission**, and reliability across dates and operators (one operator seen once so far) |
| Time-window fit (session plus travel) | User computes it mentally | Deterministic check (C12-type failures caught) | That the users' real windows are tight enough for this to matter (R00 H4) |
| Mixed venue vs activity comparison | Separate searches | Shortlist across types | That users compare across types at all (R00 H3) |
| Trust | Implicit | Explicit supported / unknown / conflict | That explicit uncertainty increases, not decreases, willingness to choose |

**Net** *[revised 27 Sep night]***:** the evidence so far shows that party/date/time feasibility is **checkable** for one bookable operator whose public site exposes slot quotes. That does **not** show bookable activities are the best market or the users' main need (R00 H1–H4 untested), and one operator is not a category. The candidate specialized value is feasibility checking where evidence exists, plus conflict surfacing. For open-ended cultural discovery, Maps/Search currently looks stronger on coverage. A first product that cannot beat Maps on the feasibility step for a few operators has no advantage.

## 4. What must stay provisional

- Retrieval engine, full-text/semantic search, vector stores: no labeled recall data.
- Ranking and diversity weights (R07).
- Production routing provider (R08). The demo is not usable commercially.
- Any integration with operator endpoints beyond research reads. No agreement exists.
- Refresh intervals. No observations on different dates yet.

## 5. Smallest next evidence run

Specified in [PROJECT_START_REVIEW §12](PROJECT_START_REVIEW.md#12-follow-up-27-sep-evening-after-r022), with acceptance criteria and owner/agent split.

## 6. Change log

**27 Sep 2026 (night), after Sol's review of `468c1cc`.** Harness v2 fixes six demonstrated defects:
- **(A)** An empty or partial inventory is no longer a known failure (`unknown_inventory_incomplete` / `unavailable`). Only complete, applicable inventory can give `contradicted_no_fitting_session`. The transferred slot fixture is marked incomplete.
- **(B)** Deadlines are `activity_end` or `back_at_origin`. Outbound and return legs and buffers are included, and unknown values stay unknown.
- **(C)** Hours are evaluated as dated, timezone-aware intervals, with overnight openings and per-date exceptions.
- **(D)** Quote age applies to every status, so a stale "Booked" is unknown. Impossible observation times are rejected. The 900 s age limit is a **synthetic test parameter**.
- **(E)** Branch links need corroboration beyond distance.
- **(F)** Case-pass preservation uses a normalized-text hash, all checkers exit nonzero on failure, and `query_satisfied` refuses to report satisfaction for an unsupplied constraint set.

Input validation now covers party size, time ordering, comparison operators and timezone-aware datetimes. The harness has **45 checks: 13 REAL (transferred) and 32 SYNTH**. §1's `historic_site` exclusion and the "Net" assessment were revised as marked.
