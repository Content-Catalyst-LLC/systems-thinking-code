CREATE TABLE IF NOT EXISTS constraints (
  constraint_id TEXT PRIMARY KEY,
  constraint_name TEXT NOT NULL,
  constraint_type TEXT NOT NULL,
  initial_capacity REAL,
  warning_indicator TEXT,
  ethical_question TEXT
);
