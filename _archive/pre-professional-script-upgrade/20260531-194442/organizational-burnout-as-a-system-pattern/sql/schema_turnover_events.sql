CREATE TABLE IF NOT EXISTS turnover_events (
  period INTEGER NOT NULL,
  role_id TEXT NOT NULL,
  open_positions INTEGER,
  departures INTEGER,
  onboarding_hours REAL,
  knowledge_loss_index REAL,
  remaining_staff_load_increase REAL,
  PRIMARY KEY (period, role_id)
);
