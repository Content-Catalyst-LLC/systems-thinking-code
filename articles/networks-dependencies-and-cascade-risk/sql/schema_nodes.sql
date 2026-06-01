CREATE TABLE IF NOT EXISTS nodes (
  node_id TEXT PRIMARY KEY,
  category TEXT NOT NULL,
  capacity REAL NOT NULL,
  threshold REAL NOT NULL,
  vulnerability REAL NOT NULL,
  recovery_capacity REAL NOT NULL
);
