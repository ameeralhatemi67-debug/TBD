"""Reproducible descriptive audit; no claims of ground-truth accuracy."""
import json,csv,collections,math,unicodedata,re,struct
from pathlib import Path
P=Path(__file__).resolve().parent
FAMILIES={
 'culture':set('museum history_museum science_museum art_museum art_gallery cultural_center historic_site monument historic_tower palace castle'.split()),
 'activity':set('movie_theater theatre_venue performing_arts_venue amusement_park arcade bowling_alley pool_billiards escape_room race_track go_kart_club paintball roller_skating_rink indoor_playcenter'.split()),
 'local_stop':set('cafe coffee_shop tea_room bookstore gift_shop art_supply_store arts_and_crafts_store'.split())}
def family(r):
 c=(r.get('taxonomy') or {}).get('primary')
 return next((k for k,v in FAMILIES.items() if c in v),None)
def name(r):return (r.get('names') or {}).get('primary','') or ''
def norm(s):return ''.join(x for x in unicodedata.normalize('NFKC',s).casefold() if x.isalnum())
def xy(r):
 g=bytes.fromhex(r['geometry']);return struct.unpack('<dd' if g[0] else '>dd',g[5:21])
def meters(a,b):
 x,y=xy(a); X,Y=xy(b)
 return math.hypot((x-X)*111320*math.cos(math.radians((y+Y)/2)),(y-Y)*111320)
summary={}; flat=[]; suspects=[]
for f in sorted(P.glob('*_overture.json')):
 area=f.stem.replace('_overture',''); rows=json.loads(f.read_text(encoding='utf-8')); pool=[r for r in rows if family(r)]
 keep=[r for r in pool if r.get('confidence') is not None and r['confidence']>=0.8 and r.get('operating_status') not in ['permanently_closed']]
 def stats(rs):
  return {'n':len(rs),'families':dict(collections.Counter(family(r) for r in rs)), 'name':sum(bool(name(r)) for r in rs),'websites':sum(bool(r.get('websites')) for r in rs),'phones':sum(bool(r.get('phones')) for r in rs),'socials':sum(bool(r.get('socials')) for r in rs),'freeform_address':sum(any(a.get('freeform') for a in r.get('addresses') or []) for r in rs),'operating_status':dict(collections.Counter(r.get('operating_status') or 'missing' for r in rs)),'source':dict(collections.Counter(next((s.get('dataset') for s in r.get('sources',[]) if s.get('property')==''),'unknown') for r in rs)),'licenses':dict(collections.Counter(s.get('license') for r in rs for s in r.get('sources',[]) if s.get('property')==''))}
 summary[area]={'all_rows':len(rows),'candidate':stats(pool),'confidence_screened':stats(keep),'confidence_sensitivity':{str(t):sum(r.get('confidence',0)>=t and r.get('operating_status')!='permanently_closed' for r in pool) for t in [0,0.7,0.8,0.9]},'taxonomy_missing':sum(not r.get('taxonomy') for r in rows)}
 groups=collections.defaultdict(list)
 for r in keep:
  groups[norm(name(r))].append(r)
  lon,lat=xy(r)
  flat.append({'area':area,'id':r['id'],'name':name(r),'family':family(r),'category':r['taxonomy']['primary'],'confidence':r['confidence'],'longitude':lon,'latitude':lat,'websites':json.dumps(r.get('websites'),ensure_ascii=False),'phones':json.dumps(r.get('phones'),ensure_ascii=False),'operating_status':r.get('operating_status'),'source':next((s.get('dataset') for s in r['sources'] if s.get('property')==''),None)})
 for ns,grp in groups.items():
  if not ns:continue
  for i,a in enumerate(grp):
   for b in grp[i+1:]:
    d=meters(a,b)
    if d<100:suspects.append({'area':area,'name':name(a),'id_a':a['id'],'id_b':b['id'],'meters':round(d,1)})
 summary[area]['near_same_name_pairs']=sum(s['area']==area for s in suspects)
(P/'overture_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
(P/'category_rules.json').write_text(json.dumps({k:sorted(v) for k,v in FAMILIES.items()},indent=2),encoding='utf-8')
(P/'duplicate_candidates.json').write_text(json.dumps(suspects,ensure_ascii=False,indent=2),encoding='utf-8')
with (P/'screened_candidates.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(flat[0]));w.writeheader();w.writerows(flat)
print(json.dumps(summary,ensure_ascii=True,indent=2))
