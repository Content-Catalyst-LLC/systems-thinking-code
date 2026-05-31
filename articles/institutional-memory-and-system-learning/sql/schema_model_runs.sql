CREATE TABLE IF NOT EXISTS model_runs (
    run_id TEXT PRIMARY KEY,
    scenario TEXT,
    turnover_rate REAL,
    documentation_quality REAL,
    feedback_closure REAL,
    authority_connection REAL,
    projected_memory_score REAL,
    projected_repeat_error_risk REAL
);
