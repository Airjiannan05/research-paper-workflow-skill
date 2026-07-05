#!/usr/bin/env python3
"""Build a Markdown revision ledger from reviewer comments in CSV or JSON.

Expected fields are flexible, but these names are preferred:
comment_id, reviewer, concern, type, severity, response_stance, evidence,
manuscript_action, experiment_action, citation_action, status.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

FIELDS = [
    "comment_id",
    "reviewer",
    "concern",
    "type",
    "severity",
    "response_stance",
    "evidence",
    "manuscript_action",
    "experiment_action",
    "citation_action",
    "status",
]

HEADERS = [
    "Comment ID",
    "Reviewer",
    "Concern",
    "Type",
    "Severity",
    "Response stance",
    "Evidence",
    "Manuscript action",
    "Experiment action",
    "Citation action",
    "Status",
]


def read_rows(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("comments", [])
        if not isinstance(data, list):
            raise ValueError("JSON must be a list or an object with comments list")
        return [dict(item) for item in data]
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def cell(value: Any) -> str:
    text = "TBD" if value is None or value == "" else str(value)
    return text.replace("|", "\\|").replace("\n", "<br>")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    rows = read_rows(args.input)
    lines = ["# Revision Ledger", ""]
    lines.append("| " + " | ".join(HEADERS) + " |")
    lines.append("|" + "|".join(["---"] * len(HEADERS)) + "|")
    for row in rows:
        lines.append("| " + " | ".join(cell(row.get(field)) for field in FIELDS) + " |")
    text = "\n".join(lines) + "\n"

    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
