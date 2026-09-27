# Claude project handoff: make the next $100 count

You are my senior product architect, discovery/search researcher, and technical research lead. I intend to use Claude Opus 5.5. Verify the actual model and available tools from the environment when possible; do not invent a model identifier or silently claim to have switched models.

Repository: https://github.com/ameeralhatemi67-debug/TBD

I have only **US$100 in Claude cloud credits** for this work, including follow-up corrections. Your goal is to give this project a strong, evidence-based start by resolving the most consequential uncertainties and producing usable project artifacts. Spending the full balance is not a success criterion. A justified decision to narrow the product is valuable.

## 1. Understand the existing project first

Inspect the connected repository. Do not ask me to upload files already present. If the repository is inaccessible, report the exact access problem and the smallest action I must take. Do not substitute a generic research topic.

Read README.md and the following documents once, in manageable sections. Preserve a compact working summary with file and section references so you do not repeatedly reload them.

1. `Product & Technical Concept v0.1.md`
2. `Product_Technical_Concept_Architecture_Review_v0.2.md`
3. `R00_User_Decision_Study.md`
4. `R01_Source_Rights_and_Economics.md`
5. `R01.2_Automation_First_Data_Strategy_and_Architecture_Correction.md`
6. `R02_Automated_Coverage_and_Feasibility_Audit.md`
7. `R02_evidence/README.md`, the retrieval manifest, audit validation, and measurement summaries.

Do not paste the large raw datasets or saved HTML notices into your context. Use targeted local computation when you need to inspect them. Preserve the original evidence snapshots and hashes. Some collection helpers overwrite their outputs; inspect before running them.

The product helps someone choose a worthwhile outing that fits their location, time, constraints, and intent. It crosses places, activities, culture, events, and local discoveries. Discovery precedes planning. It is still in concept development.

The current first-user hypothesis is a resident arranging a near-term outing for themselves and a small group. Domestic visitors are secondary. Saudi areas are test candidates, not a locked launch market. Neither the audience nor repeat use has been validated by primary research.

R01.2 corrects the operating model toward an open or owned baseline, permitted automated refresh, query-time enrichment, explicit uncertainty, and selective curation. Do not reintroduce routine manual verification of hundreds of records per city as a prerequisite.

R02 measured 13,764 source records and 1,379 category-selected candidates. This does not establish unique venues, recall, relevance, or feasible outings. Its baseline lacks practical fields. A confidence cutoff of 0.8 removed every Foursquare-origin record in that sample. Public pages exposed useful facts, conflicts, and branch ambiguity. Routing attempts failed; no travel times were measured. Human-maintenance rates and operating costs remain unknown.

Treat these as claims to inspect against the retained evidence. Later documents can correct earlier proposals, but no document is immune to challenge. Distinguish an explicit correction from an unresolved disagreement.

## 2. Budget controls and working discipline

The $100 is a total ceiling, not permission to incur a separate $100 in data, hosting, subscriptions, or API charges. Reserve **$20** for my review and revisions. Target at most **$80** for the initial work, including final synthesis. Stop earlier when the useful work is done.

Before substantial work, identify whether these credits are API credits, subscription usage credits, or cloud-provider credits. Use available account metadata without exposing secrets. Verify current official pricing and which spend controls actually apply. Do not assume dollar costs from a model name or that a natural-language instruction enforces a billing cap.

Use an applicable provider-enforced spending limit if available and already within your authority. Never enable auto-recharge, increase limits, buy credits, create billable infrastructure, or request billing credentials. If the required limit must be configured by me, state the exact setting and continue only the bounded intake below until budget control is resolved.

Maintain `PROJECT_START_REVIEW.md` with a small budget table: phase, allocation, observed spend, estimated spend if necessary, source of the number, cumulative total, and remaining reserve. Never report an estimate as actual billing. Carry costs across sessions, retries, tools, and any delegated work; a new session does not reset this project's budget. Allow for reporting delays and in-flight work. Reconcile before starting another expensive phase.

If cost telemetry is unavailable, do not claim to enforce $100. Complete a single bounded intake pass, write the summary and proposed next batch, then stop for a billing check. Do not launch an open-ended run under an imaginary budget.

Suggested allocations are ceilings, not targets:

| Work | Allocation |
|---|---:|
| Project intake and focused evidence review | $10 |
| Practical-data feasibility investigation | $25 |
| Provisional domain, trust, and evaluation artifacts | $25 |
| Stress tests and focused corrections | $10 |
| Synthesis, validation, and handoff | $10 |
| Reserved for my feedback | $20 |

Check spending at each phase boundary and before expensive batches. Save a resumable checkpoint before the initial-work ceiling is reached. If funds run short, finish the evidence-backed conclusion and list unfinished work. Do not rush out unsupported claims to label every deliverable complete.

Reduce waste:

- Use Opus for difficult synthesis, tradeoffs, and final review. Use deterministic local scripts for counts, sorting, filtering, and consistency checks.
- Keep one lead context. No agent swarm. Only use a cheaper helper if the environment supports it, the task is bounded, and expected savings exceed duplicated context and review cost. Include its charges in the same budget.
- Read each relevant document once. Use file references and compact checkpoints thereafter. Preserve stable context where supported; do not assume caching is free or available in every interface.
- Research a named uncertainty that could change a decision. Prefer first-party documentation and original sources. Stop a search when more sources would merely repeat the conclusion.
- Bound network attempts. After an initial failure and one justified retry or documented alternative, record the blocker and continue elsewhere. Do not disable TLS checks or bypass access restrictions.
- Produce one reviewed version of each required artifact. Avoid repeated polishing, redundant reports, speculative infrastructure, and exhaustive vendor surveys.

Current official starting points for budget verification, recheck for your execution environment:

- https://code.claude.com/docs/en/costs
- https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
- https://platform.claude.com/docs/en/about-claude/pricing

## 3. Work in order of decision value

### A. Establish what the evidence supports

Create `PROJECT_START_REVIEW.md`. Summarize the product, the document corrections, the strongest findings, and the five most consequential unresolved assumptions. Rank them by impact and cost of obtaining better evidence.

Check R02's retained counts and selected diagnostic examples. Reuse its validator where possible. Do not redownload the same baseline merely to reproduce a headline. Distinguish internal consistency from independent factual validation. Challenge both overconfident and overly pessimistic conclusions.

State the narrowest credible first product promise and what would falsify it. Compare a qualified discovery shortlist with a stronger claim of confirmed feasibility. Do not quietly change the product into a manually operated concierge or a generic directory.

### B. Investigate the practical-data dependency

Create `R02_1_Practical_Data_Feasibility_Followup.md` and a small evidence directory only if needed.

Choose one cultural operator and one repeatable indoor-activity operator using R02's examples and source-access findings. Prefer a compact existing test area when justified. Explain the selection before expanding scope.

For each, investigate the actual path to hours, date exceptions, duration, price, age/group restrictions, booking rules, occurrence dates, and availability. Separate technical accessibility, permission to retrieve, permission to retain/display, freshness, and factual reliability. A visible booking button is not proof of available seats. An official district page does not establish every tenant's hours.

Use permitted free sources and existing evidence. Do not purchase access, contact operators, create accounts, accept contracts, or send messages on my behalf. If authorization or credentials are required, identify the exact dependency and prepare the request for my later use. Do not invent permission or bypass it.

Where repeat retrieval is lawful and practical, perform a small bounded check with timestamps, source identity, applicable dates, branch identity, and failures. Two immediate fetches do not prove ongoing freshness or low operating effort. If the data path cannot be demonstrated, report that result and the effect on the product promise.

Use approximately 12 fixed outing cases drawn from R00 and R02, spanning tonight, weekend, a 90-minute gap, group size, budget, indoor preference, and a negative constraint. Lock the cases before examining answers. Include failures in the denominator. For each, record what can be supported automatically, what remains unknown or contradictory, and what the user still needs to check.

Distinguish no candidates, missing facts, source-access failure, rights uncertainty, and genuine constraint violations. Do not collapse them into a single success rate. Assess whether the shortlist plausibly reduces checking, while marking actual user benefit as untested.

### C. Develop only the research artifacts now justified

Continue provisionally even if a source integration is blocked, keeping the dependency explicit.

Create `R03_Domain_and_Identity_Model.md` at conceptual level. Define place/branch, operator, activity offering, occurrence/session, venue relationship, and source claim only as needed by actual cases. Address museums and exhibitions, multiple activities in one venue, chains, festivals, seasonal markets, pop-ups, changing meeting points, and multilingual names. Specify dangerous merges, reversible identity decisions, and source cross-references. No production database schema or migration.

Create `R04_Trust_and_Freshness_Policy.md` as a provisional policy. Separate provenance, observation time, valid time, freshness, confidence, rights, and conflict. Define when unknown information can appear with qualification and when a hard constraint cannot be satisfied. Distinguish known failure from unverified feasibility. Use R02's concrete examples. Avoid fabricated confidence probabilities or universal refresh intervals.

Create `R05_Query_Intent_and_Evaluation_Seed.md`. Reuse about 24 diverse queries from R00, including the fixed feasibility cases above. Define a small conceptual intent representation and expected interpretation, hard/soft constraints, missing context, ambiguity, acceptable uncertainty, and evaluation criteria. Mark annotations as analyst judgments. Cover Arabic/English variation where supported, and flag judgments needing a native speaker. Keep uninspected cases aside for later evaluation. Do not claim an unimplemented engine has passed a benchmark.

These are coherent provisional research outputs, not a mandate to complete the entire roadmap with $100. If funding is tight, prioritize B, then the shared identity/trust decisions, then a smaller explicitly incomplete evaluation seed. Record what remains.

### D. Challenge the result and leave a usable handoff

Review the artifacts for contradictions and unsupported claims. Test the conceptual model against at least these cases: separate nearby chain branches; venue hours versus activity slots; exception hours outside their valid date; event cancellation; ambiguous price unit; unknown group availability; missing accessibility evidence; and the same source fact copied by several websites.

In `PROJECT_START_REVIEW.md`, finish with:

1. Decisions supported now, with evidence.
2. Hypotheses worth testing and what would overturn them.
3. What you could not establish and why.
4. A precise next experiment: user, area, categories, inputs, measurements, proposed acceptance criteria, cost dependencies, and stop conditions.
5. Whether R06 retrieval architecture can proceed and what must remain provisional.
6. Whether application implementation is justified yet. Explain the answer without starting it.
7. The five next actions in order, separating agent work from work requiring real users, account access, permission, or my judgment.
8. Files created, checks performed, spending information, and the remaining reserve.

## 4. Evidence, repository, and scope rules

- Label measured evidence, documented facts, interpretation, hypotheses, and required primary research. Cite material external claims with direct URLs and dates checked.
- Never fabricate interviews, user quotes, usage statistics, permission, routes, live availability, research completion, or spending.
- Preserve all existing foundation reports. Create new files and link corrections to the original section. Do not silently rewrite the history.
- Keep the revised ladder: R00 user decisions; R01 rights/economics; R02 automated coverage/feasibility; R03 domain/identity; R04 trust/freshness; R05 intent/evaluation; R06 retrieval; R07 ranking/diversity; R08 travel-time feasibility; R09 field test; R10 planning/assistance.
- No website, UI, production code, deployment, microservices, vector database setup, recommendation ML, or autonomous agent framework. Small research utilities are allowed when they resolve a specific question and have a runnable check.
- Preserve data licenses and provenance. Keep restricted data separate. Do not publish secrets, private account details, or newly collected data with unclear redistribution rights.
- If repository writing is available, save the artifacts and update README links. Use a dedicated branch for commits. Do not force-push or merge into main. If writing is unavailable, provide downloadable Markdown artifacts and state the limitation.
- Work autonomously within this scope and budget. Ask only for a genuine missing prerequisite, budget control, or a decision that cannot be responsibly defaulted. Continue independent work while a dependency is unresolved.

Start by inspecting the repository and budget visibility. Give a short product-specific plan, then perform the authorized work. A generic plan alone is not the deliverable.
