#!/usr/bin/env python3
"""Create trust and prevention-value diagnostics from public health scenario outputs."""

from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TIMESERIES = ROOT / "outputs" / "tables" / "public_health_system_timeseries.csv"
OUT = ROOT / "outputs" / "tables" / "public_trust_feedback_diagnostics.csv"


def main() -> None:
    if not TIMESERIES.exists():
        raise FileNotFoundError("Run public_health_system_model.py before public_trust_health_feedback.py")

    by_scenario: dict[str, list[dict[str, str]]] = {}
    with TIMESERIES.open("r", newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            by_scenario.setdefault(row["scenario"], []).append(row)

    rows = []
    for scenario, data in sorted(by_scenario.items()):
        trust_values = [float(row["public_trust"]) for row in data]
        prevention_values = [float(row["prevention_value_index"]) for row in data]
        rows.append(
            {
                "scenario": scenario,
                "minimum_public_trust": round(min(trust_values), 3),
                "average_public_trust": round(mean(trust_values), 3),
                "final_public_trust": round(trust_values[-1], 3),
                "average_prevention_value_index": round(mean(prevention_values), 3),
                "trust_diagnostic": "trust fragility" if min(trust_values) < 45 else "trust comparatively stable",
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
