import json,hashlib,re,csv
from pathlib import Path
P=Path(__file__).resolve().parent
root=P.parent
m=json.loads((P/'retrieval_manifest.json').read_text(encoding='utf-8'))
checks={}
total=0
for area,meta in m['areas'].items():
 p=P/(area+'_overture.json');rows=json.loads(p.read_text(encoding='utf-8'));total+=len(rows)
 checks[area]={'hash_matches':hashlib.sha256(p.read_bytes()).hexdigest()==meta['sha256'],'row_count_matches':len(rows)==meta['rows']}
s=json.loads((P/'overture_summary.json').read_text(encoding='utf-8'))
checks['total_records']=total
checks['candidate_total']=sum(a['candidate']['n'] for a in s.values())
checks['screened_total']=sum(a['confidence_screened']['n'] for a in s.values())
checks['candidate_website_total']=sum(a['candidate']['websites'] for a in s.values())
with (P/'screened_candidates.csv').open(encoding='utf-8-sig') as f:checks['csv_data_rows']=len(list(csv.DictReader(f)))
text=(root/'R02_Automated_Coverage_and_Feasibility_Audit.md').read_text(encoding='utf-8')
links=re.findall(r'\]\(([^)]+)\)',text)
checks['missing_local_links']=[x for x in links if not x.startswith(('https://','http://','#')) and not (root/x.strip('<>')).exists()]
checks['numbered_sections']=[int(x) for x in re.findall(r'^## (\d+)\.',text,re.M)]
checks['checks_pass']=all(v['hash_matches'] and v['row_count_matches'] for k,v in checks.items() if k in m['areas']) and total==13764 and checks['candidate_total']==1379 and checks['screened_total']==checks['csv_data_rows']==438 and not checks['missing_local_links'] and checks['numbered_sections']==list(range(1,30))
(P/'audit_validation.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print(json.dumps(checks,indent=2))
