"""Toy delayed-response model for leverage-point timing analysis."""
from __future__ import annotations


def simulate(delay: int, correction_strength: float, periods: int = 20) -> list[float]:
    goal = 50.0
    values = [80.0] * (delay + 1)
    for t in range(periods):
        perceived = values[-delay - 1]
        correction = correction_strength * (goal - perceived)
        values.append(values[-1] + correction)
    return values[delay + 1 :]


if __name__ == "__main__":
    for d in [1, 3, 6]:
        series = simulate(delay=d, correction_strength=0.25)
        print(f"delay={d}", [round(x, 2) for x in series[:8]])
