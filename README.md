# TBD: location-aware discovery

Research for a product that helps people find worthwhile things to do within their location, available time, practical constraints, and intent.

The project is in concept development. There is no application yet. Research utilities in this repository collect and measure evidence; they are not production infrastructure.

## Read first

1. [Original concept](<Product & Technical Concept v0.1.md>)
2. [Architecture review](Product_Technical_Concept_Architecture_Review_v0.2.md)
3. [R00: user decision study](R00_User_Decision_Study.md)
4. [R01: source rights and economics](R01_Source_Rights_and_Economics.md)
5. [R01.2: automation-first correction](R01.2_Automation_First_Data_Strategy_and_Architecture_Correction.md)
6. [R02: automated coverage and feasibility audit](R02_Automated_Coverage_and_Feasibility_Audit.md)
7. [Project start review](PROJECT_START_REVIEW.md): evidence re-check, budget status, and the locked next experiment
8. [R02.1: practical-data feasibility follow-up](R02_1_Practical_Data_Feasibility_Followup.md)

R01.2 corrects the operating-model assumptions in R01. R02 supplies bounded measurements, not proof that the product or launch geography is validated. Follow the revised research numbering in the later reports rather than v0.1's original numbering.

## Current findings

R02 retrieved 13,764 source records across four Saudi sample rectangles and selected 1,379 potential discovery records by category. These are not verified distinct venues or decision-ready recommendations. The baseline lacks hours, prices, visit duration, booking rules, dated occurrences, and availability.

The leading approach combines an open or owned place baseline with permitted practical-data enrichment, explicit uncertainty, and selective curation. The next dependency is a reliable practical-data path that reduces the user's remaining checks. User demand, low maintenance cost, and a launch geography remain unvalidated.

## Evidence and reproduction

See [R02 evidence and source notices](R02_evidence/README.md). The retained raw files are approximately 20 MB. Start with manifests and summaries; do not load the raw files into an AI context window.

With Python 3 installed, `python R02_evidence/validate_audit.py` checks retained hashes, counts, report links, and section numbering. Inspect `checks_pass` in its output. This verifies internal consistency, not real-world correctness. Collection helpers can overwrite the original snapshots; preserve them and collect future evidence in a new dated directory.

Third-party datasets retain their own licenses and attribution requirements. The repository does not grant a blanket license over all its contents. Consult the evidence notices before reusing data. OSM remains a separate dataset.

## Claude handoff

Use [the $100 research prompt](CLAUDE_100_DOLLAR_PROJECT_PROMPT.md) with this repository connected. It prioritizes the unresolved feasibility question, a provisional domain model, and a small evaluation set. It does not authorize application development or spending on external services.
