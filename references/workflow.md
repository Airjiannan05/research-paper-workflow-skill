# Workflow Gates

Use this file when coordinating a full paper project or deciding where to enter the workflow.

## Gate philosophy

A stage is complete only when it produces a reusable artifact and the next owner mode can act on it. Do not skip from idea to polished writing unless the user explicitly asks for a sketch and accepts evidence placeholders. Every completed stage must expose the next owner mode through a compact `Next-step options` menu; see `next-step-menu.md`. Any stage that uses externally queried information must apply the triple-check protocol in `source-verification.md` before using information as evidence.

## Stage 0 — Project scaffold

Output or update `paper_state.yaml`.

Required fields: title, target venue, paper type, current stage, artifact paths, claim list, experiment list, review list, revision ledger.

Gate: at least one owner mode and next artifact must be clear, and the response must show a next-step menu.

## Stage 1 — Idea optimize

Output `idea_brief.md` with:

- working title;
- target venue/community;
- task and setting;
- problem;
- why it matters;
- current approach families;
- gap;
- root challenge;
- key insight;
- proposed mechanism;
- falsifiable central claim;
- minimum viable experiment;
- novelty threats;
- scope and non-goals.

Gate: the project must have a testable claim, not only an application theme.

## Stage 2 — Idea review

Output strict review:

- novelty risk;
- non-triviality;
- insight quality;
- feasibility;
- evidence path;
- likely rejection reason;
- repair conditions;
- keep/modify/kill recommendation.

Gate: do not proceed to writing until fatal novelty or evidence gaps are marked.

## Stage 3 — Literature monitor/search

Output search strategy and early paper pool:

- seed papers;
- keywords and synonyms;
- exclusion terms;
- venues and years;
- backward/forward citation expansion;
- SOTA/baseline discovery;
- negative/contradictory evidence search;
- competitor/scoop watch if recent work matters.

Gate: novelty cannot be claimed until close prior work and recent variants have been checked and load-bearing sources have existence, metadata, and support verification logged.

## Stage 4 — Related-work matrix

Create paper cards and a mechanism-based matrix. Include:

- input;
- representation;
- core mechanism;
- supervision/data;
- output;
- evaluation;
- strength;
- limitation;
- relation to this work;
- novelty threat level.

Gate: the matrix must expose a concrete gap, not merely summarize papers. Paper identities, metadata, and relation-to-our-work claims must be verified or marked partial/unverified.

## Stage 5 — Claim and evidence design

Output `claim_manifest.md` or table:

- claim;
- type: conceptual / empirical / theoretical / systems / benchmark / negative;
- required support;
- citation/result/proof source;
- strength;
- risk;
- falsifier;
- status.

Gate: every major contribution claim must have a planned evidence path.

## Stage 6 — Experiment design

Use `references/experiment-design.md`. Output datasets, baselines, metrics, ablations, robustness/failure/efficiency tests, table/figure shells, execution priority, and reproducibility passport.

Gate: each claim maps to a benchmark, baseline, ablation, proof, or qualitative analysis.

## Stage 7 — Experiment implementation

Use `references/experiment-implementation.md`, `references/research-engineering.md`, `references/result-logging.md`, and `references/reproducibility-passport.md`. Convert an approved experiment plan into a runnable research-engineering package.

Output:

- repository layout and module boundaries;
- config schema (`assets/config_schema_template.yaml`);
- run matrix CSV (`scripts/generate_run_matrix.py` or `assets/run_matrix_template.csv`);
- command templates per experiment family;
- tracking and logging schema (`assets/logging_schema_template.json`);
- baseline implementation checklist (`assets/baseline_checklist_template.md`);
- environment capture and reproducibility passport (`assets/reproducibility_passport_template.md`);
- acceptance tests for the experiment harness.

Gate: every experiment axis (dataset, baseline, ablation, seed) must have a concrete run entry with a unique run_id, config path, command, and expected output path. No paper-specific algorithm code should be implemented unless the user explicitly asks; specify interfaces, files, and acceptance tests instead.

## Stage 8 — Result engineering

Use `references/result-logging.md`. Validate supplied run logs and aggregate multi-seed results.

Output:

- run validation report: required provenance fields, missing seeds, failed runs, duplicate run IDs, metric drift;
- aggregated results CSV with mean/std/count per (dataset, method, metric);
- LaTeX/Markdown table snippets via `scripts/aggregate_results.py` and `scripts/make_latex_tables.py`;
- `result_audit.md` with per-claim coverage status.

Gate: no invented runs. Missing, failed, or incomplete runs must be marked as `missing`, `failed`, or `excluded_with_reason`. Every table cell must trace back to a real run log or an explicit placeholder.

## Stage 9 — Result analysis

Use `references/experiment-design.md` for claim-to-evidence mapping. Interpret verified results into supported claims and limitations.

Output:

- main result interpretation;
- ablation interpretation;
- failure cases;
- sensitivity/variance notes;
- cost/runtime;
- claim support status: supported / partially supported / not supported;
- required follow-up experiments.

Gate: do not write stronger claims than the evidence supports. Every claim in the manuscript must be traceable to a specific result row, figure, or explicit limitation statement.

## Stage 10 — Venue-aware writing

Use `references/writing-guide.md`, `references/venue-writing.md`, `references/storyline-blueprint.md`, and `references/section-modules.md`. Draft section by section with visible placeholders: `[CITE]`, `[VERIFY]`, `[RESULT]`, `[FIGURE]`, `[ETHICS]`.

Gate: the introduction must expose the key insight and claim-to-evidence path before style polishing. For a named target venue, apply a venue-aware section budget; route final rule verification to `submission-check`.

## Stage 11 — Review

Use `references/review-rubric.md`. Simulate a reviewer panel and produce decision-relevant findings.

Output:

- paper summary;
- calibrated stance and score/risk;
- top strengths;
- fatal/major/minor concerns with evidence basis, severity, affected criterion, repair action, owner mode, and score-impact condition;
- writing/presentation issues;
- reviewer panel composition;
- concern-to-action table;
- recommended next owner mode.

Gate: revision must address the strongest rejection reasons first. Do not rewrite the paper as the main task.

## Stage 12 — Integrity audit

Use `references/citation-integrity.md` and `references/source-verification.md`. Audit the full manuscript for evidence consistency.

Audit targets:

- claim-support alignment;
- result-to-claim traceability;
- numeric consistency across text, tables, and figures;
- figure/table/text cross-check;
- citation metadata and citation-context support;
- source verification status for all load-bearing external facts;
- missing baselines, missing ablations, reproducibility gaps;
- ethics and data-use issues.

Gate: high-risk unsupported claims and any unverified load-bearing sources must be fixed before finalization. Mark unsupported or only partially verified items instead of fixing them by invention.

## Stage 13 — Submission check

Use `assets/submission_checklist_template.md` and `references/source-verification.md`. Verify venue-specific compliance.

Checklist:

- current venue rules verified through official sources and triple-checked where possible;
- page limit and template compliance;
- anonymity and PDF metadata;
- references and appendix;
- reproducibility/artifact package;
- ethics and AI disclosure if required;
- supplementary material;
- final human verification.

Gate: the user must manually verify factual, experimental, authorship, and policy compliance. Use web search for current venue rules before final advice.

## Stage 14 — Rebuttal / revision / resubmission

Use `references/rebuttal-revision.md`. Convert reviews into a structured response plan.

Output:

- issue taxonomy from reviewer comments;
- response strategy and point-by-point replies;
- revision ledger (`assets/revision_ledger_template.md`);
- resubmission plan.

Gate: every promised change must map to evidence, manuscript edit, experiment, citation, or explicit limitation. Never invent new results; mark promised experiments as planned unless already supplied.
