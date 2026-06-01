CREATE TABLE IF NOT EXISTS model_runs (
    run_id TEXT PRIMARY KEY,
    scenario_id TEXT,
    model_name TEXT,
    run_timestamp TEXT,
    notes TEXT
);
