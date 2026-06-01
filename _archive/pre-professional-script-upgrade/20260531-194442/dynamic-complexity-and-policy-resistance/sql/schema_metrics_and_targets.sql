CREATE TABLE IF NOT EXISTS metrics_and_targets (
  metric_id TEXT PRIMARY KEY,
  metric_name TEXT NOT NULL,
  target_behavior TEXT NOT NULL,
  gaming_risk TEXT NOT NULL,
  system_health_proxy TEXT NOT NULL
);
