"""
Stock-flow simulation for systems thinking.

A stock changes according to:

    stock_next = stock_current + inflow - outflow
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StockFlowRow:
    period: int
    stock: float
    inflow: float
    outflow: float


def simulate_stock_flow(
    initial_stock: float = 100.0,
    inflow: float = 12.0,
    outflow_rate: float = 0.08,
    periods: int = 24,
) -> list[StockFlowRow]:
    stock = initial_stock
    rows: list[StockFlowRow] = []

    for period in range(1, periods + 1):
        outflow = stock * outflow_rate
        stock = stock + inflow - outflow
        rows.append(
            StockFlowRow(
                period=period,
                stock=round(stock, 2),
                inflow=round(inflow, 2),
                outflow=round(outflow, 2),
            )
        )

    return rows


def main() -> None:
    print("period,stock,inflow,outflow")
    for row in simulate_stock_flow():
        print(f"{row.period},{row.stock},{row.inflow},{row.outflow}")


if __name__ == "__main__":
    main()
