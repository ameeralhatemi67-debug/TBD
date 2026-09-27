"""Structural checks for the v2 case pass (R04 v0.2). Verifies consistency, not real-world truth.
Exits nonzero if any check fails.

Integrity policy (27 Sep 2026, after Sol's Windows checkout reported a false mismatch):
the v1 preservation check hashes NORMALIZED TEXT (UTF-8, BOM stripped, CRLF/CR -> LF), because
.gitattributes lets Git convert line endings for R02_1_evidence/ text files on checkout. This
verifies the recorded content, not exact bytes. Raw-source evidence (R02_evidence/**, marked -text)
keeps its exact-byte hashes in R02_evidence/validate_audit.py; this policy does not apply there."""
import hashlib, json, sys
from pathlib import Path
P = Path(__file__).resolve().parent
v2 = json.loads((P / 'case_outcomes_v2_2026-09-27.json').read_text(encoding='utf-8'))
def normalized_text_sha256(raw):
    t = raw.decode('utf-8-sig').replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()
v1_bytes = (P / 'case_outcomes.json').read_bytes()
v1 = json.loads(v1_bytes)
ids = {r['id'] for f in ('http_checks', 'public_app_checks', 'interpretation_checks')
       for r in json.loads((P.parent / 'R02_2_evidence' / f'{f}.json').read_text(encoding='utf-8-sig'))}
c = {}
c['v1_unchanged_normalized_text'] = normalized_text_sha256(v1_bytes) == v2['v1_sha256']
lf = v1_bytes.decode('utf-8-sig').replace('\r\n', '\n').encode('utf-8')
c['policy_selftest_lf_crlf_equivalent'] = normalized_text_sha256(lf) == normalized_text_sha256(lf.replace(b'\n', b'\r\n'))
c['policy_selftest_content_change_detected'] = normalized_text_sha256(lf) != normalized_text_sha256(lf + b' ')
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
# v3 pass (27 Sep night): C02/C12 revised; must preserve v2 and obey the same rules.
v3p = P / 'case_outcomes_v3_2026-09-27.json'
if v3p.exists():
    v3 = json.loads(v3p.read_text(encoding='utf-8'))
    c['v3_preserves_v2_normalized_text'] = normalized_text_sha256((P / 'case_outcomes_v2_2026-09-27.json').read_bytes()) == v3['v2_sha256_normalized']
    c['v3_same_12_cases'] = [x['id'] for x in v3['cases']] == ['C%02d' % i for i in range(1, 13)]
    c['v3_changes_only_c02_c12'] = sorted(x['id'] for x in v3['cases'] if x['changed_in_v3']) == ['C02', 'C12'] and all(
        a == {k: v for k, v in b.items() if k != 'changed_in_v3'} for a, b in zip(v2['cases'], v3['cases']) if not b['changed_in_v3'])
    c['v3_no_satisfaction_claimed'] = not any(x['query_satisfied'].startswith(('yes', 'satisfied')) for x in v3['cases'])
    c['v3_transferred_evidence_ids_exist'] = all(e.split(':')[-1] in ids for x in v3['cases'] for e in x['evidence'])
c['checks_pass'] = all(v for k, v in c.items() if isinstance(v, bool))
print(json.dumps(c, indent=1))
sys.exit(0 if c['checks_pass'] else 1)
