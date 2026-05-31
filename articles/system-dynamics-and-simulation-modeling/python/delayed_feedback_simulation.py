"""Delayed feedback simulation.

A balancing response uses delayed information about the stock, which can produce
oscillation or overcorrection.
"""

from __future__ import annotations

from collections import deque


def simulate_delayed_response(goal: float = 100.0, initial: float = 40.0, delay: int = 3, gain: float = 0.25, steps: int = 36):
    state = initial
    history = deque([initial] * max(delay, 1), maxlen=max(delay, 1))
    rows = []
    for t in range(steps + 1):
        perceived = history[0]
        correction = gain * (goal - perceived)
        rows.append({"time": t, "state": state, "perceived_state": perceived, "correction": correction})
        state = state + correction
        history.append(state)
    return rows


if __name__ == "__main__":
    for row in simulate_delayed_response(delay=4, gain=0.35)[:10]:
        print(row)
