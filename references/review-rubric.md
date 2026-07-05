# Review Rubric

Use this for simulated peer review, writing review, venue-fit diagnosis, and revision planning.

## Review modes

- `scientific`: novelty, soundness, evidence, experiments, reproducibility, ethics, score risk.
- `writing`: paragraph logic, section flow, contribution display, claim-evidence presentation, terminology, figure/table narration.
- `full`: scientific + writing + format + action synthesis.
- `quick`: top concerns and immediate fixes only.

## Core criteria

| Criterion | Reviewer question |
|---|---|
| Novelty | Is the core idea meaningfully new relative to close prior work? |
| Non-triviality | Does the paper solve a hard technical/conceptual problem, not just apply a tool? |
| Insight | Is there a clear mechanism, abstraction, or empirical regularity? |
| Soundness | Are assumptions, algorithms, proofs, and experiments valid? |
| Evidence | Do experiments/proofs directly test the claims? |
| Baselines | Are comparisons strong, fair, and current? |
| Ablations | Are claimed components isolated? |
| Reproducibility | Could a competent researcher reproduce the result? |
| Clarity | Can reviewers understand the contribution quickly? |
| Scope | Are limitations honest and not overclaimed? |

## Score-risk interpretation

Use scores as diagnostic feedback, not acceptance probabilities. Every low score must have a concrete deduction and repair condition.

## Reviewer panel

For a full review, simulate:

- Reviewer A: novelty and related-work specialist.
- Reviewer B: methods/soundness specialist.
- Reviewer C: experiments/reproducibility specialist.
- Reviewer D: skeptical devil's advocate.
- AC/meta-review: synthesizes risks and required repairs.

Do not force artificial disagreement. Disagreement must come from actual evidence or role-specific criteria.

## Concern-to-action table

| Concern | Severity | Evidence basis | Criterion | Fix class | Owner mode | Score-impact condition |
|---|---|---|---|---|---|---|

Fix classes: run experiment, add baseline, add ablation, narrow claim, add citation, rewrite section, clarify method, disclose limitation, verify venue rule, remove unsupported claim.

## Output contracts

### Standard review

```text
Mode:
Venue and assumptions:
Paper summary:
Likely stance and calibrated score/risk:
Quantitative scorecard:
Top strengths:
Major/fatal concerns:
Writing and presentation concerns:
Format/venue concerns:
Multi-reviewer panel:
Concern-to-action table:
Recommended next mode:
Checks run:
Unresolved or unverified:
Output self-check:
```

### Quick review

```text
Mode:
Likely stance:
Top concerns:
Immediate fixes:
Missing checks:
Next mode:
```
