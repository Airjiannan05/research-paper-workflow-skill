# Storyline Blueprint

Use this schema to keep the research story coherent across idea, experiments, writing, review, and rebuttal.

## Core chain

1. **Task / setting**: What problem family is the paper about? What are the inputs, outputs, assumptions, and constraints?
2. **Current practice**: What do strong existing methods do?
3. **Gap**: What failure, blind spot, inefficiency, or missing abstraction remains?
4. **Root challenge**: Why is the gap non-trivial? What makes naive fixes fail?
5. **Key insight**: What conceptual move makes progress possible?
6. **Mechanism**: What concrete method/system/algorithm realizes the insight?
7. **Claims**: What exactly should be true if the mechanism works?
8. **Evidence**: Which experiment, proof, analysis, or citation supports each claim?
9. **Boundary**: Where does it fail or not apply?
10. **Reviewer value**: Why should the target community care now?

## Top-conference novelty filter

A claim is weak if it is only:

- a new application of an existing agent/model/tool;
- an engineering combination without a new abstraction;
- a benchmark improvement without explanation;
- a longer prompt/workflow without falsifiable behavior;
- a literature summary without a decision rule.

A stronger contribution usually has at least one of:

- a new measurable diagnostic, objective, or representation;
- a surprising empirical regularity with controlled evidence;
- a principled algorithmic mechanism;
- a benchmark/protocol that changes how future work is evaluated;
- a negative result that invalidates a common assumption;
- a unifying taxonomy that predicts method behavior.

## Output template

```text
Working title:
Target venue/community:
Task/setting:
Current practice:
Gap:
Root challenge:
Key insight:
Mechanism:
Main claims:
Required evidence:
Closest novelty threats:
Limitations:
Minimum viable paper:
Top-conference risk:
Next artifact:
```
