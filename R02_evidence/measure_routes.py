"""Eight bounded demo requests. No traffic, bookings, or production service."""
import json,urllib.request,time,struct,math
from pathlib import Path
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
CASES={
 'eastern':((50.20,26.30),['5edcb8c0-d1d9-4ee9-bf5c-38e43cad59de','98ea1d61-7290-4533-bafa-e844a503d48f','b4fdc657-c04d-44df-a47c-8edd7a87cc53']),
 'diriyah':((46.579,24.738),['bbabefa5-f1cb-41c9-87b2-fa5db98dbead','e268a49d-22bc-4f8a-8aae-cdeb93d3ea9e','196c0f45-a92f-40aa-a0c3-54c72802f097']),
 'al_balad':((39.184,21.488),['e7803308-ae1b-4a19-82c2-1fff5007b122','bb4bc78b-dbc3-4eee-b576-f4840a89c36d','0f5dd241-fc90-4da9-9c74-74a18140220a']),
 'boulevard':((46.608,24.767),['6c08ad20-6369-47a1-b7c4-1606b62cb068','d3221d77-d202-49f2-836a-df949f630e56','ae23ae28-4886-4e1b-bf6c-827b1f1ef509'])}
log=[]
for area,(origin,ids) in CASES.items():
 rows={r['id']:r for r in json.loads((P/(area+'_overture.json')).read_text(encoding='utf-8'))}
 coords=[origin]+[struct.unpack('<dd',bytes.fromhex(rows[i]['geometry'])[5:21]) for i in ids]
 for mode in ['car','foot']:
  url='https://routing.openstreetmap.de/routed-'+mode+'/table/v1/driving/'+ ';'.join(f'{x:.6f},{y:.6f}' for x,y in coords)+'?sources=0&destinations=1;2;3&annotations=duration,distance'
  entry={'area':area,'mode':mode,'url':url,'origin':origin,'targets':[{'id':i,'name':rows[i]['names']['primary'],'coordinates':coords[j+1]} for j,i in enumerate(ids)],'timestamp_utc':datetime.now(timezone.utc).isoformat()}
  t=time.monotonic()
  try:
   req=urllib.request.Request(url,headers={'User-Agent':'R02DiscoveryResearch/1.0 (eight-request research test)'})
   entry['response']=json.load(urllib.request.urlopen(req,timeout=35))
  except Exception as e:entry['error']=str(e)
  entry['seconds']=round(time.monotonic()-t,3);log.append(entry)
  (P/'route_results.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
  print(area,mode,entry.get('error') or entry['response'].get('durations'),entry['seconds'],flush=True)
  time.sleep(1.1)
