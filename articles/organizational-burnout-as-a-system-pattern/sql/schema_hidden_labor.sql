CREATE TABLE IF NOT EXISTS hidden_labor (
  period INTEGER NOT NULL,
  role_id TEXT NOT NULL,
  coordination_hours REAL,
  emotional_labor_hours REAL,
  informal_mentoring_hours REAL,
  workaround_hours REAL,
  unpaid_extra_hours REAL,
  PRIMARY KEY (period, role_id)
);
