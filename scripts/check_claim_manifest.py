#!/usr/bin/env python3
"""Validate the structure of a claim manifest CSV/JSON.

This script checks completeness, not truth. It cannot verify whether a citation
or experiment actually supports a claim.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

REQUIRED = ["claim_id", "claim", "support_source", "strength", "risk"]


def norm(k: str) -> str:
    return k.strip().lower().replace(" ", "_").replace("-", "_")


def load(path: Path) -> list[dict[str, str]]:
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as f:
            return [{norm(k): (v or "") for k, v in row.items()} for row in csv.DictReader(f)]
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("claims", [])
        return [{norm(str(k)): str(v or "") for k, v in row.items()} for row in data]
    raise ValueError("Input must be .csv or .json")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    rows = load(args.input)

    errors = []
    for i, row in enumerate(rows, 1):
        for field in REQUIRED:
            if not row.get(field, "").strip():
                errors.append(f"row {i}: missing {field}")
        strength = row.get("strength", "").lower()
        risk = row.get("risk", "").lower()
        if strength in {"weak", "missing"} and risk != "high":
            errors.append(f"row {i}: weak/missing support should usually be high risk")

    if errors:
        print("Claim manifest structural issues:")
        for e in errors:
            print(f"- {e}")
        raise SystemExit(1)
    print(f"Claim manifest structure looks complete for {len(rows)} claims")


if __name__ == "__main__":
    main()
