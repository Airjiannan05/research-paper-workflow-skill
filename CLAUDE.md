# Claude Code Guide: Research Paper Workflow

Use this repository as a Claude Code compatible research-engineering skill for CS/AI/AI4Science paper projects. Start by reading `SKILL.md`, then load only the reference files needed for the current mode.

## Primary operating rules

1. Treat `SKILL.md` as the canonical workflow contract.
2. Maintain `paper_state.yaml` when the user wants a multi-turn or repository-backed project.
3. Keep artifact ownership separate: literature, experiment design, implementation, result engineering, writing, review, audit, submission, and rebuttal should not overwrite each other.
4. End every completed stage with the `Next-step options` menu defined in `references/next-step-menu.md`.
5. For every externally queried or source-dependent fact, apply the triple-check protocol in `references/source-verification.md`: existence check, metadata check, and support check.
6. Do not fabricate papers, citations, repositories, venue rules, datasets, benchmark results, experiment logs, or provenance.
7. Prefer concrete file edits and runnable artifacts over vague plans.

## Claude Code usage pattern

When opened inside a project, first inspect the local context:

```bash
pwd
find . -maxdepth 3 -type f | sort | sed -n '1,120p'
```

Then identify the workflow mode from the user's request:

- `pipeline`: initialize or route the whole project.
- `idea-optimize`: turn a vague direction into a falsifiable research story.
- `idea-review`: pressure-test novelty, insight, feasibility, and venue fit.
- `literature-monitor`: track recent competitors, scoop risk, arXiv/OpenReview updates.
- `literature-search`: build paper cards, related-work matrix, source verification log.
- `experiment-design`: map claims to datasets, baselines, metrics, ablations, and result-table shells.
- `experiment-implementation`: create repo layout, config schema, run matrix, commands, logging schema, acceptance tests.
- `result-engineering`: validate logs, aggregate repeated runs, produce CSV/Markdown/LaTeX tables.
- `result-analysis`: interpret verified results into supported claims and limitations.
- `paper-writer`: draft, revise, polish, compress, and preserve LaTeX/Markdown format.
- `paper-reviewer`: simulate reviewer panel and AC/meta-review.
- `integrity-audit`: check claim, citation, numeric, result, and source-support consistency.
- `submission-check`: verify venue-specific rules, anonymity, PDF metadata, artifacts, and AI disclosure.
- `rebuttal`: build issue taxonomy, revision ledger, and point-by-point response plan.

## Recommended project files

For a local paper project, create or update these files as needed:

```text
paper_state.yaml
idea_brief.md
literature_search_plan.md
paper_cards.md
related_work_matrix.md
claim_manifest.md
experiment_plan.md
implementation_plan.md
run_matrix.csv
source_verification_log.md
results/raw/runs.csv
results/processed/aggregated_results.csv
paper/main.tex or paper_draft.md
review_report.md
integrity_report.md
submission_checklist.md
revision_ledger.md
```

Use templates from `assets/` whenever creating a new artifact.

## Running bundled scripts

The scripts are intentionally lightweight and standard-library first. Run them from the skill root or pass explicit paths.

Examples:

```bash
python scripts/validate_paper_state.py paper_state.yaml
python scripts/check_claim_manifest.py claim_manifest.md
python scripts/generate_run_matrix.py --help
python scripts/validate_result_logs.py results/raw/runs.csv
python scripts/aggregate_results.py results/raw/runs.csv --metrics accuracy,f1 --out results/processed/aggregated_results.csv
python scripts/make_latex_tables.py results/processed/aggregated_results.csv --out results/tables/main_results.tex
python scripts/check_source_verification_log.py source_verification_log.md
```

If a script interface differs from these examples, inspect the script help or source before running it. Do not assume missing files exist.

## Research-engineering default workflow

For empirical CS/AI projects, prefer this route:

```text
claim-manifest
-> experiment-design
-> experiment-implementation
-> run experiments outside the skill
-> result-engineering
-> result-analysis
-> paper-writer
-> integrity-audit
-> paper-reviewer
-> submission-check
```

If a gate fails, do not continue as if it passed. Use the repair route and show the user the smallest concrete fix.

## Source verification behavior

When using web search, local PDFs, GitHub repositories, venue pages, or benchmark documentation:

1. Confirm that the source exists.
2. Confirm metadata: title/name, authors/owners, date/version, venue/source, URL/DOI/arXiv/repository path, and current/superseded status.
3. Confirm that the source actually supports the claim being made.

Record load-bearing facts in `source_verification_log.md`. Mark unresolved facts as `partial`, `unverified`, or `conflict`. Do not cite or write them as settled facts.

## Human-in-the-loop boundaries

The user owns research decisions, authorship, final claims, experiment truth, and submission choices. Claude Code may propose artifacts, edit files, run structural scripts, and check consistency, but must not invent hidden work, fabricate results, bypass disclosure rules, or present unverified claims as evidence.
