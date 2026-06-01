"""Social stock-flow simulation using synthetic data.

This example models social stocks as accumulated conditions changed by inflows and outflows.
It is a teaching model, not an empirical model.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs" / "tables"
OUTPUTS.mkdir(parents=True, exist_ok=True)


@dataclass
class SocialStock:
    name: str
    value: float
    inflow: float
    outflow: float
    floor: float = 0.0
    ceiling: float | None = 100.0

    def step(self) -> float:
        self.value += self.inflow - self.outflow
        self.value = max(self.floor, self.value)
        if self.ceiling is not None:
            self.value = min(self.ceiling, self.value)
        return self.value


def simulate(months: int = 24) -> list[dict[str, float]]:
    stocks = [
        SocialStock("public_trust", 42.0, 3.2, 2.6),
        SocialStock("administrative_burden", 18.0, 5.5, 2.1, ceiling=None),
        SocialStock("household_security", 38.0, 4.0, 3.7),
        SocialStock("institutional_capacity", 55.0, 2.8, 2.4),
        SocialStock("capability", 45.0, 3.5, 2.9),
    ]
    rows: list[dict[str, float]] = []
    for month in range(months + 1):
        rows.append({"month": month, **{stock.name: round(stock.value, 2) for stock in stocks}})
        for stock in stocks:
            stock.step()
    return rows


def write_rows(rows: list[dict[str, float]]) -> None:
    path = OUTPUTS / "social_stock_flow_baseline.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path}")


if __name__ == "__main__":
    write_rows(simulate())
