CREATE TABLE IF NOT EXISTS loop_variables (
    variable_id TEXT PRIMARY KEY,
    variable_name TEXT NOT NULL,
    description TEXT,
    unit TEXT,
    initial_value REAL
);
