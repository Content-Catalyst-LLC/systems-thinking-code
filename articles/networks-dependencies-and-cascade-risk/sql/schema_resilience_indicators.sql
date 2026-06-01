CREATE TABLE IF NOT EXISTS resilience_indicators (
  node_id TEXT PRIMARY KEY,
  redundancy_score REAL,
  diversity_score REAL,
  modularity_score REAL,
  recovery_capacity REAL,
  visibility_score REAL
);
