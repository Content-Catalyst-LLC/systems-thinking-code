CREATE TABLE IF NOT EXISTS model_runs (
    run_id TEXT PRIMARY KEY,
    scenario_id TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    model_name TEXT,
    notes TEXT,
    FOREIGN KEY(scenario_id) REFERENCES policy_scenarios(scenario_id)
);
