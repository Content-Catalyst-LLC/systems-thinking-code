CREATE TABLE IF NOT EXISTS capacity_stocks (
  period INTEGER PRIMARY KEY,
  capacity_stock REAL NOT NULL,
  trust_stock REAL NOT NULL,
  burden_stock REAL NOT NULL
);
