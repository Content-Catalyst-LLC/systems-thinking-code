CREATE TABLE IF NOT EXISTS outputs (
  scenario_id TEXT PRIMARY KEY,
  projected_pressure_index REAL,
  projected_burnout_risk REAL,
  projected_turnover_risk REAL,
  projected_memory_fragility REAL,
  projected_quality_risk REAL
);
