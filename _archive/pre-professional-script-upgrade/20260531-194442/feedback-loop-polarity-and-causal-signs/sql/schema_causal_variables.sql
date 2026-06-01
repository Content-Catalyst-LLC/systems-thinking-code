CREATE TABLE IF NOT EXISTS causal_variables (
  variable_id TEXT PRIMARY KEY,
  variable_name TEXT NOT NULL,
  domain TEXT,
  description TEXT,
  unit_hint TEXT
);
