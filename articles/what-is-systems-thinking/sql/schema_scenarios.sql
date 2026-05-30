CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    resource_multiplier REAL NOT NULL,
    demand_multiplier REAL NOT NULL,
    delay_multiplier REAL NOT NULL,
    shock_period INTEGER DEFAULT 0,
    shock_size REAL DEFAULT 0
);
