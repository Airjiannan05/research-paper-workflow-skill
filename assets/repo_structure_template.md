# Suggested Repo Structure

```text
project/
├── README.md
├── pyproject.toml or requirements.txt
├── configs/
│   ├── default.yaml
│   ├── datasets/
│   ├── methods/
│   ├── baselines/
│   └── ablations/
├── src/
│   ├── data/
│   ├── methods/
│   ├── baselines/
│   ├── evaluation/
│   ├── analysis/
│   └── utils/
├── scripts/
│   ├── run_experiment.py
│   ├── run_matrix.py
│   ├── aggregate_results.py
│   └── make_tables.py
├── results/
│   ├── raw/
│   ├── processed/
│   ├── tables/
│   └── figures/
├── logs/
├── notebooks/
└── paper/
```
