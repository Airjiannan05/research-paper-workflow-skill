# Research Engineering Guidelines

Use this reference to convert research plans into maintainable engineering work.

## Principle

Treat experiments as code: executable, versioned, auditable, debuggable, reusable, and scalable. A result should be traceable back to code, config, data, seed, environment, command, and raw output.

## Engineering layers

1. Scientific intent: claim, hypothesis, evidence type.
2. Experiment design: dataset, baseline, metric, ablation, robustness.
3. Implementation: modules, configs, run commands, logging.
4. Execution: run matrix, job status, failures, retries.
5. Aggregation: raw logs -> processed tables -> paper figures.
6. Audit: provenance, reproducibility, claim support.

## Repo design rules

- One entry point for running experiments, e.g. `scripts/run_experiment.py --config configs/main.yaml`.
- One aggregator entry point, e.g. `scripts/aggregate_results.py --logs results/raw --out results/processed`.
- One table/figure generator entry point, e.g. `scripts/make_tables.py --results results/processed`.
- No manual copy-paste from terminal output into paper tables.
- All paper numbers should come from a machine-readable result file.
- Separate `pilot`, `main`, `ablation`, `robustness`, and `debug` configs.
- Record failed and excluded runs with reasons.

## Suggested repo scaffold

```text
src/data/          dataset adapters, splits, preprocessing
src/methods/       proposed method implementation
src/baselines/     baseline wrappers with same interface as method
src/evaluation/    metrics and statistical tests
src/analysis/      aggregation and plotting helpers
src/utils/         seeding, logging, config, environment capture
configs/           parameterized experiment configs
scripts/           CLI entry points
results/raw/       immutable per-run logs
results/processed/ aggregated CSV/JSON/Markdown
results/tables/    LaTeX/Markdown tables
results/figures/   generated figures
```

## Run phases

- `pilot`: one dataset, one seed, small budget, prove pipeline works.
- `calibration`: tune hyperparameters on validation splits only.
- `final`: locked configs and seeds; no cherry-picking.
- `stress`: robustness, shifted data, failure cases, efficiency.
- `audit`: reproduce key table from raw logs on a clean checkout.

## Hardware-aware guidance

When resources are limited:

- Rank experiments by claim importance.
- Start with toy/small datasets to test interfaces.
- Use fewer seeds for pilot, more seeds for final claims.
- Prefer cheaper baselines first to catch pipeline bugs.
- Record hardware and runtime so claims do not imply unlimited compute.

## Done definition

Implementation is ready when:

- A new collaborator can run one smoke test from README.
- Every run has a unique `run_id`.
- Raw logs validate against the logging schema.
- Aggregation regenerates the main result table.
- The reproducibility passport identifies all code/data/config/environment dependencies.
