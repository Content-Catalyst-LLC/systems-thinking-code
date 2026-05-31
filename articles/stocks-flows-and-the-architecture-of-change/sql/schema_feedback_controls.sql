CREATE TABLE IF NOT EXISTS feedback_controls (
  control_id TEXT PRIMARY KEY,
  flow_id TEXT NOT NULL,
  controlled_by TEXT NOT NULL,
  polarity TEXT NOT NULL CHECK (polarity IN ('positive', 'negative')),
  delay_periods INTEGER DEFAULT 0,
  description TEXT,
  FOREIGN KEY (flow_id) REFERENCES system_flows(flow_id)
);
