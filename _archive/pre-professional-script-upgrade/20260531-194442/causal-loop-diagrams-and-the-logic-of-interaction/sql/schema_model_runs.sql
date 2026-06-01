CREATE TABLE IF NOT EXISTS model_runs (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_name TEXT NOT NULL,
    model_type TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
