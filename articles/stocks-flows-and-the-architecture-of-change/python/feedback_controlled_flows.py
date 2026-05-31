"""Illustrate flows controlled by feedback from the current stock."""
from __future__ import annotations


def run_feedback_model(initial_stock: float, target: float, base_inflow: float, outflow: float, responsiveness: float, periods: int) -> list[dict[str, float]]:
    stock = initial_stock
    rows: list[dict[str, float]] = []
    for period in range(periods):
        gap = max(target - stock, 0)
        inflow = base_inflow + responsiveness * gap
        next_stock = stock + inflow - outflow
        rows.append({"period": period, "stock": stock, "gap": gap, "inflow": inflow, "outflow": outflow, "next_stock": next_stock})
        stock = next_stock
    return rows


if __name__ == "__main__":
    for row in run_feedback_model(40, 80, 2, 3, 0.12, 12):
        print(row)
