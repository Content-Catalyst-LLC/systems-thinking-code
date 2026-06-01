"""Synthetic policy delay simulation showing consequences of delayed capacity investment."""
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
rows = []
for delay in [0, 2, 5, 8]:
    backlog = 100.0
    capacity = 45.0
    for year in range(0, 16):
        if year >= delay:
            capacity += 2.0
        backlog = max(0, backlog + 8.0 - capacity * 0.15)
        rows.append({"delay_years": delay, "year": year, "capacity": round(capacity, 2), "backlog": round(backlog, 2)})
with (OUT / "policy_delay_simulation.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=["delay_years", "year", "capacity", "backlog"])
    writer.writeheader(); writer.writerows(rows)
print(f"Wrote {OUT / 'policy_delay_simulation.csv'}")
