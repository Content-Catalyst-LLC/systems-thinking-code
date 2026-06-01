CREATE TABLE IF NOT EXISTS failure_events (
  event_id INTEGER PRIMARY KEY,
  scenario_id TEXT NOT NULL,
  step INTEGER NOT NULL,
  failed_node TEXT NOT NULL,
  service_loss_index REAL
);
