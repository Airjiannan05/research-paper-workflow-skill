#!/usr/bin/env python3
"""Convert an aggregated CSV to a simple LaTeX tabular snippet."""
from __future__ import annotations
import argparse, csv

ROW_END = r" \\"  # LaTeX row terminator

def esc(s):
    return str(s).replace('_', r'\_').replace('%', r'\%').replace('&', r'\&')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csvfile")
    ap.add_argument("--out", default="table.tex")
    args = ap.parse_args()
    with open(args.csvfile, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)
    spec = 'l' * len(fields)
    lines = ["\\begin{tabular}{%s}" % spec, "\\toprule"]
    lines.append(' & '.join(esc(x) for x in fields) + ROW_END)
    lines.append("\\midrule")
    for r in rows:
        lines.append(' & '.join(esc(r.get(f, '')) for f in fields) + ROW_END)
    lines += ["\\bottomrule", "\\end{tabular}"]
    open(args.out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print(f"wrote {args.out}")

if __name__ == "__main__":
    main()
