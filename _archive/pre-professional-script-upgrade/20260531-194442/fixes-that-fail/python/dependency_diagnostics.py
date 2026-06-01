#!/usr/bin/env python3
"""Compute a dependency indicator for repeated quick-fix use."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_model_runs.csv"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    flagged = []
    with DATA.open(newline="") as f:
        for row in csv.DictReader(f):
            ratio = float(row["dependency_ratio"])
            if ratio >= 1.0:
                row["risk_flag"] = "dependency_risk"
            else:
                row["risk_flag"] = "lower_dependency"
            flagged.append(row)
    path = OUT / "dependency_diagnostics.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(flagged[0].keys()))
        writer.writeheader()
        writer.writerows(flagged)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
