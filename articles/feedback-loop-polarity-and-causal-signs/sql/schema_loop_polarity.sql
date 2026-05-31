CREATE TABLE IF NOT EXISTS loop_polarity (
  loop_id TEXT PRIMARY KEY,
  negative_edge_count INTEGER NOT NULL,
  loop_polarity TEXT NOT NULL CHECK (loop_polarity IN ('reinforcing', 'balancing'))
);
