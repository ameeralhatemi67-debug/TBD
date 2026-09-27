"""R02.3 bounded collector (research only). Python 3.9+, standard library only.
Usage:
  python collect_run.py --dry-run [--pass full|slots]   list planned requests, no network
  python collect_run.py --selftest                       offline checks of classification and safety rules
  python collect_run.py --pass full|slots                one real run into runs/<Riyadh-date>_<pass>/
'full' = all sources (morning pass); 'slots' = repeated-session slot re-queries only (later pass same date).
Writes manifest.json (requests), observations.json (facts), derived.json (calculations). Raw bodies go to
../.local_source_checks/R02_3/<run>/ (git-ignored) and are never published. Refuses to overwrite any run.
Never books, holds, logs in, submits forms, or pays: GET requests to listed URLs only."""
import argparse, hashlib, json, re, sys, time, urllib.error, urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RIYADH = timezone(timedelta(hours=3))
PLAN = json.loads((HERE / 'plan.json').read_text(encoding='utf-8'))
L = PLAN['limits']
TIME_RE = re.compile(r'\b\d{1,2}[:.]\d{2}\b')

def app_shell_hash():
    for r in json.loads((ROOT / 'R02_2_evidence' / 'http_checks.json').read_text(encoding='utf-8-sig')):
        if r['id'] == 'escape_main':
            return r.get('sha256_utf8_decoded_content')

# ------------------------------------------------------------ classification (pure, self-tested)
def classify(kind, status, body, shell_hash):
    """Returns (classification, parsed_or_None). kind: branches|rooms|slots|html|osrm."""
    if status is None:
        return 'retrieval_error', None
    if status != 200:
        return 'http_error', None
    text = body.decode('utf-8-sig', errors='replace')
    if kind == 'html':
        if hashlib.sha256(text.encode('utf-8')).hexdigest() == shell_hash:
            return 'html_shell', None
        if len(text.strip()) < 200:
            return 'error_body', None
        return 'valid_html', None
    try:
        data = json.loads(text)
    except ValueError:
        low = text.lstrip().lower()
        if low.startswith('<!doctype') or low.startswith('<html'):
            return 'html_shell_or_page', None
        return ('error_body' if len(text.strip()) < 200 else 'malformed'), None
    if not isinstance(data, (dict, list)):
        return 'error_body', None                             # e.g. body "404" parses as a JSON number
    ok = {
        'branches': lambda d: isinstance(d, list) and all(isinstance(x, dict) and 'id' in x and 'name' in x for x in d),
        'rooms': lambda d: isinstance(d, list) and all(isinstance(x, dict) and {'id', 'branchId', 'minPlayers', 'maxPlayers', 'duration'} <= set(x) for x in d),
        'slots': lambda d: isinstance(d, dict) and isinstance(d.get('slots'), list) and all(
            isinstance(s, dict) and {'startTime', 'endTime', 'status'} <= set(s) for s in d['slots']),
        'osrm': lambda d: isinstance(d, dict) and d.get('code') == 'Ok' and d.get('routes'),
    }[kind](data)
    return ('valid_json' if ok else 'unsupported_schema'), (data if ok else None)

def inventory_completeness(data):
    """The slots API documents no completeness guarantee. Never report 'complete' from a list alone."""
    keys = set(data) - {'slots'}
    if keys & {'page', 'pageSize', 'total', 'next', 'hasMore', 'cursor'}:
        return 'partial_or_paginated', f'pagination keys present: {sorted(keys)}'
    return 'unknown', 'no documented completeness guarantee; no pagination keys observed; empty or short lists are not proof of no sessions'

# ------------------------------------------------------------ run planning
def previous_room_resolution():
    for m in sorted((HERE / 'runs').glob('*/manifest.json')) if (HERE / 'runs').exists() else []:
        r = json.loads(m.read_text(encoding='utf-8')).get('resolved_rooms')
        if r:
            return r
    return None

def plan_requests(pass_name, run_date, rooms):
    api = PLAN['escape']['api']; reqs = []
    if pass_name == 'full':
        reqs += [('escape_branches', 'branches', f'{api}/branches')]
        reqs += [(f'escape_rooms_b{b}', 'rooms', f'{api}/rooms?branchId={b}') for b in PLAN['escape']['branches']]
        reqs += [(p['id'], 'html', p['url']) for p in PLAN['static_pages']]
        reqs += [(r['id'], 'osrm', r['url']) for r in PLAN['routes']]
        reqs += [(f"slots_r{PLAN['escape']['same_day_room']}_p{PLAN['escape']['same_day_party']}_{run_date}", 'slots',
                  f"{api}/availability/slots?roomId={PLAN['escape']['same_day_room']}&date={run_date}&players={PLAN['escape']['same_day_party']}")]
    for room in rooms:
        for d in PLAN['repeated_session_dates']:
            for p in PLAN['repeated_session_parties']:
                reqs.append((f'slots_r{room}_p{p}_{d}', 'slots', f'{api}/availability/slots?roomId={room}&date={d}&players={p}'))
    return reqs

# ------------------------------------------------------------ network (only in a real run)
def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'TBD-research-bounded/1 (no booking; contact via repository owner)'})
    try:
        with urllib.request.urlopen(req, timeout=L['timeout_s']) as r:
            return r.status, r.read(), dict(r.headers), None
    except urllib.error.HTTPError as e:
        return e.code, e.read() or b'', dict(e.headers or {}), f'HTTP {e.code}'
    except Exception as e:                                   # timeout, DNS, TLS, connection
        return None, b'', {}, f'{type(e).__name__}: {e}'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pass', dest='pass_name', choices=['full', 'slots'], default='full')
    ap.add_argument('--dry-run', action='store_true'); ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    now_utc = datetime.now(timezone.utc); run_date = now_utc.astimezone(RIYADH).date().isoformat()
    if run_date >= min(PLAN['repeated_session_dates']):
        sys.exit(f'refusing: run date {run_date} is not before the repeated session dates')
    prev = previous_room_resolution()
    rooms = [prev['branch1_primary'], prev['branch1_second'], prev['branch3']] if prev else [PLAN['escape']['fixed_rooms']['branch1_primary']]
    if not prev and a.pass_name == 'slots':
        sys.exit('refusing: run a full pass first so the second branch-1 room and the branch-3 room are resolved')
    reqs = plan_requests(a.pass_name, run_date, rooms)
    print(f'{len(reqs)} planned requests (limit {L["max_attempts_per_date"]} attempts per date incl. retries); rooms known now: {rooms}')
    if a.dry_run:
        for r in reqs: print('  ', r[0], r[2])
        if not prev: print('   + up to 8 more slot requests after rooms are resolved in this full pass')
        return
    out = HERE / 'runs' / f'{run_date}_{a.pass_name}'
    priv = ROOT / '.local_source_checks' / 'R02_3' / out.name
    if out.exists() or priv.exists():
        sys.exit(f'refusing to overwrite existing run {out}')
    out.mkdir(parents=True); priv.mkdir(parents=True)
    run(a.pass_name, run_date, reqs, prev, out, priv)

def run(pass_name, run_date, reqs, prev, out, priv):
    shell = app_shell_hash(); manifest = {'run': out.name, 'pass': pass_name, 'run_date_riyadh': run_date,
        'plan_sha256': hashlib.sha256((HERE / 'plan.json').read_bytes()).hexdigest(), 'rights_state': PLAN['rights_state'],
        'resolved_rooms': prev, 'requests': [], 'stopped': None}
    obs, derived = {}, {}
    # the 40-attempt ceiling is per date across passes: count attempts already made today
    attempts = sum(len(json.loads(m.read_text(encoding='utf-8'))['requests'])
                   for m in (HERE / 'runs').glob(f'{run_date}_*/manifest.json') if m.parent != out)
    manifest['prior_attempts_same_date'] = attempts
    host_fail, last_hit = {}, {}
    queue = list(reqs)
    while queue:
        rid, kind, url = queue.pop(0)
        host = urlparse(url).hostname
        if host_fail.get(host, 0) >= L['stop_host_after_failures']:
            manifest['requests'].append({'id': rid, 'url': url, 'skipped': 'host stopped after repeated failures'}); continue
        for attempt in (1, 2):
            if attempts >= L['max_attempts_per_date']:
                manifest['stopped'] = 'attempt limit reached'; queue = []; break
            gap = L['osrm_spacing_s'] if kind == 'osrm' else L['same_host_spacing_s']
            wait = last_hit.get(host, 0) + gap - time.monotonic()
            if wait > 0: time.sleep(wait)
            attempts += 1; t0 = datetime.now(timezone.utc)
            status, body, headers, err = fetch(url); last_hit[host] = time.monotonic()
            cls, data = classify(kind, status, body, shell)
            rec = {'id': rid, 'kind': kind, 'url': url, 'attempt': attempt, 'observed_utc': t0.isoformat(),
                   'query_time_riyadh': t0.astimezone(RIYADH).isoformat(), 'status': status, 'error': err,
                   'classification': cls, 'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest() if body else None,
                   'server_date': headers.get('Date'), 'last_modified': headers.get('Last-Modified')}
            if body: (priv / f'{rid}.a{attempt}.body').write_bytes(body)
            manifest['requests'].append(rec)
            if status in L['stop_all_on_status']:
                manifest['stopped'] = f'access denial or rate-limit signal (HTTP {status}) on {host}'; queue = []; break
            retryable = status is None or (status is not None and status >= 500)
            if cls in ('valid_json', 'valid_html') or not retryable or attempt == 2:
                if cls not in ('valid_json', 'valid_html'): host_fail[host] = host_fail.get(host, 0) + 1
                break
            host_fail[host] = host_fail.get(host, 0) + 1; time.sleep(30)
        if data is not None or cls == 'valid_html':
            project(rid, kind, data, body, obs, derived, rec)
        if rid == 'escape_rooms_b3' and data is not None and prev is None:
            prev = resolve_rooms(obs); manifest['resolved_rooms'] = prev
            queue += plan_requests('slots', run_date, [prev['branch1_second'], prev['branch3']]) if prev else []
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
    (out / 'observations.json').write_text(json.dumps({'label': 'FACTUAL PROJECTIONS of operator/provider responses; research only; rights unresolved', **obs}, ensure_ascii=False, indent=1), encoding='utf-8')
    (out / 'derived.json').write_text(json.dumps({'label': 'DERIVED CALCULATIONS, not operator statements', **derived}, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'wrote {out} ({attempts} attempts); stopped={manifest["stopped"]}')

def resolve_rooms(obs):
    b1 = sorted(r['id'] for r in obs.get('escape_rooms_b1', []) if r['branchId'] == 1)
    b3 = sorted(r['id'] for r in obs.get('escape_rooms_b3', []) if r['branchId'] == 3)
    if 1 not in b1 or len(b1) < 2 or not b3:
        return None
    return {'branch1_primary': 1, 'branch1_second': [x for x in b1 if x != 1][0], 'branch3': b3[0], 'rule': PLAN['escape']['fixed_rooms']}

def project(rid, kind, data, body, obs, derived, rec):
    """Small factual projections only. No descriptions, images, scripts, or customer data."""
    if kind == 'branches':
        obs[rid] = [{k: b.get(k) for k in ('id', 'name', 'area', 'mapUrl')} for b in data]
    elif kind == 'rooms':
        obs[rid] = [{k: r.get(k) for k in ('id', 'name', 'slug', 'branchId', 'minPlayers', 'maxPlayers', 'duration',
                     'ageRestrictionFrom', 'ageRestrictionTo', 'priceDisplayText')} for r in data]
    elif kind == 'slots':
        comp, basis = inventory_completeness(data)
        slots = [{'startTime': s.get('startTime'), 'endTime': s.get('endTime'), 'status': s.get('status'),
                  'slot_id': s.get('id'), 'amount': (s.get('price') or {}).get('amount'), 'currency': (s.get('price') or {}).get('currency')}
                 for s in data['slots']]
        obs[rid] = {'observed_utc': rec['observed_utc'], 'completeness': comp, 'completeness_basis': basis, 'slots': slots}
        party = int(rid.split('_p')[1].split('_')[0])
        derived[rid] = [{'startTime': s['startTime'], 'equal_share_if_amount_is_party_total': round(float(s['amount']) / party, 2)}
                        for s in slots if s['amount'] not in (None, '')]
    elif kind == 'osrm':
        r0 = data['routes'][0]
        obs[rid] = {'duration_s': r0.get('duration'), 'distance_m': r0.get('distance'),
                    'snap_m': [w.get('distance') for w in data.get('waypoints', [])], 'label': 'OSRM demo model output; traffic unverified'}
    elif kind == 'html':
        text = re.sub(r'<[^>]+>', '\n', body.decode('utf-8', errors='replace'))
        lines = [re.sub(r'\s+', ' ', l).strip() for l in text.split('\n')]
        meta = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]{0,400})"', body.decode('utf-8', errors='replace'))
        obs[rid] = {'time_bearing_lines': [l[:120] for l in lines if TIME_RE.search(l)][:20],
                    'meta_description': meta.group(1)[:300] if meta else None,
                    'note': 'short factual lines only; full page kept local'}

def selftest():
    shell = 'x' * 64; checks = []
    def t(name, got, want): checks.append((name, got == want, got, want))
    t('network error -> retrieval_error', classify('slots', None, b'', shell)[0], 'retrieval_error')
    t('HTTP 404 -> http_error', classify('slots', 404, b'nope', shell)[0], 'http_error')
    t('HTML returned for JSON endpoint -> html_shell_or_page', classify('rooms', 200, b'<!doctype html><div id=root></div>', shell)[0], 'html_shell_or_page')
    t('short non-JSON body -> error_body', classify('branches', 200, b'404', shell)[0], 'error_body')
    t('long non-JSON body -> malformed', classify('branches', 200, b'x' * 300, shell)[0], 'malformed')
    t('JSON with wrong shape -> unsupported_schema', classify('slots', 200, b'{"items": []}', shell)[0], 'unsupported_schema')
    ok = json.dumps({'slots': [{'startTime': 'a', 'endTime': 'b', 'status': 'Available'}]}).encode()
    t('valid slots -> valid_json', classify('slots', 200, ok, shell)[0], 'valid_json')
    t('empty slot list is valid JSON but completeness unknown', inventory_completeness({'slots': []})[0], 'unknown')
    t('pagination keys -> partial_or_paginated', inventory_completeness({'slots': [], 'next': 'x'})[0], 'partial_or_paginated')
    body = b'<html>' + b'a' * 300
    t('page equal to known app shell -> html_shell', classify('html', 200, body, hashlib.sha256(body.decode().encode()).hexdigest())[0], 'html_shell')
    t('tiny HTML body -> error_body', classify('html', 200, b'404', shell)[0], 'error_body')
    reqs = plan_requests('full', '2026-09-30', [1, 2, 7])
    t('full pass with resolved rooms stays within 40 attempts', len(reqs) <= L['max_attempts_per_date'], True)
    t('slots pass = 3 rooms x 2 dates x 2 parties', len(plan_requests('slots', '2026-09-30', [1, 2, 7])), 12)
    t('full pass (15 + 8) plus slots pass (12) on one date fit within 40', len(plan_requests('full', '2026-09-30', [1])) + 8 + 12 <= L['max_attempts_per_date'], True)
    t('no booking/hold/checkout/login paths planned', any(re.search(r'book|hold|checkout|login|payment|reserve', u, re.I) for _, _, u in reqs), False)
    t('rights state carried as unresolved', PLAN['rights_state'].startswith('UNRESOLVED'), True)
    t('app shell hash available from R02.2 manifest', bool(app_shell_hash()), True)
    for n, okk, g, w in checks: print(('PASS ' if okk else 'FAIL ') + n + ('' if okk else f' got={g} want={w}'))
    n = sum(c[1] for c in checks); print(f'{n}/{len(checks)} selftests pass (offline; no network)')
    return sys.exit(0 if n == len(checks) else 1)

if __name__ == '__main__':
    main()
