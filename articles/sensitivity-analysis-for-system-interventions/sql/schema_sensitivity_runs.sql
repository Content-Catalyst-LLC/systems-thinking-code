CREATE TABLE IF NOT EXISTS sensitivity_runs (
    run_id INTEGER PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    varied_parameter TEXT NOT NULL,
    varied_value REAL NOT NULL,
    outcome_name TEXT NOT NULL,
    outcome_value REAL NOT NULL
);
