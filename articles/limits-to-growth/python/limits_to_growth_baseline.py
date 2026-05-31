"""Baseline limits-to-growth simulation.

This script models a reinforcing growth process that slows as it approaches a
constraint. It uses a logistic-style formulation to demonstrate why early growth
can mislead analysts when a limiting capacity is not yet visible.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv


@dataclass(frozen=True)
class GrowthConfig:
    initial_scale: float = 100.0
    growth_rate: float = 0.13
    capacity: float = 260.0
    years: int = 25


def simulate(config: GrowthConfig) -> list[dict[str, float]]:
    scale = config.initial_scale
    rows: list[dict[str, float]] = []
    for year in range(config.years + 1):
        constraint_pressure = scale / config.capacity
        rows.append(
            {
                "year": year,
                "system_scale": round(scale, 3),
                "constraint_pressure": round(constraint_pressure, 3),
            }
        )
        net_growth = config.growth_rate * scale * (1 - scale / config.capacity)
        scale += net_growth
    return rows


def write_csv(rows: list[dict[str, float]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "outputs" / "tables" / "baseline_growth.csv"
    write_csv(simulate(GrowthConfig()), output)
    print(f"Wrote {output}")
