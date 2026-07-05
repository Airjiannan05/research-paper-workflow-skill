# Artifact Flow

```text
idea_brief.md
  -> literature_search_plan.md
  -> paper_cards.md
  -> related_work_matrix.md
  -> claim_manifest.md
  -> experiment_plan.md
  -> implementation_plan.md
  -> run_matrix.csv
  -> results/raw/runs.csv
  -> results/processed/aggregated_results.csv
  -> results_analysis.md
  -> paper/main.tex or paper_draft.md
  -> integrity_report.md
  -> review_report.md
  -> submission_checklist.md
  -> revision_ledger.md
```

Each transition should preserve provenance. Do not move from one artifact to the next if the previous gate failed without clearly marking the failure and offering a repair route.
