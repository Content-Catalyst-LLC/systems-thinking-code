CREATE TABLE IF NOT EXISTS resource_allocations (
  scenario TEXT NOT NULL,
  actor_id TEXT NOT NULL,
  period INTEGER NOT NULL,
  performance_score REAL NOT NULL,
  need_score REAL NOT NULL,
  resource_award REAL NOT NULL,
  allocation_rule TEXT NOT NULL
);
