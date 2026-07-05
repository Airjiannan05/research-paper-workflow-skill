---
name: rpw-common
description: "Shared governance for the Research Paper Workflow skill family: routing, source verification, next-step menus, artifact contracts, and paper_state.yaml schema. Use only when maintaining skills or resolving routing conflicts; not for ordinary research tasks."
metadata:
  rpw_skill_controls:
    handoff_question_mode: partial
    shared_controls: ./
---

# RPW Common

## Core Rule

This is the shared control module. Do not use it for research tasks. Use it to keep routing, source verification, handoff behavior, and artifact ownership consistent across all `rpw-*` skills.

## Shared Controls

Load only the file needed:

- `../references/routing-and-artifacts.md`: Which skill owns which request and artifact.
- `../references/source-verification.md`: Triple-check protocol (existence, metadata, support).
- `../references/next-step-menu.md`: Menu contract, successor mapping, gate-failure behavior.
- `../references/workflow.md`: Full stage gates.
- `../assets/paper_state_template.yaml`: Shared `paper_state.yaml` schema.

## Routing Rules

When a user request is ambiguous between two skills, prefer the skill that:
1. Produces the earlier-stage artifact (don't skip gates).
2. Matches the user's explicit intent words ("design" → experiment-design, "write" → paper-writer).
3. Is listed in the trigger boundary table (see README §6).

## Handoff Modes

Every skill uses `handoff_question_mode: partial`:
- When the user's request goes beyond the skill's scope, offer a next-step menu with the correct owner skill as `[Recommended]`.
- Do not silently hand off; always show the user where they're being routed and why.

## Output Contract

When auditing or updating this skill family, report:

```text
Routing impact:
Handoff mode impact:
Source-verification changes:
Artifact-contract changes:
Validation result:
```
