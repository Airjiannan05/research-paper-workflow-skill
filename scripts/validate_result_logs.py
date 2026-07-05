#!/usr/bin/env python3
"""Validate CSV or JSONL experiment logs for provenance and metric fields."""
from __future__ import annotations
import argparse, csv, json, math, sys
from pathlib import Path

REQUIRED = ["run_id","claim_id","experiment_family","dataset","method","seed","config_path","status"]
PROVENANCE = ["git_commit","dataset_version"]

def read_rows(path: Path):
    if path.suffix.lower() == ".jsonl":
        rows=[]
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                obj=json.loads(line)
                if "metrics" in obj and isinstance(obj["metrics"], dict):
                    for k,v in obj["metrics"].items(): obj[k]=v
                rows.append(obj)
        return rows
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("logfile")
    ap.add_argument("--metrics", default="", help="comma-separated required metric columns")
    args=ap.parse_args()
    rows=read_rows(Path(args.logfile))
    errors=[]; warnings=[]; seen=set()
    metrics=[m.strip() for m in args.metrics.split(',') if m.strip()]
    for i,row in enumerate(rows, start=1):
        rid=row.get("run_id","")
        if rid in seen: errors.append(f"row {i}: duplicate run_id {rid}")
        seen.add(rid)
        for k in REQUIRED:
            if row.get(k) in (None, ""):
                errors.append(f"row {i}: missing required field {k}")
        for k in PROVENANCE:
            if row.get(k) in (None, ""):
                warnings.append(f"row {i}: missing provenance field {k}")
        if row.get("status") == "failed" and not row.get("failure_reason"):
            errors.append(f"row {i}: failed run without failure_reason")
        for m in metrics:
            val=row.get(m)
            if val in (None, ""):
                errors.append(f"row {i}: missing metric {m}")
            else:
                try:
                    x=float(val)
                    if math.isnan(x): errors.append(f"row {i}: NaN metric {m}")
                except Exception:
                    errors.append(f"row {i}: nonnumeric metric {m}={val}")
    print(f"rows: {len(rows)}")
    print(f"errors: {len(errors)}")
    for e in errors: print("ERROR:", e)
    print(f"warnings: {len(warnings)}")
    for w in warnings: print("WARN:", w)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
