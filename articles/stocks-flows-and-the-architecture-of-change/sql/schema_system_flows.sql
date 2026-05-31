CREATE TABLE IF NOT EXISTS system_flows (
  flow_id TEXT PRIMARY KEY,
  stock_id TEXT NOT NULL,
  flow_name TEXT NOT NULL,
  flow_type TEXT NOT NULL CHECK (flow_type IN ('inflow', 'outflow')),
  baseline_rate REAL NOT NULL,
  unit_per_period TEXT NOT NULL,
  description TEXT,
  FOREIGN KEY (stock_id) REFERENCES system_stocks(stock_id)
);
