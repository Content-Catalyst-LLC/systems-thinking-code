CREATE TABLE IF NOT EXISTS advantage_metrics (
  actor_id TEXT NOT NULL,
  period INTEGER NOT NULL,
  advantage_index REAL NOT NULL,
  capacity_index REAL NOT NULL,
  visibility_index REAL NOT NULL,
  credibility_index REAL NOT NULL,
  opportunity_index REAL NOT NULL
);
