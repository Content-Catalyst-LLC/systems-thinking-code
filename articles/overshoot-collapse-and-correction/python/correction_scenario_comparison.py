"""Compare correction scenarios."""
from __future__ import annotations

from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows_by_scenario: dict[str, list[dict[str, str]]] = defaultdict(list)
    with (DATA / "outcomes.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            rows_by_scenario[row["scenario_id"]].append(row)
    summary = []
    for scenario_id, rows in rows_by_scenario.items():
        rows.sort(key=lambda r: int(r["month"]))
        first, last = rows[0], rows[-1]
        summary.append({
            "scenario_id": scenario_id,
            "performance_change": round(float(last["system_performance"]) - float(first["system_performance"]), 3),
            "stock_change": round(float(last["stock_level"]) - float(first["stock_level"]), 3),
            "final_correction_cost": last["correction_cost"],
            "final_distributional_burden": last["distributional_burden"],
        })
    out_path = OUT / "correction_scenario_comparison.csv"
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        writer.writeheader()
        writer.writerows(summary)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
