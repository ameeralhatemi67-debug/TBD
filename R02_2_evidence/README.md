# R02.2 evidence

Research observations collected on 27 September 2026, following the blocked R02.1 run. Read [R02.2](../R02_2_Source_Access_Recovery_and_Review.md) for interpretation and limits.

## Contents

- `http_checks.json`: initial 12 formal direct requests.
- `public_app_checks.json`: 7 public app/data and routing requests.
- `interpretation_checks.json`: 3 privacy, price-display, and return-route checks.
- `measured_observations.json`: compact factual projections and calculated comparisons, with limitations.
- `collect_public_checks.ps1`: the bounded request lists and collection method. Existing manifests are protected against overwrite. Review source rules and use a new dated directory before any future collection.
- `summarize_checks.py`: offline checks of local response hashes and selected response fields; derives the compact measurements.

The 22 formal requests had 19 HTTP 200 responses, one DNS failure and two timeouts. HTTP 200 includes an app shell and a robots URL whose body was merely `404`. It is not a usable-data success rate. Exploratory web-tool and direct reads preceded the formal manifests and are described in the report.

Hashes cover the UTF-8 bytes of the decoded response content, not the compressed wire response. Response dates, request times, and any Last-Modified header are distinct. None independently verifies fact freshness.

## Publication boundary

Full operator HTML, JavaScript and response bodies remain in the ignored local `.local_source_checks/` directory. They are not distributed as a production corpus. The JSON projections are limited research observations, not a grant to republish an operator feed. No personal customer, booking, or payment records were accessed.

The private source responses were checked against every successful manifest hash before publication. A clone cannot independently repeat those historical raw-content hash checks because it does not contain the private bodies. It can inspect the manifests and projections, and it can make a new permitted observation later. Do not claim the hashes alone prove the reported facts.

The retained Overture IDs and coordinates used for the diagnostic comparison originate in the separately licensed [R02 evidence](../R02_evidence/README.md). Operator-supplied map links were observed in its branch response; no Google Maps dataset was downloaded. OSRM research route outputs use OpenStreetMap contributor data and remain separate. See [OSRM demo terms](https://github.com/Project-OSRM/osrm-backend/wiki/Demo-server) and [OpenStreetMap attribution](https://www.openstreetmap.org/copyright).

All slot quotes are historical snapshots. They are not current booking offers. No production access rights, contracted API, or continuous service reliability has been established.
