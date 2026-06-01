CREATE TABLE IF NOT EXISTS redesign_scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  capacity_investment REAL NOT NULL,
  feedback_quality_gain REAL NOT NULL,
  workload_reduction REAL NOT NULL,
  memory_embedding_gain REAL NOT NULL,
  expected_burden_reduction REAL NOT NULL
);
