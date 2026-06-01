CREATE TABLE IF NOT EXISTS model_parameters (
    parameter_name TEXT PRIMARY KEY,
    baseline_value REAL NOT NULL,
    min_value REAL,
    max_value REAL,
    unit TEXT,
    description TEXT
);
