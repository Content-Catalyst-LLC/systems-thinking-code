CREATE TABLE IF NOT EXISTS scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  boundary_inclusion REAL CHECK (boundary_inclusion BETWEEN 0 AND 1),
  affected_voice REAL CHECK (affected_voice BETWEEN 0 AND 1),
  accountability_quality REAL CHECK (accountability_quality BETWEEN 0 AND 1),
  harm_exposure REAL CHECK (harm_exposure BETWEEN 0 AND 1)
);
