#!/usr/bin/env python3
"""Rank policy robustness from synthetic scenario results."""
from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

def main() -> None:
    grouped: dict[str, list[float]] = defaultdict(list)
    with (DATA / "synthetic_distributional_outputs.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            grouped[row["scenario"]].append(float(row["resilience"]))
    rows = []
    for scenario, vals in grouped.items():
        rows.append({"scenario": scenario, "worst_case_resilience": round(min(vals), 3), "average_resilience": round(sum(vals)/len(vals), 3), "cases": len(vals)})
    rows.sort(key=lambda r: (-r["worst_case_resilience"], -r["average_resilience"]))
    with (OUT / "robustness_comparison.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT / 'robustness_comparison.csv'}")

if __name__ == "__main__":
    main()
