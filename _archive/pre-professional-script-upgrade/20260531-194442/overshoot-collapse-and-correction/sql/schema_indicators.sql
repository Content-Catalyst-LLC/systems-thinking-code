CREATE TABLE IF NOT EXISTS indicators (
  month INTEGER NOT NULL,
  domain TEXT NOT NULL,
  pressure REAL NOT NULL,
  stock_level REAL NOT NULL,
  buffer_level REAL NOT NULL,
  early_warning_signal REAL NOT NULL,
  collapse_risk REAL NOT NULL,
  PRIMARY KEY (month, domain)
);
