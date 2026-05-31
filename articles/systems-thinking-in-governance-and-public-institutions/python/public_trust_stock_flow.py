from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
trust_stock = 0.50
for row in read_csv("synthetic_trust_indicators.csv"):
    gains = (f(row, "reliability") + f(row, "fairness") + f(row, "accountability")) / 3
    losses = (f(row, "harm") + f(row, "burden") + f(row, "opacity")) / 3
    trust_stock = max(0.0, min(1.0, trust_stock + 0.20 * gains - 0.16 * losses))
    rows.append({
        "period": row["period"],
        "domain": row["domain"],
        "observed_trust_score": row["trust_score"],
        "modeled_trust_stock": round(trust_stock, 3),
        "trust_gain_driver": round(gains, 3),
        "trust_loss_driver": round(losses, 3),
    })

write_csv("public_trust_stock_flow.csv", rows)
