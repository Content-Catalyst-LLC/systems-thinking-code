"""Delayed balancing-loop example showing oscillation risk."""

from __future__ import annotations


def simulate(initial: float = 80.0, goal: float = 50.0, correction: float = 0.45, delay: int = 3, periods: int = 25) -> list[tuple[int, float]]:
    values = [initial] * (delay + 1)
    rows: list[tuple[int, float]] = []
    current = initial
    for period in range(1, periods + 1):
        delayed_value = values[-delay]
        current = current + correction * (goal - delayed_value)
        values.append(current)
        rows.append((period, round(current, 4)))
    return rows


def main() -> None:
    print("period,value")
    for period, value in simulate():
        print(f"{period},{value}")


if __name__ == "__main__":
    main()
