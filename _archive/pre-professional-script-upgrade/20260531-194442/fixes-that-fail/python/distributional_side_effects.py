#!/usr/bin/env python3
"""Estimate who bears delayed side effects from quick fixes."""
from __future__ import annotations

GROUPS = {
    "frontline_staff": {"exposure": 0.85, "buffer": 0.35},
    "low_buffer_households": {"exposure": 0.75, "buffer": 0.20},
    "high_buffer_households": {"exposure": 0.35, "buffer": 0.80},
    "future_residents": {"exposure": 0.65, "buffer": 0.40},
}


def burden_score(exposure: float, buffer: float, consequence: float = 0.70) -> float:
    return consequence * exposure * (1.0 - buffer)


def main() -> None:
    for group, vals in GROUPS.items():
        score = burden_score(vals["exposure"], vals["buffer"])
        print(f"{group}: delayed_side_effect_burden={score:.3f}")


if __name__ == "__main__":
    main()
