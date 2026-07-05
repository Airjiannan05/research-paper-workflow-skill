---
name: rpw-experiment-design
description: "Design experiments that test paper claims: datasets, baselines, metrics, ablations, robustness tests, and result-table shells. Produce a claim-to-test mapping with execution priority. Use for experiment design, baseline planning, 实验设计, 设计baseline, 消融实验规划. Do not implement code — that's rpw-experiment-implementation."
---

# RPW Experiment Designer

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill designs what to test; it does not write code. Route implementation to `rpw-experiment-implementation`.

## Core Rule

Every experiment must serve a claim. Every major claim must have an evidence path through experiments. Use `../references/experiment-design.md` for the full protocol.

## Workflow

1. Load the claim manifest and idea brief. Identify every claim that requires empirical support.
2. For each claim, design the evidence package: datasets/workloads, baselines, metrics, ablations, robustness/failure tests, and efficiency analysis.
3. Apply the baseline policy: strong classical baseline, recent SOTA baseline, domain-specific baseline, simple heuristic, oracle/upper-bound, closest competitor.
4. Apply the ablation policy: remove each named component, replace with simpler variant, vary hyperparameters, test sensitivity to data/noise/domain shift.
5. Design result-table shells with `TBD` placeholders (do not invent values).
6. Plan statistical reliability: multiple seeds, mean/std or confidence intervals.
7. Assign execution priority: P0 (must-have for claims), P1 (strengthens claims), P2 (nice-to-have).
8. Record reproducibility passport items per `../references/reproducibility-passport.md`.

## Output Contract

```text
Venue and assumptions:
Claim-to-test mapping:
| Claim | Evidence | Dataset | Baselines | Ablation | Metric | Robustness | Priority | Status |
|---|---|---|---|---|---|---|---|
...
Baseline matrix (with rationale for any omission):
Ablation plan:
Result table shells:
Statistics plan:
Reproducibility passport (partial — to be completed by implementation):
```

## Handoff

End with a next-step menu. Recommended: `rpw-experiment-implementation`.

## Reference Files

- `../references/experiment-design.md`: Full protocol.
- `../references/reproducibility-passport.md`: Reproducibility tracking.
- `../assets/experiment_plan_template.md`: Plan template.
