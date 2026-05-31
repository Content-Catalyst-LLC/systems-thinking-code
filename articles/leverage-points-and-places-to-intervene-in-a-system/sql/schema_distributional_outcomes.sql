CREATE TABLE IF NOT EXISTS distributional_outcomes (
  group_id TEXT PRIMARY KEY,
  group_name TEXT NOT NULL,
  baseline_burden REAL,
  post_intervention_burden REAL,
  baseline_access REAL,
  post_intervention_access REAL
);
