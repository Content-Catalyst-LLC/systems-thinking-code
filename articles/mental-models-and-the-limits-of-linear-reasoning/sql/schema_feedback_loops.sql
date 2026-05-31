CREATE TABLE IF NOT EXISTS feedback_loops (
  loop_id TEXT PRIMARY KEY,
  loop_name TEXT NOT NULL,
  domain TEXT,
  loop_type TEXT,
  description TEXT,
  delay_strength REAL,
  learning_priority TEXT
);
