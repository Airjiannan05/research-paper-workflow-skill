---
name: rpw-submission-check
description: "Verify venue-specific submission compliance: page limits, anonymization, PDF metadata, template, references, appendix, artifact package, reproducibility checklist, ethics, and AI disclosure. Use for submission check, venue compliance, 投稿检查, 格式检查, 匿名检查, camera-ready. Do not polish content — that's rpw-paper-writer."
---

# RPW Submission Checker

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill checks compliance; it does not modify manuscript content. Route content changes to `rpw-paper-writer`. Current venue rules must be verified against official sources — use web search and triple-check before final advice.

## Core Rule

The user must manually verify factual, experimental, authorship, and policy compliance. This skill provides a structured checklist; it does not make submission decisions.

## Workflow

1. Identify the target venue, year, track, and any special requirements.
2. Search for current venue rules (page limits, template version, anonymization policy, supplementary material rules, AI disclosure requirements).
3. Check each item against `../assets/submission_checklist_template.md`:
   - **Page budget**: Within limits? Overfull/underfull?
   - **Anonymity**: Author names removed? Acknowledgments blinded? No self-identifying references?
   - **PDF metadata**: Author field cleared? No tracking IDs?
   - **Template compliance**: Correct template? Correct font/size/margins?
   - **References**: All cited? No broken references?
   - **Appendix**: Within page budget if counted?
   - **Artifact package**: Code, data, models ready?
   - **Reproducibility checklist**: Completed?
   - **Ethics statement**: Included if required?
   - **AI disclosure**: Included if required by venue?
4. Use web search for current venue rules before final advice. Triple-check with official venue pages.
5. Produce `submission_checklist.md` with pass/fail/fix-needed status for each item.

## Output Contract

```text
Venue: <name> <year> <track>
Page check: <current> / <limit> — pass / over by N / under by N
| Item | Status | Detail | Fix |
|---|---|---|---|
| Page limit | pass/fail | ... | ... |
| Anonymity | pass/fail | ... | ... |
| PDF metadata | pass/fail | ... | ... |
| Template | pass/fail | ... | ... |
| References | pass/fail | ... | ... |
| Appendix | pass/fail | ... | ... |
| Artifact package | pass/fail | ... | ... |
| Reproducibility | pass/fail | ... | ... |
| Ethics | pass/fail | ... | ... |
| AI disclosure | pass/fail | ... | ... |
Overall readiness: ready / fix N items before submission
```

## Handoff

End with a next-step menu. If clean: final human verification. If issues: route to the relevant owner skill for each fix.

## Reference Files

- `../assets/submission_checklist_template.md`: Checklist template.
- `../references/source-verification.md`: Triple-check for venue rules.
- `../references/next-step-menu.md`: For menu contract.
