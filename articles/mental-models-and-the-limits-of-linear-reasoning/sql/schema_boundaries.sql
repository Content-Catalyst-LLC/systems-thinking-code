CREATE TABLE IF NOT EXISTS boundaries (
  boundary_id TEXT PRIMARY KEY,
  model_id TEXT REFERENCES mental_models(model_id),
  included_elements TEXT,
  excluded_elements TEXT,
  ethical_risk_score REAL
);
