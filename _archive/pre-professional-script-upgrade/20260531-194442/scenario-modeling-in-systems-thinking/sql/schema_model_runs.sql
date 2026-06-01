CREATE TABLE IF NOT EXISTS model_runs (
    run_id TEXT PRIMARY KEY,
    scenario_id TEXT NOT NULL,
    model_version TEXT NOT NULL,
    run_timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);
