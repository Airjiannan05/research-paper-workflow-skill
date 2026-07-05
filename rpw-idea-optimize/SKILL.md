---
name: rpw-idea-optimize
description: "Turn rough research directions into a concrete, falsifiable research story: problem, gap, root challenge, insight, method, minimum experiment, and novelty threats. Use for idea optimization, direction shaping, rescue routes, 优化idea, 找方向, 研究思路优化, 方向探索. Do not rank or score multiple ideas — that's rpw-idea-review."
metadata:
  rpw_skill_controls:
    handoff_question_mode: partial
    shared_controls: ../rpw-common/
---

# RPW Idea Optimizer

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. Load `../references/source-verification.md` before making novelty claims.

## Core Rule

Optimize the idea before optimizing the writing. Turn a vague direction into a falsifiable research story. Do not inflate novelty, invent related work, or turn weak ideas into confident claims. For fuzzy ideas, generate diverse concretizations; mark novelty as uncertain until searched.

## Workflow

1. Identify target venue, field, and idea maturity. If no venue is named, assume a generic CCF-A target and label the assumption.
2. Apply the storyline blueprint from `../references/storyline-blueprint.md`: problem → gap → root challenge → insight → method → evidence → limitation.
3. Normalize the idea into: working title, task/setting, problem, why it matters, current approach families, gap, root challenge, key insight, proposed mechanism, falsifiable central claim, minimum viable experiment, novelty threats, scope and non-goals.
4. If the idea is fuzzy, generate 3-5 candidate concretizations with diverse angles. Do not kill a direction just because it's currently weak; produce at least one rescue route.
5. Classify innovation type: problem, setting, method, data/benchmark, theory, system, empirical finding, evaluation, or synthesis.
6. Mark novelty as `needs-search` until grounded against closest known work.
7. Produce the output contract below.

## Output Contract

```text
Working title:
Target venue / community:
Task and setting:
Problem:
Why it matters:
Current approach families:
Gap:
Root challenge:
Key insight:
Proposed mechanism:
Falsifiable central claim:
Minimum viable experiment:
Novelty threats (marked needs-search / verified / partial):
Scope and non-goals:
Rescue routes (if applicable):
```

## Handoff

End with a next-step menu per `../references/next-step-menu.md`. Recommended: `rpw-idea-review` for pressure-testing, or `rpw-literature-search` if novelty is unverified.

## Reference Files

Load only what is needed:
- `../references/storyline-blueprint.md`: For problem-gap-insight-method chain.
- `../references/source-verification.md`: Before making novelty claims.
- `../references/next-step-menu.md`: For menu contract.
