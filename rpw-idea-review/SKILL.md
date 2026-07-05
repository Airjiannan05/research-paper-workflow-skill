---
name: rpw-idea-review
description: "Strictly review a research idea for novelty, non-triviality, insight quality, feasibility, evidence path, and venue fit. Score and recommend keep/modify/kill. Use for idea ranking, scoring, go/no-go decisions, 评审idea, idea打分, 判断创新性, 取舍. Do not optimize or rescue ideas — that's rpw-idea-optimize."
metadata:
  rpw_skill_controls:
    handoff_question_mode: partial
    shared_controls: ../rpw-common/
---

# RPW Idea Reviewer

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill judges; it does not rescue. Route idea improvement requests to `rpw-idea-optimize`.

## Core Rule

Review strictly. Score novelty, non-triviality, insight, feasibility, evidence path, and venue fit. Give repair conditions; do not continue optimizing unless asked. A kill recommendation must cite a specific, unfixable gap.

## Workflow

1. Load the idea brief (`idea_brief.md`) or the user's idea description.
2. Score each dimension on a 1-5 scale with evidence basis:
   - **Novelty**: Is the problem, mechanism, or setting new vs. known prior work?
   - **Non-triviality**: Does the method require non-obvious insight?
   - **Insight quality**: Is the core insight deep and generalizable?
   - **Feasibility**: Can this be executed with available resources?
   - **Evidence path**: Is there a clear path from claim to experiment?
   - **Venue fit**: Does the contribution match the target venue's bar?
3. Identify the most likely rejection reason.
4. List repair conditions: what must change for each weak dimension.
5. Give a keep / modify / kill recommendation with rationale.

## Output Contract

```text
Venue and assumptions:
Scores:
  Novelty: X/5 — <evidence>
  Non-triviality: X/5 — <evidence>
  Insight quality: X/5 — <evidence>
  Feasibility: X/5 — <evidence>
  Evidence path: X/5 — <evidence>
  Venue fit: X/5 — <evidence>
Likely rejection reason:
Repair conditions:
Recommendation: keep / modify / kill
If modify: what to change and in which order.
If kill: the specific unfixable gap.
```

## Handoff

End with a next-step menu. If keep/modify: `[Recommended] rpw-literature-search`. If kill: `[Repair first] rpw-idea-optimize`.

## Reference Files

- `../references/source-verification.md`: Before validating novelty claims against external sources.
- `../references/next-step-menu.md`: For menu contract.
