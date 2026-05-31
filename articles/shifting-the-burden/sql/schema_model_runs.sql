CREATE TABLE IF NOT EXISTS model_runs (
  run_id INTEGER PRIMARY KEY,
  scenario TEXT NOT NULL,
  repair_investment REAL NOT NULL,
  symptomatic_reliance REAL NOT NULL,
  final_problem_pressure REAL NOT NULL,
  final_capacity REAL NOT NULL,
  final_dependency REAL NOT NULL
);
