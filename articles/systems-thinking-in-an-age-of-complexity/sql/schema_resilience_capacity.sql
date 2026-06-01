CREATE TABLE IF NOT EXISTS resilience_capacity (
  domain TEXT PRIMARY KEY,
  redundancy REAL CHECK (redundancy BETWEEN 0 AND 1),
  modularity REAL CHECK (modularity BETWEEN 0 AND 1),
  learning_capacity REAL CHECK (learning_capacity BETWEEN 0 AND 1),
  response_variety REAL CHECK (response_variety BETWEEN 0 AND 1),
  trust REAL CHECK (trust BETWEEN 0 AND 1),
  diagnostic TEXT
);
