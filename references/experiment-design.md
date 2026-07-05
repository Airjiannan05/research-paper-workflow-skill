# CS/AI Experiment Design Protocol

Use this file for ML, AI, AI4Science, agent, genetic programming, optimization, systems, and numerical-solver papers.

## Core rule

Design experiments that test the paper's central claims. Build result tables and publication figures only from supplied real values or explicit `TBD` placeholders.

## Claim-to-test mapping

Create a table:

| Claim | Required evidence | Dataset/benchmark | Baselines | Ablation | Metric | Robustness/failure test | Status |
|---|---|---|---|---|---|---|---|

No major claim should lack a test or a stated reason why it is theoretical/analytical instead of empirical.

## Baseline policy

Include:

- strong classical baseline when relevant;
- recent neural/agentic/SOTA baseline;
- domain-specific baseline used by the target community;
- simple heuristic baseline if it tests whether complexity is necessary;
- oracle, upper bound, or positive control when possible;
- previous method from the closest competitor.

If a baseline is omitted, document why: unavailable code, compute infeasible, incompatible setting, licensing issue, or not relevant.

## Ablation policy

Ablate every component named as a contribution:

- remove component;
- replace with simpler variant;
- vary hyperparameter or threshold;
- test sensitivity to data size/noise/domain shift;
- test negative, hard, or adversarial cases;
- isolate retrieval, planning, representation, objective, and feedback modules when applicable.

## Reliability and statistics

When variance matters, use multiple seeds and report mean/std or confidence intervals. For expensive agent experiments, use a smaller pilot plus targeted full run and disclose sample size limits. Use statistical tests only when their assumptions are credible.

## Reproducibility passport

Record:

- code repository or commit;
- environment and package versions;
- model names and versions;
- prompts or agent configs;
- random seeds;
- hardware;
- dataset versions and splits;
- exact command or notebook path;
- cost or runtime;
- raw log/table locations.

## Top-conference stress tests

Add at least one stress test when feasible:

- out-of-domain transfer;
- low-data setting;
- noisy input;
- adversarial or hard subset;
- scaling with problem size;
- compute/cost-efficiency frontier;
- failure-case taxonomy;
- contamination/leakage check for LLM or benchmark tasks.

## Result presentation

For every table or figure, state:

- What claim it tests.
- What result supports the claim.
- What result weakens the claim.
- What alternative explanation remains.
- What limitation should be disclosed.

## Default output

```text
Mode:
Venue and assumptions:
Central claims:
Claim-evidence matrix:
Dataset / benchmark needs:
Baseline matrix:
Main experiments:
Ablations:
Robustness / failure / efficiency:
Statistics and reliability:
Result tables or figure specs:
Reproducibility passport:
Missing values:
Execution priority:
No-fabrication status:
Next mode:
```
