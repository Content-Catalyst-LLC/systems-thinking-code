#!/usr/bin/env python3
"""Show how repeated fixes can deplete fundamental capacity."""
from __future__ import annotations


def update_capacity(capacity: float, quick_fix: float, repair: float) -> float:
    return max(0.0, min(1.5, capacity + 0.08 * repair - 0.07 * quick_fix))


def main() -> None:
    capacity = 1.0
    for t in range(10):
        quick_fix = 0.75 if t < 6 else 0.35
        repair = 0.10 if t < 6 else 0.80
        capacity = update_capacity(capacity, quick_fix, repair)
        print(f"period={t}, quick_fix={quick_fix:.2f}, repair={repair:.2f}, capacity={capacity:.3f}")


if __name__ == "__main__":
    main()
