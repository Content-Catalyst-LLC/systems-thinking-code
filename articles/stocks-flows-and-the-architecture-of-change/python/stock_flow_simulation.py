"""Basic stock-flow simulation with synthetic systems data."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"


@dataclass
class StockFlowState:
    period: int
    stock: float
    inflow: float
    outflow: float

    @property
    def next_stock(self) -> float:
        return self.stock + self.inflow - self.outflow


def simulate(initial: float, inflow: float, outflow: float, periods: int = 12) -> list[StockFlowState]:
    states: list[StockFlowState] = []
    stock = initial
    for period in range(periods):
        state = StockFlowState(period=period, stock=stock, inflow=inflow, outflow=outflow)
        states.append(state)
        stock = state.next_stock
    return states


def write_csv(states: list[StockFlowState], path: Path) -> None:
    OUTPUTS.mkdir(exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["period", "stock", "inflow", "outflow", "next_stock"])
        writer.writeheader()
        for state in states:
            writer.writerow({
                "period": state.period,
                "stock": round(state.stock, 3),
                "inflow": state.inflow,
                "outflow": state.outflow,
                "next_stock": round(state.next_stock, 3),
            })


if __name__ == "__main__":
    baseline = simulate(initial=55, inflow=4, outflow=5, periods=10)
    write_csv(baseline, OUTPUTS / "trust_stock_flow_simulation.csv")
    print("Wrote outputs/trust_stock_flow_simulation.csv")
