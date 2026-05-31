"""Simple stock-flow simulation utilities."""

from __future__ import annotations

from typing import Callable


def simulate_stock(
    initial_stock: float,
    inflow: Callable[[int, float], float],
    outflow: Callable[[int, float], float],
    steps: int,
) -> list[dict[str, float]]:
    stock = initial_stock
    rows: list[dict[str, float]] = []
    for t in range(steps + 1):
        i = inflow(t, stock)
        o = outflow(t, stock)
        rows.append({"time": t, "stock": stock, "inflow": i, "outflow": o, "net_flow": i - o})
        stock = max(0.0, stock + i - o)
    return rows


if __name__ == "__main__":
    result = simulate_stock(
        initial_stock=100.0,
        inflow=lambda t, s: 12.0,
        outflow=lambda t, s: 0.05 * s,
        steps=24,
    )
    for row in result[:5]:
        print(row)
