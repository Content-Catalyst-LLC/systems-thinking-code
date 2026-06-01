"""Compare stock repair scenarios using synthetic rates."""
from __future__ import annotations

SCENARIOS = {
    "baseline": {"inflow": 4.0, "outflow": 5.0},
    "prevention": {"inflow": 4.0, "outflow": 3.5},
    "repair": {"inflow": 7.0, "outflow": 5.0},
    "balanced": {"inflow": 7.0, "outflow": 3.5},
}


def simulate(initial: float, inflow: float, outflow: float, periods: int = 10) -> list[float]:
    values = [initial]
    stock = initial
    for _ in range(periods):
        stock += inflow - outflow
        values.append(stock)
    return values


if __name__ == "__main__":
    for name, rates in SCENARIOS.items():
        print(name, simulate(55, rates["inflow"], rates["outflow"]))
