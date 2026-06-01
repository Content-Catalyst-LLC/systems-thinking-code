CREATE TABLE IF NOT EXISTS control_actions (
  action_id TEXT PRIMARY KEY,
  action_type TEXT NOT NULL,
  response_speed TEXT,
  control_strength REAL CHECK (control_strength BETWEEN 0 AND 1),
  accountability_requirement TEXT,
  risk_if_misused TEXT
);
