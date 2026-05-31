CREATE TABLE IF NOT EXISTS scenario_definitions (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    description TEXT,
    time_horizon_years INTEGER NOT NULL
);
