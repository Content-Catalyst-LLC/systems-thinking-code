"""Delayed constraint feedback example."""

from __future__ import annotations

from pathlib import Path
import csv


def simulate(delay: int = 4, years: int = 30):
    growth = 100.0
    capacity = 240.0
    history = [growth] * (delay + 1)
    rows = []
    for year in range(years + 1):
        delayed_growth = history[0]
        perceived_pressure = delayed_growth / capacity
        actual_pressure = growth / capacity
        correction = max(0.0, perceived_pressure - 0.9)
        growth_rate = max(-0.05, 0.16 - 0.18 * correction)
        rows.append(
            {
                "year": year,
                "growth": round(growth, 3),
                "actual_pressure": round(actual_pressure, 3),
                "perceived_pressure": round(perceived_pressure, 3),
                "growth_rate": round(growth_rate, 3),
            }
        )
        history.append(growth)
        history.pop(0)
        growth += growth_rate * growth
    return rows


def main() -> None:
    rows = simulate()
    out = Path(__file__).resolve().parents[1] / "outputs" / "tables" / "delayed_constraint_feedback.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
