CREATE TABLE IF NOT EXISTS leverage_points (
  leverage_id TEXT PRIMARY KEY,
  leverage_name TEXT NOT NULL,
  leverage_level TEXT NOT NULL,
  relative_depth INTEGER NOT NULL,
  example_intervention TEXT,
  diagnostic_question TEXT
);
