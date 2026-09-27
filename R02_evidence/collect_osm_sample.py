"""Bounded ODbL research extracts, kept separate from Overture."""
import json, urllib.request, urllib.parse, time, hashlib
from pathlib import Path
from datetime import datetime, timezone
OUT=Path(__file__).resolve().parent
boxes={'eastern':(50.07,26.28,50.24,26.47),'diriyah':(46.55,24.71,46.585,24.765),'al_balad':(39.17,21.475,39.20,21.505),'boulevard':(46.585,24.755,46.635,24.80)}
manifest={'source':'https://overpass.private.coffee/api/interpreter','retrieved_utc':datetime.now(timezone.utc).isoformat(),'license':'ODbL 1.0; copyright OpenStreetMap contributors','areas':{}}
for area,(w,s,e,n) in boxes.items():
    b=f'({s},{w},{n},{e})'
    selectors=['[tourism~"^(museum|gallery|attraction|theme_park|artwork)$"]','[amenity~"^(cafe|cinema|theatre|arts_centre)$"]','[leisure~"^(bowling_alley|escape_game|amusement_arcade|sports_centre|park)$"]','[shop~"^(books|art|craft|coffee|gift)$"]']
    q='[out:json][timeout:60];('+''.join('nwr'+x+b+';' for x in selectors)+');out center tags;'
    t=time.monotonic()
    try:
        req=urllib.request.Request(manifest['source'],data=urllib.parse.urlencode({'data':q}).encode(),headers={'User-Agent':'R02DiscoveryResearch/1.0 (bounded research sample)'})
        raw=urllib.request.urlopen(req,timeout=90).read()
        data=json.loads(raw)
        p=OUT/(area+'_osm.json');p.write_bytes(raw)
        manifest['areas'][area]={'query':q,'count':len(data.get('elements',[])),'seconds':round(time.monotonic()-t,2),'remark':data.get('remark'),'timestamp_osm_base':data.get('osm3s',{}).get('timestamp_osm_base'),'sha256':hashlib.sha256(raw).hexdigest()}
        print(area,manifest['areas'][area],flush=True)
    except Exception as e:
        manifest['areas'][area]={'query':q,'error':str(e),'seconds':round(time.monotonic()-t,2)}
        print(area,str(e),flush=True)
    (OUT/'osm_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
