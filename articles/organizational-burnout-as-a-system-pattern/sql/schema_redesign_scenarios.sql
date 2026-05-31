CREATE TABLE IF NOT EXISTS redesign_scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  workload_reduction REAL,
  capacity_increase REAL,
  recovery_increase REAL,
  rework_reduction REAL,
  hidden_labor_visibility REAL,
  expected_burnout_reduction REAL
);
