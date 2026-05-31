CREATE TABLE IF NOT EXISTS feedback_signals (
  period INTEGER NOT NULL,
  team_id TEXT NOT NULL,
  observed_signal REAL NOT NULL,
  distortion REAL NOT NULL,
  decision_delay INTEGER NOT NULL,
  authority_to_change REAL NOT NULL,
  PRIMARY KEY (period, team_id)
);
