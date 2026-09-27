"""Structural checks for the v2 case pass (R04 v0.2). Verifies consistency, not real-world truth."""
import hashlib, json
from pathlib import Path
P = Path(__file__).resolve().parent
v2 = json.loads((P / 'case_outcomes_v2_2026-09-27.json').read_text(encoding='utf-8'))
v1_bytes = (P / 'case_outcomes.json').read_bytes()
v1 = json.loads(v1_bytes)
ids = {r['id'] for f in ('http_checks', 'public_app_checks', 'interpretation_checks')
       for r in json.loads((P.parent / 'R02_2_evidence' / f'{f}.json').read_text(encoding='utf-8-sig'))}
c = {}
c['v1_unchanged'] = hashlib.sha256(v1_bytes).hexdigest() == v2['v1_sha256']
c['same_12_cases'] = [x['id'] for x in v2['cases']] == [x['id'] for x in v1['cases']] == ['C%02d' % i for i in range(1, 13)]
c['v1_classes_recorded_correctly'] = all(a['v1_primary'] == b['primary_class'] for a, b in zip(v2['cases'], v1['cases']))
c['four_separate_columns'] = all(all(k in x for k in v2['columns']) for x in v2['cases'])
c['transferred_evidence_ids_exist'] = all(e.split(':')[-1] in ids for x in v2['cases'] for e in x['evidence'])
# A query may only be marked satisfied (in any form) if every hard constraint is supported.
def ok(x):
    sat = not x['query_satisfied'].startswith('no')
    allsup = all(v.startswith('supported') for v in x['factual_support'].values())
    return (not sat) or allsup or 'ambiguity, not a pass' in x['query_satisfied']
c['no_satisfaction_without_full_support'] = all(ok(x) for x in v2['cases'])
c['no_publication_claimed'] = not any('publication-eligible' in x['rights_state'] and 'not publication-eligible' not in x['rights_state'] for x in v2['cases'])
c['query_satisfied_counts'] = {
    'satisfied_at_observation_time_only': sum(x['query_satisfied'].startswith('satisfied at observation') for x in v2['cases']),
    'not_satisfied_or_unknown': sum(x['query_satisfied'].startswith('no') for x in v2['cases'])}
c['checks_pass'] = all(v for k, v in c.items() if isinstance(v, bool))
print(json.dumps(c, indent=1))
