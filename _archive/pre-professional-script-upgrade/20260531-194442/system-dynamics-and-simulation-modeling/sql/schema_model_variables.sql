CREATE TABLE IF NOT EXISTS model_variables (
    variable_id TEXT PRIMARY KEY,
    variable_name TEXT NOT NULL,
    variable_type TEXT NOT NULL CHECK (variable_type IN ('stock','flow','auxiliary','parameter')),
    unit TEXT,
    description TEXT
);
