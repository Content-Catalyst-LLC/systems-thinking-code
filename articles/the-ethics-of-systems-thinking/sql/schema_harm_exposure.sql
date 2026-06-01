CREATE TABLE IF NOT EXISTS harm_exposure (
  group_id TEXT PRIMARY KEY,
  group_name TEXT NOT NULL,
  exposure_score REAL CHECK (exposure_score BETWEEN 0 AND 100),
  protection_score REAL CHECK (protection_score BETWEEN 0 AND 100),
  cumulative_burden REAL CHECK (cumulative_burden BETWEEN 0 AND 100),
  notes TEXT
);
