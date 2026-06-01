CREATE TABLE IF NOT EXISTS model_outputs (
  resource_id TEXT NOT NULL,
  scenario TEXT NOT NULL,
  year INTEGER NOT NULL,
  stock REAL,
  use_total REAL,
  regeneration REAL,
  governance_quality REAL,
  externalized_burden REAL
);
