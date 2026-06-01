"""Simple balancing-loop simulation for systems thinking."""

from __future__ import annotations


def simulate(initial: float = 85.0, goal: float = 50.0, correction: float = 0.2, periods: int = 20) -> list[tuple[int, float]]:
    value = initial
    rows: list[tuple[int, float]] = []
    for period in range(1, periods + 1):
        value = value + correction * (goal - value)
        rows.append((period, round(value, 4)))
    return rows


def main() -> None:
    print("period,value")
    for period, value in simulate():
        print(f"{period},{value}")


if __name__ == "__main__":
    main()
