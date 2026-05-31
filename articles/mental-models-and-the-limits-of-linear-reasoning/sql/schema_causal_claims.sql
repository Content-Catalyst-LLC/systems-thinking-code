CREATE TABLE IF NOT EXISTS causal_claims (
  claim_id TEXT PRIMARY KEY,
  model_id TEXT REFERENCES mental_models(model_id),
  cause TEXT,
  effect TEXT,
  polarity TEXT,
  delay TEXT,
  claim_type TEXT
);
