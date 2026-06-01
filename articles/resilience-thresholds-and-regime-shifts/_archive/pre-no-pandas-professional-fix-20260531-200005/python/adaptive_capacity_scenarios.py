#!/usr/bin/env python3
"""Adaptive capacity scenario scorecard."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = ROOT / "outputs" / "tables"
TABLE_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    rows = [
        {"strategy": "status_quo", "diversity": 42, "redundancy": 35, "learning": 38, "trust": 46, "authority": 34, "equity": 31},
        {"strategy": "monitoring_and_alerts", "diversity": 45, "redundancy": 38, "learning": 66, "trust": 51, "authority": 44, "equity": 39},
        {"strategy": "buffer_building", "diversity": 52, "redundancy": 68, "learning": 59, "trust": 58, "authority": 50, "equity": 45},
        {"strategy": "adaptive_governance", "diversity": 66, "redundancy": 63, "learning": 78, "trust": 72, "authority": 71, "equity": 65},
        {"strategy": "transformative_redesign", "diversity": 75, "redundancy": 70, "learning": 84, "trust": 76, "authority": 82, "equity": 79},
    ]
    df = pd.DataFrame(rows)
    weights = {"diversity": 0.16, "redundancy": 0.16, "learning": 0.18, "trust": 0.18, "authority": 0.16, "equity": 0.16}
    df["adaptive_capacity_score"] = sum(df[col] * weight for col, weight in weights.items()).round(2)
    df["diagnostic"] = df["adaptive_capacity_score"].apply(
        lambda x: "strong" if x >= 75 else "improving" if x >= 60 else "fragile"
    )
    df.to_csv(TABLE_DIR / "adaptive_capacity_scorecard.csv", index=False)
    print("Adaptive capacity scorecard")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
