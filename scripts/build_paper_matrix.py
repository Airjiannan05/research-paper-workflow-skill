#!/usr/bin/env python3
"""Build a Markdown related-work matrix from paper-card CSV or JSON.

Input CSV columns are flexible; common fields are normalized when present.
This script checks structure only. It does not verify factual correctness.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Iterable

COLUMNS = [
    "method_family",
    "title",
    "input",
    "representation",
    "core_mechanism",
    "output",
    "data_or_benchmark",
    "strength",
    "limitations",
    "relation_to_our_work",
]

ALIASES = {
    "paper": "title",
    "name": "title",
    "method": "core_mechanism",
    "mechanism": "core_mechanism",
    "benchmark": "data_or_benchmark",
    "dataset": "data_or_benchmark",
    "limitation": "limitations",
    "relation": "relation_to_our_work",
    "family": "method_family",
}


def normalize_key(key: str) -> str:
    k = key.strip().lower().replace(" ", "_").replace("-", "_")
    return ALIASES.get(k, k)


def load_rows(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [{normalize_key(k): v for k, v in row.items()} for row in reader]
    if suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("papers", [])
        if not isinstance(data, list):
            raise ValueError("JSON input must be a list or an object with a 'papers' list")
        return [{normalize_key(str(k)): v for k, v in row.items()} for row in data]
    raise ValueError("Input must be .csv or .json")


def cell(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\n", " ").replace("|", "\\|").strip()
    return text


def build_markdown(rows: Iterable[dict[str, Any]]) -> str:
    header = "| " + " | ".join(COLUMNS) + " |"
    sep = "|" + "|".join(["---"] * len(COLUMNS)) + "|"
    lines = ["# Related Work Matrix", "", header, sep]
    for row in rows:
        lines.append("| " + " | ".join(cell(row.get(c, "")) for c in COLUMNS) + " |")
    lines.append("")
    lines.append("Note: this matrix is generated from provided paper cards and has not been fact-checked.")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="paper-card CSV or JSON")
    parser.add_argument("-o", "--output", type=Path, default=Path("related_work_matrix.md"))
    args = parser.parse_args()

    rows = load_rows(args.input)
    args.output.write_text(build_markdown(rows), encoding="utf-8")
    print(f"Wrote {args.output} with {len(rows)} rows")


if __name__ == "__main__":
    main()
