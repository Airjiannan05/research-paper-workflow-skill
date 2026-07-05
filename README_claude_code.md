# Research Paper Workflow for Claude Code

This package is a Claude Code compatible research workflow skill for developing CS/AI/AI4Science papers from idea to submission. It adds Claude Code oriented instructions on top of the generic `SKILL.md` workflow.

## What this adds

The base skill already contains:

- `SKILL.md`: the canonical skill entry point.
- `references/`: workflow rules for literature search, experiment design, research engineering, writing, review, audit, submission, and rebuttal.
- `assets/`: reusable templates.
- `scripts/`: lightweight structural utilities.

The Claude Code compatibility layer adds:

- `CLAUDE.md`: local project instructions for Claude Code.
- `README_claude_code.md`: this guide.
- `examples/`: copyable Claude Code prompts and example artifact flows.
- `scripts/requirements.txt`: dependency note for bundled scripts.

## Quick install

**Clone and symlink** (recommended — easy to update):

```bash
git clone https://github.com/Airjiannan05/research-paper-workflow-skill.git ~/research-paper-workflow-skill
ln -s ~/research-paper-workflow-skill ~/.claude/skills/research-paper-workflow
```

**Manual copy — project-local** (only this project):

```bash
git clone https://github.com/Airjiannan05/research-paper-workflow-skill.git
mkdir -p .claude/skills/research-paper-workflow
cp -r research-paper-workflow-skill/SKILL.md research-paper-workflow-skill/CLAUDE.md research-paper-workflow-skill/references/ research-paper-workflow-skill/assets/ research-paper-workflow-skill/scripts/ .claude/skills/research-paper-workflow/
```

Restart Claude Code after installation. Verify with: `/list-skills` or ask *"What skills are available?"*

## How to use

Open Claude Code in your paper project directory, then just describe your task in natural language — the skill triggers automatically:

```text
Use research-paper-workflow. Initialize a paper_state.yaml for a top-conference CS/AI paper. Start with pipeline + idea-optimize. End with next-step options.
```

For a project-local setup, you can also copy `CLAUDE.md` into your paper repository root and keep the full skill folder under `skills/research-paper-workflow/`.

Suggested layout:

```text
my-paper-project/
├── CLAUDE.md
├── skills/
│   └── research-paper-workflow/
├── paper_state.yaml
├── idea_brief.md
├── experiment_plan.md
├── implementation_plan.md
├── run_matrix.csv
├── results/
└── paper/
```

## Quick start prompts

Initialize a project:

```text
Use research-paper-workflow. Initialize a paper_state.yaml for a top-conference CS/AI paper. Start with pipeline + idea-optimize. End with next-step options.
```

Turn an experiment plan into implementation tasks:

```text
Use experiment-implementation mode. Based on experiment_plan.md, create implementation_plan.md, config schema, run_matrix.csv, command templates, result logging schema, baseline checklist, acceptance tests, and reproducibility passport.
```

Validate and aggregate results:

```text
Use result-engineering mode. Check results/raw/runs.csv against run_matrix.csv. Report duplicate run IDs, missing seeds, failed runs, missing provenance, and aggregate mean/std/count tables. Generate LaTeX table snippets.
```

Audit sources and claims:

```text
Use integrity-audit mode. For each load-bearing claim, check claim support, citation support, numeric consistency, and source verification status. Apply the three-check source verification protocol.
```

## Mode map

| Mode | Use when | Main outputs |
|---|---|---|
| `pipeline` | You need the full project route | stage plan, artifact contract, next owner |
| `idea-optimize` | Idea is vague or weak | idea brief, falsifiable claim, novelty threats |
| `idea-review` | You need a strict go/no-go assessment | novelty/insight/feasibility diagnosis |
| `literature-search` | You need prior art, benchmark, baseline evidence | paper cards, taxonomy, source verification log |
| `experiment-design` | You need experiments that test claims | claim-to-test map, baselines, ablations, table shells |
| `experiment-implementation` | You need runnable engineering tasks | repo layout, config schema, run matrix, logging schema |
| `result-engineering` | You have run logs/results | validation report, aggregated CSV, LaTeX tables |
| `result-analysis` | You need paper-ready interpretation | supported claims, limitations, safe wording |
| `paper-writer` | You need draft/revision/polish | manuscript sections, compressed text, venue-aware writing |
| `paper-reviewer` | You need reviewer-style criticism | reviewer panel, AC view, repair roadmap |
| `integrity-audit` | You need evidence consistency checks | claim/citation/result/source audit |
| `submission-check` | You are near submission | venue rule checklist and readiness report |
| `rebuttal` | You have reviewer comments | issue taxonomy, revision ledger, rebuttal skeleton |

## Required behavior after each stage

Every stage should end with a compact menu:

```text
Next-step options:
A. [Recommended] ...
B. ...
C. ...

Suggested next command: "Continue with A."
```

You can continue by replying `A`, `B`, `next`, `repair`, or a mode name.

## Source accuracy rule

Any external information must pass three checks before it is used as evidence:

1. Existence check.
2. Metadata check.
3. Support check.

Use `assets/source_verification_log_template.md` for logging and `scripts/check_source_verification_log.py` for structural validation.

## Script dependencies

Most scripts use only the Python standard library. See `scripts/requirements.txt`.

## Safety and provenance

Do not use this skill to fabricate citations, results, experiments, reviewer comments, or provenance. The workflow is designed to make uncertainty visible, not to hide it.
