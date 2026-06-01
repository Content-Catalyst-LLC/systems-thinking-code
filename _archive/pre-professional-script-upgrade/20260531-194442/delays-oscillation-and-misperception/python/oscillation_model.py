"""Oscillation model caused by delayed correction."""

from __future__ import annotations


def run(periods: int = 30, goal: float = 100.0, initial: float = 40.0, delay: int = 4, gain: float = 0.55):
    values = [initial] * (delay + 1)
    rows = []

    for t in range(periods):
        observed = values[-delay]
        error = goal - observed
        next_value = values[-1] + gain * error
        values.append(next_value)
        rows.append((t + 1, round(next_value, 2), round(observed, 2), round(error, 2)))

    return rows


def main() -> None:
    print("period,value,delayed_observation,error")
    for row in run():
        print(",".join(map(str, row)))


if __name__ == "__main__":
    main()
