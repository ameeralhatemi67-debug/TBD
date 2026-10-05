# R02.3 — Three-date collection findings

**Status:** Fixed collection complete on 5 October 2026. This is research evidence, not a permitted production feed or a validation of user value.

## What ran

| Riyadh date | Full pass | Repeated slots | Actual attempts | Access denial |
|---|---|---|---:|---|
| 28 September | About 09:53–09:56 | About 12:01–12:02 | 36/40 | None |
| 2 October | About 09:01–09:04 | About 15:01 | 36/40 | None |
| 5 October | About 09:01–09:03 | About 15:01 | 36/40 | None |

The first repeat happened earlier than the intended 15:00 Riyadh target because the initial automation recurrence used UTC. It still met the fixed same-day window and was recorded at its actual time. The recurrence was corrected for the later dates. Every run reported `finished: true` and `stopped: null`. Total actual attempts: **108**. The automation is now paused.

The dated [manifests and projections](runs/) identify each URL, response classification, observation time, selected room and request hash. Full source bodies stayed in the local Git-ignored `.local_source_checks/` directory. The [plan](plan.json) was fixed before collection. No booking, hold, login, payment or operator contact occurred.

## Evidence gained

1. **The fixed Escape The Room path was reachable on all three dates.** Each full pass returned structurally valid branch, room and slot JSON. The same room IDs remained pinned: branch 1 rooms 1 and 2, branch 3 room 14. Each repeated slots pass also returned 12 structurally valid responses. This supports short-run technical access to those specific public paths from this environment. It does not establish a contract or long-term reliability.
2. **The selected future-session projections did not change in this sample.** Across the fixed 15 and 17 October dates, party sizes two and four, and three rooms, the same 16 projected session IDs per request carried the same start, end, status, displayed amount and currency across six observations. This does not establish a suitable production refresh rate, complete inventory or guaranteed availability. Every observed slot list has **unknown completeness**.
3. **Scitech's price-page structure changed by 5 October.** On 28 September and 2 October the visible HTML table had adult and child rows with three price columns. On 5 October the body had hall and IMAX headings with two values but no earlier adult/child rows or combined-ticket column. HTTP 200 alone would miss this field-level change. The collector's line extraction and metadata do not safely map the new amounts to a ticket type. Earlier category-specific prices should not be carried forward as current facts. Scitech's dated ordinary hours also remain unresolved.
4. **Some access problems repeated.** Ithra timed out twice on each full pass. The OSRM demo endpoint failed Python TLS certificate validation twice on each full pass; the reverse leg was skipped after the host failure limit. These are retrieval outcomes in this environment, not findings that Ithra is closed or that Saudi routes do not work. Scitech hours pages and Sparky's location page returned HTML, but no dated, branch-specific practical fact was validated from those responses here.

## What this study cannot answer

- **Rights:** The public responses do not establish permission to store, refresh or display these facts in a commercial product. Follow the operator permission requests or a source-specific legal review.
- **User value:** No participant used an evidence card or completed a comparison task. Run the prepared R00 pilot before claiming reduced decision time or better choices.
- **Case satisfaction:** A displayed price can omit final fees. A status is a historical quote. Unknown slot completeness cannot prove no session exists. The selected responses cannot establish Scitech's dated opening, safe arrival and return travel, or all L01–L05 requirements. Apply R04 and R06 to each live case before claiming a match.
- **Wider supply:** Three rooms at one operator plus a few fixed pages do not measure the Eastern Province's total useful coverage.

## Recommended next work

1. Have Opus evaluate **L01–L05** against these dated manifests and the existing R04/R06 rules. Keep each constraint's evidence, observation time and unknowns separate. The [handoff](SOL_HANDOFF.md) contains a bounded prompt. Preserve historical C01–C12 outcomes.
2. Obtain an operator clarification on the **Scitech 5 October table** and its date and ticket-type scope. Keep the 28 September and 2 October representations as historical evidence, not current defaults.
3. Decide whether to send the drafted operator requests about approved read-only access, storage/display rights, refresh limits, changes and fees.
4. Recruit and run the eight-person directional R00 pilot. The current collection shows technical data access, not that the shortlist promise helps users.

No additional collection date should be implied by these results. Define a new question and plan before requesting more source reads.
