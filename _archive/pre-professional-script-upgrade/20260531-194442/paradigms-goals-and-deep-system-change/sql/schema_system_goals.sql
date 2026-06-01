CREATE TABLE IF NOT EXISTS system_goals (
  goal_id TEXT PRIMARY KEY,
  system_domain TEXT NOT NULL,
  goal_name TEXT NOT NULL,
  goal_type TEXT CHECK (goal_type IN ('explicit', 'implicit')),
  description TEXT
);
