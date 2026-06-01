CREATE TABLE IF NOT EXISTS parameter_ranges (
    range_id INTEGER PRIMARY KEY,
    parameter_name TEXT NOT NULL,
    low_value REAL NOT NULL,
    high_value REAL NOT NULL,
    range_source TEXT,
    rationale TEXT
);
