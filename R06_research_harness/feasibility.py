"""R06 research harness: offline constraint evaluation over labeled observations.
Research code only. No network, no storage, no UI. Implements R04 v0.2 rules so they can be tested.
States: supported | contradicted | unknown | conflict | boundary_ambiguity."""
import math
from datetime import datetime, timedelta

def meters(a, b):
    """Approximate distance between (lon, lat) points."""
    return math.hypot((a[0]-b[0]) * 111320 * math.cos(math.radians((a[1]+b[1]) / 2)), (a[1]-b[1]) * 111320)

def link_record_to_branch(record_pt, branches, max_m):
    """Provisional 'describes' link only if exactly one operator branch point lies within max_m.
    Branches without a point are unresolvable by distance. Returns (state, branch_id, meters)."""
    near = [(meters(record_pt, b['pt']), b['id']) for b in branches if b.get('pt')]
    near = sorted(x for x in near if x[0] <= max_m)
    if len(near) == 1:
        return 'provisional_link', near[0][1], round(near[0][0], 1)
    return 'undecided', None, None

def price_check(observations, op, limit, phrase_unit, party_size):
    """observations: [{'amount','unit':'per_person'|'party_total','kind':'displayed'|'derived'|'final'}].
    op: 'lt' for 'under', 'le' for 'at most'. Strict 'under' with equality -> boundary_ambiguity.
    Disagreeing observations are a conflict unless every value gives the same outcome."""
    if not observations:
        return 'unknown'
    outcomes = set()
    for o in observations:
        amt = o['amount']
        if o['unit'] != phrase_unit:
            if o['unit'] == 'party_total' and phrase_unit == 'per_person' and party_size:
                amt = amt / party_size          # derived equal share, labeled by caller
            elif o['unit'] == 'per_person' and phrase_unit == 'party_total' and party_size:
                amt = amt * party_size
            else:
                outcomes.add('unknown'); continue   # unit cannot be reconciled (e.g. party unknown)
        if amt == limit and op == 'lt':
            outcomes.add('boundary_ambiguity')
        else:
            outcomes.add('supported' if (amt < limit if op == 'lt' else amt <= limit) else 'contradicted')
    if len(outcomes) == 1:
        return outcomes.pop()
    return 'unknown' if 'unknown' in outcomes else 'conflict'

def representation_conflict(values):
    """values: [{'channel': 'body'|'metadata'|'lang:ar'|..., 'value': x}]. Any disagreement is a conflict."""
    return 'conflict' if len({v['value'] for v in values}) > 1 else ('agree' if values else 'none')

def is_shared_app_shell(url_hashes):
    """Different URLs returning identical content cannot identify distinct offerings."""
    return len(set(url_hashes.values())) < len(url_hashes)

def hours_state(claims, window_start, window_end):
    """claims: [{'kind':'regular'|'exception','valid_from','valid_to','open','close','scope_clear':bool}] (datetimes).
    Only claims whose valid interval covers the window's date and whose scope is clear are admissible."""
    d = window_start.date()
    adm = [c for c in claims if c['scope_clear'] and c['valid_from'] <= d <= c['valid_to']]
    exc = [c for c in adm if c['kind'] == 'exception']
    use = exc or [c for c in adm if c['kind'] == 'regular']
    if not use:
        return 'unknown'
    res = {('supported' if c['open'] <= window_start.time() and window_end.time() <= c['close'] else 'contradicted') for c in use}
    return res.pop() if len(res) == 1 else 'conflict'

def session_fit(slots, depart, deadline, travel_s, observed_at, query_at, max_quote_age_s):
    """Is there an Available slot that starts after arrival and ends by the deadline?
    A quote older than max_quote_age_s cannot support *current* availability.
    Returns (state, slot) where state describes fit at observation time or now."""
    arrive = depart + timedelta(seconds=travel_s)
    fits = [s for s in slots if s['start'] >= arrive and s['end'] <= deadline]
    if not fits:
        return 'contradicted', None           # known failure for this offering and date
    avail = [s for s in fits if s['status'] == 'Available']
    if not avail:
        return ('contradicted' if all(s['status'] == 'Booked' for s in fits) else 'unknown'), None
    if (query_at - observed_at).total_seconds() > max_quote_age_s:
        return 'unknown_current_availability', avail[0]
    return 'supported_as_quote', avail[0]    # a quote, never a booking

def query_satisfied(states):
    """Complete-query satisfaction requires every hard constraint supported. Leads are not matches."""
    if any(s == 'contradicted' for s in states.values()):
        return 'no_known_failure'
    if all(s.startswith('supported') for s in states.values()):
        return 'yes_research_support'
    return 'no_unverified_lead'
