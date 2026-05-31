"""Overshoot and collapse demonstration using delayed perception of limits."""

from __future__ import annotations


def simulate(periods: int = 40, initial: float = 20.0, growth_rate: float = 0.18, carrying_capacity: float = 100.0, delay: int = 4):
    values = [initial] * (delay + 1)
    rows = []

    for t in range(periods):
        perceived_state = values[-delay]
        growth = growth_rate * values[-1] * (1 - perceived_state / carrying_capacity)
        next_value = max(0.0, values[-1] + growth)
        values.append(next_value)
        rows.append((t + 1, round(next_value, 2), round(perceived_state, 2), round(growth, 2)))

    return rows


def main() -> None:
    print("period,state,perceived_state,growth")
    for row in simulate():
        print(",".join(map(str, row)))


if __name__ == "__main__":
    main()
