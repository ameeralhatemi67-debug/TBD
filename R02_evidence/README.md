# R02 evidence package

Collected 26 September 2026 for the location-aware discovery project. These are research extracts and measurements, not an application or a production ingestion system.

## Sources and attribution

The four `*_overture.json` files contain bounding-box extracts of Overture Places release `2026-09-23.1`. Point geometry is serialized as hexadecimal WKB. All original source properties are retained. Each record's `sources` array identifies its upstream license. Data from Meta and Microsoft use CDLA Permissive 2.0; Foursquare data use Apache 2.0; AllThePlaces data use CC0. Other sources, if present outside the selected candidate pool, retain their own recorded licenses. Read [Overture attribution](https://docs.overturemaps.org/attribution/) and the saved notices in `licenses/` before reuse.

Foursquare attribution: Copyright 2024 Foursquare Labs, Inc. All rights reserved, as credited by Overture. The current Foursquare NOTICE page also carries copyright 2026 Foursquare Labs, Inc. Its full notice is retained in `licenses/Foursquare-NOTICE.html`. Overture transformed Foursquare data into its schema. R02 further selected geographic subsets, serialized geometry, and produced field-count/category projections on 26 September 2026. No source fact was manually corrected in the raw samples.

`eastern_osm.json` is a separate OSM extract. Copyright OpenStreetMap contributors, licensed under [ODbL 1.0](https://www.openstreetmap.org/copyright). It has not been merged into the Overture records. Its server-reported database timestamp is 31 May 2026. This is not a current-hours source. OSM terms and license are retained in `licenses/ODbL-1.0.txt`.

## Files

| File | Purpose |
|---|---|
| `retrieval_manifest.json` | Exact Overture release, rectangles, record counts, observed extraction seconds, schema columns, SHA-256 hashes |
| `stac_attempt_manifest.json` | Initial catalog-filter attempt returned no files; not a zero-coverage finding |
| `*_overture.json` | Full raw records for four sample rectangles |
| `category_rules.json` | Deliberately narrow, exact-category first-pass selection rules |
| `overture_summary.json` | Family, contact-field, source, license and confidence-threshold counts |
| `screened_candidates.csv` | 438 candidates surviving the illustrative 0.8 confidence threshold; **not** a recommended production shortlist |
| `anchor_matches.json` | Post-hoc name-pattern matches, including false positives, for diagnosis; not a gold-standard set |
| `duplicate_candidates.json` | Exact normalized-name pairs under 100 m after 0.8 screening; empty result does not establish absence of duplicates |
| `additional_metrics.json` | Selected query pools, observed OSM field counts and absent Overture columns |
| `osm_manifest.json` | Four public-mirror requests; one response, one HTTP 504, two client read timeouts |
| `osm_tls_attempt.json` | First OSM endpoint failed client TLS certificate validation |
| `route_results.json` | Eight failed routing attempts, synthetic origins and target IDs; no travel times were obtained |
| `audit_validation.json` | Raw-file hash/count checks, candidate totals, CSV count, report section sequence and local-link checks |
| `licenses/` | License texts, upstream notices, and their URLs |

The small Python files reproduce research collection and counting. The Overture reader was installed in a temporary folder, with no application dependencies added to the project. `collect_open_sample.py` requires the official `overturemaps` package and PyArrow dependencies. Other measurements use Python's standard library. Rerunning network collection overwrites the corresponding evidence snapshots and may yield different results; preserve this dated package first. No paid credentials or source accounts were used.

First-party web pages were read for source-feasibility research, and the report retains short original research observations and citations. They were **not** imported into a reusable listing corpus. Public-page readability is not a production data license. No booking or availability was confirmed by completing a transaction.

## Important limitations

The rectangles have unequal sizes. Record counts are not neighborhood completeness, unique venue counts, or decision-ready choice counts. The named anchors were examined after retrieval and cannot yield unbiased recall. The 0.8 threshold is a diagnostic experiment; it removed every Foursquare-sourced record in this sample. Opening hours, price, duration, booking rules and dated occurrences are absent from the retrieved Overture schema. The report keeps failed access, missing fields, conflicts, and untested services distinct.
