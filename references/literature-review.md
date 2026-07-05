# Literature Review Protocol

Use this file for literature monitoring, literature search, paper cards, related-work matrices, and evidence synthesis.

## Two different tasks

- **Literature search** finds prior work, benchmarks, datasets, baselines, and gaps.
- **Citation integrity audit** verifies whether already-cited papers support specific manuscript claims.

Do not confuse them. A paper can be relevant prior work but still not support a specific sentence.

## Search strategy

Build a search plan with:

- seed papers and authors;
- keywords and synonyms;
- task names, benchmark names, and dataset names;
- method-family keywords;
- exclusion terms;
- target venues and years;
- backward citation expansion;
- forward citation expansion;
- recent arXiv/OpenReview/venue monitoring;
- negative or contradictory evidence queries;
- implementation/code availability search.

When novelty matters, search for both direct matches and adjacent formulations that could scoop the contribution under different terminology.

## Paper card schema

For each important paper, extract:

```text
Citation:
Problem setting:
Assumptions:
Input/output/data:
Core mechanism:
Representation/objective:
Benchmarks/metrics:
Strongest evidence:
Limitations/failure modes:
What it does NOT show:
Relation to this project:
Novelty threat: low | medium | high
Useful citation role:
```

## Related-work matrix columns

Use a mechanism-based matrix:

| Work | Setting | Input | Representation | Mechanism | Evidence | Strength | Limitation | Relation | Threat |
|---|---|---|---|---|---|---|---|---|---|

## Gap synthesis

A good gap statement has four parts:

1. Existing families do X.
2. They fail or under-specify Y.
3. Y matters because Z.
4. The proposed insight addresses Y by mechanism M.

Avoid gaps that only say "few works apply method X to domain Y" unless the domain exposes a genuinely new technical constraint.

## Related Work writing

Organize by families, not chronology. For each family:

- define what the family optimizes or assumes;
- name representative works;
- state the family-level limitation;
- explain how the current paper differs;
- avoid strawman claims.

## Output contracts

### Search plan

```text
Research question:
Seed papers:
Search strings:
Venues/sources:
Inclusion criteria:
Exclusion criteria:
Backward/forward expansion:
Benchmark/baseline search:
Novelty-threat search:
Expected outputs:
```

### Literature synthesis

```text
Paper pool:
Taxonomy:
Related-work matrix:
Closest competitors:
Novelty threats:
Open gap:
Citation candidates:
Missing searches:
Next mode:
```


## Source verification in literature work

Before using a paper, benchmark, dataset, code repository, or leaderboard as a load-bearing source, apply the triple-check protocol in `source-verification.md`:

- confirm existence from a primary or reliable index;
- confirm metadata such as title, authors, year, venue, DOI/arXiv/OpenReview/repository;
- confirm the source actually supports the relationship claimed in the matrix, such as baseline relevance, limitation, novelty threat, or benchmark status.

For large searches, keep discovery separate from verification. Use `candidate` for search hits, `screened` for read abstracts, and `verified` only after all three checks pass.
