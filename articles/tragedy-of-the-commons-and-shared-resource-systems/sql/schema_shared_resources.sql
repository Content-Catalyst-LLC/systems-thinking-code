CREATE TABLE IF NOT EXISTS shared_resources (
  resource_id TEXT PRIMARY KEY,
  resource_name TEXT NOT NULL,
  resource_type TEXT NOT NULL,
  initial_stock REAL NOT NULL,
  carrying_capacity REAL,
  regeneration_rate REAL,
  critical_threshold REAL,
  unit TEXT
);
