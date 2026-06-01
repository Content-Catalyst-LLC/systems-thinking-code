CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    demand_multiplier REAL,
    capacity_multiplier REAL,
    delay_factor REAL,
    investment_rate REAL,
    shock_period INTEGER,
    shock_size REAL
);
