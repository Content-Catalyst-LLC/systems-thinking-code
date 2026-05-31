CREATE TABLE IF NOT EXISTS capacity_investments (
  scenario TEXT NOT NULL,
  year INTEGER NOT NULL,
  investment_level REAL NOT NULL,
  implementation_delay INTEGER NOT NULL,
  expected_capacity_gain REAL,
  PRIMARY KEY (scenario, year)
);
