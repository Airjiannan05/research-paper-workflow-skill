---
name: rpw-result-engineering
description: "Validate experiment logs, detect missing/failed/duplicate runs, aggregate multi-seed results into mean/std tables, and generate CSV/Markdown/LaTeX output. Use for result processing, log validation, table generation, 结果工程, 日志验证, 聚合结果, 生成LaTeX表格. Do not interpret results — that's rpw-result-analysis."
---

# RPW Result Engineering

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill validates and aggregates; it does not interpret what results mean. Route interpretation to `rpw-result-analysis`.

## Core Rule

Never invent missing runs. Validate every log against the run matrix, aggregate with provenance, and mark gaps as `missing`, `failed`, or `excluded_with_reason`. Every table cell must trace back to a real run log or an explicit placeholder.

## Workflow

1. Load the run matrix (`run_matrix.csv`) and result logs (`results/raw/runs.csv` or JSONL).
2. Validate logs with `../scripts/validate_result_logs.py`: check required fields (`run_id`, `claim_id`, `dataset`, `method`, `seed`, `config_path`, `status`), provenance fields (`git_commit`, `dataset_version`), duplicate run IDs, missing seeds, and failed runs.
3. Report run coverage: which claims and baselines have complete data, which are missing.
4. Aggregate multi-seed results with `../scripts/aggregate_results.py`: mean, std, count per (dataset, method, metric) group.
5. Generate LaTeX table snippets with `../scripts/make_latex_tables.py`.
6. Produce `result_audit.md` with per-claim coverage status.
7. Flag metric drift, outlier seeds, or unexpected variance.

## Output Contract

```text
Run validation:
  Total runs expected: N
  Runs found: N
  Missing: N (list)
  Failed: N (list with reasons)
  Duplicates: N (list)
Seed coverage: complete / partial (list gaps)
Baseline coverage: complete / partial (list gaps)
Aggregated results: results/processed/aggregated_results.csv
LaTeX tables: results/tables/main_results.tex, ablation_results.tex
Claim coverage: supported / partial / unsupported
```

## Handoff

End with a next-step menu. Recommended: `rpw-result-analysis` if coverage is sufficient; otherwise repair missing runs.

## Reference Files

- `../references/result-logging.md`: Logging and validation rules.
- `../scripts/validate_result_logs.py`: Log validation.
- `../scripts/aggregate_results.py`: Multi-seed aggregation.
- `../scripts/make_latex_tables.py`: LaTeX table generation.
