"""Compare accumulation and depletion trajectories for a synthetic stock."""
from __future__ import annotations


def trajectory(initial: float, inflows: list[float], outflows: list[float]) -> list[float]:
    if len(inflows) != len(outflows):
        raise ValueError("Inflows and outflows must have equal length.")
    stock = initial
    values = [stock]
    for inflow, outflow in zip(inflows, outflows):
        stock += inflow - outflow
        values.append(stock)
    return values


if __name__ == "__main__":
    inflows = [6, 6, 6, 7, 7, 8]
    outflows = [4, 5, 6, 7, 8, 9]
    print(trajectory(70, inflows, outflows))
