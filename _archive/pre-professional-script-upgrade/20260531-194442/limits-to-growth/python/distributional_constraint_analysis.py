"""Distributional lens for limits-to-growth constraints."""

from __future__ import annotations

from pathlib import Path
import csv

GROUPS = [
    ("low_buffer_households", 0.90),
    ("frontline_workers", 0.82),
    ("high_access_households", 0.35),
    ("future_generations", 0.95),
    ("ecosystems", 1.00),
]


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    with (base / "data" / "synthetic_outputs.csv").open() as f:
        outputs = list(csv.DictReader(f))
    rows = []
    for output in outputs:
        severity = {"low": 1, "moderate": 2, "high": 3, "severe": 4}[output["distributional_risk"]]
        for group, exposure in GROUPS:
            rows.append(
                {
                    "scenario": output["scenario"],
                    "group": group,
                    "exposure_weight": exposure,
                    "risk_score": round(severity * exposure, 3),
                }
            )
    out = base / "outputs" / "tables" / "distributional_constraint_analysis.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
