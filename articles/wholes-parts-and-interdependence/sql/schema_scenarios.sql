CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    shock_part TEXT,
    shock_size REAL NOT NULL,
    redundancy_multiplier REAL NOT NULL,
    coordination_multiplier REAL NOT NULL
);
