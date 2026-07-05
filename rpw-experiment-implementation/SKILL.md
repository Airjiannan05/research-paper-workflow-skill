---
name: rpw-experiment-implementation
description: "Turn an experiment plan into a runnable research-engineering package: repo layout, config schema, run matrix, command templates, logging schema, baseline checklist, and reproducibility passport. Use for experiment implementation, code scaffold, run matrix generation, 实验实现, 代码工程, 生成run matrix. Do not design experiments — that's rpw-experiment-design."
metadata:
  rpw_skill_controls:
    handoff_question_mode: partial
    shared_controls: ../rpw-common/
---

# RPW Experiment Implementation

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill implements experiment infrastructure; it does not design what to test. Route design back to `rpw-experiment-design`. Do not implement paper-specific algorithm code unless the user explicitly asks; specify interfaces, files, and acceptance tests instead.

## Core Rule

Convert scientific intent into a runnable, traceable, reproducible research-engineering package. Every experiment axis (dataset, baseline, ablation, seed) must have a concrete run entry with a unique `run_id`, config path, command, and expected output path.

## Workflow

1. Load the experiment plan, claim manifest, and idea brief.
2. Design repository layout and module boundaries. Use `../assets/repo_structure_template.md`.
3. Create config schema. Use `../assets/config_schema_template.yaml`.
4. Generate run matrix: expand all experiment axes (claims × families × datasets × methods × baselines × ablations × seeds) into individual runs. Use `../scripts/generate_run_matrix.py` or `../assets/run_matrix_template.csv`.
5. Write command templates per experiment family.
6. Design tracking and logging schema. Use `../assets/logging_schema_template.json`.
7. Create baseline implementation checklist. Use `../assets/baseline_checklist_template.md`.
8. Capture environment and complete reproducibility passport. Use `../assets/reproducibility_passport_template.md` and `../references/reproducibility-passport.md`.
9. Define acceptance tests for the experiment harness.

## Output Contract

```text
Repository layout:
Config schema:
Run matrix: run_matrix.csv (N runs)
Command templates:
Logging schema:
Baseline checklist:
Reproducibility passport:
Acceptance tests:
```

## Handoff

End with a next-step menu. Recommended: execute runs, then return logs to `rpw-result-engineering`.

## Reference Files

- `../references/experiment-implementation.md`: Full protocol.
- `../references/research-engineering.md`: Engineering practices.
- `../references/result-logging.md`: Logging schema.
- `../references/reproducibility-passport.md`: Passport requirements.
- `../scripts/generate_run_matrix.py`: Run matrix generation.
- `../assets/`: All templates listed above.
