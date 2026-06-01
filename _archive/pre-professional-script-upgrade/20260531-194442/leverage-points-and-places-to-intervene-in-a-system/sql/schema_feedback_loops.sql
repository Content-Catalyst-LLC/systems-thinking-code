CREATE TABLE IF NOT EXISTS feedback_loops (
  loop_id TEXT PRIMARY KEY,
  loop_name TEXT NOT NULL,
  loop_type TEXT CHECK (loop_type IN ('reinforcing','balancing')),
  variables TEXT,
  description TEXT
);
