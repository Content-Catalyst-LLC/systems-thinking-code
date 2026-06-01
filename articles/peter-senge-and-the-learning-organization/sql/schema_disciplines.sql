CREATE TABLE IF NOT EXISTS learning_disciplines (
  discipline_id TEXT PRIMARY KEY,
  discipline_name TEXT NOT NULL,
  baseline_score REAL CHECK (baseline_score BETWEEN 0 AND 100),
  target_score REAL CHECK (target_score BETWEEN 0 AND 100),
  diagnostic_question TEXT
);
