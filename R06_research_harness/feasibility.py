"""R06 research harness: offline constraint evaluation over labeled observations.
Research code only. No network, no storage, no UI. Implements R04 v0.2 rules so they can be tested.

States used: supported | contradicted | unknown | conflict | boundary_ambiguity, plus the
explicitly named variants documented on each function. Callers: check_harness.py only.

v2 (27 Sep 2026, after Sol's review of 468c1cc): inventory completeness, deadline meaning and
return travel, dated hours intervals, freshness for every capacity status, identity corroboration,
input validation, and a guard against unevaluated constraint sets. See R06 section 2 change log."""
import math
from datetime import date, datetime, time, timedelta, timezone

def _require(cond, msg):
    if not cond:
        raise ValueError(msg)

def _aware(d, name):
    _require(isinstance(d, datetime) and d.tzinfo is not None, f'{name} must be a timezone-aware datetime')

def meters(a, b):
    """Approximate distance between (lon, lat) points."""
    return math.hypot((a[0]-b[0]) * 111320 * math.cos(math.radians((a[1]+b[1]) / 2)), (a[1]-b[1]) * 111320)

# ---------------------------------------------------------------- identity

def _norm(s):
    return ''.join(ch for ch in (s or '').casefold() if ch.isalnum())

def link_record_to_branch(record, branches, max_m, operator):
    """Distance proposes candidates; corroborating identity evidence is required before a link that
    transfers facts. record: {'pt', 'name', 'websites'}; branches: [{'id', 'pt' or None}];
    operator: {'names': [...], 'domains': [...]}.
    Returns (state, branch_id, detail). States:
      provisional_link                 one located branch within max_m AND name/domain corroboration
      candidate_only_no_corroboration  nearby branch but nothing ties the record to the operator
      undecided                        several nearby branches, or corroborated but not near any located
                                       branch while some branch has no coordinates"""
    _require(max_m > 0, 'max_m must be positive')
    names = [_norm(n) for n in operator['names']]
    name_ok = any(n and n in _norm(record.get('name')) for n in names)
    domain_ok = any(d in (w or '').casefold() for d in operator['domains'] for w in (record.get('websites') or []))
    corroborated = name_ok or domain_ok
    near = sorted((meters(record['pt'], b['pt']), b['id']) for b in branches if b.get('pt'))
    near = [x for x in near if x[0] <= max_m]
    unlocated = [b['id'] for b in branches if not b.get('pt')]
    detail = {'name_match': name_ok, 'domain_match': domain_ok, 'unlocated_branches': unlocated}
    if len(near) == 1 and corroborated:
        return 'provisional_link', near[0][1], dict(detail, meters=round(near[0][0], 1))
    if len(near) == 1:
        return 'candidate_only_no_corroboration', None, dict(detail, meters=round(near[0][0], 1))
    reason = 'several_nearby_branches' if len(near) > 1 else ('possible_unlocated_branch' if corroborated and unlocated else 'no_nearby_branch')
    return 'undecided', None, dict(detail, reason=reason)

# ---------------------------------------------------------------- price

OPS = {'lt', 'le', 'under_ambiguous'}

def price_check(observations, op, limit, phrase_unit, party_size):
    """observations: [{'amount','unit':'per_person'|'party_total','kind':'displayed'|'derived'|'final'}].
    op: 'lt' = explicitly resolved strict (equality contradicts); 'le' = inclusive ("at most");
    'under_ambiguous' = the phrase "under" not yet resolved, so equality is a boundary_ambiguity.
    Disagreeing observations are a conflict unless every value gives the same outcome.
    Note: 'supported' here compares the observed amount only; a displayed or derived amount is not
    a verified final payable charge (callers must keep that caveat)."""
    _require(op in OPS, f'unsupported comparison operator {op!r}')
    _require(isinstance(limit, (int, float)) and limit >= 0, 'limit must be a non-negative number')
    _require(party_size is None or (isinstance(party_size, int) and party_size > 0), 'party_size must be a positive integer or None')
    if not observations:
        return 'unknown'
    outcomes = set()
    for o in observations:
        amt = o['amount']
        _require(amt >= 0, 'amount must be non-negative')
        if o['unit'] != phrase_unit:
            if party_size is None:
                outcomes.add('unknown'); continue
            amt = amt / party_size if o['unit'] == 'party_total' else amt * party_size
        if amt == limit and op == 'under_ambiguous':
            outcomes.add('boundary_ambiguity')
        elif amt < limit or (op == 'le' and amt == limit):
            outcomes.add('supported')
        else:
            outcomes.add('contradicted')
    if len(outcomes) == 1:
        return outcomes.pop()
    return 'unknown' if 'unknown' in outcomes else 'conflict'

def representation_conflict(values):
    """values: [{'channel': 'body'|'metadata'|'lang:ar'|..., 'value': x}]. Any disagreement is a conflict."""
    return 'conflict' if len({v['value'] for v in values}) > 1 else ('agree' if values else 'none')

def is_shared_app_shell(url_hashes):
    """Different URLs returning identical content cannot identify distinct offerings."""
    return len(set(url_hashes.values())) < len(url_hashes)

# ---------------------------------------------------------------- hours (dated intervals)

def _tz(offset):
    sign = 1 if offset[0] == '+' else -1
    h, m = offset[1:].split(':')
    return timezone(sign * timedelta(hours=int(h), minutes=int(m)))

def hours_state(claims, visit_start, visit_end):
    """claims: [{'kind':'regular'|'exception','valid_from':date,'valid_to':date,'open':time,'close':time,
    'utc_offset':'+03:00','scope_clear':bool}]. A close <= open means the opening runs past midnight.
    Each operating date's interval is built from that date's exception, else its regular claim.
    supported     some dated opening interval contains the whole visit
    contradicted  every date that could contain the visit has an admissible claim, and none contains it
    unknown       any such date lacks an admissible claim (no guessing across unknown dates)
    conflict      two admissible claims of the same kind disagree for one date"""
    _aware(visit_start, 'visit_start'); _aware(visit_end, 'visit_end')
    _require(visit_start < visit_end, 'visit_start must be before visit_end')
    adm = [c for c in claims if c['scope_clear']]
    if not adm:
        return 'unknown'
    tz = _tz(adm[0]['utc_offset'])
    _require(all(c['utc_offset'] == adm[0]['utc_offset'] for c in adm), 'mixed utc offsets not supported')
    s, e = visit_start.astimezone(tz), visit_end.astimezone(tz)
    d, last, intervals, any_missing = s.date() - timedelta(days=1), e.date(), [], False
    while d <= last:
        day = [c for c in adm if c['valid_from'] <= d <= c['valid_to']]
        chosen = [c for c in day if c['kind'] == 'exception'] or [c for c in day if c['kind'] == 'regular']
        if not chosen:
            any_missing = True
        elif len({(c['open'], c['close']) for c in chosen}) > 1:
            return 'conflict'
        else:
            c = chosen[0]
            o = datetime.combine(d, c['open'], tz)
            cl = datetime.combine(d + timedelta(days=1 if c['close'] <= c['open'] else 0), c['close'], tz)
            intervals.append((o, cl))
        d += timedelta(days=1)
    if any(o <= s and e <= cl for o, cl in intervals):
        return 'supported'
    return 'unknown' if any_missing else 'contradicted'

# ---------------------------------------------------------------- sessions

DEADLINE_KINDS = {'activity_end', 'back_at_origin'}

def _timing(slot, w):
    """Immutable timing check for one session. Unknown legs or buffers are not treated as zero:
    a slot that fails even with zero for every unknown is contradicted; one that passes only if
    unknowns are small is unknown."""
    out, ret = w.get('outbound_s'), w.get('return_s')
    before, after = w.get('buffer_before_s'), w.get('buffer_after_s')
    need_return = w['deadline_kind'] == 'back_at_origin'
    lower_arrive = w['depart'] + timedelta(seconds=(out or 0) + (before or 0))
    lower_finish = slot['end'] + (timedelta(seconds=(ret or 0) + (after or 0)) if need_return else timedelta(0))
    if slot['start'] < lower_arrive or lower_finish > w['deadline']:
        return 'contradicted'
    required = [out, before] + ([ret, after] if need_return else [])
    return 'unknown' if any(v is None for v in required) else 'supported'

def session_fit(inventory, window, query_at, max_quote_age_s):
    """inventory: {'response_ok': bool, 'complete': True|False|None, 'observed_at': aware dt,
    'slots': [{'start','end','status'}]}; window: {'depart','deadline','deadline_kind', 'outbound_s',
    'return_s','buffer_before_s','buffer_after_s'} (None = unknown, 0 = explicitly none).
    max_quote_age_s is a policy parameter supplied by the caller (tests use a SYNTHETIC value).
    Timing (immutable) is judged separately from capacity status (volatile, ages with the quote).
    Returns (state, detail). States:
      unknown_inventory_unavailable   failed/unavailable response
      supported_as_quote              fresh Available session that fits (a quote, never a booking)
      unknown_current_availability    a fitting session exists but its status is stale or unclear
      unknown_timing                  some session's fit depends on unknown travel or buffers
      contradicted_no_fitting_session complete, applicable inventory and every session fails
      unknown_inventory_incomplete    observed sessions fail but completeness is not established"""
    _require(window['deadline_kind'] in DEADLINE_KINDS, 'unsupported deadline_kind')
    for k in ('depart', 'deadline'):
        _aware(window[k], k)
    _require(window['depart'] < window['deadline'], 'depart must be before deadline')
    _aware(query_at, 'query_at')
    _require(max_quote_age_s > 0, 'max_quote_age_s must be positive')
    if not inventory.get('response_ok'):
        return 'unknown_inventory_unavailable', {}
    obs = inventory['observed_at']
    _aware(obs, 'observed_at')
    _require(obs <= query_at, 'impossible observation time: observed after the query time')
    fresh = (query_at - obs).total_seconds() <= max_quote_age_s
    per, fit_unclear_status, timing_unknown = [], [], False
    for sl in inventory['slots']:
        _aware(sl['start'], 'slot start'); _aware(sl['end'], 'slot end')
        _require(sl['start'] < sl['end'], 'slot start must be before end')
        t = _timing(sl, window)
        if t == 'contradicted':
            per.append((sl['start'].isoformat(), 'timing_fails')); continue
        if t == 'unknown':
            timing_unknown = True; per.append((sl['start'].isoformat(), 'timing_unknown')); continue
        if not fresh or sl['status'] not in ('Available', 'Booked'):
            fit_unclear_status.append(sl); per.append((sl['start'].isoformat(), 'fits_status_stale_or_unclear')); continue
        if sl['status'] == 'Available':
            return 'supported_as_quote', {'slot': sl['start'].isoformat(), 'quote_age_s': (query_at - obs).total_seconds()}
        per.append((sl['start'].isoformat(), 'fits_but_booked_fresh'))
    detail = {'per_slot': per, 'complete': inventory.get('complete')}
    if fit_unclear_status:
        return 'unknown_current_availability', detail
    if timing_unknown:
        return 'unknown_timing', detail
    if inventory.get('complete') is True:
        return 'contradicted_no_fitting_session', detail
    return 'unknown_inventory_incomplete', detail

# ---------------------------------------------------------------- query

def query_satisfied(states, required, no_hard_constraints=False):
    """Complete-query satisfaction requires every *required* hard constraint to be evaluated and supported.
    required: the constraint names the parsed query declares. An empty 'required' is valid only with
    no_hard_constraints=True (a query that genuinely has none). Leads are not matches."""
    _require(required is not None, 'required constraint set must be supplied')
    if not required:
        return 'yes_no_hard_constraints' if no_hard_constraints else 'not_evaluated'
    missing = set(required) - set(states)
    if missing:
        return 'not_evaluated'
    vals = [states[k] for k in required]
    if any(v.startswith('contradicted') for v in vals):
        return 'no_known_failure'
    if all(v.startswith('supported') for v in vals):
        return 'yes_research_support'
    return 'no_unverified_lead'
