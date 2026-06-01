"""Micro-meso-macro systems model using synthetic level indicators."""

from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_indicators.csv"


def load_rows() -> list[dict[str, float]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = []
        for row in csv.DictReader(handle):
            rows.append({key: float(value) for key, value in row.items()})
        return rows


def compute_level_pressure(row: dict[str, float]) -> dict[str, float]:
    micro_pressure = row["individual_burden"]
    meso_capacity_gap = 100 - ((row["team_coordination"] + row["organizational_capacity"]) / 2)
    macro_pressure = ((100 - row["institutional_trust"]) + row["ecological_stress"]) / 2
    return {
        "period": row["period"],
        "micro_pressure": round(micro_pressure, 2),
        "meso_capacity_gap": round(meso_capacity_gap, 2),
        "macro_pressure": round(macro_pressure, 2),
    }


def main() -> None:
    print("period,micro_pressure,meso_capacity_gap,macro_pressure")
    for row in load_rows():
        result = compute_level_pressure(row)
        print(f"{int(result['period'])},{result['micro_pressure']},{result['meso_capacity_gap']},{result['macro_pressure']}")


if __name__ == "__main__":
    main()
