"""One-off research measurement, not application code. Uses licensed Overture Places only."""
import json, time, hashlib
from pathlib import Path
from datetime import datetime, timezone
from overturemaps import record_batch_reader

OUT = Path(__file__).resolve().parent
RELEASE = '2026-09-23.1'
BOXES = {
    'eastern': (50.07, 26.28, 50.24, 26.47),
    'diriyah': (46.55, 24.71, 46.585, 24.765),
    'al_balad': (39.17, 21.475, 39.20, 21.505),
    'boulevard': (46.585, 24.755, 46.635, 24.80),
}
manifest = {'release': RELEASE, 'started_utc': datetime.now(timezone.utc).isoformat(), 'areas': {}}
for area, bbox in BOXES.items():
    t = time.monotonic()
    try:
        reader = record_batch_reader('place', bbox=bbox, release=RELEASE, stac=False, connect_timeout=20, request_timeout=60)
        table = reader.read_all()
        # Preserve every source field. WKB geometry is hexadecimal in JSON.
        rows = table.to_pylist()
        payload = json.dumps(rows, ensure_ascii=False, default=lambda x: x.hex() if isinstance(x, bytes) else str(x))
        p = OUT / (area + '_overture.json')
        p.write_text(payload, encoding='utf-8')
        manifest['areas'][area] = {'bbox': bbox, 'rows': len(rows), 'seconds': round(time.monotonic()-t,2), 'columns': table.column_names, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
        print(area, len(rows), round(time.monotonic()-t,2), flush=True)
    except Exception as e:
        manifest['areas'][area] = {'bbox': bbox, 'error': str(e), 'seconds': round(time.monotonic()-t,2)}
        print(area, str(e), flush=True)
    (OUT/'retrieval_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
