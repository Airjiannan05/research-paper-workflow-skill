#!/usr/bin/env python3
"""Generate a reproducible run matrix from a small JSON/YAML spec.

Input schema (JSON or simple YAML if PyYAML is installed):
{
  "claims": ["C1"],
  "families": ["main"],
  "datasets": ["dataset1"],
  "methods": ["ours"],
  "baselines": [""],
  "ablations": ["none"],
  "seeds": [0,1,2],
  "config_template": "configs/{family}/{dataset}_{method}_{ablation}_s{seed}.yaml",
  "command_template": "python scripts/run_experiment.py --config {config_path}",
  "priority": "P0"
}
"""
from __future__ import annotations
import argparse, csv, json, sys
from itertools import product
from pathlib import Path

FIELDS = ["run_id","claim_id","experiment_family","dataset","method","baseline","ablation","seed","config_path","command","expected_outputs","status","priority"]

def load_spec(path: Path):
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except Exception as exc:
            raise SystemExit("YAML input requires PyYAML. Use JSON or install pyyaml.") from exc
        return yaml.safe_load(text)
    return json.loads(text)

def as_list(spec, key, default):
    val = spec.get(key, default)
    if val is None:
        return default
    return val if isinstance(val, list) else [val]

def safe(s):
    return str(s).replace("/", "-").replace(" ", "_")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", help="JSON/YAML run matrix spec")
    ap.add_argument("--out", default="run_matrix.csv")
    args = ap.parse_args()
    spec = load_spec(Path(args.spec))
    claims = as_list(spec, "claims", ["C1"])
    families = as_list(spec, "families", ["main"])
    datasets = as_list(spec, "datasets", ["dataset1"])
    methods = as_list(spec, "methods", ["ours"])
    baselines = as_list(spec, "baselines", [""])
    ablations = as_list(spec, "ablations", ["none"])
    seeds = as_list(spec, "seeds", [0])
    cfg_tpl = spec.get("config_template", "configs/{family}/{dataset}_{method}_{ablation}_s{seed}.yaml")
    cmd_tpl = spec.get("command_template", "python scripts/run_experiment.py --config {config_path}")
    priority = spec.get("priority", "P0")
    rows=[]
    for claim, family, dataset, method, baseline, ablation, seed in product(claims, families, datasets, methods, baselines, ablations, seeds):
        config_path = cfg_tpl.format(claim=claim, family=family, dataset=dataset, method=method, baseline=baseline or "none", ablation=ablation, seed=seed)
        run_id = safe(f"{family}_{dataset}_{method}_{baseline or 'nobase'}_{ablation}_s{seed}")
        rows.append({
            "run_id": run_id,
            "claim_id": claim,
            "experiment_family": family,
            "dataset": dataset,
            "method": method,
            "baseline": baseline,
            "ablation": ablation,
            "seed": seed,
            "config_path": config_path,
            "command": cmd_tpl.format(config_path=config_path, run_id=run_id),
            "expected_outputs": f"results/raw/{run_id}.json",
            "status": "planned",
            "priority": priority,
        })
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader(); writer.writerows(rows)
    print(f"wrote {len(rows)} runs to {args.out}")

if __name__ == "__main__":
    main()
