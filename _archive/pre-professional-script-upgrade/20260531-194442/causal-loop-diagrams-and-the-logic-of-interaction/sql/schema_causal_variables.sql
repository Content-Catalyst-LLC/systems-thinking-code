CREATE TABLE IF NOT EXISTS causal_variables (
    variable_id TEXT PRIMARY KEY,
    variable_name TEXT NOT NULL,
    domain TEXT,
    variable_type TEXT,
    description TEXT,
    unit_or_scale TEXT
);
