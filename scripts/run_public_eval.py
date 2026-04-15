#!/usr/bin/env python3
"""
Minimal public entrypoint for a VeriScope release repository.

This script is intentionally lightweight. It validates the released bundle
layout, checks a prediction file, and writes a compact run manifest. Replace or
extend it with the final public evaluation wrapper when wiring the exported code
modules into the public repository.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FILES = {"problem.md", "config.yaml", "testbench.v"}


def collect_problem_dirs(root: Path) -> list[Path]:
    return sorted(path for path in root.glob("*/*") if path.is_dir())


def validate_bundles(root: Path) -> list[dict]:
    rows = []
    for problem_dir in collect_problem_dirs(root):
        files = {p.name for p in problem_dir.iterdir() if p.is_file()}
        rows.append(
            {
                "problem_id": problem_dir.name,
                "level": problem_dir.parent.name,
                "missing": sorted(REQUIRED_FILES - files),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--problems", type=Path, required=True)
    parser.add_argument("--predictions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--mode", default="full", choices=["functional", "full"])
    args = parser.parse_args()

    if not args.problems.exists():
        raise SystemExit(f"Missing problems directory: {args.problems}")
    if not args.predictions.exists():
        raise SystemExit(f"Missing predictions file: {args.predictions}")

    bundle_report = validate_bundles(args.problems)
    invalid = [row for row in bundle_report if row["missing"]]
    predictions = json.loads(args.predictions.read_text(encoding="utf-8"))

    summary = {
        "mode": args.mode,
        "problem_root": str(args.problems),
        "prediction_file": str(args.predictions),
        "bundle_count": len(bundle_report),
        "invalid_bundle_count": len(invalid),
        "prediction_count": len(predictions),
        "status": "layout_valid" if not invalid else "layout_has_missing_files",
        "note": "Replace this lightweight wrapper with the final public evaluation entrypoint for the release.",
    }

    payload = {
        "summary": summary,
        "invalid_bundles": invalid[:20],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
