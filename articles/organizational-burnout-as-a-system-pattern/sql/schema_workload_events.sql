CREATE TABLE IF NOT EXISTS workload_events (
  period INTEGER NOT NULL,
  role_id TEXT NOT NULL,
  visible_workload REAL,
  meeting_load REAL,
  interruptions REAL,
  rework_hours REAL,
  urgent_requests REAL,
  capacity_index REAL,
  PRIMARY KEY (period, role_id)
);
