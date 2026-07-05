# Reproducibility Passport

Use this reference to document whether a result can be reproduced by the authors, reviewers, or future users.

## Passport sections

1. Code
   - repository URL or local path
   - commit hash or snapshot ID
   - license
   - uncommitted changes noted

2. Environment
   - OS
   - Python/conda version
   - package lock file
   - CUDA/ROCm/CPU details when relevant
   - hardware summary

3. Data
   - dataset name
   - version or download date
   - source URL or local provenance
   - preprocessing
   - split definition
   - access restrictions and license

4. Experiments
   - run matrix path
   - configs path
   - seeds
   - commands
   - expected runtime and compute

5. Results
   - raw logs path
   - aggregated results path
   - table/figure generation command
   - failed/excluded runs

6. Claims
   - claim IDs supported by each table/figure
   - unsupported or weak claims
   - limitations

7. Release readiness
   - can the environment be recreated?
   - can the main table be regenerated?
   - can baselines be rerun?
   - are any private data/code restrictions documented?

## Output style

Use a table with `item`, `status`, `evidence`, `risk`, and `fix` columns. Status values:

- `ready`
- `partial`
- `missing`
- `not applicable`
- `blocked`
