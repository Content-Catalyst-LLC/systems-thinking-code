CREATE TABLE IF NOT EXISTS feedback_variables (
    variable_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    initial_value REAL,
    unit TEXT
);
