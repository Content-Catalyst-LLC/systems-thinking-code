CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    trigger_period INTEGER,
    trigger_size REAL,
    capacity_investment REAL,
    trust_repair REAL,
    adaptive_investment REAL
);
