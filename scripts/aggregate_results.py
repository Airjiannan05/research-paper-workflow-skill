#!/usr/bin/env python3
"""Aggregate multi-seed experiment results from CSV into mean/std/count rows."""
from __future__ import annotations
import argparse, csv, statistics
from collections import defaultdict

DEFAULT_GROUP=["claim_id","experiment_family","dataset","method","baseline","ablation"]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csvfile")
    ap.add_argument("--metrics", required=True, help="comma-separated numeric metrics")
    ap.add_argument("--group-by", default=','.join(DEFAULT_GROUP))
    ap.add_argument("--out", default="aggregated_results.csv")
    args=ap.parse_args()
    metrics=[m.strip() for m in args.metrics.split(',') if m.strip()]
    groups=[g.strip() for g in args.group_by.split(',') if g.strip()]
    with open(args.csvfile, newline="", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    buckets=defaultdict(list)
    for r in rows:
        if r.get("status", "completed") != "completed":
            continue
        key=tuple(r.get(g,"") for g in groups)
        buckets[key].append(r)
    out_fields=groups + sum(([f"{m}_mean", f"{m}_std", f"{m}_n"] for m in metrics), [])
    out=[]
    for key,rs in buckets.items():
        row={g:v for g,v in zip(groups,key)}
        for m in metrics:
            vals=[]
            for r in rs:
                try: vals.append(float(r[m]))
                except Exception: pass
            row[f"{m}_mean"] = f"{statistics.mean(vals):.6g}" if vals else ""
            row[f"{m}_std"] = f"{statistics.stdev(vals):.6g}" if len(vals)>1 else "0" if vals else ""
            row[f"{m}_n"] = len(vals)
        out.append(row)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=out_fields); w.writeheader(); w.writerows(out)
    print(f"wrote {len(out)} aggregated rows to {args.out}")

if __name__ == "__main__":
    main()
