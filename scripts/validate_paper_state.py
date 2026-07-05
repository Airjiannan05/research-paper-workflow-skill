#!/usr/bin/env python3
"""Validate a research-paper-workflow paper_state.yaml file.

This script checks structure only. It does not verify factual claims, venue rules,
experimental results, or citation support.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception as exc:  # pragma: no cover
    print("ERROR: PyYAML is required to read YAML files.", file=sys.stderr)
    print(str(exc), file=sys.stderr)
    sys.exit(2)

REQUIRED_TOP = [
    "project",
    "artifacts",
    "claims",
    "experiments",
    "reviews",
    "revision_ledger",
    "submission_checks",
]
REQUIRED_PROJECT = ["title", "target_venue", "stage", "paper_type"]
REQUIRED_ARTIFACTS = [
    "idea_brief",
    "literature_notes",
    "related_work_matrix",
    "claim_manifest",
    "experiment_plan",
    "results",
    "manuscript",
    "review_report",
    "integrity_report",
    "submission_check",
    "revision_ledger",
]
VALID_STAGES = {
    "idea",
    "literature",
    "experiment",
    "writing",
    "review",
    "audit",
    "submission",
    "rebuttal",
}


def is_missing(value: Any) -> bool:
    return value is None or value == "" or value == "TBD"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paper_state", type=Path)
    args = parser.parse_args()

    try:
        data = yaml.safe_load(args.paper_state.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: cannot read YAML: {exc}")
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        print("ERROR: root must be a mapping")
        return 1

    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"missing top-level key: {key}")

    project = data.get("project", {})
    if not isinstance(project, dict):
        errors.append("project must be a mapping")
        project = {}
    for key in REQUIRED_PROJECT:
        if key not in project:
            errors.append(f"missing project key: {key}")
        elif is_missing(project[key]):
            warnings.append(f"project.{key} is TBD")
    stage = project.get("stage")
    if stage not in VALID_STAGES and stage is not None:
        errors.append(f"invalid project.stage: {stage}")

    artifacts = data.get("artifacts", {})
    if not isinstance(artifacts, dict):
        errors.append("artifacts must be a mapping")
        artifacts = {}
    for key in REQUIRED_ARTIFACTS:
        if key not in artifacts:
            errors.append(f"missing artifact key: {key}")

    for seq_key in ["claims", "experiments", "reviews", "revision_ledger", "submission_checks"]:
        if seq_key in data and not isinstance(data[seq_key], list):
            errors.append(f"{seq_key} must be a list")

    if errors:
        print("FAIL")
        for item in errors:
            print(f"ERROR: {item}")
    else:
        print("PASS")

    for item in warnings:
        print(f"WARN: {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
