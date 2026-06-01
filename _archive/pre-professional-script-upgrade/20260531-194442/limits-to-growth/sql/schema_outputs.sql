CREATE TABLE IF NOT EXISTS outputs (
  scenario TEXT PRIMARY KEY,
  final_scale REAL,
  minimum_quality REAL,
  remaining_resource REAL,
  overshoot_flag BOOLEAN,
  distributional_risk TEXT
);
