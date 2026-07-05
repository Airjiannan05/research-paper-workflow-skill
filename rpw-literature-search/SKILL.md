---
name: rpw-literature-search
description: "Systematic literature search for prior art, benchmarks, baselines, SOTA methods, and open gaps. Produce paper cards, a mechanism-level related-work matrix, and a gap synthesis. Use for related work search, literature review, benchmark discovery, 文献检索, 相关工作搜索, 找baseline, 找benchmark. Do not verify already-cited sources in a manuscript — that's rpw-integrity-audit."
metadata:
  rpw_skill_controls:
    handoff_question_mode: partial
    shared_controls: ../rpw-common/
---

# RPW Literature Searcher

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill discovers and organizes sources; it does not audit citations already in a manuscript. Route citation verification to `rpw-integrity-audit`.

## Core Rule

Search systematically. Produce paper cards with mechanism-level analysis, a related-work matrix that exposes concrete gaps, and a source verification log. Every load-bearing fact must pass the triple-check protocol in `../references/source-verification.md`.

## Workflow

1. Identify keywords, synonyms, exclusion terms, target venues, and year range. Load `../references/literature-review.md` for search strategy.
2. Search with seed papers, backward/forward citation expansion, SOTA/baseline discovery, and negative/contradictory evidence.
3. For each relevant paper, create a paper card: input, representation, core mechanism, supervision/data, output, evaluation, strength, limitation, relation to this work, novelty threat level.
4. Build a mechanism-level related-work matrix. Load `../assets/related_work_matrix_template.md`.
5. Run triple-check verification: existence, metadata, and support for every load-bearing fact.
6. Update `source_verification_log.md` with verdicts (verified / partial / unverified / conflict).
7. Synthesize gaps: what is NOT solved, what settings are unexplored, what mechanisms are untried.

## Output Contract

```text
Search strategy:
Paper cards (N papers):
Related-work matrix:
Gap synthesis:
Source verification log:
Novelty implications:
```

## Handoff

End with a next-step menu. Recommended: `rpw-claim-manifest` if gaps are clear, or deepen search if gaps are thin.

## Reference Files

- `../references/literature-review.md`: Search strategy and paper card format.
- `../references/source-verification.md`: Triple-check protocol.
- `../assets/paper_card_template.md`: Paper card template.
- `../assets/related_work_matrix_template.md`: Matrix template.
- `../assets/source_verification_log_template.md`: Log template.
