# Experiment Implementation Mode

Use this reference after `experiment-design` has produced a claim-to-test experiment plan. The goal is to turn scientific intent into a runnable, traceable, reproducible research-engineering package.

## Inputs to request or infer

- `idea_brief`: problem, insight, central claims, target venue.
- `claim_manifest`: claim IDs and required evidence.
- `experiment_plan`: datasets/workloads, methods, baselines, ablations, metrics, priorities.
- Available codebase/repo, preferred language, framework, package manager, hardware, OS, time budget.
- Constraints: local-only, cloud, cluster, AMD/NVIDIA/CPU, offline, proprietary data, licensing.

If codebase details are missing, create a framework-neutral interface plan rather than pretending to know the user's repo.

## Output contract

Produce these artifacts when applicable:

1. `implementation_plan.md`
2. `repo_structure.md`
3. `config_schema.yaml`
4. `run_matrix.csv`
5. `commands.md`
6. `logging_schema.json`
7. `baseline_checklist.md`
8. `reproducibility_passport.md`
9. `acceptance_tests.md`

## Workflow

### 1. Translate claims into implementation units

For each claim, define:

- `claim_id`
- required experiment family: main, baseline, ablation, robustness, failure, efficiency, user study, proof, or case study
- executable module responsible for evidence
- expected output artifact
- minimum acceptance criterion
- risk if missing

### 2. Define repository boundaries

Prefer this layout unless user has an existing repo:

```text
project/
├── README.md
├── pyproject.toml or requirements.txt
├── configs/
│   ├── default.yaml
│   ├── datasets/
│   ├── methods/
│   ├── baselines/
│   └── ablations/
├── src/
│   ├── data/
│   ├── methods/
│   ├── baselines/
│   ├── evaluation/
│   ├── analysis/
│   └── utils/
├── scripts/
│   ├── run_experiment.py
│   ├── run_matrix.py
│   ├── aggregate_results.py
│   └── make_tables.py
├── results/
│   ├── raw/
│   ├── processed/
│   ├── tables/
│   └── figures/
├── logs/
├── notebooks/
└── paper/
```

Rules:

- Keep method code separate from baseline code.
- Keep evaluation logic shared across methods and baselines.
- Keep raw run logs immutable; write processed tables separately.
- Never edit code manually between runs without changing config, commit, or run metadata.

### 3. Config-first implementation

Require runnable experiments to be parameterized by config, not by ad hoc code edits. Define:

- dataset/workload block
- method block
- baseline block
- seed block
- metric block
- resource block
- logging block
- output paths

If the user uses Hydra, mention that Hydra supports command-line or config-based multi-run sweeps over parameter combinations. If not, provide plain YAML/JSON and CSV commands.

### 4. Build a run matrix

Each row is one executable run. Required columns:

```csv
run_id,claim_id,experiment_family,dataset,method,baseline,ablation,seed,config_path,command,expected_outputs,status,priority
```

Status values:

- `planned`
- `running`
- `completed`
- `failed`
- `excluded_with_reason`
- `needs_rerun`

### 5. Define logging and provenance before running

Every run must record:

- `run_id`
- `claim_id`
- git commit or code version
- config file path and resolved config hash if possible
- dataset name, version, split, preprocessing
- method/baseline name and version
- seed
- metrics
- wall-clock time and compute device
- status and failure reason
- artifact paths

Optional integrations:

- MLflow: parameters, metrics, code versions, artifacts, run grouping.
- W&B: configs, metrics over time, outputs/artifacts, dashboards.
- DVC: data/model versioning, pipeline dependencies, metrics, plots, experiment comparisons.

Do not require any specific tool unless user asks. A local JSONL/CSV logger is acceptable for MVP.

### 6. Baseline implementation checklist

For each baseline:

- Source: official code, faithful reimplementation, library implementation, or paper-only reconstruction.
- Same dataset split and preprocessing as proposed method.
- Same evaluation script and metrics.
- Comparable tuning budget.
- Fixed seeds and hyperparameters recorded.
- Known deviations from the original paper recorded.
- Failure cases recorded rather than silently dropped.

### 7. Acceptance tests before long runs

Before expensive experiments, require:

- smoke test on tiny data
- determinism test for fixed seed where feasible
- metric sanity test on toy data
- baseline parity test if official numbers exist
- output schema validation
- one complete end-to-end run from config to table

## What not to do

- Do not fabricate code results or benchmark numbers.
- Do not collapse exploratory tuning and final evaluation into the same table.
- Do not compare methods with different preprocessing or metrics unless clearly labeled.
- Do not recommend large infrastructure if a simple local JSONL/CSV workflow is enough.
