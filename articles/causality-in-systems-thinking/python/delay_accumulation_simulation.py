"""
Delay and accumulation simulation.

The visible outcome appears after accumulated backlog crosses a threshold.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DelayRow:
    period: int
    backlog: float
    capacity: float
    visible_failure: int


def simulate(periods: int = 24, threshold: float = 150.0) -> list[DelayRow]:
    backlog = 100.0
    capacity = 58.0
    rows: list[DelayRow] = []

    for period in range(1, periods + 1):
        incoming_work = 18.0
        completed_work = capacity * 0.22
        backlog = backlog + incoming_work - completed_work
        capacity -= max(0.0, backlog - 120.0) * 0.01
        visible_failure = 1 if backlog >= threshold else 0

        rows.append(DelayRow(period, round(backlog, 2), round(capacity, 2), visible_failure))

    return rows


def main() -> None:
    print("period,backlog,capacity,visible_failure")
    for row in simulate():
        print(f"{row.period},{row.backlog},{row.capacity},{row.visible_failure}")


if __name__ == "__main__":
    main()
