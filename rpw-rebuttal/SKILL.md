---
name: rpw-rebuttal
description: "Convert reviewer comments into an issue taxonomy, point-by-point response, revision ledger, and resubmission plan. Use for rebuttal writing, reviewer response, revision planning, 审稿回复, rebuttal写作, revision ledger, 重投计划. Do not write the revised paper directly — that's rpw-paper-writer."
---

# RPW Rebuttal Writer

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill plans and drafts responses; it does not execute manuscript revisions. Route actual text changes to `rpw-paper-writer`. Never invent new results; mark promised experiments as planned unless already supplied.

## Core Rule

Every promised change must map to evidence, manuscript edit, experiment, citation, or explicit limitation. Do not promise experiments that were not completed. The revision ledger tracks every reviewer concern to a concrete action with status (done / planned / pending / cannot-do).

## Workflow

1. Load reviewer comments, the manuscript, and any supporting artifacts.
2. Build an issue taxonomy: group reviewer concerns by type (novelty, soundness, evidence, presentation, missing baselines, etc.).
3. For each concern, determine:
   - **Response stance**: accept and fix / clarify without change / respectfully disagree with evidence.
   - **Required action**: manuscript edit, new experiment, citation addition, clarification, limitation statement.
   - **Owner skill**: which skill should execute the fix.
   - **Status**: done / planned / pending / cannot-do.
4. Draft point-by-point responses. Be respectful, specific, and evidence-grounded.
5. Build the revision ledger using `../assets/revision_ledger_template.md`.
6. Create a resubmission plan: what must be completed before resubmission, in what order.
7. If the user needs manuscript changes, hand off specific edit instructions to `rpw-paper-writer`.

## Output Contract

```text
Issue taxonomy:
| Type | Count | Example concerns |
|---|---|---|
...

Point-by-point response:
Reviewer A, Concern 1: <summary>
  Response: <text>
  Action: <description> → owner: <skill> → status: <done/planned/pending/cannot-do>
...

Revision ledger: revision_ledger.md
Resubmission plan:
  Before resubmission:
    1. <action> (owner: <skill>)
    2. ...
  At resubmission:
    - Updated manuscript
    - Response letter
    - Revision ledger
    - Any new experiments or citations
```

## Handoff

End with a next-step menu. Planned manuscript edits route to `rpw-paper-writer`. Planned experiments route to `rpw-experiment-design` or `rpw-experiment-implementation`.

## Reference Files

- `../references/rebuttal-revision.md`: Rebuttal strategy and workflow.
- `../assets/revision_ledger_template.md`: Ledger template.
- `../scripts/build_revision_ledger.py`: Build ledger from CSV/JSON.
- `../references/next-step-menu.md`: For menu contract.
