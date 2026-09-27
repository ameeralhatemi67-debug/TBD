"""Runnable research check for R06. Offline, standard library only. Exits nonzero on any failure.
Passing shows the harness implements R04 v0.2 decisions on these fixtures. It does NOT validate
real users, current availability, publication rights, retrieval coverage, or any live or licensed
integration. v2 (27 Sep 2026) adds regression checks for defects found in Sol's review of 468c1cc."""
import json
from datetime import datetime, date, time
from pathlib import Path
import feasibility as F

H = Path(__file__).resolve().parent
real = json.loads((H / 'fixtures_real_transferred.json').read_text(encoding='utf-8'))
syn = json.loads((H / 'fixtures_synthetic.json').read_text(encoding='utf-8'))
AGE = syn['policy_parameters']['max_quote_age_s']      # SYNTHETIC policy parameter, not a measured refresh interval
dt = datetime.fromisoformat
results = []
def expect(tag, name, got, want):
    results.append((tag, name, got == want, got, want))
def raises(tag, name, fn):
    try:
        fn(); results.append((tag, name, False, 'no error', 'ValueError'))
    except ValueError:
        results.append((tag, name, True, None, None))
def slots_of(raw):
    return [dict(s, start=dt(s['start']), end=dt(s['end'])) for s in raw]
def window(depart, deadline, kind='activity_end', out=0, ret=0, before=0, after=0):
    return {'depart': dt(depart), 'deadline': dt(deadline), 'deadline_kind': kind,
            'outbound_s': out, 'return_s': ret, 'buffer_before_s': before, 'buffer_after_s': after}
def claim(c):
    c = dict(c); c['valid_from'] = date.fromisoformat(c['valid_from']); c['valid_to'] = date.fromisoformat(c['valid_to'])
    c['open'] = time.fromisoformat(c['open']); c['close'] = time.fromisoformat(c['close']); return c

# ================= REAL (transferred from R02.2; not fetched by this agent) =================
br, op = real['escape_branches'], real['operator']
rec = real['overture_records']
st, b, d = F.link_record_to_branch(rec[0], br, 50, op)
expect('REAL', 'Overture b4fdc657: 2.3 m + name/domain corroboration -> provisional link to branch 1', (st, b, round(d['meters'])), ('provisional_link', 1, 2))
st, b, d = F.link_record_to_branch(rec[1], br, 50, op)
expect('REAL', 'Overture 8a251b82 (9 km): corroborated brand, not near a located branch, branch 3 unlocated -> undecided', (st, d['reason']), ('undecided', 'possible_unlocated_branch'))
so = real['slot_observation']; s0 = so['slots'][0]
expect('REAL', 'C02 < 150 each: displayed party total 384 / 4 = 96 (derived; final charge unverified)',
       F.price_check([s0], 'lt', 150, 'per_person', so['party']), 'supported')
inv = {'response_ok': so['response_ok'], 'complete': so['complete'], 'observed_at': dt(so['observed_at_utc'].replace('Z', '+00:00')), 'slots': slots_of(so['slots'])}
out_s = real['route_origin_to_branch1_s']['value']
w12 = window('2026-09-27T18:30:00+03:00', '2026-09-27T20:00:00+03:00', 'activity_end', out=out_s, before=None)
expect('REAL', 'C12: both observed sessions fail, but the abbreviated fixture is not complete inventory',
       F.session_fit(inv, w12, inv['observed_at'], AGE)[0], 'unknown_inventory_incomplete')
w02 = window('2026-09-27T18:00:00+03:00', '2026-09-27T23:00:00+03:00', 'activity_end', out=out_s, before=0)
expect('REAL', 'C02 tonight: 18:15 session is a quote at observation time (buffer explicitly 0 for this rule test)',
       F.session_fit(inv, w02, inv['observed_at'], AGE)[0], 'supported_as_quote')
expect('REAL', 'Same quote re-used hours later is not current availability',
       F.session_fit(inv, w02, dt('2026-09-27T17:55:00+03:00'), AGE)[0], 'unknown_current_availability')
w02u = dict(w02, buffer_before_s=None)
expect('REAL', 'Unknown arrival buffer (e.g. arrive-early rule) keeps fit unknown, not zero',
       F.session_fit(inv, w02u, inv['observed_at'], AGE)[0], 'unknown_timing')
sp = real['scitech_adult_halls_price']
expect('REAL', 'Scitech adult halls: body vs metadata is a conflict', F.representation_conflict(sp), 'conflict')
pp = [{'amount': v['value'], 'unit': 'per_person', 'kind': 'displayed'} for v in sp]
expect('REAL', 'C01 < 50: both representations below threshold -> supported for this threshold', F.price_check(pp, 'lt', 50, 'per_person', 1), 'supported')
expect('REAL', 'Threshold between the two representations -> conflict', F.price_check(pp, 'lt', 21, 'per_person', 1), 'conflict')
expect('REAL', 'Scitech exception end AR 22:00 vs EN 23:00 -> conflict', F.representation_conflict(real['scitech_exception_end']), 'conflict')
man = {r['id']: r.get('sha256_utf8_decoded_content') for r in json.loads((H.parent / 'R02_2_evidence' / 'http_checks.json').read_text(encoding='utf-8-sig'))}
expect('REAL', 'Homepage and old room URL share one app shell (manifest hashes)', F.is_shared_app_shell({k: man[k] for k in real['app_shell_ids']}), True)
expect('REAL', 'C12 overall: model drive estimate + incomplete inventory -> unverified, not a known failure',
       F.query_satisfied({'drive': 'supported_model_estimate', 'session': 'unknown_inventory_incomplete'}, ['drive', 'session']), 'no_unverified_lead')

# ================= SYNTHETIC (invented edge cases; never evidence) =================
expect('SYNTH', 'Record between two same-brand branches 300 m apart -> undecided',
       F.link_record_to_branch({'pt': syn['record_between_branches'], 'name': 'Escape The Room', 'websites': []},
                               syn['nearby_same_brand_branches'], 200, op)[0], 'undecided')
ub = syn['unrelated_business_beside_branch']
expect('SYNTH', 'REGRESSION E: unrelated business beside a branch -> candidate only, no link',
       F.link_record_to_branch(ub['record'], [ub['branch']], 50, ub['operator'])[0], 'candidate_only_no_corroboration')
p = syn['prices']
expect('SYNTH', 'Unresolved "under 150" with price exactly 150 -> boundary ambiguity', F.price_check(p['exact_boundary'], 'under_ambiguous', 150, 'per_person', 4), 'boundary_ambiguity')
expect('SYNTH', 'Resolved strict "< 150" with price exactly 150 -> contradicted', F.price_check(p['exact_boundary'], 'lt', 150, 'per_person', 4), 'contradicted')
expect('SYNTH', '"at most 150" with price exactly 150 -> supported', F.price_check(p['exact_boundary'], 'le', 150, 'per_person', 4), 'supported')
expect('SYNTH', 'Per-person price vs total budget with unknown party -> unknown', F.price_check(p['per_person_vs_total_unknown_party'], 'lt', 300, 'party_total', None), 'unknown')
expect('SYNTH', 'Two prices straddling the limit -> conflict', F.price_check(p['conflict_straddling'], 'lt', 150, 'per_person', 1), 'conflict')
hrs = syn['hours']; allc = [claim(hrs['regular']), claim(hrs['exception_short'])]
expect('SYNTH', 'Exception inside its date overrides regular hours -> contradicted',
       F.hours_state(allc, dt('2026-10-02T18:00:00+03:00'), dt('2026-10-02T20:00:00+03:00')), 'contradicted')
expect('SYNTH', 'Exception not applied outside its date -> regular hours supported',
       F.hours_state(allc, dt('2026-10-03T18:00:00+03:00'), dt('2026-10-03T20:00:00+03:00')), 'supported')
expect('SYNTH', 'Only an ambiguous-scope line -> unknown',
       F.hours_state([claim(hrs['ambiguous_scope'])], dt('2026-10-02T17:00:00+03:00'), dt('2026-10-02T18:00:00+03:00')), 'unknown')
expect('SYNTH', 'REGRESSION C: open 16-22, visit 23:30-00:30 crossing midnight -> contradicted',
       F.hours_state([claim(hrs['regular'])], dt('2026-10-03T23:30:00+03:00'), dt('2026-10-04T00:30:00+03:00')), 'contradicted')
expect('SYNTH', 'Overnight opening 18:00-02:00 covers 23:30-00:30 -> supported',
       F.hours_state([claim(hrs['overnight_regular'])], dt('2026-10-03T23:30:00+03:00'), dt('2026-10-04T00:30:00+03:00')), 'supported')
expect('SYNTH', 'Previous date has no claim, so a possible overnight opening is unknown, not contradicted',
       F.hours_state([claim(hrs['regular_from_2_oct_only'])], dt('2026-10-02T00:30:00+03:00'), dt('2026-10-02T01:00:00+03:00')), 'unknown')
ss = slots_of(syn['slots']); t0 = dt('2026-10-01T12:00:00+03:00')
full = {'response_ok': True, 'complete': True, 'observed_at': t0, 'slots': ss}
expect('SYNTH', 'Complete inventory, only fitting slot freshly Booked -> contradicted_no_fitting_session',
       F.session_fit(full, window('2026-10-01T18:45:00+03:00', '2026-10-01T20:05:00+03:00'), t0, AGE)[0], 'contradicted_no_fitting_session')
expect('SYNTH', 'Late slot crossing midnight evaluated by timestamps, not business date',
       F.session_fit(full, window('2026-10-01T23:00:00+03:00', '2026-10-02T00:45:00+03:00'), t0, AGE)[0], 'supported_as_quote')
wq = window('2026-10-01T18:00:00+03:00', '2026-10-01T21:00:00+03:00')
expect('SYNTH', 'REGRESSION A: empty slot list without completeness -> unknown, not contradicted',
       F.session_fit({'response_ok': True, 'complete': None, 'observed_at': t0, 'slots': []}, wq, t0, AGE)[0], 'unknown_inventory_incomplete')
expect('SYNTH', 'REGRESSION A: failed inventory response -> unknown_inventory_unavailable',
       F.session_fit({'response_ok': False}, wq, t0, AGE)[0], 'unknown_inventory_unavailable')
expect('SYNTH', 'Complete, applicable empty inventory -> contradicted_no_fitting_session',
       F.session_fit({'response_ok': True, 'complete': True, 'observed_at': t0, 'slots': []}, wq, t0, AGE)[0], 'contradicted_no_fitting_session')
rt = syn['return_trip_case']; rs = [dict(rt['slot'], start=dt(rt['slot']['start']), end=dt(rt['slot']['end']))]
rinv = {'response_ok': True, 'complete': True, 'observed_at': t0, 'slots': rs}
expect('SYNTH', 'REGRESSION B: ends 19:55, back-at-origin 20:00, 10-min return -> contradicted',
       F.session_fit(rinv, window(rt['depart'], rt['deadline'], 'back_at_origin', rt['outbound_s'], rt['return_s'], 0, 0), t0, AGE)[0], 'contradicted_no_fitting_session')
expect('SYNTH', 'Same session with an activity-end deadline -> supported_as_quote',
       F.session_fit(rinv, window(rt['depart'], rt['deadline'], 'activity_end', rt['outbound_s'], None, 0, None), t0, AGE)[0], 'supported_as_quote')
expect('SYNTH', 'Back-at-origin with unknown return leg (not assumed zero) -> unknown_timing',
       F.session_fit(rinv, window(rt['depart'], '2026-10-01T20:30:00+03:00', 'back_at_origin', rt['outbound_s'], None, 0, 0), t0, AGE)[0], 'unknown_timing')
sb = syn['stale_booked']; sbs = [dict(sb['slot'], start=dt(sb['slot']['start']), end=dt(sb['slot']['end']))]
expect('SYNTH', 'REGRESSION D: stale Booked observation -> unknown current availability, not rejection',
       F.session_fit({'response_ok': True, 'complete': True, 'observed_at': dt(sb['observed_at']), 'slots': sbs},
                     wq, dt(sb['query_at']), AGE)[0], 'unknown_current_availability')
expect('SYNTH', 'Boundary ambiguity leaves the query unsatisfied (a lead, not a match)',
       F.query_satisfied({'price': 'boundary_ambiguity', 'hours': 'supported'}, ['price', 'hours']), 'no_unverified_lead')
expect('SYNTH', 'REGRESSION F: required constraint never evaluated -> not_evaluated',
       F.query_satisfied({'hours': 'supported'}, ['hours', 'price']), 'not_evaluated')
expect('SYNTH', 'Empty constraint set without an explicit no-hard-constraints flag -> not_evaluated', F.query_satisfied({}, []), 'not_evaluated')
expect('SYNTH', 'Query that genuinely has no hard constraints -> yes_no_hard_constraints', F.query_satisfied({}, [], no_hard_constraints=True), 'yes_no_hard_constraints')
# ---- input validation (SYNTHETIC)
raises('SYNTH', 'Unsupported comparison operator is rejected', lambda: F.price_check(p['exact_boundary'], 'gt', 150, 'per_person', 1))
raises('SYNTH', 'Party size 0 is rejected', lambda: F.price_check(p['exact_boundary'], 'lt', 150, 'per_person', 0))
raises('SYNTH', 'Departure after deadline is rejected', lambda: F.session_fit(full, window('2026-10-01T21:00:00+03:00', '2026-10-01T20:00:00+03:00'), t0, AGE))
raises('SYNTH', 'Observation after query time is rejected as impossible', lambda: F.session_fit(full, wq, dt('2026-10-01T11:00:00+03:00'), AGE))
raises('SYNTH', 'Visit ending before it starts is rejected', lambda: F.hours_state(allc, dt('2026-10-02T20:00:00+03:00'), dt('2026-10-02T18:00:00+03:00')))
raises('SYNTH', 'Missing required constraint list is rejected', lambda: F.query_satisfied({}, None))

for tag, name, ok, got, want in results:
    print(f"{'PASS' if ok else 'FAIL'} [{tag}] {name}" + ('' if ok else f'  got={got} want={want}'))
n = sum(r[2] for r in results)
print(f"\n{n}/{len(results)} checks pass. REAL checks use transferred R02.2 observations; SYNTH checks use invented values.")
raise SystemExit(0 if n == len(results) else 1)
