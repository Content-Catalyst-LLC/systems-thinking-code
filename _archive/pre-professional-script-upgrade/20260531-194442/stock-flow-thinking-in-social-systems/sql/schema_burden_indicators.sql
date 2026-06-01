CREATE TABLE IF NOT EXISTS burden_indicators (
    indicator_id TEXT PRIMARY KEY,
    indicator_name TEXT NOT NULL,
    unit TEXT,
    baseline_value REAL,
    description TEXT
);
