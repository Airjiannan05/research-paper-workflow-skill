# Section Modules

Use these modules when drafting, revising, or reviewing paper sections.

## Abstract

Structure: setting -> gap -> insight/method -> evidence -> contribution.

Avoid unsupported superlatives. If results are missing, use evidence placeholders instead of fake numbers.

## Introduction

Paragraph roles:

1. Broad problem and why it matters to the venue community.
2. Existing approach families and their shared limitation.
3. Root challenge: why the limitation is hard.
4. Key insight and proposed mechanism.
5. Evidence preview: benchmarks, ablations, analysis.
6. Contributions as specific, testable claims.

## Related Work

Use a taxonomy, not a chronological list. For each class: summarize mechanism, identify limitation, and position the current paper. End with the gap that motivates the method.

## Method

Make the mechanism testable:

- inputs/outputs;
- assumptions;
- algorithm or architecture;
- objective or decision rule;
- complexity/cost when relevant;
- why each component exists;
- expected failure mode.

## Experiments

Open with claim-to-test mapping. Then describe datasets/workloads, baselines, metrics, implementation details, main results, ablations, robustness/failure/efficiency, and limitations.

## Limitations

State concrete boundaries. Prefer: setting limitation, evidence limitation, method limitation, compute/data limitation, external validity limitation.

## Conclusion

Do not introduce new claims. Restate the insight, evidence, and future direction cautiously.
