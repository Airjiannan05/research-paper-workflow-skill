# Manuscript Writing Guide

Use this file when drafting, revising, polishing, compressing, or translating paper text.

## Core writing rule

Write for argument structure first, prose second. A polished sentence that hides a weak claim is worse than a plain sentence with clear evidence boundaries.

## Format preservation

- Preserve LaTeX commands, citation keys, labels, equations, figure/table environments, Markdown headings, lists, and table shapes whenever possible.
- For line edits, polishing, or compression, return the revised text first in the same format.
- Add notes only when meaning changed, evidence is missing, or a claim became weaker/stronger.
- Do not turn a user-requested paragraph edit into a full review unless asked.

## From-scratch paper drafting

For a full-paper request, produce a submission-shaped artifact, not only an outline:

1. Title.
2. Abstract.
3. Introduction.
4. Background / Related Work / Preliminaries as appropriate.
5. Method / System / Algorithm.
6. Experiments / Evaluation.
7. Analysis / Ablation / Failure cases.
8. Limitations / Ethics / Reproducibility when relevant.
9. Conclusion.
10. References placeholders and appendix/checklist placeholders.

If the input is short, expand with mechanism detail, experiment setup, analysis scaffolds, limitations, and visible placeholders. Do not invent results or citations.

## Abstract moves

1. Problem and stakes.
2. Missing capability or gap.
3. Proposed idea or mechanism.
4. Evidence type or concrete result if supplied.
5. Implication and scope.

Do not include unsupported numeric claims.

## Introduction moves

1. Field context in one paragraph.
2. Concrete problem and why it is hard.
3. Limitation of existing method families.
4. Key insight in plain language.
5. Method overview.
6. Evidence summary.
7. Contributions as falsifiable bullets.

Good contribution bullets contain mechanism + evidence, not just system names.

## Related Work

Organize by method family and gap. End each subsection with the relation to this work. Avoid chronological listing.

## Method

Include problem definition, assumptions, overview figure description, algorithm/procedure, design rationale, complexity/cost if relevant, and implementation details needed for reproduction.

## Experiments

Use claim-driven order:

1. Claim-to-test map.
2. Experimental setup.
3. Main result.
4. Ablation.
5. Robustness/sensitivity.
6. Qualitative/failure analysis.
7. Cost/reproducibility.

## Style rules

- Prefer concrete nouns and verbs.
- Avoid hype: revolutionary, unprecedented, universal, solves, guarantees.
- Replace vague claims with scoped claims.
- Keep placeholders visible: `[CITE]`, `[VERIFY]`, `[RESULT]`, `[FIGURE]`, `[ETHICS]`.
- Avoid generic filler such as "with the rapid development of" unless it carries a specific argument.
- Make paragraph topic sentences carry claims; make final sentences explain consequence or transition.

## Compression rules

When compressing:

- preserve claims, numbers, citations, equations, and limitations;
- remove duplicated motivation first;
- merge background that does not affect the argument;
- shorten method prose only after preserving definitions and algorithmic steps;
- never cut caveats that prevent overclaiming unless the user explicitly accepts the risk.

## Writing self-check

Before calling a section ready, check:

- Does each paragraph have a role?
- Is the key insight visible?
- Are claims scoped to evidence?
- Are citations needed and marked?
- Is the reviewer likely to understand what is new?
- Are limitations honest but not self-destructive?
