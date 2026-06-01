CREATE TABLE IF NOT EXISTS causal_relationships (
  relationship_id INTEGER PRIMARY KEY AUTOINCREMENT,
  source_variable TEXT NOT NULL,
  target_variable TEXT NOT NULL,
  polarity TEXT CHECK (polarity IN ('positive', 'negative')),
  mechanism TEXT
);
