CREATE TABLE IF NOT EXISTS simulation_runs (
    run_id TEXT PRIMARY KEY,
    scenario_id TEXT NOT NULL,
    run_date TEXT,
    model_version TEXT,
    time_horizon_months INTEGER,
    status TEXT,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(scenario_id)
);
