#!/usr/bin/env python3
"""Create asset-level maintenance priority diagnostics from the main workflow outputs."""

from __future__ import annotations
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing {path.name}. Run intelligent_infrastructure_system_model.py first.")
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("No diagnostics rows to write.")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = read_csv(TABLES / "intelligent_infrastructure_timeseries.csv")
    final_year = max(int(row["year"]) for row in rows)
    final_rows = [row for row in rows if int(row["year"]) == final_year]
    diagnostics = []
    for row in final_rows:
        risk = float(row["risk_score"])
        equity = float(row["equity_priority"])
        redundancy_gap = 100.0 - float(row["redundancy"])
        maintenance = float(row["maintenance_action_score"])
        priority = risk * 0.48 + equity * 0.24 + redundancy_gap * 0.18 - maintenance * 0.10
        diagnostics.append(
            {
                "scenario": row["scenario"],
                "asset_id": row["asset_id"],
                "category": row["category"],
                "risk_score": round(risk, 3),
                "equity_priority": round(equity, 3),
                "redundancy_gap": round(redundancy_gap, 3),
                "maintenance_action_score": round(maintenance, 3),
                "public_priority_score": round(priority, 3),
                "priority_band": "urgent" if priority >= 50 else "elevated" if priority >= 35 else "routine",
            }
        )
    diagnostics.sort(key=lambda r: (r["scenario"], -float(r["public_priority_score"])))
    write_csv(TABLES / "asset_priority_diagnostics.csv", diagnostics)
    print(f"Wrote {TABLES / 'asset_priority_diagnostics.csv'}")


if __name__ == "__main__":
    main()
