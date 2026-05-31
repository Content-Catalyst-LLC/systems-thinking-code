CREATE TABLE IF NOT EXISTS mental_models (
  model_id TEXT PRIMARY KEY,
  model_name TEXT NOT NULL,
  domain TEXT NOT NULL,
  dominant_assumption TEXT,
  linear_score REAL,
  feedback_score REAL,
  boundary_score REAL,
  power_awareness_score REAL
);
