"""Lightweight validation checks for synthetic system dynamics models."""

from __future__ import annotations

from system_dynamics_baseline_model import Parameters, simulate


def check_nonnegative_stocks() -> None:
    rows = simulate(Parameters())
    for row in rows:
        assert row["backlog"] >= 0, "Backlog should never be negative"
        assert row["staff_capacity"] >= 0, "Staff capacity should never be negative"
        assert 0 <= row["public_trust"] <= 100, "Trust should stay on 0-100 scale"


def check_extreme_capacity() -> None:
    rows = simulate(Parameters(initial_staff=200, months=12))
    assert rows[-1]["backlog"] < rows[0]["backlog"], "High capacity should reduce backlog in this synthetic model"


if __name__ == "__main__":
    check_nonnegative_stocks()
    check_extreme_capacity()
    print("Validation checks passed.")
