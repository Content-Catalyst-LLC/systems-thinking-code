CREATE TABLE IF NOT EXISTS time_series_indicators (
  indicator_id INTEGER PRIMARY KEY AUTOINCREMENT,
  year INTEGER NOT NULL,
  indicator_name TEXT NOT NULL,
  indicator_value REAL NOT NULL,
  unit TEXT,
  system_area TEXT
);
