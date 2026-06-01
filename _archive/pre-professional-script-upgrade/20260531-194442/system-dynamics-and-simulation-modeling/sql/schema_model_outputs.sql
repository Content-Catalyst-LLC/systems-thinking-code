CREATE TABLE IF NOT EXISTS model_outputs (
    output_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL,
    time_month INTEGER NOT NULL,
    variable_name TEXT NOT NULL,
    value REAL NOT NULL,
    unit TEXT,
    FOREIGN KEY (run_id) REFERENCES simulation_runs(run_id)
);
