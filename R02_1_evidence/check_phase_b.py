"""Consistency check for Phase B evidence. Verifies structure only, not real-world truth."""
import json, collections
from pathlib import Path
P = Path(__file__).resolve().parent
o = json.loads((P / 'case_outcomes.json').read_text(encoding='utf-8'))
ids = [c['id'] for c in o['cases']]
dist = collections.Counter(c['primary_class'] for c in o['cases'])
supported_cases = [c['id'] for c in o['cases'] if c['primary_class'] == 'supported_qualified_shortlist']
ok_supported = all(all(v.startswith('supported') for v in c['constraints'].values()) for c in o['cases'] if c['id'] in supported_cases)
pools = json.loads((P / 'case_pools.json').read_text(encoding='utf-8'))
checks = {'denominator_12': ids == ['C%02d' % i for i in range(1, 13)],
          'classes_valid': all(c['primary_class'] in o['classes'] for c in o['cases']),
          'shortlist_cases_have_all_hard_constraints_supported': ok_supported,
          'pool_counts': pools['counts'], 'primary_class_distribution': dict(dist)}
CATEGORY_LEVEL = {'museum', 'indoor', 'escape_room', 'not_food', 'not_cafe', 'indoor_cultural'}
prac = [v for c in o['cases'] for k, v in c['constraints'].items() if k not in CATEGORY_LEVEL]
checks['practical_hard_constraints'] = {'total': len(prac), 'supported_any': sum(v.startswith('supported') for v in prac)}
checks['checks_pass'] =checks['denominator_12'] and checks['classes_valid'] and ok_supported and sum(dist.values()) == 12
print(json.dumps(checks, indent=1))
