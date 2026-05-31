"""One-at-a-time sensitivity analysis for synthetic parameters."""

from __future__ import annotations

from dataclasses import replace
from system_dynamics_baseline_model import Parameters, simulate


def final_backlog(params: Parameters) -> float:
    return simulate(params)[-1]["backlog"]


def sensitivity() -> list[dict[str, float | str]]:
    base = Parameters()
    base_value = final_backlog(base)
    tests = []
    for name, factor in [("demand_growth_rate", 1.25), ("productivity_per_staff", 1.25), ("hiring_rate", 1.25), ("turnover_rate", 1.25)]:
        varied = replace(base, **{name: getattr(base, name) * factor})
        value = final_backlog(varied)
        tests.append({"parameter": name, "base_final_backlog": base_value, "varied_final_backlog": value, "change": value - base_value})
    return tests


if __name__ == "__main__":
    for row in sensitivity():
        print(row)
