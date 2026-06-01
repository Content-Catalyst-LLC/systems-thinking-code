CREATE TABLE IF NOT EXISTS stock_flow_observations (
  observation_id INTEGER PRIMARY KEY,
  stock_id TEXT NOT NULL,
  period INTEGER NOT NULL,
  stock_value REAL NOT NULL,
  inflow_value REAL,
  outflow_value REAL,
  FOREIGN KEY (stock_id) REFERENCES system_stocks(stock_id)
);
