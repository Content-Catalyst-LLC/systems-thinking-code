"""Simple stock-flow intervention model for teaching leverage analysis."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StockFlowState:
    stock: float
    inflow: float
    outflow: float

    def step(self, intervention_strength: float = 0.0) -> "StockFlowState":
        adjusted_outflow = max(0.0, self.outflow - intervention_strength)
        next_stock = self.stock + self.inflow - adjusted_outflow
        return StockFlowState(next_stock, self.inflow, adjusted_outflow)


if __name__ == "__main__":
    state = StockFlowState(stock=60.0, inflow=8.0, outflow=4.0)
    for t in range(1, 11):
        state = state.step(intervention_strength=1.5)
        print(t, round(state.stock, 2))
