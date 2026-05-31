CREATE TABLE IF NOT EXISTS externalized_burdens (
  period INTEGER NOT NULL,
  actor_group TEXT NOT NULL,
  burden_type TEXT NOT NULL,
  burden_score REAL NOT NULL,
  PRIMARY KEY (period, actor_group, burden_type)
);
