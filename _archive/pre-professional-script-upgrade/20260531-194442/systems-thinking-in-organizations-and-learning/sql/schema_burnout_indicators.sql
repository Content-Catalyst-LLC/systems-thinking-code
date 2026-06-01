CREATE TABLE IF NOT EXISTS burnout_indicators (
  period INTEGER NOT NULL,
  team_id TEXT NOT NULL,
  overtime_hours REAL NOT NULL,
  recovery_hours REAL NOT NULL,
  turnover_risk REAL NOT NULL,
  error_rate REAL NOT NULL,
  psychological_safety REAL NOT NULL,
  PRIMARY KEY (period, team_id)
);
