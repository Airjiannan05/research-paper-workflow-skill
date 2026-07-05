---
name: research-paper-workflow
description: "End-to-end research paper workflow skill family for CS, AI, AI4Science papers. 16 governed skills from idea to submission. Use when the user wants to develop a paper: project scaffolding, idea optimization, idea review, literature monitoring/search, paper cards, related-work matrix, claim design, experiment design, experiment implementation, result engineering, result analysis, manuscript drafting or polishing, venue-aware writing, simulated peer review, claim/citation/result integrity audit, submission check, rebuttal, and resubmission. For top-conference or CCF-A/AAAI/NeurIPS/ICLR/CVPR/ACL/GECCO-style work."
---

# Research Paper Workflow

A 16-skill family for shaping the research storyline of CS/AI papers. Each skill is an independent module — only the matching skill loads, keeping context lean and triggers precise.

## Architecture

This is a **multi-skill family**. The root `SKILL.md` is an index. Individual skills live in `rpw-*/` directories, each with its own `SKILL.md`, description, and trigger phrases. Shared governance lives in `rpw-common/`.

```
research-paper-workflow/
├── SKILL.md                    ← this index
├── rpw-common/                 ← shared governance
├── rpw-pipeline/               ← project scaffold + stage plan
├── rpw-idea-optimize/          ← idea → falsifiable research story
├── rpw-idea-review/            ← strict novelty/feasibility scoring
├── rpw-literature-monitor/     ← competitor/scoop tracking
├── rpw-literature-search/      ← systematic related-work search
├── rpw-claim-manifest/         ← claim → evidence mapping
├── rpw-experiment-design/      ← baselines, metrics, ablations
├── rpw-experiment-implementation/ ← code, configs, run matrix
├── rpw-result-engineering/     ← log validation, aggregation, tables
├── rpw-result-analysis/        ← interpret results → claims
├── rpw-paper-writer/           ← draft, polish, compress
├── rpw-paper-reviewer/         ← simulated reviewer panel + AC
├── rpw-integrity-audit/        ← claim/citation/number consistency
├── rpw-submission-check/       ← venue compliance
├── rpw-rebuttal/               ← reviewer response + revision ledger
├── references/                 ← shared reference files
├── assets/                     ← shared templates
└── scripts/                    ← shared utility scripts
```

## Entry Point Table

The agent loads only the matching `rpw-*` skill:

| User intent | Load |
|---|---|
| Vague idea, weak topic, direction rescue | `rpw-idea-optimize` |
| Compare/rank ideas, novelty risk, go/no-go | `rpw-idea-review` |
| Recent competitor, scoop, arXiv/OpenReview tracking | `rpw-literature-monitor` |
| Related work, datasets, benchmarks, prior art | `rpw-literature-search` |
| Map claims to evidence | `rpw-claim-manifest` |
| Design experiments, baselines, metrics, ablations | `rpw-experiment-design` |
| Turn experiment plan into code/config/run matrix | `rpw-experiment-implementation` |
| Validate logs, aggregate seeds, generate tables | `rpw-result-engineering` |
| Interpret results into claims and limitations | `rpw-result-analysis` |
| Draft, revise, polish, compress paper text | `rpw-paper-writer` |
| Simulate reviewer panel and AC/meta-review | `rpw-paper-reviewer` |
| Check claim/citation/result/number consistency | `rpw-integrity-audit` |
| Verify venue rules, anonymity, PDF metadata | `rpw-submission-check` |
| Respond to reviewers, revision ledger | `rpw-rebuttal` |
| Full project breakdown into stages | `rpw-pipeline` |

## First Action

When the user asks to use this workflow, identify the entry point above and load only that skill's `SKILL.md`. If the request is ambiguous, load `rpw-common/SKILL.md` and consult `references/routing-and-artifacts.md`.

## Operating Rules

1. Load only the `rpw-*` skill that matches the user's primary intent.
2. Every skill ends with a next-step menu from `references/next-step-menu.md`.
3. All externally queried facts must pass the triple-check protocol in `references/source-verification.md`.
4. Do not fabricate papers, citations, repositories, venue rules, datasets, benchmark results, experiment logs, or provenance.
5. The user owns research decisions, authorship, final claims, experiment truth, and submission choices.
