# Citation and Integrity Audit

Use this for claim-support, citation, numeric, and provenance checks. It is not a broad literature search mode.

## Audit modes

- `claim-audit`: each important claim has support.
- `numeric-audit`: numbers, units, deltas, metric directions, seeds, confidence intervals, and table/figure/text agreement.
- `citation-audit`: citation metadata and citation-context support.
- `full`: all checks.

## Claim status labels

| Label | Meaning |
|---|---|
| supported | direct evidence supports the claim |
| partially supported | evidence supports a narrower version |
| unsupported | no supplied citation/result/proof supports it |
| overstated | wording exceeds evidence strength |
| contradicted | supplied evidence conflicts with claim |
| unclear | claim or evidence is ambiguous |

## Citation-context check

For each citation:

1. Identify the exact sentence or clause the citation supports.
2. Verify the cited work exists and metadata is plausible.
3. Check whether the cited work directly supports the sentence.
4. Separate metadata problems from support problems.
5. Suggest safe wording: narrow, hedge, split claim, add missing evidence, or remove citation.

## Numeric consistency check

Check abstract, introduction, results section, tables, figures, captions, conclusion, appendix, and response letters for:

- inconsistent values;
- wrong metric direction;
- missing units;
- incompatible denominators;
- rounded deltas that change interpretation;
- claiming significance without test details;
- averages without variance when variance matters.

## Output contract

```text
Mode:
Artifacts checked:
Claim-evidence matrix:
Numeric consistency findings:
Citation metadata findings:
Citation-context findings:
Severity ranking:
Safe edit suggestions:
Unverified items:
No-invention status:
Next mode:
```


## Required source verification layer

For every citation or external factual claim that is load-bearing, apply `source-verification.md` before marking it safe. A citation is safe only when:

1. the cited work exists;
2. its metadata matches the manuscript reference;
3. the cited passage supports the exact sentence or claim.

Add a `verification_status` field to audit tables with one of: `verified`, `partial`, `unverified`, or `conflict`. Never upgrade `partial` or `unverified` sources by rewriting the claim into a stronger statement. Either weaken the wording, add a stronger source, or mark `[VERIFY]`.
