"""
Stock-and-flow model for systems thinking.

A stock changes through inflows and outflows. This simple model can represent
capacity, trust, pollution, debt, institutional memory, or other accumulations.
"""

from __future__ import annotations

import pandas as pd


def simulate_stock_flow(
    initial_stock: float = 50.0,
    inflow: float = 5.0,
    outflow: float = 3.5,
    steps: int = 80
) -> pd.DataFrame:
    stock = [initial_stock]

    for _ in range(1, steps):
        next_stock = max(0.0, stock[-1] + inflow - outflow)
        stock.append(next_stock)

    return pd.DataFrame({
        "time": range(steps),
        "stock": stock,
        "inflow": inflow,
        "outflow": outflow
    })


def main() -> None:
    results = simulate_stock_flow()
    print(results.head())
    print(results.tail())

    results.to_csv("../outputs/stock_flow_model.csv", index=False)


if __name__ == "__main__":
    main()
