CREATE TABLE IF NOT EXISTS intervention_scenarios (
  scenario TEXT PRIMARY KEY,
  description TEXT NOT NULL,
  performance_weight REAL NOT NULL,
  need_weight REAL NOT NULL,
  improvement_weight REAL NOT NULL,
  network_weight REAL NOT NULL,
  capacity_building_pool REAL NOT NULL
);
