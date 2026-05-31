CREATE TABLE IF NOT EXISTS implementation_milestones (
  policy_id TEXT NOT NULL,
  milestone_month INTEGER NOT NULL,
  milestone_name TEXT NOT NULL,
  status TEXT NOT NULL,
  completion_ratio REAL NOT NULL
);
