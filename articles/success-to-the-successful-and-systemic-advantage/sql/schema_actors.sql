CREATE TABLE IF NOT EXISTS actors (
  actor_id TEXT PRIMARY KEY,
  actor_name TEXT NOT NULL,
  actor_group TEXT NOT NULL,
  domain TEXT NOT NULL,
  initial_advantage REAL NOT NULL,
  initial_capacity REAL NOT NULL,
  need_score REAL NOT NULL,
  network_connections INTEGER NOT NULL
);
