from __future__ import annotations

from _common import write_csv

memory = 0.52
rows = []
for period in range(1, 9):
    learning = 0.055 + 0.01 * period
    documentation = 0.045 + 0.005 * period
    sharing = 0.035
    turnover_loss = 0.05 if period in {2, 5, 7} else 0.025
    forgetting = 0.028
    obsolescence = 0.018
    memory = max(0.0, min(1.0, memory + learning + documentation + sharing - turnover_loss - forgetting - obsolescence))
    rows.append({
        "period": period,
        "learning": round(learning, 3),
        "documentation": round(documentation, 3),
        "sharing": round(sharing, 3),
        "turnover_loss": round(turnover_loss, 3),
        "forgetting": forgetting,
        "obsolescence": obsolescence,
        "memory_stock": round(memory, 3),
    })

write_csv("memory_stock_flow_model.csv", rows)
