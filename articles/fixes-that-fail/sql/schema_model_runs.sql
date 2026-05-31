CREATE TABLE IF NOT EXISTS model_runs (
    run_id INTEGER NOT NULL,
    scenario TEXT NOT NULL,
    period INTEGER NOT NULL,
    symptom_level REAL NOT NULL,
    capacity_stock REAL NOT NULL,
    delayed_consequence REAL NOT NULL,
    dependency_ratio REAL NOT NULL,
    PRIMARY KEY (run_id, scenario, period)
);
