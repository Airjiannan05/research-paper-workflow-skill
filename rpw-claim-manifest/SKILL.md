---
name: rpw-claim-manifest
description: "Map every major paper claim to its required evidence: citation, result, proof, or design rationale. Produce a claim manifest with type, support, strength, risk, and falsifier. Use for claim design, evidence planning, claim表, 声明与证据映射. Do not design experiments — that's rpw-experiment-design."
metadata:
  rpw_skill_controls:
    handoff_question_mode: partial
    shared_controls: ../rpw-common/
---

# RPW Claim Manifest

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill maps claims to evidence needs; it does not design the experiments themselves. Route experiment design to `rpw-experiment-design`.

## Core Rule

Every major contribution claim must have a planned evidence path. Claims without evidence are marked `TBD` or `needs evidence`. Use `../assets/claim_manifest_template.md` for structure.

## Workflow

1. Extract all claims from the idea brief, related-work matrix, and user input.
2. Classify each claim: conceptual, empirical, theoretical, systems, benchmark, or negative.
3. For each claim, specify:
   - Required support: citation, experimental result, proof, design rationale, or qualitative analysis.
   - Source: which citation, experiment, or proof will provide the support.
   - Strength: strong / moderate / weak / hypothesis.
   - Risk: what would falsify this claim.
   - Status: planned / in-progress / supported / needs-evidence / at-risk.
4. Validate with `../scripts/check_claim_manifest.py` if a manifest file exists.
5. Identify claims with no evidence path and mark them explicitly.

## Output Contract

```text
Claim manifest:
| Claim | Type | Required support | Source | Strength | Risk | Falsifier | Status |
|---|---|---|---|---|---|---|---|
...
Unsupported claims:
Claims needing stronger evidence:
```

## Handoff

End with a next-step menu. Recommended: `rpw-experiment-design` if claims are empirical.

## Reference Files

- `../assets/claim_manifest_template.md`: Manifest structure.
- `../scripts/check_claim_manifest.py`: Structural validation.
