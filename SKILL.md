---
name: research-paper-workflow
description: "End-to-end research paper workflow for CS, AI, AI4Science, machine learning, agent, and systems research. Use when the user wants to develop a paper from idea to submission: project scaffolding, research storyline, literature monitoring/search, paper cards, related-work matrix, novelty and gap analysis, method design, experiment design, result-table/figure planning, experiment implementation, research-engineering repo scaffolding, run-matrix generation, config/logging schemas, result aggregation, manuscript drafting or polishing, venue-aware writing, claim/citation/result integrity audit, simulated peer review, revision ledger, rebuttal, resubmission, and submission package readiness. Especially use for top-conference or CCF-A/AAAI/NeurIPS/ICLR/CVPR/ACL/GECCO-style work requiring novelty, non-trivial insight, clean baselines, ablations, reproducibility, and human-in-the-loop gates."
---

# Research Paper Workflow

Use this skill as a staged, human-in-the-loop paper operating system. Produce the next concrete artifact, not a vague plan. Do not promise background work. Do not fabricate citations, experiments, results, venue rules, reviewer opinions, or provenance. For any task that queries or depends on external factual information, use the triple-check source verification protocol in `references/source-verification.md`.


## Claude Code compatibility

This skill includes a Claude Code compatibility layer. When running in Claude Code or another local coding agent environment, also read `CLAUDE.md` and `README_claude_code.md`. Use `examples/claude_code_prompts.md` for copyable commands and `examples/local_project_layout.md` for repository layout. Keep `SKILL.md` as the canonical workflow contract; use `CLAUDE.md` only for local execution conventions, file-editing behavior, and script usage.

## Operating philosophy

- Treat a paper as a research storyline, not as a text-generation task: problem -> gap -> root challenge -> insight -> method -> evidence -> limitation -> reviewer response.
- Keep the user as principal investigator. The user owns research questions, true results, authorship, claims, and submission decisions.
- Separate owner modes: planning, literature, experiment design, writing, review, audit, submission, and rebuttal must not overwrite each other's artifacts.
- Keep every claim connected to a citation, result, proof, design rationale, or explicit placeholder. Any externally queried claim must pass three checks: existence, metadata, and claim-support.
- Mark uncertainty with `TBD`, `needs evidence`, `hypothesis`, `unverified`, `partial`, `conflict`, or `scope-change required` instead of hiding it.
- For top-conference work, actively pressure-test novelty, non-triviality, insight, baseline strength, ablations, statistics, reproducibility, and reviewer-facing clarity.
- After each completed stage, show a compact `Next-step options` menu with one recommended next action so the user can continue by replying `A`, `B`, `next`, or a mode name. Use `references/next-step-menu.md`.


## Source verification requirement

Use `references/source-verification.md` for every mode that involves querying or relying on outside information. This applies to literature search, literature monitoring, citation use, benchmark/dataset facts, repository/tool/library facts, venue rules, current deadlines, pricing/compute availability, and any factual claim the user asks to verify.

For each load-bearing external fact, perform three checks before using it as evidence:

1. Existence check: confirm the paper/source/rule/dataset/repository/artifact exists at a primary or reliable source.
2. Metadata check: confirm title/name, authors/owners, date/version, venue/source, URL/DOI/arXiv ID/repository path, and current/superseded status.
3. Support check: confirm the cited passage or evidence actually supports the claim.

If all three checks pass, mark the item `verified`. If only some pass, mark it `partial`. If verification fails or cannot be completed, mark it `unverified` or `conflict` and do not use it as a load-bearing claim. For non-trivial searches, include or update `source_verification_log.md` using `assets/source_verification_log_template.md`.

## First action

Classify the user's entry point and run the nearest mode:

| Entry point | Mode |
|---|---|
| vague idea, weak topic, or direction rescue | `idea-optimize` |
| compare/rank ideas, novelty risk, top-conference feasibility | `idea-review` |
| recent competitor / scoop / arXiv or OpenReview tracking | `literature-monitor` |
| related work, datasets, benchmarks, prior art, evidence search | `literature-search` |
| experiment design, baselines, ablations, tables, figure specs | `experiment-design` |
| turn an experiment plan into runnable code tasks, repo structure, configs, run matrix, logging, aggregation | `experiment-implementation` |
| check run logs/results, aggregate multi-seed metrics, produce LaTeX tables | `result-engineering` |
| paper writing, polishing, compression, LaTeX, abstract/introduction/method/experiments | `paper-writer` |
| full scientific review, writing review, score-risk diagnosis | `paper-reviewer` |
| claim/citation/result/number consistency audit | `integrity-audit` |
| venue page limit, anonymization, metadata, reproducibility checklist | `submission-check` |
| reviewer response, revision ledger, resubmission strategy | `rebuttal` |
| user wants the full project broken into stages | `pipeline` |

If critical information is missing, make a conservative assumption and state it, unless factual accuracy, ethics, authorship, or provenance would be compromised.

## Next-step interaction

After producing any reusable artifact or completing any mode, append a short `Next-step options` block. Use `references/next-step-menu.md` for the exact menu contract, recommended successor mapping, gate-failure behavior, and shortcut commands.

Rules:

- Always offer 3 to 6 concrete options unless the user explicitly asks for no extra text.
- Mark exactly one option as `[Recommended]`, or `[Repair first]` if the current gate failed.
- Make the first option the natural next workflow step when the gate passes.
- Include a copyable command such as `Continue with A.`
- If the user replies `A`, `B`, `C`, `next`, `repair`, or a mode name, execute the selected option directly.
- Keep menus short; do not let navigation overwhelm the artifact.

## Shared project state

For multi-turn projects, maintain a compact `paper_state.yaml` view in the response or as a file when requested. Use `references/routing-and-artifacts.md` and `assets/paper_state_template.yaml`.

Minimum state fields:

```yaml
project:
  title: TBD
  target_venue: TBD
  stage: idea | literature | experiment-design | implementation | execution | result-analysis | writing | review | audit | submission | rebuttal
  paper_type: empirical | theoretical | systems | survey | benchmark | position | other
artifacts:
  idea_brief: TBD
  literature_notes: TBD
  experiment_plan: TBD
  implementation_plan: TBD
  run_matrix: TBD
  result_logs: TBD
  results: TBD
  manuscript: TBD
  review_report: TBD
  integrity_report: TBD
  submission_check: TBD
claims: []
experiments: []
runs: []
reviews: []
revision_ledger: []
submission_checks: []
```

## Stage map

Read `references/workflow.md` for stage gates.

| Stage | Goal | Primary artifact |
|---|---|---|
| 0. Project scaffold | initialize state, target venue, artifact contract | `paper_state.yaml` |
| 1. Idea optimize | turn vague direction into falsifiable research story | `idea_brief.md` |
| 2. Idea review | strict novelty / feasibility / insight assessment | `idea_review.md` |
| 3. Literature monitor/search | competitor tracking, related-work pool, benchmark search | `literature_search_plan.md`, `paper_cards.md` |
| 4. Related-work matrix | classify methods and expose open gaps | `related_work_matrix.md` |
| 5. Claim and evidence design | map every claim to evidence needs | `claim_manifest.md` |
| 6. Experiment design | baselines, metrics, ablations, robustness, result table plan | `experiment_plan.md` |
| 7. Experiment implementation | repo scaffold, config schema, run matrix, logging, tracking, commands | `implementation_plan.md`, `run_matrix.csv` |
| 8. Result engineering | validate logs, aggregate seeds, generate paper tables/figures | `result_audit.md`, `tables/*.tex` |
| 9. Result analysis | turn real logs/tables into supported claims and limitations | `results_analysis.md` |
| 10. Venue-aware writing | draft/revise/polish/compress paper text | `paper_draft.tex` or `paper_draft.md` |
| 11. Review | simulated reviewers, AC view, writing review, repair roadmap | `review_report.md` |
| 12. Integrity audit | claim-support, citation, numeric, figure/table consistency, source verification status | `integrity_report.md`, `source_verification_log.md` |
| 13. Submission check | template/page/anonymity/artifact/readiness check | `submission_checklist.md` |
| 14. Rebuttal/resubmission | response plan, revision ledger, resubmission strategy | `revision_ledger.md` |

## Mode rules

### `pipeline`

Create a stage plan, gate criteria, artifact handoff map, and next owner mode. Do not write the manuscript or invent research content.

### `idea-optimize`

Use `references/storyline-blueprint.md`. Output problem, gap, root challenge, insight, proposed mechanism, falsifiable claims, minimum experiment, novelty threats, and rescue routes.

### `idea-review`

Review strictly. Score novelty, non-triviality, insight, feasibility, evidence path, and venue fit. Give repair conditions; do not continue optimizing unless asked.

### `literature-monitor` and `literature-search`

Use `references/literature-review.md` and `references/source-verification.md`. If current literature or novelty matters, search the web. Extract paper cards using `assets/paper_card_template.md`; then build a taxonomy and gap map. For load-bearing literature facts, run existence, metadata, and support checks and maintain a source verification log. Do not treat broad related-work search as citation-context verification.

### `experiment-design`

Use `references/experiment-design.md`. Map every major claim to datasets/workloads, baselines, metrics, ablations, robustness/failure tests, efficiency, statistical reliability, and execution priority. Build tables with `TBD` placeholders unless the user supplied real values.


### `experiment-implementation`

Use `references/experiment-implementation.md`, `references/research-engineering.md`, `references/result-logging.md`, and `references/reproducibility-passport.md`. Convert an approved experiment plan into a runnable research-engineering package. Output repository layout, module boundaries, config schema, run matrix, command templates, tracking/logging schema, baseline implementation checklist, environment capture, and reproducibility passport. Prefer simple local workflows first; mention optional Hydra/MLflow/DVC/W&B only when useful. Do not implement paper-specific algorithm code unless the user asks; specify interfaces, files, and acceptance tests.

### `result-engineering`

Use `references/result-logging.md`. Validate supplied run logs/results for required fields, missing seeds, failed runs, duplicate run IDs, metric drift, and claim coverage. Aggregate repeated runs into mean/std/count tables and generate CSV/Markdown/LaTeX-ready output. Never invent missing runs; mark them `missing`, `failed`, or `excluded_with_reason`.

### `paper-writer`

Use `references/writing-guide.md`, `references/storyline-blueprint.md`, `references/venue-writing.md`, and `references/section-modules.md`.

- Preserve the user's requested format: LaTeX stays LaTeX, Markdown stays Markdown, tables stay tables.
- For polishing/compression, return the revised text first; add notes only for meaning changes, unsupported claims, or risky edits.
- For a full-paper draft, produce a submission-shaped artifact, not only an outline: title, abstract, introduction, related work/background, method, experiments, analysis/ablation, limitations, reproducibility/ethics if relevant, conclusion, references placeholders, appendix/checklist placeholders.
- If the draft is underfilled for the target venue, expand with mechanism detail, experiment setup, analysis scaffolds, limitations, and explicit evidence placeholders. Do not pad or invent results.
- If a target venue is named, use a venue-aware section budget, but route final current rule verification to `submission-check`.

### `paper-reviewer`

Use `references/review-rubric.md`. Act as strict but fair reviewers and AC. Produce decision-relevant findings with evidence basis, severity, affected criterion, repair action, owner mode, and score-impact condition. Do not rewrite the paper as the main task.

### `integrity-audit`

Use `references/citation-integrity.md` and `references/source-verification.md`. Check claim-support, result-to-claim, numeric consistency, figure/table/text consistency, citation metadata, citation-context support, and source verification status. Mark unsupported or only partially verified items instead of fixing them by invention.

### `submission-check`

Use `assets/submission_checklist_template.md` and `references/source-verification.md`. Check page budget, anonymity, PDF metadata, template compliance, reproducibility/artifact package, appendix, ethics, and AI disclosure if required. Use web search for current venue rules before final advice and triple-check venue rules with official venue pages whenever possible.

### `rebuttal`

Use `references/rebuttal-revision.md`. Convert reviews into issue taxonomy, response strategy, revision ledger, point-by-point reply, and resubmission plan. Never invent new results; mark promised experiments as planned unless already supplied.

## Script use

Use scripts only for structural checks, not factual verification:

- `scripts/build_paper_matrix.py`: convert paper-card CSV/JSON to related-work matrix.
- `scripts/check_claim_manifest.py`: validate claim manifest completeness.
- `scripts/validate_paper_state.py`: validate `paper_state.yaml` keys and artifact consistency.
- `scripts/build_revision_ledger.py`: convert reviewer comments/action CSV to a revision ledger.
- `scripts/generate_run_matrix.py`: expand experiment axes into a reproducible run matrix.
- `scripts/validate_result_logs.py`: check JSONL/CSV run logs for required provenance and metric fields.
- `scripts/aggregate_results.py`: aggregate multi-seed results into mean/std/count tables.
- `scripts/make_latex_tables.py`: convert aggregated CSV results into LaTeX tabular snippets.
- `scripts/check_source_verification_log.py`: structurally validate source verification logs and flag missing triple-check fields.

## Handoff requirement

Every mode must end with:

```text
Next-step options:
A. [Recommended] ...
B. ...
C. ...

Suggested next command: "Continue with A."
```

If a gate fails, replace `[Recommended]` with `[Repair first]` and make option A the repair path.

## Stop and warn

Warn or pause when a claim needs evidence, a source has not passed triple-check verification, results are missing, citation support is unknown, ethics/IRB/privacy review may be required, venue rules are current and must be checked, or the user asks to hide AI use, fabricate provenance, or bypass human review.
