CREATE TABLE IF NOT EXISTS model_runs (
    run_id TEXT PRIMARY KEY,
    scenario TEXT,
    administrative_burden REAL,
    trust_stock REAL,
    coordination_density REAL,
    institutional_capacity REAL,
    feedback_closure REAL,
    public_value_score REAL
);
