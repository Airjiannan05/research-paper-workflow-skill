# Routing and Artifact Contract

Use this file to keep the workflow stable when multiple paper tasks appear in one conversation.

## Owner boundaries

| User intent | Use mode | Do not use as main mode |
|---|---|---|
| Shape a weak idea into a research proposal | idea-optimize | idea-review |
| Score, rank, or kill/keep ideas | idea-review | idea-optimize |
| Track recent competitors or scoop risk | literature-monitor | integrity-audit |
| Search related work, benchmarks, datasets, baselines | literature-search | paper-writer |
| Verify already-used citations, source metadata, and claim contexts | integrity-audit | literature-search |
| Design baselines, metrics, ablations, result tables | experiment-design | paper-writer |
| Write, polish, compress, translate, or format paper text | paper-writer | paper-reviewer |
| Judge acceptance risk or simulate reviews | paper-reviewer | paper-writer |
| Check page limits, anonymity, PDF/package readiness | submission-check | paper-writer |
| Respond to reviewers or maintain revision ledger | rebuttal | paper-reviewer |

## Artifact ownership

| Artifact | Primary owner | Other modes may |
|---|---|---|
| `paper_state.yaml` | pipeline | read/update stage status |
| idea brief | idea-optimize | review, derive experiments, write intro |
| idea review | idea-review | guide rescue and experiment changes |
| literature notes/cards | literature-search | support related work and citation audit; include verification status for load-bearing sources |
| experiment plan/results | experiment-design | support writing and integrity audit |
| manuscript | paper-writer | review/audit/check only unless asked to revise |
| review report | paper-reviewer | drive revision and rebuttal |
| integrity report and source verification log | integrity-audit | drive safe edits and evidence search |
| submission checklist | submission-check | guide final formatting |
| revision ledger | rebuttal | track review-to-action closure |

## Handoff format

When handing off, include:

```text
Current mode:
Artifact produced:
Evidence gaps:
Risks:
Recommended next mode:
Why this mode:
```

Avoid listing irrelevant next modes. If the user asks for direct output, provide the output first and handoff notes after.


## Next-step menu

After the handoff format, append a compact menu from `next-step-menu.md`. The recommended option must be the next owner mode unless a gate failed. If the user replies with a letter, `next`, `repair`, or a mode name, route directly to that option without asking for clarification.


## Source verification routing

When a user asks for search, verification, current rules, or source-backed claims, route through `references/source-verification.md`. Literature search discovers and organizes sources; integrity audit verifies whether already-used sources truly support manuscript claims. Do not let writing mode introduce unverified facts. If a writer needs a fact, add `[VERIFY]` and hand off to literature-search or integrity-audit.
