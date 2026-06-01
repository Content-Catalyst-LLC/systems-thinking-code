#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "accountability_sensitivity.csv"


def main() -> None:
    path = RAW / "synthetic_control_actions.csv"
    if not path.exists():
        print("Skipping accountability sensitivity; missing synthetic_control_actions.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        strength = float(row["control_strength"])
        requires_high = row["accountability_requirement"].lower() == "high"
        risk_score = strength * 100.0 + (20.0 if requires_high else 8.0)
        output.append({
            "action_id": row["action_id"],
            "action_type": row["action_type"],
            "response_speed": row["response_speed"],
            "control_strength": round(strength, 3),
            "accountability_requirement": row["accountability_requirement"],
            "control_risk_score": round(risk_score, 3),
            "risk_if_misused": row["risk_if_misused"],
            "diagnostic": "strong accountability required before deployment" if risk_score >= 70 else "standard review with transparency",
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
