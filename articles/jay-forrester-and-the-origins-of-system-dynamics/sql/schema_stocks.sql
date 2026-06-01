CREATE TABLE IF NOT EXISTS system_stocks (
  stock_id TEXT PRIMARY KEY,
  stock_name TEXT NOT NULL,
  initial_value REAL NOT NULL,
  unit TEXT,
  lower_bound REAL,
  upper_bound REAL,
  notes TEXT
);
