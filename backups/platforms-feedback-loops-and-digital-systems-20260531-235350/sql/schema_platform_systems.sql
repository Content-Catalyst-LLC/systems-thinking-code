-- SQL schema for synthetic platform systems analysis.
CREATE TABLE IF NOT EXISTS platform_events (
  event_id INTEGER PRIMARY KEY,
  period INTEGER NOT NULL,
  platform_area TEXT NOT NULL,
  event_type TEXT NOT NULL,
  engagement_index REAL NOT NULL,
  harmful_cascade_risk REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS moderation_actions (
  action_id INTEGER PRIMARY KEY,
  period INTEGER NOT NULL,
  queue_type TEXT NOT NULL,
  flagged_items INTEGER NOT NULL,
  reviewed_items INTEGER NOT NULL,
  appeals INTEGER NOT NULL,
  average_response_hours REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS governance_controls (
  control_id INTEGER PRIMARY KEY,
  scenario TEXT NOT NULL,
  transparency_strength REAL NOT NULL,
  appeal_quality REAL NOT NULL,
  portability_strength REAL NOT NULL,
  friction_strength REAL NOT NULL,
  public_value_weight REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS platform_outputs (
  output_id INTEGER PRIMARY KEY,
  scenario TEXT NOT NULL,
  period INTEGER NOT NULL,
  engagement_index REAL NOT NULL,
  moderation_backlog REAL NOT NULL,
  platform_dependency REAL NOT NULL,
  user_trust REAL NOT NULL,
  public_value_index REAL NOT NULL,
  platform_risk_index REAL NOT NULL
);
