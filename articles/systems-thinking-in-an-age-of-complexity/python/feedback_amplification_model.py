#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "feedback_amplification_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_feedback_patterns.csv"
    if not path.exists():
        print("Skipping feedback amplification model; missing synthetic_feedback_patterns.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        intensity = float(row["intensity"])
        delay = int(row["delay_periods"])
        amplification_risk = intensity * 100.0 + min(20.0, delay * 1.5)
        output.append({
            "pattern_id": row["pattern_id"],
            "pattern_name": row["pattern_name"],
            "loop_type": row["loop_type"],
            "intensity": round(intensity, 3),
            "delay_periods": delay,
            "amplification_risk_score": round(amplification_risk, 3),
            "diagnostic": "high feedback amplification risk" if amplification_risk >= 80 else "moderate feedback risk",
            "notes": row["notes"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
