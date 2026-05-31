CREATE TABLE IF NOT EXISTS model_runs (
    run_id TEXT PRIMARY KEY,
    scenario_id TEXT,
    run_timestamp TEXT,
    model_name TEXT,
    assumptions TEXT,
    output_path TEXT,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(scenario_id)
);
