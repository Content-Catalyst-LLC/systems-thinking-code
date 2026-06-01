CREATE TABLE IF NOT EXISTS edges (
  edge_id INTEGER PRIMARY KEY,
  source_node TEXT NOT NULL,
  target_node TEXT NOT NULL,
  relationship_type TEXT NOT NULL,
  weight REAL NOT NULL
);
