CREATE TABLE IF NOT EXISTS system_stocks (
  stock_id TEXT PRIMARY KEY,
  stock_name TEXT NOT NULL,
  domain TEXT NOT NULL,
  initial_level REAL NOT NULL,
  regeneration_rate REAL NOT NULL,
  critical_threshold REAL NOT NULL,
  measurement_unit TEXT NOT NULL
);
