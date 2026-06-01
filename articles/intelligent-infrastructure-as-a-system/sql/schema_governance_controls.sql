CREATE TABLE IF NOT EXISTS governance_controls (
  control_id TEXT PRIMARY KEY,
  control_area TEXT NOT NULL,
  control_name TEXT NOT NULL,
  control_strength REAL CHECK (control_strength BETWEEN 0 AND 100),
  accountable_party TEXT,
  review_frequency TEXT,
  notes TEXT
);
