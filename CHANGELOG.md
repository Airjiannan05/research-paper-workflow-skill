# Changelog

## v1.0.0 - 2026-07-05

### Added
- **Plugin manifests**: `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` for one-click install via `/plugin install`.
- **AGENT_GUIDE.md**: Dedicated AI agent routing guide with mode routing table, artifact ownership, gate behavior, source verification, and shortcut commands.
- **CHANGELOG.md**: Version history tracking.
- **LICENSE**: MIT license.
- **.gitignore**: Prevent accidental commits of Python cache, OS junk, editor configs, environment secrets, and user-generated paper artifacts.
- **README.md**: GitHub entry point (Chinese), with language switcher to English.
- **Installation section (§4)** in both READMEs: Claude Code (4 methods), ChatGPT Custom GPT, OpenAI Codex CLI, and Cursor/Windsurf/Gemini/Copilot path table.
- Multi-platform badges (Claude Code, ChatGPT, Cursor) on all READMEs.

### Fixed
- **workflow.md stage numbering**: Stages 7–14 now correctly aligned with SKILL.md. Added missing Stage 7 (Experiment implementation) and Stage 8 (Result engineering).
- **Stage name consistency**: workflow.md stages 4–5 aligned with SKILL.md ("Related-work matrix", "Claim and evidence design").
- **CLAUDE.md script example**: `aggregate_results.py` command now includes the required `--metrics` flag.
- **`idea_brief.md` naming**: All references unified from `research_brief.md` → `idea_brief.md`. Template renamed `assets/research_brief_template.md` → `assets/idea_brief_template.md`.
- **README directory trees**: Updated in both language versions to include all current files.

### Changed
- GitHub default README set to Chinese; English available as `README_en.md`.
- CLAUDE.md `research_brief.md` references updated to `idea_brief.md`.

---

## v0.1.0 - 2026-06 (initial)

### Initial release
- Complete 14-stage research paper workflow: project scaffold → idea optimize → idea review → literature search → related-work matrix → claim manifest → experiment design → experiment implementation → result engineering → result analysis → paper writing → peer review → integrity audit → submission check → rebuttal.
- Triple-check source verification protocol (`references/source-verification.md`).
- Next-step menu navigation system (`references/next-step-menu.md`).
- 9 Python utility scripts (standard library only).
- 17 reusable template assets.
- 16 reference files covering experiment design, writing, review, rebuttal, and more.
- Claude Code compatibility layer (`CLAUDE.md`, `README_claude_code.md`, examples).
- Bilingual README (Chinese and English).
