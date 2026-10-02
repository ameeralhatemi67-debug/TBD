# R02.3 collection handoff

Prepared by Sol on 27 September 2026, after Opus commit `0201e31`.

## Current state

The collector is ready and the collection heartbeat is active. **Four of six planned passes have run:** both D1 passes on 28 September and both D2 passes on 2 October. See the [D2 morning note](RUN_2026-10-02_full.md) and [D2 repeat note](RUN_2026-10-02_slots.md). Both D3 passes remain pending.

One separate transport diagnostic succeeded at **2026-09-27 23:17:38 +03:00**. A single GET to `https://api.escapetheroomsa.com/api/branches` returned HTTP 200 and a structurally valid JSON response, 1,015 bytes. See [diagnostic record](diagnostics/2026-09-27_access.json). This confirms access to that endpoint from this environment at that time. It does not establish access to every source, repeated reliability, reuse rights, or practical feasibility. It does not choose or pin rooms.

The diagnostic's response body stays in the ignored `.local_source_checks/R02_3/diagnostics/` directory. No source body is included in this handoff.

## Scheduled observations

The Codex thread heartbeat `tbd-r02-3-collection` is active. Its recurrence uses UTC. After the early D1 repeat, it was corrected to **06:00 and 12:00 UTC**, corresponding to 09:00 and 15:00 Riyadh. The local system timezone was checked as UTC+03:00, Kuwait/Riyadh.

| Observation | Date in Riyadh | Full pass | Slots pass | Status at handoff |
|---|---|---|---|---|
| D1 | Monday 28 September 2026 | Ran around 09:53 | Ran around 12:01 | Both passes complete; repeat occurred earlier than intended |
| D2 | Friday 2 October 2026 | Ran around 09:01-09:04 | Ran around 15:01 | Both passes complete |
| D3 | Monday 5 October 2026 | 09:00 | 15:00 | Scheduled, not collected |

D2 is a weekend date. D3 is seven days after D1. Both session dates, 15 and 17 October, remain in the future. The schedule ends after the final slots pass.

This is a local scheduled task, not an always-running hosted collector. Keep this computer awake, connected, and Codex available for the scheduled times. Actual manifests determine whether a pass happened. A scheduled job is not evidence of execution. Report missed runs rather than inventing or backdating them. If D1 is missed, revise the remaining schedule explicitly within the original observation windows before collecting.

## Collector corrections and verification

The fixed targets and sampling plan are unchanged.

- Slot projection now preserves the API's `eventId` as `slot_id`, with `id` as a fallback. The original projection looked only for `id` and would lose the known API identifier needed for comparisons.
- The request loop checks the daily ceiling before taking the next request. Previously, reaching the ceiling between requests could reuse the previous response under the next request ID.
- Daily accounting counts attempted requests, excluding entries that were skipped without a network call.
- The manifest is checkpointed after each response. `finished: false` means execution did not reach its normal end. `finished: true` does not imply all requests succeeded; inspect `stopped`, classifications, missing outputs and skipped requests.

Verification on 27 September:

- Collector self-test: **21/21**, all offline. Four new checks cover the identifier and request-cap regression using synthetic data and a mocked fetch.
- Full dry-run: **15 initial requests**, plus up to eight after room selection, as specified by Opus.
- Existing feasibility checks: **45/45**.
- Historical case preservation and v3 checks: **passed**. Their historical outputs are unchanged.

These tests verify the stated cases only. They do not establish source correctness, rights or user benefit.

## Execution instructions

Workspace: `D:\Agents\main\projects\ideas\TBD`.

Expected branch: `codex/r02-3-collection`, based on Opus's `0201e31`. Push this branch only. Do not change `main` or `claude/gifted-davinci-wv2qnj`, force-push, discard local work, or switch away from another task's active checkout.

Bundled Python:

```powershell
& 'C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' R02_3_collection/collect_run.py --selftest
& 'C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' R02_3_collection/collect_run.py --dry-run
```

On each scheduled morning, use the same executable with `--pass full`. At 15:00, use `--pass slots`. A delayed full pass must still be in the morning. A delayed slots pass must finish before 16:00. Never relabel a late observation or overwrite an existing run.

Before each pass:

1. Confirm the actual Riyadh date and time, correct branch and clean working tree.
2. Read earlier manifests for the date. If any request received HTTP 401, 403 or 429, stop collection for that date. The collector stops the current run, but does not itself carry this denial rule into a later process.
3. If an earlier run is unfinished or missing outputs, preserve it and report the problem. Do not start another pass until its attempts are accounted for. An interrupted request may have reached the server without a completed response record.
4. Do not start a slots pass without a resolved room set from a completed full pass. Keep that room set fixed thereafter.

After each pass:

1. Inspect `finished`, `stopped`, every request classification and skipped request. A failure or unusual response is not a cancellation.
2. Count actual attempt records across all runs on that Riyadh date. Stay within **40**, including retries. A normal resolved full pass uses 23 requests and the slots pass uses 12, leaving only five attempts for retries.
3. Check that resolved branch/room IDs match earlier observations and that each quote retains date, group size and observation time through its request record.
4. Review the local HTML bodies before interpreting page projections. `valid_html` is a coarse response classification. The collector's regular expression can match prices as times and can include script text; extracted lines are not validated opening-hour claims. Do not publish script fragments, generic page descriptions or unreviewed excerpts as factual evidence. Keep the original bodies and their hashes local, and document any curated projection separately.
5. Preserve unknown inventory completeness, conflicting Scitech representations, uncertain scope, unverified final charges and unresolved rights. The two OSRM responses are modelled drive estimates without verified traffic, parking or entrance time.
6. Commit only reviewed research projections, manifests and a short run note. Verify that `.local_source_checks/` is excluded. Push `codex/r02-3-collection` without force.

The first complete pass can be evaluated by Opus while later dates are pending. One pass must not be described as a completed repeatability study.

## Next handoff to Opus

Wait for an actual dated run to be pushed. Use a fresh session to avoid rereading the large conversation. Give it the collection branch and this bounded task:

> Read R02_3_collection/SOL_HANDOFF.md, plan.json, the newly completed run files and the relevant R04/R06 rules. Evaluate L01-L05 against this dated evidence. Separate supported historical quotes, unknowns, contradictions, final-price uncertainty and publication rights. Keep C01-C12 unchanged. Do not treat missing inventory as proof of no availability, or collected HTML lines as verified facts. Report what this one pass adds and what still requires later dates. Make only corrections necessary to evaluate these cases. Do not implement an app or expand the research scope. Keep this evaluation to a $3 target and $5 estimated stop threshold, using the owner's newly confirmed remaining balance and retaining the $20 reserve. Report estimates honestly; do not claim an enforceable billing cap. Commit to your existing Claude branch and stop at the checkpoint.

Do not start that evaluation from tonight's branch-list diagnostic. It contains no session or price evidence.

## Owner actions

1. Keep the local machine and Codex available for the six scheduled passes. Collection success will be reported after execution.
2. Use [the pilot kit](../R00_Pilot_Execution_Kit.md) to invite about 12 people in the Eastern Province and aim for eight completed, 30-40 minute sessions. Follow the screener, consent and neutral tasks. Do not present the concept before observing their usual workflow. Keep participant contact details and raw recordings out of the public Git repository.
3. Decide whether to send the two permission requests in [PROJECT_START_REVIEW section 12.6](../PROJECT_START_REVIEW.md#126-revised-operator-request-drafts-not-sent). Adapt sender identity truthfully. Ask about read-only access, storage/display scope, update frequency, change notices and fees. No requests have been sent by Sol or Opus.
4. Leave Opus paused until the first real run is available. Its next useful work is the bounded case evaluation above. Collection alone cannot answer permission or user-value questions.

The last owner-confirmed Claude balance in the conversation was $79 before Opus's latest estimated $2-3 batch. The current balance is not independently verified. Codex has not inspected or changed Claude billing settings.
