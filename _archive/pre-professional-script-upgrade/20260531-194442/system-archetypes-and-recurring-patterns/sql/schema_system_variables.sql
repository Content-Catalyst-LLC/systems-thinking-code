CREATE TABLE IF NOT EXISTS system_variables (
    variable_id TEXT PRIMARY KEY,
    variable_name TEXT NOT NULL,
    variable_type TEXT NOT NULL,
    unit TEXT,
    description TEXT
);
