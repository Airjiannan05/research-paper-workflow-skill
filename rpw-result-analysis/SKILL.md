---
name: rpw-result-analysis
description: "Interpret verified experiment results into supported claims and limitations. Produce main result interpretation, ablation analysis, failure cases, and claim support status. Use for result analysis, claim interpretation, 结果分析, 解释实验结果, claim支持判断. Do not write the paper — that's rpw-paper-writer."
---

# RPW Result Analysis

## Invocation Controls

Load `../rpw-common/SKILL.md` for shared governance. This skill interprets results; it does not write manuscript prose. Route writing to `rpw-paper-writer`.

## Core Rule

Do not write stronger claims than the evidence supports. Every claim in the manuscript must be traceable to a specific result row, figure, or explicit limitation statement. Map every result back to the claim it was designed to test.

## Workflow

1. Load the claim manifest, experiment plan, aggregated results, and result audit.
2. For each claim, assess the evidence:
   - **Supported**: Results are statistically reliable and directionally correct.
   - **Partially supported**: Some metrics/seeds/datasets support, others don't.
   - **Not supported**: Results contradict or are inconclusive.
3. Interpret main results: what is the primary takeaway from each table/figure.
4. Interpret ablations: which components matter, which don't, and why.
5. Analyze failure cases: when does the method break, and what does that reveal.
6. Assess sensitivity: variance across seeds, datasets, hyperparameters.
7. Report cost/runtime trade-offs.
8. List required follow-up experiments for claims that are still weak.
9. Produce safe wording recommendations: what can be stated confidently, what needs hedging.

## Output Contract

```text
Claim support summary:
| Claim | Status | Supporting evidence | Weakness | Safe wording |
|---|---|---|---|---|
...
Main result interpretation:
Ablation interpretation:
Failure case analysis:
Sensitivity and variance:
Cost/runtime:
Follow-up experiments needed:
Limitations to disclose:
```

## Handoff

End with a next-step menu. Recommended: `rpw-paper-writer` if claims are supported; otherwise `rpw-experiment-design` or `rpw-experiment-implementation` for repair.

## Reference Files

- `../references/experiment-design.md`: Claim-to-evidence mapping.
- `../references/next-step-menu.md`: For menu contract.
