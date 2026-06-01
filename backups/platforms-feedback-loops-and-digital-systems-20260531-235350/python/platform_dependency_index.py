#!/usr/bin/env python3
"""Analyze platform dependency and lock-in pressure."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "platform_feedback_timeseries.csv"
OUTPUT = TABLES / "platform_dependency_diagnostics.csv"


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
        final = subset[-1]
        avg_dependency = mean(float(row["platform_dependency"]) for row in subset)
        avg_trust = mean(float(row["user_trust"]) for row in subset)
        final_dependency = float(final["platform_dependency"])
        dependency_trust_gap = final_dependency - float(final["user_trust"])
        diagnostics.append(
            {
                "scenario": scenario,
                "average_platform_dependency": round(avg_dependency, 3),
                "average_user_trust": round(avg_trust, 3),
                "final_platform_dependency": round(final_dependency, 3),
                "dependency_trust_gap": round(dependency_trust_gap, 3),
                "diagnostic": "dependency exceeds trust" if dependency_trust_gap > 10 else "dependency and trust more balanced",
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
