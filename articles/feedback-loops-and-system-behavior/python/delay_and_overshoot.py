"""Delayed feedback and overshoot demonstration."""

from __future__ import annotations

from collections import deque


def delayed_balancing(periods: int = 40, goal: float = 100.0, delay: int = 5, correction: float = 0.35) -> list[tuple[int, float]]:
    value = 40.0
    history: deque[float] = deque([value] * (delay + 1), maxlen=delay + 1)
    rows: list[tuple[int, float]] = []

    for period in range(1, periods + 1):
        observed = history[0]
        value = value + correction * (goal - observed)
        history.append(value)
        rows.append((period, round(value, 2)))

    return rows


def main() -> None:
    print("period,value")
    for period, value in delayed_balancing():
        print(f"{period},{value}")


if __name__ == "__main__":
    main()
