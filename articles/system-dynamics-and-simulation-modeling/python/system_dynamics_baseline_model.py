"""Baseline system dynamics model for a synthetic service-backlog system.

The model demonstrates stocks, flows, feedback, and behavior over time.
Data are synthetic and intended for methodological demonstration only.
"""

from __future__ import annotations

from dataclasses import dataclass
import csv
from pathlib import Path


@dataclass
class Parameters:
    months: int = 36
    initial_backlog: float = 1200.0
    initial_staff: float = 45.0
    initial_trust: float = 68.0
    base_demand: float = 420.0
    demand_growth_rate: float = 0.012
    productivity_per_staff: float = 8.0
    hiring_rate: float = 1.8
    turnover_rate: float = 1.0
    trust_loss_scale: float = 0.006


def simulate(params: Parameters) -> list[dict[str, float]]:
    backlog = params.initial_backlog
    staff = params.initial_staff
    trust = params.initial_trust
    rows: list[dict[str, float]] = []

    for month in range(params.months + 1):
        demand = params.base_demand * ((1 + params.demand_growth_rate) ** month)
        completion = min(backlog + demand, staff * params.productivity_per_staff)
        backlog_pressure = max(backlog / 1000.0 - 1.0, 0.0)
        trust = max(0.0, min(100.0, trust - backlog_pressure * params.trust_loss_scale * 100))
        rows.append({
            "month": float(month),
            "backlog": round(backlog, 2),
            "staff_capacity": round(staff, 2),
            "public_trust": round(trust, 2),
            "demand": round(demand, 2),
            "completion": round(completion, 2),
        })
        backlog = max(0.0, backlog + demand - completion)
        staff = max(0.0, staff + params.hiring_rate - params.turnover_rate)
    return rows


def write_outputs(rows: list[dict[str, float]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    article_dir = Path(__file__).resolve().parents[1]
    output_path = article_dir / "outputs" / "tables" / "baseline_simulation.csv"
    rows = simulate(Parameters())
    write_outputs(rows, output_path)
    print(f"Wrote {output_path}")
