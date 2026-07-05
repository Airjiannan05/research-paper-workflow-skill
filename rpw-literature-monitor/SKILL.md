---
name: rpw-literature-monitor
description: "Track recent competitors, scoop risk, and new papers on arXiv, OpenReview, and conference venues. Use for competitor monitoring, new-paper tracking, scoop watch, 竞品监控, 新论文追踪, 最近有没有类似idea. Do not do deep related-work search — that's rpw-literature-search."
---

# RPW Literature Monitor

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill watches for recent and upcoming work; it does not perform deep literature review. Route systematic search requests to `rpw-literature-search`.

## Core Rule

Monitor recent publications and preprints for competitor overlap. Detect scoop risk early. For each finding, assess overlap level and recommend action: RELAX (no conflict), RESEARCH (need more detail), or FOLLOW-UP (high overlap — escalate to idea review or literature search).

## Workflow

1. Identify the research topic, keywords, target venues, and time window.
2. Search arXiv, OpenReview, and venue proceedings for recent matches. Apply the triple-check protocol from `../references/source-verification.md` for every paper found.
3. For each relevant paper, assess:
   - Problem overlap: same / related / different
   - Method overlap: same mechanism / similar family / different approach
   - Setting overlap: same dataset/domain / related / different
   - Evidence overlap: same claims / overlapping / distinct
4. Assign overlap level and action:
   - **RELAX**: No material overlap — note and move on.
   - **RESEARCH**: Partial overlap — flag for deeper search.
   - **FOLLOW-UP**: High overlap — escalate with specific concerns.
5. Produce a monitoring report with handoff recommendations.

## Output Contract

```text
Monitoring period:
Keywords and venues searched:
Papers found: N
Overlap summary:
  RELAX: N papers — <brief note>
  RESEARCH: N papers — <what to investigate>
  FOLLOW-UP: N papers — <specific concern and recommended action>
Handoff: <rpw-literature-search | rpw-idea-review | rpw-idea-optimize>
```

## Handoff

End with a next-step menu. FOLLOW-UP items route to `rpw-literature-search` or `rpw-idea-review`.

## Reference Files

- `../references/source-verification.md`: Triple-check every paper found.
- `../references/literature-review.md`: For search strategy and paper card format.
- `../references/next-step-menu.md`: For menu contract.
