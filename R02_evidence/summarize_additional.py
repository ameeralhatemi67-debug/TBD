import json,collections,math
from pathlib import Path
P=Path(__file__).resolve().parent
osm=json.loads((P/'eastern_osm.json').read_text(encoding='utf-8'))['elements']
fields=['name','opening_hours','website','contact:website','phone','fee','charge','duration','reservation','wheelchair','indoor','check_date']
summary={'all_osm_elements':len(osm),'fields':{k:sum(bool(x.get('tags',{}).get(k)) for x in osm) for k in fields},'opening_hours_categories':dict(collections.Counter(next((x['tags'][k] for k in ['amenity','leisure','shop','tourism'] if k in x['tags']),'unknown') for x in osm if x.get('tags',{}).get('opening_hours')))}
rows={a:json.loads((P/(a+'_overture.json')).read_text(encoding='utf-8')) for a in ['eastern','diriyah','al_balad','boulevard']}
qtypes={'museum':['museum','history_museum','science_museum','art_museum','art_gallery'], 'active':['arcade','bowling_alley','pool_billiards','escape_room','go_kart_club','paintball','roller_skating_rink','indoor_playcenter'], 'cafe':['cafe','coffee_shop','tea_room'], 'heritage':['historic_site','history_museum','monument','historic_tower','palace','castle']}
summary['query_pools']={a:{k:sum((r.get('taxonomy') or {}).get('primary') in vals for r in rs) for k,vals in qtypes.items()} for a,rs in rows.items()}
summary['missing_fields_in_overture']=[k for k in ['opening_hours','price','duration','booking','occurrence_date','age_rule','availability','indoor'] if not any(k in r for rs in rows.values() for r in rs)]
summary['unique_ids']=len({r['id'] for rs in rows.values() for r in rs})
(P/'additional_metrics.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
