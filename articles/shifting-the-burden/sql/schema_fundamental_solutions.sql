CREATE TABLE IF NOT EXISTS fundamental_solutions (
  period INTEGER NOT NULL,
  solution_name TEXT NOT NULL,
  investment REAL NOT NULL,
  repair_effect REAL NOT NULL,
  implementation_delay INTEGER NOT NULL,
  PRIMARY KEY (period, solution_name)
);
