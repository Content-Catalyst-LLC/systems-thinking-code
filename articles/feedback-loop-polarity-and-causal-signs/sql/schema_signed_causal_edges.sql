CREATE TABLE IF NOT EXISTS signed_causal_edges (
  edge_id TEXT PRIMARY KEY,
  source_variable TEXT NOT NULL,
  target_variable TEXT NOT NULL,
  sign TEXT NOT NULL CHECK (sign IN ('+', '-')),
  delay TEXT CHECK (delay IN ('none', 'short', 'medium', 'long')),
  mechanism TEXT,
  confidence TEXT
);
