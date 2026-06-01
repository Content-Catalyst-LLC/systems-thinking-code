PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS model_runs (
  run_id INTEGER PRIMARY KEY,
  scenario TEXT NOT NULL,
  period INTEGER NOT NULL,
  drift_index REAL NOT NULL,
  feedback_bias_index REAL NOT NULL,
  group_a_error REAL NOT NULL,
  group_b_error REAL NOT NULL,
  automation_burden REAL NOT NULL,
  governance_readiness REAL NOT NULL,
  ai_system_risk REAL NOT NULL,
  public_trust REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS governance_controls (
  control_id INTEGER PRIMARY KEY,
  control_name TEXT NOT NULL,
  control_category TEXT NOT NULL,
  implementation_strength REAL NOT NULL CHECK (implementation_strength BETWEEN 0 AND 100),
  notes TEXT
);

CREATE TABLE IF NOT EXISTS incidents (
  incident_id INTEGER PRIMARY KEY,
  scenario TEXT NOT NULL,
  incident_type TEXT NOT NULL,
  affected_group TEXT NOT NULL,
  severity REAL NOT NULL CHECK (severity BETWEEN 0 AND 100),
  remedy_status TEXT NOT NULL
);
