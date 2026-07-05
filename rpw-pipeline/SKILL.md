---
name: rpw-pipeline
description: "Initialize a paper project, break it into stages with gates, create paper_state.yaml, and decide the next owner skill. Use for project scaffolding, full-project planning, 初始化论文项目, 项目规划, 拆阶段. Do not generate research content or write the manuscript."
---

# RPW Pipeline

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. Load `../references/routing-and-artifacts.md` for artifact ownership.

## Core Rule

Create a stage plan with clear gates, artifact handoffs, and next owner. Do not invent research content — the user owns all research decisions.

## Workflow

1. Ask for target venue, paper type, and current stage (or infer from what the user provides).
2. Create or update `paper_state.yaml` using `../assets/paper_state_template.yaml`.
3. Break the project into stages using the stage map in `../references/workflow.md`.
4. For each stage: name the owner skill, input artifact, output artifact, and gate criteria.
5. Identify the nearest missing artifact and recommend the next owner skill.

## Output Contract

```text
Project: <title>
Target venue: <venue>
Current stage: <stage>
Next owner skill: <skill>
Stage plan:
  0. project scaffold → paper_state.yaml [done]
  1. idea-optimize → idea_brief.md [recommended]
  ...
Blocking risks: <list>
```

## Handoff

End with a next-step menu per `../references/next-step-menu.md`. The recommended option must be the first missing artifact's owner skill.
