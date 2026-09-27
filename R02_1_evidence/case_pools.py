"""Phase B candidate pools for the locked cases (PROJECT_START_REVIEW.md s9).
Reads the retained R02 Eastern Overture extract only; writes case_pools.json. No network."""
import json, math, struct, collections
from pathlib import Path
P = Path(__file__).resolve().parent; R02 = P.parent / 'R02_evidence'
ORIGIN = (50.200, 26.300)   # synthetic origin from R02 route_results.json
RADIUS_KM = 12.0            # straight-line screen only; NOT a travel-time claim
rules = json.loads((R02 / 'category_rules.json').read_text())
fam = {c: k for k, v in rules.items() for c in v}
def xy(r):
    g = bytes.fromhex(r['geometry']); return struct.unpack('<dd' if g[0] else '>dd', g[5:21])
def km(a, b):
    return math.hypot((a[0]-b[0])*111.32*math.cos(math.radians((a[1]+b[1])/2)), (a[1]-b[1])*111.32)
rows = json.loads((R02 / 'eastern_overture.json').read_text(encoding='utf-8'))
out = collections.defaultdict(list)
for r in rows:
    cat = (r.get('taxonomy') or {}).get('primary'); f = fam.get(cat)
    if not f: continue
    d = km(ORIGIN, xy(r))
    if d > RADIUS_KM: continue
    src = next((s['dataset'] for s in r['sources'] if s.get('property') == ''), None)
    out[f].append({'id': r['id'], 'name': (r.get('names') or {}).get('primary'), 'category': cat,
                   'km_straight': round(d, 2), 'confidence': round(r['confidence'], 2), 'source': src,
                   'has_website': bool(r.get('websites'))})
res = {'origin': ORIGIN, 'radius_km_straight_line': RADIUS_KM,
       'counts': {k: len(v) for k, v in out.items()},
       'category_counts': {k: dict(collections.Counter(x['category'] for x in v)) for k, v in out.items()},
       'culture': sorted(out['culture'], key=lambda x: x['km_straight']),
       'activity': sorted(out['activity'], key=lambda x: x['km_straight'])}
(P / 'case_pools.json').write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps({k: res[k] for k in ('counts', 'category_counts')}, ensure_ascii=False, indent=1))
