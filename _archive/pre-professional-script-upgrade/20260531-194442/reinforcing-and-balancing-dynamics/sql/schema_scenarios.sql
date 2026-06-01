CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    growth_rate REAL,
    correction_strength REAL,
    delay INTEGER,
    carrying_capacity REAL
);
