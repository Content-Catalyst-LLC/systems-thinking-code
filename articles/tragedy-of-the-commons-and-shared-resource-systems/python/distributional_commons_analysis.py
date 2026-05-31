#!/usr/bin/env python3
"""Analyze distribution of commons benefits, burdens, and voice."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    with (DATA / "synthetic_distributional_impacts.csv").open(newline="") as handle:
        impacts = list(csv.DictReader(handle))
    rows = []
    for row in impacts:
        benefit = float(row["benefit_share"])
        burden = float(row["depletion_burden_share"])
        voice = float(row["voice_in_governance"])
        vulnerability = float(row["vulnerability_score"])
        injustice_risk = max(0.0, burden - benefit) * (1.0 - voice) * (0.5 + vulnerability)
        rows.append(
            {
                "resource_id": row["resource_id"],
                "user_group": row["user_group"],
                "benefit_share": benefit,
                "depletion_burden_share": burden,
                "voice_in_governance": voice,
                "vulnerability_score": vulnerability,
                "injustice_risk_index": round(injustice_risk, 4),
            }
        )
    output = OUT / "distributional_commons_results.csv"
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
