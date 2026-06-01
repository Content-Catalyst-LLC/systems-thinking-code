CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    delay_multiplier REAL,
    capacity_investment REAL,
    shock_period INTEGER,
    shock_size REAL
);
