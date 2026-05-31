CREATE TABLE IF NOT EXISTS symptomatic_solutions (
  period INTEGER NOT NULL,
  solution_name TEXT NOT NULL,
  intensity REAL NOT NULL,
  short_term_relief REAL NOT NULL,
  hidden_side_effect REAL NOT NULL,
  PRIMARY KEY (period, solution_name)
);
