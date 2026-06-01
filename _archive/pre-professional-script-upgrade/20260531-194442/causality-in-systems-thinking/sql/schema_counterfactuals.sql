CREATE TABLE IF NOT EXISTS counterfactuals (
    counterfactual_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    resource_multiplier REAL,
    demand_multiplier REAL,
    delay_multiplier REAL,
    backlog_reduction REAL,
    threshold_level REAL
);
