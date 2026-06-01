CREATE TABLE IF NOT EXISTS system_flows (
  flow_id TEXT PRIMARY KEY,
  flow_name TEXT NOT NULL,
  source_stock_id TEXT REFERENCES system_stocks(stock_id),
  target_stock_id TEXT REFERENCES system_stocks(stock_id),
  flow_equation TEXT,
  unit TEXT,
  notes TEXT
);
