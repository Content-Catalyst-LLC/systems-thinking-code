CREATE TABLE IF NOT EXISTS assumptions (
  assumption_id TEXT PRIMARY KEY,
  model_id TEXT REFERENCES mental_models(model_id),
  assumption_text TEXT NOT NULL,
  confidence REAL,
  disconfirming_signal TEXT,
  revision_priority TEXT
);
