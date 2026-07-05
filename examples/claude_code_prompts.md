# Claude Code Prompt Examples

## 1. Start a new paper project

```text
Read skills/research-paper-workflow/SKILL.md and skills/research-paper-workflow/CLAUDE.md.
Use research-paper-workflow to initialize this repository as a top-conference paper project.
Create paper_state.yaml and idea_brief.md.
My direction is: <insert idea>.
Target venue: <insert venue>.
End with next-step options.
```

## 2. Literature search and verification

```text
Use literature-search mode.
Search for prior work related to <topic>.
Create paper_cards.md, related_work_matrix.md, and source_verification_log.md.
For every load-bearing fact, apply existence, metadata, and support checks.
```

## 3. Experiment design

```text
Use experiment-design mode.
Based on claim_manifest.md and related_work_matrix.md, create experiment_plan.md.
Include claim-to-test mapping, datasets, baselines, metrics, ablations, robustness checks, failure cases, and result table shells.
```

## 4. Experiment implementation

```text
Use experiment-implementation mode.
Based on experiment_plan.md, create implementation_plan.md, run_matrix.csv, config_schema.yaml, logging_schema.json, baseline_checklist.md, and reproducibility_passport.md.
Prefer a simple local workflow and avoid heavyweight tools unless they are clearly useful.
```

## 5. Result engineering

```text
Use result-engineering mode.
Validate results/raw/runs.csv against run_matrix.csv.
Detect missing runs, failed runs, duplicate run IDs, missing seeds, missing config/commit/provenance, and metric inconsistencies.
Generate results/processed/aggregated_results.csv and results/tables/main_results.tex.
```

## 6. Writing and audit

```text
Use paper-writer mode to draft the Introduction and Method from idea_brief.md, related_work_matrix.md, claim_manifest.md, and experiment_plan.md.
Do not invent results or citations. Use TBD or needs evidence where necessary.
Then suggest the next step menu.
```

```text
Use integrity-audit mode.
Check paper/main.tex for unsupported claims, citation-context mismatch, numeric inconsistency, and table/text mismatch.
Update integrity_report.md and source_verification_log.md.
```

## 7. Rebuttal

```text
Use rebuttal mode.
Read reviews.md and create revision_ledger.md with issue taxonomy, response stance, required manuscript changes, required experiments, and point-by-point response skeleton.
Do not promise experiments unless results are supplied.
```
