CREATE TABLE IF NOT EXISTS system_variables (
  variable_id TEXT PRIMARY KEY,
  variable_name TEXT NOT NULL,
  system_domain TEXT,
  variable_type TEXT,
  description TEXT
);
