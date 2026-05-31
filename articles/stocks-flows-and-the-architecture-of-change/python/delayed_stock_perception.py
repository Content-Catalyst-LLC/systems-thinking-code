"""Delayed perception model for stock-flow decision-making."""
from __future__ import annotations


def delayed_response(initial: float, target: float, delay: int, periods: int) -> list[float]:
    history = [initial]
    stock = initial
    for _ in range(periods):
        perceived = history[max(0, len(history) - 1 - delay)]
        corrective_inflow = 0.2 * max(target - perceived, 0)
        natural_outflow = 2.0
        stock = stock + corrective_inflow - natural_outflow
        history.append(stock)
    return history


if __name__ == "__main__":
    print(delayed_response(initial=50, target=80, delay=3, periods=15))
