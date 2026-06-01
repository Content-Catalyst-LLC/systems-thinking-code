CREATE TABLE IF NOT EXISTS scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  disturbance_variety REAL CHECK (disturbance_variety BETWEEN 0 AND 1),
  response_variety REAL CHECK (response_variety BETWEEN 0 AND 1),
  feedback_quality REAL CHECK (feedback_quality BETWEEN 0 AND 1),
  accountability_quality REAL CHECK (accountability_quality BETWEEN 0 AND 1)
);
