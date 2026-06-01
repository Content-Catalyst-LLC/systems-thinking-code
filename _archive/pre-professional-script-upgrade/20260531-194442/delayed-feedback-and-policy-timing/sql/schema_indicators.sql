CREATE TABLE IF NOT EXISTS indicators (
  month INTEGER NOT NULL,
  domain TEXT NOT NULL,
  leading_indicator REAL NOT NULL,
  lagging_indicator REAL NOT NULL,
  stock_level REAL NOT NULL,
  policy_pressure REAL NOT NULL
);
