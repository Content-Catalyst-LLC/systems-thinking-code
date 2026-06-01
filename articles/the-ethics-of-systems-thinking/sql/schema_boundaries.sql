CREATE TABLE IF NOT EXISTS boundary_cases (
  case_id TEXT PRIMARY KEY,
  domain TEXT NOT NULL,
  consequences_experienced REAL,
  consequences_counted REAL,
  excluded_consequence TEXT,
  boundary_question TEXT
);
