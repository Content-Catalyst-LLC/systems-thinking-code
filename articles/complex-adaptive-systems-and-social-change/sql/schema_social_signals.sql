CREATE TABLE IF NOT EXISTS social_signals (
  signal_id TEXT PRIMARY KEY,
  period INTEGER NOT NULL,
  signal_type TEXT NOT NULL,
  reach_score REAL CHECK (reach_score BETWEEN 0 AND 100),
  trust_score REAL CHECK (trust_score BETWEEN 0 AND 100),
  legitimacy_score REAL CHECK (legitimacy_score BETWEEN 0 AND 100),
  notes TEXT
);
