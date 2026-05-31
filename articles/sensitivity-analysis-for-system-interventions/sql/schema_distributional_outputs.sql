CREATE TABLE IF NOT EXISTS distributional_outputs (
    output_id INTEGER PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    outcome_name TEXT NOT NULL,
    outcome_value REAL NOT NULL,
    sensitivity_flag TEXT
);
