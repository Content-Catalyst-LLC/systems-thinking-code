"""Limited-growth model: reinforcing growth constrained by carrying capacity."""

from __future__ import annotations


def simulate(initial: float = 5.0, rate: float = 0.35, capacity: float = 100.0, periods: int = 30) -> list[tuple[int, float]]:
    value = initial
    rows: list[tuple[int, float]] = []
    for period in range(1, periods + 1):
        value = value + rate * value * (1 - value / capacity)
        rows.append((period, round(value, 4)))
    return rows


def main() -> None:
    print("period,value")
    for period, value in simulate():
        print(f"{period},{value}")


if __name__ == "__main__":
    main()
