"""Delayed feedback policy model for systems-thinking examples."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


@dataclass
class PolicyLag:
    policy_id: str
    effect: int
    information: int
    decision: int
    implementation: int
    recovery: int

    @property
    def total_active_lag(self) -> int:
        return self.effect + self.information + self.decision + self.implementation


def read_lags() -> list[PolicyLag]:
    rows: list[PolicyLag] = []
    with (DATA / "feedback_lags.csv").open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                PolicyLag(
                    policy_id=row["policy_id"],
                    effect=int(row["effect_lag_months"]),
                    information=int(row["information_lag_months"]),
                    decision=int(row["decision_lag_months"]),
                    implementation=int(row["implementation_lag_months"]),
                    recovery=int(row["recovery_lag_months"]),
                )
            )
    return rows


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = read_lags()
    with (OUT / "policy_lag_summary.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["policy_id", "total_active_lag_months", "recovery_lag_months"])
        for lag in rows:
            writer.writerow([lag.policy_id, lag.total_active_lag, lag.recovery])
    for lag in rows:
        print(f"{lag.policy_id}: active lag={lag.total_active_lag} months, recovery={lag.recovery} months")


if __name__ == "__main__":
    main()
