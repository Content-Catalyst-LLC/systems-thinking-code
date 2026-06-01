#!/usr/bin/env python3
"""Analyze moderation capacity and governance stress across platform scenarios."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "platform_feedback_timeseries.csv"
OUTPUT = TABLES / "moderation_capacity_diagnostics.csv"


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Run the base platform model first.")
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = read_rows(INPUT)
    diagnostics: list[dict[str, object]] = []
    for scenario in sorted({row["scenario"] for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario]
        peak_backlog = max(float(row["moderation_backlog"]) for row in subset)
        peak_cascade = max(float(row["harmful_cascade_risk"]) for row in subset)
        average_governance = mean(float(row["governance_readiness"]) for row in subset)
        stress_ratio = peak_backlog / max(average_governance, 1.0)
        diagnostics.append(
            {
                "scenario": scenario,
                "peak_moderation_backlog": round(peak_backlog, 3),
                "peak_harmful_cascade_risk": round(peak_cascade, 3),
                "average_governance_readiness": round(average_governance, 3),
                "moderation_stress_ratio": round(stress_ratio, 3),
                "diagnostic": "moderation capacity overloaded" if stress_ratio >= 1.25 else "moderation capacity comparatively stable",
            }
        )

    write_csv(OUTPUT, diagnostics)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
