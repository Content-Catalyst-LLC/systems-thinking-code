#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "backlash_resistance_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_resistance_events.csv"
    if not path.exists():
        print("Skipping backlash diagnostics; missing synthetic_resistance_events.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []
    cumulative = 0.0

    for row in rows:
        intensity = float(row["intensity"])
        cumulative += intensity
        output.append({
            "event_id": row["event_id"],
            "period": row["period"],
            "resistance_type": row["resistance_type"],
            "intensity": round(intensity, 3),
            "cumulative_resistance_pressure": round(cumulative, 3),
            "diagnostic": "high counter-adaptation signal" if intensity >= 0.50 else "moderate counter-adaptation signal",
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
