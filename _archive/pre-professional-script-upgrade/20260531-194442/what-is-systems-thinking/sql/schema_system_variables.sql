CREATE TABLE IF NOT EXISTS system_variables (
    variable_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    unit TEXT,
    initial_value REAL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
