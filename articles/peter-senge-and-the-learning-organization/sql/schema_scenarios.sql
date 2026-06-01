CREATE TABLE IF NOT EXISTS scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  feedback_quality REAL CHECK (feedback_quality BETWEEN 0 AND 1),
  psychological_safety REAL CHECK (psychological_safety BETWEEN 0 AND 1),
  systems_thinking_practice REAL CHECK (systems_thinking_practice BETWEEN 0 AND 1),
  blame_tendency REAL CHECK (blame_tendency BETWEEN 0 AND 1)
);
