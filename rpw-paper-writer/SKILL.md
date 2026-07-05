---
name: rpw-paper-writer
description: "Draft, revise, polish, and compress paper text in LaTeX or Markdown. Produce submission-shaped manuscripts: title, abstract, introduction, related work, method, experiments, analysis, limitations, conclusion. Use for paper writing, polishing, compression, 写论文, 润色, 压缩, 改写, 起草. Do not review or judge the paper — that's rpw-paper-reviewer."
---

# RPW Paper Writer

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill writes and revises; it does not review, audit, or check submission rules. Route review to `rpw-paper-reviewer`, audit to `rpw-integrity-audit`, submission check to `rpw-submission-check`.

## Core Rule

Preserve the user's requested format (LaTeX stays LaTeX, Markdown stays Markdown). Never invent results, citations, or provenance. Mark missing evidence with `[CITE]`, `[VERIFY]`, `[RESULT]`, `[FIGURE]`, `TBD`, or `needs evidence`. A full-paper request must yield a submission-shaped artifact, not an outline.

## Workflow

1. Identify the target venue, input artifacts (idea brief, claim manifest, experiment plan, result analysis), and the user's desired output (full draft, single section, polish, compress).
2. If a target venue is named, apply a venue-aware section budget. Use `../references/venue-writing.md`.
3. Draft section by section with visible evidence placeholders. Use `../references/section-modules.md` for section-specific guidance.
4. Follow the storyline blueprint from `../references/storyline-blueprint.md`: the introduction must expose the key insight and claim-to-evidence path.
5. For underfilled drafts: expand with mechanism detail, experiment setup, analysis scaffolds, limitations, and explicit evidence placeholders. Do not pad.
6. For polishing/compression: return the revised text first; add notes only for meaning changes, unsupported claims, or risky edits.
7. Ensure every factual claim has a visible evidence anchor or placeholder.

## Output Contract

A complete submission-shaped manuscript includes:
- Title
- Abstract
- Introduction (with key insight and contribution summary)
- Related Work / Background
- Method
- Experimental Setup
- Results
- Analysis / Ablation
- Limitations
- Conclusion
- References (placeholders with `[CITE]` or `[VERIFY]`)
- Appendix / Checklist placeholders

## Handoff

End with a next-step menu. Recommended: `rpw-paper-reviewer` for acceptance-risk diagnosis, or `rpw-integrity-audit` if claims/citations are dense.

## Reference Files

- `../references/writing-guide.md`: Writing standards and conventions.
- `../references/storyline-blueprint.md`: Storyline structure.
- `../references/venue-writing.md`: Venue-specific formatting.
- `../references/section-modules.md`: Section-by-section guidance.
- `../references/next-step-menu.md`: For menu contract.
