CREATE TABLE IF NOT EXISTS outputs (
    output_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    metric_name TEXT NOT NULL,
    metric_value REAL,
    interpretation TEXT
);
