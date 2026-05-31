CREATE TABLE IF NOT EXISTS teams (
  team_id TEXT PRIMARY KEY,
  team_name TEXT NOT NULL,
  function TEXT NOT NULL,
  baseline_capacity REAL NOT NULL,
  starting_trust REAL NOT NULL,
  starting_memory REAL NOT NULL
);
