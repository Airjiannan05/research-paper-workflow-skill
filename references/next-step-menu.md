# Next-Step Menu Contract

Use this file whenever a mode finishes an artifact or a stage gate. The skill must make the next action explicit so the user can continue without remembering the whole workflow.

## Default rule

After every completed artifact, include a compact `Next-step options` block at the end of the response. Treat it as a required handoff unless the user explicitly asks for only the artifact, no extra text, or a one-shot final deliverable.

Do not ask an open-ended “what next?” question. Offer 3 to 6 concrete options with labels the user can copy, such as `A`, `B`, `C`, or mode names.

## Menu shape

Use this exact structure in normal chat responses:

```text
Next-step options:
A. [Recommended] <next mode> — <one-sentence purpose>. Best if: <condition>.
B. <alternative mode> — <one-sentence purpose>. Best if: <condition>.
C. <alternative mode> — <one-sentence purpose>. Best if: <condition>.
D. Pause / export — <save, package, or summarize the current artifact>.

Suggested next command: “Continue with A.”
```

Keep the block short. The artifact must remain the main output; the menu is navigation.

## Recommendation rule

Always mark exactly one option as `[Recommended]` unless the current artifact failed a gate. If the gate failed, mark one option as `[Repair first]` and make it the recommended path.

Prefer the natural workflow successor:

| Current mode | Recommended successor |
|---|---|
| `pipeline` | `idea-optimize` or the first missing artifact mode |
| `idea-optimize` | `idea-review` |
| `idea-review` with keep/modify | `literature-search` |
| `idea-review` with kill | `idea-optimize` |
| `literature-monitor` | `literature-search` or `idea-review` |
| `literature-search` | `related-work matrix` / `claim-manifest` |
| `related-work matrix` | `claim-manifest` |
| `claim-manifest` | `experiment-design` |
| `experiment-design` | `experiment-implementation` |
| `experiment-implementation` | `result-engineering` after runs exist; otherwise `execution checklist` |
| `result-engineering` | `result-analysis` |
| `result-analysis` | `paper-writer` if claims are supported; otherwise `experiment-design` or `experiment-implementation` repair |
| `paper-writer` | `paper-reviewer` |
| `paper-reviewer` | the repair owner for the strongest concern |
| `integrity-audit` | repair owner for high-risk unsupported claims; otherwise `submission-check` |
| `submission-check` | `final human verification` or `rebuttal` only after reviews exist |
| `rebuttal` | `revision-ledger update` or `resubmission check` |

## Gate-aware options

When a stage gate passes, offer the next stage plus useful alternates:

- continue forward;
- deepen the current artifact;
- repair a risk;
- export/update state.

When a stage gate fails, options must prioritize repair:

- repair the failed gate;
- gather missing evidence;
- narrow scope;
- pause/export with the risk clearly marked.

## Mode-specific menus

### After `idea-optimize`

Offer:

- `idea-review` to pressure-test novelty and feasibility;
- `literature-search` to check prior art if the idea is promising but unverified;
- `experiment-design` only if the claim is already clear;
- export/update `paper_state.yaml`.

### After `idea-review`

Offer:

- if keep/modify: `literature-search`;
- if fatal novelty/evidence risk: `idea-optimize` repair;
- `claim-manifest` only if claims are already explicit;
- export reviewer-style decision.

### After `literature-search` or matrix

Offer:

- `claim-manifest` to convert gaps into testable claims;
- deepen search for recent competitors/scoop risk;
- add paper cards or run matrix-building script if structured files are supplied;
- update `paper_state.yaml`.

### After `experiment-design`

Offer:

- `experiment-implementation` to create repo scaffold, config schema, run matrix, logging schema, commands, and acceptance tests;
- repair baseline/ablation weakness;
- cost/prioritization pass;
- export experiment plan.

### After `experiment-implementation`

Offer:

- execute runs outside ChatGPT and return logs for `result-engineering`;
- refine configs/run matrix;
- add baseline adapters or acceptance tests;
- export implementation package.

### After `result-engineering`

Offer:

- `result-analysis` if required runs are complete;
- repair missing/failed runs;
- generate LaTeX/Markdown tables;
- update reproducibility passport.

### After `paper-writer`

Offer:

- `paper-reviewer` for acceptance-risk diagnosis;
- `integrity-audit` if claims/results/citations are dense;
- revise a specific section;
- export draft.

### After `paper-reviewer`

Offer options based on the strongest concern. Examples:

- `literature-search` if novelty/prior art is weak;
- `experiment-design` if baselines/ablations are weak;
- `paper-writer` if narrative clarity is weak;
- `integrity-audit` if evidence support is questionable.

### After `integrity-audit`

Offer:

- repair unsupported claims;
- verify citations/recent venue rules with web search;
- `submission-check` if no high-risk issues remain;
- export audit report.

## State update

When using `paper_state.yaml`, update `project.stage`, the produced artifact field, and the recommended next mode. If no file is being produced, show a compact state delta:

```yaml
state_delta:
  completed_artifact: experiment_plan.md
  current_stage: experiment-design
  recommended_next_mode: experiment-implementation
  blocking_risks:
    - missing official baseline implementation
```

## User command shortcuts

Accept short user replies as commands:

- `A`, `B`, `C`, `D`;
- `继续 A`;
- `next` means choose the recommended option;
- `repair` means choose the repair option;
- a mode name such as `experiment-implementation`.

If the user selects an option, execute it directly. Do not re-explain the whole menu.
