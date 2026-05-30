CREATE TABLE IF NOT EXISTS model_runs (
    run_id TEXT PRIMARY KEY,
    scenario_id TEXT,
    model_name TEXT NOT NULL,
    model_version TEXT,
    assumptions TEXT,
    run_timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
    output_path TEXT,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(scenario_id)
);
