# Architecture

## Design Philosophy

This skill treats a paper as a **research storyline**, not a text-generation task. The core insight is: paper quality comes from the quality of sequential decisions — idea formation, literature positioning, experiment design, implementation, result interpretation, writing, review, audit, submission, and rebuttal. Each stage has a clear owner; artifacts don't overwrite each other; gates must pass before proceeding.

### Why Monolithic

This skill uses a single `SKILL.md` rather than splitting into 15 individual skill directories. The trade-off:

| Approach | Pros | Cons |
|---|---|---|
| **Monolithic** (this skill) | Simpler install, no routing ambiguity, consistent state via `paper_state.yaml` | Full context loaded every time; harder to maintain individual modes |
| **Multi-skill** (CCFA-Skills) | Progressive disclosure, independent evolution, clear trigger boundaries | Complex install, routing conflicts, cross-skill state sync |

For most solo researchers, the monolithic approach is sufficient. Teams or projects that need independent mode evolution should consider splitting.

## Architecture Layers

```
User Request
    │
    ▼
┌─────────────────────────────────────────┐
│ SKILL.md          ← Canonical contract   │
│ Entry point table → mode routing         │
│ Stage map → stage gates                  │
│ Mode rules → behavior per mode           │
└──────────────┬──────────────────────────┘
               │ loads on demand
    ┌──────────┼──────────┐
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│references/ │ assets/  │ scripts/│
│            │          │         │
│ workflow   │ templates│ validate │
│ source-    │ paper    │ generate │
│  verification│ state  │ aggregate│
│ experiment │ config   │ check    │
│  design    │ logging  │ build    │
│ writing    │ run      │ make     │
│ review     │ matrix   │ latex    │
│ rebuttal   │ ...      │ ...      │
└────┬───────┘ └────┬────┘ └────┬────┘
     │              │           │
     └──────────────┼───────────┘
                    ▼
            paper_state.yaml
            (shared project state)
                    │
                    ▼
            User's Paper Project
            (code, results, manuscript)
```

## Platform Adapters

| Layer | File | Platform |
|---|---|---|
| Canonical contract | `SKILL.md` | All platforms |
| Agent routing | `AGENT_GUIDE.md` | All AI agents |
| Plugin manifest | `.claude-plugin/plugin.json` | Claude Code |
| Plugin manifest | `.codex-plugin/plugin.json` | OpenAI Codex CLI |
| Interface metadata | `agents/openai.yaml` | ChatGPT Custom GPT |
| Local conventions | `CLAUDE.md` | Claude Code (project-local) |
| Quick-start guide | `README_claude_code.md` | Claude Code users |
| Prompt examples | `examples/claude_code_prompts.md` | Claude Code users |

## Data Flow

```text
idea_brief.md
  → literature_search_plan.md
  → paper_cards.md
  → related_work_matrix.md
  → claim_manifest.md
  → experiment_plan.md
  → implementation_plan.md
  → run_matrix.csv
  → results/raw/runs.csv
  → results/processed/aggregated_results.csv
  → result_audit.md
  → results_analysis.md
  → paper_draft.tex / paper_draft.md
  → review_report.md
  → integrity_report.md
  → submission_checklist.md
  → revision_ledger.md
```

Each transition preserves provenance. No artifact moves forward if the previous gate failed.

## Gate System

Every stage has an explicit gate. If a gate fails:

1. The next-step menu marks `[Repair first]` instead of `[Recommended]`
2. The repair path is option A
3. Downstream stages are blocked until the gate passes

Gates prevent: writing without evidence, submitting without audit, rebutting without revision tracking.

## Source Verification Layer

All externally queried facts pass through `references/source-verification.md`:

```text
Claim → Existence check → Metadata check → Support check → Verdict
                                                              │
                                    ┌─────────────────────────┼──────────────────────┐
                                    ▼                         ▼                      ▼
                                verified                   partial              unverified
                                (usable)              (cautious wording)      (marked [VERIFY])
```

Unverified facts are never used as load-bearing claims.

## Extension Points

- **New mode**: Add entry to SKILL.md stage map + mode rules + AGENT_GUIDE.md routing + next-step-menu.md successor
- **New script**: Add to `scripts/`, document in CLAUDE.md
- **New template**: Add to `assets/`, reference in the relevant mode rule
- **New reference**: Add to `references/`, link from the mode that needs it
- **New platform**: Add plugin manifest, update README installation section
