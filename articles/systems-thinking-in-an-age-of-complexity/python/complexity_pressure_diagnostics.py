#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "complexity_pressure_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_complexity_parameters.csv"
    if not path.exists():
        print("Skipping complexity pressure diagnostics; missing synthetic_complexity_parameters.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        pressure = (
            float(row["interdependence"]) * 22.0
            + float(row["feedback_intensity"]) * 22.0
            + float(row["delay_pressure"]) * 18.0
            + float(row["adaptation_rate"]) * 16.0
            + float(row["uncertainty"]) * 22.0
        )
        capacity = (
            float(row["redundancy"]) * 18.0
            + float(row["modularity"]) * 16.0
            + float(row["learning_capacity"]) * 18.0
            + float(row["trust"]) * 14.0
            + float(row["response_variety"]) * 20.0
        )
        output.append({
            "scenario": row["scenario"],
            "complexity_pressure": round(pressure, 3),
            "response_capacity": round(capacity, 3),
            "pressure_capacity_gap": round(pressure - capacity, 3),
            "diagnostic": "complexity pressure exceeds response capacity" if pressure > capacity else "response capacity comparatively adequate",
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
