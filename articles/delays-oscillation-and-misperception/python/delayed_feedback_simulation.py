"""Delayed feedback simulation for systems thinking."""

from __future__ import annotations

from collections import deque


def simulate(goal: float = 50.0, initial: float = 80.0, correction: float = 0.25, delay: int = 3, periods: int = 24):
    state = initial
    history = deque([initial] * (delay + 1), maxlen=delay + 1)
    rows = []

    for period in range(1, periods + 1):
        delayed_state = history[0]
        adjustment = correction * (goal - delayed_state)
        state = state + adjustment
        history.append(state)
        rows.append((period, round(state, 3), round(delayed_state, 3), round(adjustment, 3)))

    return rows


def main() -> None:
    print("period,state,delayed_state,adjustment")
    for row in simulate():
        print(",".join(map(str, row)))


if __name__ == "__main__":
    main()
