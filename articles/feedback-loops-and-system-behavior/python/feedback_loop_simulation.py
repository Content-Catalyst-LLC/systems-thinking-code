"""
Feedback-loop simulation for "Feedback Loops and System Behavior".

This script compares a reinforcing loop, a balancing loop, and a delayed balancing loop.
It uses only the Python standard library.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FeedbackRow:
    period: int
    reinforcing: float
    balancing: float
    delayed_balancing: float


def simulate(periods: int = 30, delay: int = 4) -> list[FeedbackRow]:
    reinforcing = 10.0
    balancing = 85.0
    delayed = 85.0
    delayed_history = [delayed] * (delay + 1)
    goal = 50.0

    rows: list[FeedbackRow] = []

    for period in range(1, periods + 1):
        reinforcing = reinforcing * 1.10
        balancing = balancing + 0.22 * (goal - balancing)

        delayed_observation = delayed_history[0]
        delayed = delayed + 0.30 * (goal - delayed_observation)
        delayed_history.append(delayed)
        delayed_history.pop(0)

        rows.append(
            FeedbackRow(
                period=period,
                reinforcing=round(reinforcing, 2),
                balancing=round(balancing, 2),
                delayed_balancing=round(delayed, 2),
            )
        )

    return rows


def main() -> None:
    print("period,reinforcing,balancing,delayed_balancing")
    for row in simulate():
        print(f"{row.period},{row.reinforcing},{row.balancing},{row.delayed_balancing}")


if __name__ == "__main__":
    main()
