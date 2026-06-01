"""Scenario comparison for capacity investment timing."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv


@dataclass(frozen=True)
class Scenario:
    name: str
    growth_rate: float
    initial_capacity: float
    annual_investment: float
    investment_delay: int


SCENARIOS = [
    Scenario("baseline", 0.12, 230.0, 5.0, 3),
    Scenario("early_capacity", 0.10, 260.0, 16.0, 1),
    Scenario("delayed_capacity", 0.12, 230.0, 16.0, 5),
    Scenario("throughput_pressure", 0.18, 220.0, 3.0, 3),
    Scenario("steady_state_shift", 0.05, 250.0, 12.0, 1),
]


def simulate(scenario: Scenario, years: int = 25):
    scale = 100.0
    capacity = scenario.initial_capacity
    pending: list[float] = []
    rows = []
    for year in range(years + 1):
        if len(pending) > scenario.investment_delay:
            capacity += pending.pop(0)
        else:
            pending.append(scenario.annual_investment)
        pressure = scale / capacity
        quality = max(0.1, 1.0 - max(0.0, pressure - 0.75))
        rows.append(
            {
                "scenario": scenario.name,
                "year": year,
                "scale": round(scale, 3),
                "capacity": round(capacity, 3),
                "pressure": round(pressure, 3),
                "quality": round(quality, 3),
            }
        )
        scale += scenario.growth_rate * scale * quality
    return rows


def main() -> None:
    rows = [row for scenario in SCENARIOS for row in simulate(scenario)]
    out = Path(__file__).resolve().parents[1] / "outputs" / "tables" / "capacity_investment_scenarios.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
