"""Overshoot simulation for systems-thinking examples."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"


@dataclass
class OvershootState:
    month: int
    pressure: float
    stock: float
    buffer: float
    collapse_risk: float


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def simulate(months: int = 36, growth_rate: float = 0.07, feedback_delay: int = 6, correction_strength: float = 0.35) -> list[OvershootState]:
    states: list[OvershootState] = []
    pressure = 0.42
    stock = 0.78
    buffer = 0.66
    safe_limit = 0.58
    history: list[float] = [pressure]

    for month in range(months + 1):
        delayed_pressure = history[max(0, len(history) - feedback_delay - 1)]
        correction = max(0.0, delayed_pressure - safe_limit) * correction_strength
        pressure = clamp(pressure + growth_rate * pressure - correction)
        depletion = max(0.0, pressure - safe_limit) * 0.08
        stock = clamp(stock - depletion + 0.015)
        buffer = clamp(buffer - depletion * 0.7 + 0.01)
        collapse_risk = clamp((pressure * 0.45) + ((1 - stock) * 0.35) + ((1 - buffer) * 0.20))
        states.append(OvershootState(month, pressure, stock, buffer, collapse_risk))
        history.append(pressure)
    return states


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = simulate()
    out_path = OUT / "overshoot_simulation.csv"
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["month", "pressure", "stock", "buffer", "collapse_risk"])
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
