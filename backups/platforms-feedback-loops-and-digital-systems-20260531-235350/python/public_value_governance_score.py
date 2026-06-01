#!/usr/bin/env python3
"""Create a compact public-value and governance diagnostic table."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "platform_feedback_timeseries.csv"
OUTPUT = TABLES / "public_value_governance_diagnostics.csv"


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Run the base platform model first.")
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = read_rows(INPUT)
    diagnostics: list[dict[str, object]] = []
    for scenario in sorted({row["scenario"] for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario]
        avg_governance = mean(float(row["governance_readiness"]) for row in subset)
        avg_public_value = mean(float(row["public_value_index"]) for row in subset)
        avg_risk = mean(float(row["platform_risk_index"]) for row in subset)
        public_value_margin = avg_public_value + avg_governance - avg_risk
        diagnostics.append(
            {
                "scenario": scenario,
                "average_governance_readiness": round(avg_governance, 3),
                "average_public_value_index": round(avg_public_value, 3),
                "average_platform_risk_index": round(avg_risk, 3),
                "public_value_margin": round(public_value_margin, 3),
                "diagnostic": "public-value capacity exceeds modeled risk" if public_value_margin >= 50 else "public-value governance needs strengthening",
            }
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(diagnostics[0].keys()))
        writer.writeheader()
        writer.writerows(diagnostics)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
