CREATE TABLE IF NOT EXISTS workload_events (
  period INTEGER NOT NULL,
  team_id TEXT NOT NULL,
  new_work REAL NOT NULL,
  urgent_work REAL NOT NULL,
  rework REAL NOT NULL,
  meetings_hours REAL NOT NULL,
  PRIMARY KEY (period, team_id)
);
