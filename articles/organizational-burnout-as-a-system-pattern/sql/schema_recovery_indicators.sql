CREATE TABLE IF NOT EXISTS recovery_indicators (
  period INTEGER NOT NULL,
  role_id TEXT NOT NULL,
  protected_focus_hours REAL,
  recovery_hours REAL,
  training_hours REAL,
  peer_support_score REAL,
  autonomy_score REAL,
  PRIMARY KEY (period, role_id)
);
