CREATE TABLE IF NOT EXISTS system_metrics (
  metric_id TEXT PRIMARY KEY,
  metric_name TEXT NOT NULL,
  domain TEXT NOT NULL,
  metric_type TEXT NOT NULL,
  related_goal TEXT,
  warning TEXT
);
