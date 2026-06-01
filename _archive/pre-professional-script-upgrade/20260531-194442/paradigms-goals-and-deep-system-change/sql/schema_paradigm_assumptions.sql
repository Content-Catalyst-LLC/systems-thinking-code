CREATE TABLE IF NOT EXISTS paradigm_assumptions (
  paradigm_id TEXT PRIMARY KEY,
  paradigm_name TEXT NOT NULL,
  assumption TEXT NOT NULL,
  possible_risk TEXT
);
