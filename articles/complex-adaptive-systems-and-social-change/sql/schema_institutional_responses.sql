CREATE TABLE IF NOT EXISTS institutional_responses (
  response_id TEXT PRIMARY KEY,
  period INTEGER NOT NULL,
  institution_name TEXT,
  response_type TEXT NOT NULL,
  response_strength REAL CHECK (response_strength BETWEEN 0 AND 100),
  accountability_quality REAL CHECK (accountability_quality BETWEEN 0 AND 100),
  notes TEXT
);
