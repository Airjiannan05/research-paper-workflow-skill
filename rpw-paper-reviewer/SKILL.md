---
name: rpw-paper-reviewer
description: "Simulate a strict but fair reviewer panel and AC/meta-review. Produce decision-relevant findings with scores, evidence basis, severity, repair actions, and score-impact conditions. Use for paper review, simulated review, acceptance risk, 审稿, 模拟审稿, 论文评分, 写作评审. Do not rewrite the paper — that's rpw-paper-writer."
---

# RPW Paper Reviewer

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill judges; it does not rewrite. Route revision to `rpw-paper-writer`. Do not write rebuttal text — route to `rpw-rebuttal`.

## Core Rule

Act as a strict but fair reviewer and AC. Tie every concern to manuscript evidence or a verifiable source. Do not invent citations, results, consensus, or acceptance probabilities. Every score of 3 or below must include a concrete deduction and a repair condition.

## Workflow

1. Identify review mode: scientific, writing/presentation, or full (scientific + writing).
2. Extract the paper summary, claimed contributions, evidence package, and major claims.
3. Apply the review rubric from `../references/review-rubric.md`.
4. For scientific review, assess: novelty, soundness, evidence quality, baseline strength, ablation thoroughness, reproducibility, ethics.
5. For writing review, assess: clarity, structure, contribution display, figure/table narration, terminology consistency.
6. Produce concerns with: severity (fatal / major / minor), evidence basis, affected criterion, fix class (writing-fixable / design-fixable / evidence-fixable / requires-new-result), owner skill, and score-impact condition.
7. Simulate a multi-reviewer panel with independent perspectives (2-4 reviewers). Disagreement must come from evidence, not forced contrast.
8. Produce an AC/meta-review synthesis: calibrated score, top strengths, strongest rejection risk, and repair roadmap.

## Output Contract

```text
Mode: scientific / writing / full
Venue and assumptions:
Paper summary:
Likely stance and calibrated score:
Top strengths (evidence-grounded):
Major/fatal concerns:
| Concern | Severity | Evidence | Criterion | Fix class | Owner | Score impact |
|---|---|---|---|---|---|---|
...
Minor concerns:
Reviewer panel (Reviewer A/B/C/D):
AC/meta-review:
Repair roadmap:
```

## Handoff

End with a next-step menu. Route the strongest concern to its owner skill (e.g., weak novelty → `rpw-literature-search`, weak baselines → `rpw-experiment-design`, weak narrative → `rpw-paper-writer`).

## Reference Files

- `../references/review-rubric.md`: Review criteria and scoring.
- `../assets/reviewer_report_template.md`: Report template.
- `../references/next-step-menu.md`: For menu contract.
