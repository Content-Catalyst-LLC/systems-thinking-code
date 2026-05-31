"""Hidden accumulation model using a simple stock-flow equation."""

from __future__ import annotations


def simulate(initial_stock: float = 120.0, inflow: float = 12.0, outflow: float = 5.0, periods: int = 20):
    stock = initial_stock
    rows = []
    for period in range(1, periods + 1):
        stock = stock + inflow - outflow
        visible_warning = stock > 180
        rows.append((period, round(stock, 2), visible_warning))
    return rows


def main() -> None:
    print("period,hidden_stock,visible_warning")
    for period, stock, warning in simulate():
        print(f"{period},{stock},{warning}")


if __name__ == "__main__":
    main()
