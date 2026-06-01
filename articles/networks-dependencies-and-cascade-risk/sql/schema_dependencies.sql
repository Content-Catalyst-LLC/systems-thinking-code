CREATE TABLE IF NOT EXISTS dependencies (
  dependency_id INTEGER PRIMARY KEY,
  dependent_node TEXT NOT NULL,
  provider_node TEXT NOT NULL,
  dependency_weight REAL NOT NULL,
  dependency_type TEXT NOT NULL DEFAULT 'functional'
);
