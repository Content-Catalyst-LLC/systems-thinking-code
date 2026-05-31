CREATE TABLE IF NOT EXISTS scenarios (
  scenario TEXT PRIMARY KEY,
  description TEXT,
  growth_rate REAL,
  constraint_capacity REAL,
  delay INTEGER,
  regeneration_rate REAL,
  policy_note TEXT
);
