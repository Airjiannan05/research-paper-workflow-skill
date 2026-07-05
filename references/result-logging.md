# Result Logging and Aggregation

Use this reference for `result-engineering` and for implementation planning.

## Required per-run fields

Minimum JSONL/CSV fields:

```text
run_id,claim_id,experiment_family,dataset,dataset_version,split,method,baseline,ablation,seed,config_path,config_hash,git_commit,status,metric_name,metric_value,metric_unit,wall_time_sec,device,artifact_path,failure_reason,notes
```

For wide CSV logs, metric columns such as `accuracy`, `f1`, `runtime_sec`, and `memory_gb` are acceptable, but provenance fields remain mandatory.

## Log file conventions

- Write one immutable raw record per run to `results/raw/runs.jsonl` or `results/raw/runs.csv`.
- Store training curves separately, e.g. `results/raw/curves/{run_id}.csv`.
- Store predictions only when needed for failure analysis.
- Store generated tables under `results/tables/` and figures under `results/figures/`.

## Validation checks

Check for:

- duplicate `run_id`
- missing claim coverage
- missing seeds
- missing required provenance fields
- failed runs without `failure_reason`
- numeric metrics that are not parseable
- incompatible metrics grouped together
- table values that cannot be traced to raw logs

## Aggregation rules

Group by stable experiment keys:

```text
claim_id,experiment_family,dataset,method,baseline,ablation,metric_name
```

Aggregate across seeds:

- `mean`
- `std`
- `n`
- optionally `min`, `max`, `median`

Never drop failed or missing runs silently. Report counts and exclusions.

## Paper table policy

Every table cell must be one of:

- derived from validated raw logs
- explicitly marked `TBD`
- explicitly marked `not run`
- explicitly marked `excluded_with_reason`

Use table notes for seed count, metric direction, confidence intervals, and known deviations.
