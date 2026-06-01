CREATE TABLE IF NOT EXISTS actor_responses (
  actor_group TEXT NOT NULL,
  response_type TEXT NOT NULL,
  response_strength REAL NOT NULL,
  likely_effect TEXT NOT NULL,
  notes TEXT
);
