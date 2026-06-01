CREATE TABLE IF NOT EXISTS delay_variables (
    variable_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    unit TEXT,
    initial_value REAL
);
