"""Simple reinforcing-loop simulation for systems thinking."""

from __future__ import annotations


def simulate(initial: float = 10.0, rate: float = 0.12, periods: int = 20) -> list[tuple[int, float]]:
    value = initial
    rows: list[tuple[int, float]] = []
    for period in range(1, periods + 1):
        value = value + rate * value
        rows.append((period, round(value, 4)))
    return rows


def main() -> None:
    print("period,value")
    for period, value in simulate():
        print(f"{period},{value}")


if __name__ == "__main__":
    main()
