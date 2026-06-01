CREATE TABLE IF NOT EXISTS delays (
  delay_id TEXT PRIMARY KEY,
  delay_type TEXT NOT NULL,
  delay_periods INTEGER NOT NULL,
  affected_stock_or_flow TEXT,
  risk_if_ignored TEXT
);
