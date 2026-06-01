CREATE TABLE IF NOT EXISTS feedback_channels (
  channel_id TEXT PRIMARY KEY,
  channel_name TEXT,
  formality TEXT,
  signal_richness REAL,
  retaliation_risk REAL,
  decision_proximity REAL,
  closure_quality REAL
);
