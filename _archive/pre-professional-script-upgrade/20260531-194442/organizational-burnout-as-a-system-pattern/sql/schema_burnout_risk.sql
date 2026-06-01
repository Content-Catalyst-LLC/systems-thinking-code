CREATE TABLE IF NOT EXISTS burnout_risk (
  period INTEGER NOT NULL,
  role_id TEXT NOT NULL,
  exhaustion_score REAL,
  cynicism_score REAL,
  efficacy_loss_score REAL,
  reported_stress REAL,
  quality_risk REAL,
  PRIMARY KEY (period, role_id)
);
