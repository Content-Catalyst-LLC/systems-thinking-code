CREATE TABLE IF NOT EXISTS roles (
  role_id TEXT PRIMARY KEY,
  role_name TEXT NOT NULL,
  function TEXT,
  criticality REAL,
  decision_authority REAL,
  emotional_load REAL,
  hidden_labor_share REAL
);
