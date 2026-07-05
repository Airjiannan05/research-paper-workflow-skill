---
name: rpw-integrity-audit
description: "Audit a manuscript for claim-support alignment, citation-context accuracy, numeric consistency, figure/table/text cross-check, and source verification status. Use for integrity audit, citation check, fact verification, 完整性审计, 引用检查, 数字核对, claim验证. Do not do broad literature search — that's rpw-literature-search."
---

# RPW Integrity Auditor

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill verifies what is already in the manuscript; it does not search for new sources. Route broad literature search to `rpw-literature-search`.

## Core Rule

Audit strictly. Mark unsupported or only partially verified items instead of fixing them by invention. Every load-bearing external fact must pass the triple-check protocol: existence, metadata, and support. High-risk unsupported claims must be fixed before submission.

## Workflow

1. Load the manuscript, claim manifest, experiment results, and source verification log.
2. **Claim-support audit**: For every major claim, verify it is supported by a result, citation, proof, or design rationale. Flag overclaiming.
3. **Citation audit**: For every citation, verify existence, metadata (title/authors/date/venue), and context support (does the cited passage actually support the sentence?). Use `../references/citation-integrity.md`.
4. **Numeric audit**: Cross-check all numbers across text, tables, and figures. Flag inconsistencies.
5. **Figure/table audit**: Verify every table/figure is referenced in text, every value is sourced.
6. **Source verification audit**: Check that all load-bearing external facts have completed triple-check verification. Use `../scripts/check_source_verification_log.py`.
7. **Reproducibility audit**: Check that baselines are documented, code/environment are captured, seeds are recorded.
8. Produce `integrity_report.md` with all findings, severities, and required fixes.

## Output Contract

```text
Claim-support status:
| Claim | Support | Issue |
|---|---|---|
...
Citation issues:
| Citation | Problem | Fix |
|---|---|---|
...
Numeric inconsistencies:
| Location | Value A | Value B | Resolution |
|---|---|---|---|
...
Source verification gaps:
| Fact | Verdict | Needed |
|---|---|---|
...
Reproducibility gaps:
Required fixes (ranked by severity):
```

## Handoff

End with a next-step menu. If high-risk issues remain: `[Repair first]`. If clean: `rpw-submission-check`.

## Reference Files

- `../references/citation-integrity.md`: Citation audit protocol.
- `../references/source-verification.md`: Triple-check protocol.
- `../scripts/check_source_verification_log.py`: Log validation.
- `../assets/source_verification_log_template.md`: Log template.
- `../references/next-step-menu.md`: For menu contract.
