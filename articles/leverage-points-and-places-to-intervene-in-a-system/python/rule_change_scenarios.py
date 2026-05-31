"""Compare shallow parameter adjustment with deeper rule-change scenario."""
from __future__ import annotations

scenarios = {
    "parameter_only": {"burden": -0.05, "trust": 0.02, "access": 0.03},
    "rule_change": {"burden": -0.32, "trust": 0.12, "access": 0.20},
    "goal_and_rule_change": {"burden": -0.42, "trust": 0.24, "access": 0.30},
}

for name, values in scenarios.items():
    score = sum(values.values())
    print(f"{name}: composite={score:.2f}, details={values}")
