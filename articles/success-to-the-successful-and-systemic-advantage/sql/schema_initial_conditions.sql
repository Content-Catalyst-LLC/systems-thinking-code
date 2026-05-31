CREATE TABLE IF NOT EXISTS initial_conditions (
  actor_id TEXT NOT NULL,
  starting_resources REAL NOT NULL,
  starting_visibility REAL NOT NULL,
  starting_credibility REAL NOT NULL,
  starting_opportunity REAL NOT NULL,
  context_constraint TEXT NOT NULL
);
