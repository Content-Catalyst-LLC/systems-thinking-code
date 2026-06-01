CREATE TABLE IF NOT EXISTS resource_stocks (
  year INTEGER PRIMARY KEY,
  resource_stock REAL NOT NULL,
  regeneration REAL NOT NULL,
  extraction REAL NOT NULL,
  capacity_stock REAL,
  degradation REAL,
  capacity_investment REAL
);
