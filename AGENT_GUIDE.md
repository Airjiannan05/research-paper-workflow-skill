# Agent Guide

Use this guide when operating the Research Paper Workflow skill as an agent.

## Core Rules

1. Read `SKILL.md` first, then load only the reference files needed for the current mode.
2. Route by the user's primary intent using the entry point table in `SKILL.md`, not by possible downstream work.
3. Treat `paper_state.yaml` as the shared project state. Update `project.stage` and the produced artifact after every completed gate.
4. For every externally queried or source-dependent fact, apply the triple-check protocol in `references/source-verification.md`: existence check, metadata check, and support check.
5. End every completed stage with the `Next-step options` menu defined in `references/next-step-menu.md`. Mark exactly one option as `[Recommended]` or `[Repair first]`.
6. If a gate fails, do not continue as if it passed. Offer repair as the first option and clearly mark the failure.
7. Do not fabricate papers, citations, repositories, venue rules, datasets, benchmark results, experiment logs, or provenance.

## Mode Routing

| User says | Route to | Do NOT use |
|---|---|---|
| Vague idea, weak topic, direction rescue | `idea-optimize` | idea-review, paper-writer |
| Compare/rank ideas, novelty risk, go/no-go | `idea-review` | idea-optimize |
| Recent competitor, scoop watch, arXiv tracking | `literature-monitor` | literature-search |
| Related work, datasets, benchmarks, prior art | `literature-search` | integrity-audit |
| Design experiments, baselines, metrics, ablations | `experiment-design` | paper-writer |
| Turn experiment plan into code/config/run matrix | `experiment-implementation` | experiment-design |
| Validate logs, aggregate seeds, generate tables | `result-engineering` | paper-writer |
| Interpret results into claims and limitations | `result-analysis` | paper-writer |
| Draft, revise, polish, compress paper text | `paper-writer` | paper-reviewer |
| Simulate reviewer panel and AC/meta-review | `paper-reviewer` | paper-writer |
| Check claim/citation/result/number consistency | `integrity-audit` | literature-search |
| Verify venue rules, anonymity, PDF metadata | `submission-check` | paper-writer |
| Respond to reviewers, revision ledger | `rebuttal` | paper-reviewer |
| Full project breakdown into stages | `pipeline` | any single owner mode |

## Artifact Ownership

- `paper_state.yaml` — pipeline (read/update by all modes)
- `idea_brief.md` — idea-optimize (review, derive experiments, write intro)
- `idea_review.md` — idea-review (guide rescue and experiment changes)
- `literature_search_plan.md`, `paper_cards.md` — literature-search (support related work and citation audit)
- `related_work_matrix.md` — literature-search (expose concrete gaps)
- `claim_manifest.md` — claim-manifest (drive experiment design)
- `experiment_plan.md` — experiment-design (support implementation and writing)
- `implementation_plan.md`, `run_matrix.csv` — experiment-implementation (feed result engineering)
- `result_audit.md`, `tables/*.tex` — result-engineering (drive result analysis)
- `results_analysis.md` — result-analysis (supported claims → paper-writer)
- `paper_draft.tex` or `paper_draft.md` — paper-writer (review/audit/check only)
- `review_report.md` — paper-reviewer (drive revision and rebuttal)
- `integrity_report.md`, `source_verification_log.md` — integrity-audit (drive safe edits)
- `submission_checklist.md` — submission-check (guide final formatting)
- `revision_ledger.md` — rebuttal (track review-to-action closure)

## Output Shape

- For broad requests, produce dense artifacts rather than fragments.
- A full-paper request should yield a submission-shaped manuscript, not an outline.
- Polishing preserves the user's original Markdown/LaTeX format.
- From-scratch manuscripts use venue-aware section budgets with `TBD`/`[CITE]`/`[VERIFY]` placeholders.
- Never invent results, citations, or provenance to fill gaps.

## Gate Behavior

If a gate fails, the artifact is incomplete. The next-step menu must offer:

```
A. [Repair first] <repair action> — <what to fix and why>.
B. <narrow scope or gather missing evidence>.
C. <pause/export with risk marked>.
```

Do not route to the next stage until the gate passes.

## Source Verification

Before using any externally queried fact as evidence:
1. **Existence check** — confirm the source exists at a primary/reliable source.
2. **Metadata check** — confirm title, authors, date, version, venue, URL/DOI/arXiv/repo path.
3. **Support check** — confirm the cited passage actually supports the claim.

Mark results as `verified`, `partial`, `unverified`, or `conflict`. Never use unverified facts as load-bearing claims.

## Shortcut Commands

Accept these user replies as commands:
- `A`, `B`, `C`, `D` — execute the corresponding next-step option.
- `next` — execute the recommended option.
- `repair` — execute the repair option.
- A mode name (e.g., `experiment-implementation`) — route directly to that mode.
