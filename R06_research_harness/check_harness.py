"""Runnable research check for R06. Offline, standard library only.
Passing shows the harness implements R04 v0.2 decisions on these fixtures. It does NOT validate
real users, current availability, publication rights, or any live or licensed integration."""
import json
from datetime import datetime, date, time
from pathlib import Path
import feasibility as F

H = Path(__file__).resolve().parent
real = json.loads((H / 'fixtures_real_transferred.json').read_text(encoding='utf-8'))
syn = json.loads((H / 'fixtures_synthetic.json').read_text(encoding='utf-8'))
dt = datetime.fromisoformat
results = []
def expect(tag, name, got, want):
    results.append((tag, name, got == want, got, want))

def slots_of(raw):
    return [dict(s, start=dt(s['start']), end=dt(s['end'])) for s in raw]

# ---------- REAL (transferred from R02.2) ----------
br = real['escape_branches']
st, b, m = F.link_record_to_branch(real['overture_records'][0]['pt'], br, 50)
expect('REAL', 'Overture b4fdc657 -> provisional link to branch 1 (~2.3 m)', (st, b, round(m)), ('provisional_link', 1, 2))
expect('REAL', 'Overture 8a251b82 (9 km) stays undecided; not assigned to branch 3 by name',
       F.link_record_to_branch(real['overture_records'][1]['pt'], br, 50)[0], 'undecided')
so = real['slot_observation']; s0 = so['slots'][0]
expect('REAL', 'C02 under 150 each: displayed party total 384 / 4 = 96 (derived)',
       F.price_check([s0], 'lt', 150, 'per_person', so['party']), 'supported')
slots = slots_of(so['slots']); obs = dt(so['observed_at_utc'].replace('Z', '+00:00'))
travel = real['route_origin_to_branch1_s']['value']
expect('REAL', 'C12 depart 18:30, finish by 20:00: room 1 contradicted on 27 Sep',
       F.session_fit(slots, dt('2026-09-27T18:30:00+03:00'), dt('2026-09-27T20:00:00+03:00'), travel, obs, obs, 900)[0], 'contradicted')
expect('REAL', 'C02 tonight: 18:15 slot is a quote at observation time',
       F.session_fit(slots, dt('2026-09-27T18:00:00+03:00'), dt('2026-09-27T23:00:00+03:00'), travel, obs, obs, 900)[0], 'supported_as_quote')
expect('REAL', 'Same quote re-used hours later is not current availability',
       F.session_fit(slots, dt('2026-09-27T18:00:00+03:00'), dt('2026-09-27T23:00:00+03:00'), travel, obs, dt('2026-09-27T17:55:00+03:00'), 900)[0], 'unknown_current_availability')
sp = real['scitech_adult_halls_price']
expect('REAL', 'Scitech adult halls: body vs metadata is a conflict', F.representation_conflict(sp), 'conflict')
pp = [{'amount': v['value'], 'unit': 'per_person', 'kind': 'displayed'} for v in sp]
expect('REAL', 'C01 under 50: both representations below threshold -> supported for this threshold', F.price_check(pp, 'lt', 50, 'per_person', 1), 'supported')
expect('REAL', 'Threshold between the two representations -> conflict', F.price_check(pp, 'lt', 21, 'per_person', 1), 'conflict')
expect('REAL', 'Scitech exception end AR 22:00 vs EN 23:00 -> conflict', F.representation_conflict(real['scitech_exception_end']), 'conflict')
man = {r['id']: r.get('sha256_utf8_decoded_content') for r in json.loads((H.parent / 'R02_2_evidence' / 'http_checks.json').read_text(encoding='utf-8-sig'))}
expect('REAL', 'Homepage and old room URL share one app shell (manifest hashes)', F.is_shared_app_shell({k: man[k] for k in real['app_shell_ids']}), True)
expect('REAL', 'C12 overall: model drive estimate + contradicted session -> known failure',
       F.query_satisfied({'drive': 'supported_model_estimate', 'session': 'contradicted'}), 'no_known_failure')

# ---------- SYNTHETIC (invented edge cases) ----------
expect('SYNTH', 'Record between two same-brand branches 300 m apart -> undecided',
       F.link_record_to_branch(syn['record_between_branches'], [dict(b) for b in syn['nearby_same_brand_branches']], 200)[0], 'undecided')
p = syn['prices']
expect('SYNTH', '"under 150" with price exactly 150 -> boundary ambiguity', F.price_check(p['exact_boundary'], 'lt', 150, 'per_person', 4), 'boundary_ambiguity')
expect('SYNTH', '"at most 150" with price exactly 150 -> supported', F.price_check(p['exact_boundary'], 'le', 150, 'per_person', 4), 'supported')
expect('SYNTH', 'Per-person price vs total budget with unknown party -> unknown', F.price_check(p['per_person_vs_total_unknown_party'], 'lt', 300, 'party_total', None), 'unknown')
expect('SYNTH', 'Two prices straddling the limit -> conflict', F.price_check(p['conflict_straddling'], 'lt', 150, 'per_person', 1), 'conflict')
def claim(c):
    c = dict(c); c['valid_from'] = date.fromisoformat(c['valid_from']); c['valid_to'] = date.fromisoformat(c['valid_to'])
    c['open'] = time.fromisoformat(c['open']); c['close'] = time.fromisoformat(c['close']); return c
hrs = syn['hours']; allc = [claim(hrs['regular']), claim(hrs['exception_short'])]
expect('SYNTH', 'Exception inside its date overrides regular hours -> contradicted',
       F.hours_state(allc, datetime(2026, 10, 2, 18), datetime(2026, 10, 2, 20)), 'contradicted')
expect('SYNTH', 'Exception not applied outside its date -> regular hours supported',
       F.hours_state(allc, datetime(2026, 10, 3, 18), datetime(2026, 10, 3, 20)), 'supported')
expect('SYNTH', 'Only an ambiguous-scope line -> unknown',
       F.hours_state([claim(hrs['ambiguous_scope'])], datetime(2026, 10, 2, 17), datetime(2026, 10, 2, 18)), 'unknown')
ss = slots_of(syn['slots']); t0 = dt('2026-10-01T12:00:00+03:00')
expect('SYNTH', 'Only fitting slot is Booked -> contradicted',
       F.session_fit(ss, dt('2026-10-01T18:45:00+03:00'), dt('2026-10-01T20:05:00+03:00'), 0, t0, t0, 900)[0], 'contradicted')
expect('SYNTH', 'Late slot crossing midnight evaluated by timestamps, not business date',
       F.session_fit(ss, dt('2026-10-01T23:00:00+03:00'), dt('2026-10-02T00:45:00+03:00'), 0, t0, t0, 900)[0], 'supported_as_quote')
expect('SYNTH', 'Boundary ambiguity leaves the query unsatisfied (a lead, not a match)',
       F.query_satisfied({'price': 'boundary_ambiguity', 'hours': 'supported'}), 'no_unverified_lead')

for tag, name, ok, got, want in results:
    print(f"{'PASS' if ok else 'FAIL'} [{tag}] {name}" + ('' if ok else f'  got={got} want={want}'))
n = sum(r[2] for r in results)
print(f"\n{n}/{len(results)} checks pass. REAL checks use transferred R02.2 observations; SYNTH checks use invented values.")
raise SystemExit(0 if n == len(results) else 1)
