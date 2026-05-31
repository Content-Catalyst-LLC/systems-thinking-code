CREATE TABLE IF NOT EXISTS intervention_frames (
  frame_id TEXT PRIMARY KEY,
  model_id TEXT REFERENCES mental_models(model_id),
  intervention_name TEXT,
  intervention_type TEXT,
  expected_short_term_effect TEXT,
  likely_system_response TEXT,
  redesign_score REAL
);
