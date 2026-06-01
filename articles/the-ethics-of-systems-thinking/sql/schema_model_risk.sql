CREATE TABLE IF NOT EXISTS model_risks (
  risk_id TEXT PRIMARY KEY,
  risk_type TEXT NOT NULL,
  severity REAL CHECK (severity BETWEEN 0 AND 1),
  likelihood REAL CHECK (likelihood BETWEEN 0 AND 1),
  mitigation TEXT
);
