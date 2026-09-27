import urllib.request,json
from pathlib import Path
P=Path(__file__).resolve().parent/'licenses';P.mkdir(exist_ok=True)
urls={
 'Apache-2.0.txt':'https://www.apache.org/licenses/LICENSE-2.0.txt',
 'CDLA-Permissive-2.0.txt':'https://raw.githubusercontent.com/spdx/license-list-data/main/text/CDLA-Permissive-2.0.txt',
 'CC0-1.0.txt':'https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC0-1.0.txt',
 'ODbL-1.0.txt':'https://raw.githubusercontent.com/spdx/license-list-data/main/text/ODbL-1.0.txt',
 'Foursquare-NOTICE.html':'https://opensource.foursquare.com/places-notice-txt/',
 'Overture-attribution.html':'https://docs.overturemaps.org/attribution/'
}
for fn,u in urls.items():
 try:
  b=urllib.request.urlopen(u,timeout=25).read();(P/fn).write_bytes(b);print(fn,len(b),flush=True)
 except Exception as e: print(fn,str(e),flush=True)
(P/'sources.json').write_text(json.dumps(urls,indent=2),encoding='utf-8')
