CREATE TABLE IF NOT EXISTS system_variables (
    variable_id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    unit TEXT NOT NULL,
    initial_value REAL NOT NULL
);
