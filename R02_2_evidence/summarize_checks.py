"""One-off research projections. No network calls and no writes to earlier evidence."""
import hashlib
import json
import math
import struct
from pathlib import Path

P = Path(__file__).resolve().parent
ROOT = P.parent
LOCAL = ROOT / '.local_source_checks'

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def main():
    manifests = [read(P / name) for name in
                 ('http_checks.json', 'public_app_checks.json', 'interpretation_checks.json')]
    requests = [item for manifest in manifests for item in manifest]
    assert len(requests) == 22
    assert len({item['id'] for item in requests}) == 22
    successful = [r for r in requests if r.get('status') == 200]
    assert len(successful) == 19
    for item in successful:
        path = LOCAL / (item['id'] + '.html')
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256_utf8_decoded_content'], item['id']

    branches = read(LOCAL / 'escape_branches.html')
    rooms = read(LOCAL / 'escape_rooms1.html')
    slots = read(LOCAL / 'escape_slots4.html')['slots']
    outbound = read(LOCAL / 'route_demo.html')
    inbound = read(LOCAL / 'route_demo_return.html')
    assert len(branches) == 3 and len(rooms) == 7
    assert all(r['branchId'] == 1 for r in rooms)
    assert rooms[0]['minPlayers'] <= 4 <= rooms[0]['maxPlayers']
    assert rooms[0]['duration'] == 60
    assert len(slots) == 10
    assert sum(s['status'] == 'Available' for s in slots) == 9
    assert all(s['price']['amount'] == '384.00' for s in slots if s['status'] == 'Available')
    assert outbound['code'] == inbound['code'] == 'Ok'

    # Diagnostic nearest-point comparison only; this does not establish entity identity.
    matches = []
    for row in read(ROOT / 'R02_evidence/eastern_overture.json'):
        name = (row.get('names') or {}).get('primary', '') or ''
        if 'escape' not in name.lower() or 'room' not in name.lower():
            continue
        geometry = bytes.fromhex(row['geometry'])
        lon, lat = struct.unpack('<dd' if geometry[0] else '>dd', geometry[5:21])
        distance = math.hypot((lon - 50.1945561) * 111320 * math.cos(math.radians(lat)),
                              (lat - 26.3055142) * 111320)
        matches.append({'overture_id': row['id'], 'name': name, 'lonlat': [lon, lat],
                        'meters_to_operator_branch_1_map_point_approx': round(distance, 1)})

    result = {
        'purpose': 'Bounded research observations, not a licensed production feed or booking guarantee.',
        'formal_http_attempts': 22, 'http_200': 19, 'failed': 3,
        'raw_local_hash_checks_pass': True,
        'branches': [{k: b.get(k) for k in ('id', 'name', 'area', 'mapUrl')} for b in branches],
        'branch_1_room_count': len(rooms),
        'room_1': {k: rooms[0].get(k) for k in ('id', 'name', 'slug', 'branchId', 'minPlayers', 'maxPlayers', 'duration', 'ageRestrictionFrom', 'ageRestrictionTo', 'priceDisplayText')},
        'availability_observation': {
            'room_id': 1, 'players': 4, 'requested_date': '2026-09-27',
            'slots_returned': 10, 'available': 9, 'booked': 1,
            'example': next({k: s[k] for k in ('startTime','endTime','price','status')} for s in slots if 'T18:15:' in s['startTime']),
            'displayed_group_total_sar': 384, 'derived_equal_share_sar': 96,
            'unit_basis': 'Public room-detail client uses selected slot amount as Your total is; no hold or checkout performed.',
            'final_fees_tax_and_admission_not_verified': True,
            'commercial_reuse_rights': 'unresolved',
        },
        'route_observations': {
            'source': 'OSRM public demo; OpenStreetMap contributors; separate from owned place baseline',
            'origin_lonlat': [50.2, 26.3], 'target_operator_point_lonlat': [50.1945561,26.3055142],
            'outbound_seconds': outbound['routes'][0]['duration'],
            'outbound_meters': outbound['routes'][0]['distance'],
            'return_seconds': inbound['routes'][0]['duration'],
            'return_meters': inbound['routes'][0]['distance'],
            'outbound_snaps_meters': [w['distance'] for w in outbound['waypoints']],
            'traffic_parking_accessibility_entrance_not_verified': True,
        },
        'name_matched_overture_records': matches,
    }
    (P / 'measured_observations.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=True, indent=2))

if __name__ == '__main__':
    main()
