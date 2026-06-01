CREATE TABLE IF NOT EXISTS defensive_routines (
  routine_id TEXT PRIMARY KEY,
  routine_type TEXT NOT NULL,
  intensity REAL CHECK (intensity BETWEEN 0 AND 1),
  learning_risk TEXT,
  possible_countermeasure TEXT
);
