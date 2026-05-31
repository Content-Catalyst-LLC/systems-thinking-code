CREATE TABLE IF NOT EXISTS sensitivity_parameters (
    parameter_id INTEGER PRIMARY KEY,
    parameter_name TEXT NOT NULL,
    description TEXT,
    baseline_value REAL NOT NULL,
    unit TEXT,
    notes TEXT
);
