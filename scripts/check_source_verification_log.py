#!/usr/bin/env python3
"""Validate a source verification log CSV.

Required columns:
- id
- claim_or_fact
- check_1_existence
- check_2_metadata
- check_3_support
- verdict

Verdict must be one of: verified, partial, unverified, conflict.
"""

import argparse
import csv
import sys
from pathlib import Path

REQUIRED = [
    "id",
    "claim_or_fact",
    "check_1_existence",
    "check_2_metadata",
    "check_3_support",
    "verdict",
]
ALLOWED_VERDICTS = {"verified", "partial", "unverified", "conflict"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate source verification log CSV")
    parser.add_argument("path", help="Path to source_verification_log.csv")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    errors = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("ERROR: empty CSV or missing header", file=sys.stderr)
            return 2
        missing_cols = [c for c in REQUIRED if c not in reader.fieldnames]
        if missing_cols:
            errors.append(f"missing columns: {', '.join(missing_cols)}")
        for line_no, row in enumerate(reader, start=2):
            for col in REQUIRED:
                if col in row and not (row.get(col) or "").strip():
                    errors.append(f"line {line_no}: empty {col}")
            verdict = (row.get("verdict") or "").strip().lower()
            if verdict and verdict not in ALLOWED_VERDICTS:
                errors.append(f"line {line_no}: invalid verdict '{verdict}'")
            if verdict == "verified":
                for col in ["check_1_existence", "check_2_metadata", "check_3_support"]:
                    val = (row.get(col) or "").strip().lower()
                    if val in {"", "tbd", "unknown", "no", "failed", "unverified"}:
                        errors.append(f"line {line_no}: verified verdict but weak {col}: '{row.get(col)}'")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print("OK: source verification log passed structural checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
