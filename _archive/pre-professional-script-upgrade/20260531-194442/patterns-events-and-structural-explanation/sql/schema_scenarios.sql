CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    capacity_multiplier REAL NOT NULL,
    backlog_multiplier REAL NOT NULL,
    trust_repair_rate REAL NOT NULL,
    shock_period INTEGER NOT NULL,
    shock_size REAL NOT NULL
);
