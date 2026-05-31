CREATE TABLE IF NOT EXISTS memory_assets (
  unit_id TEXT PRIMARY KEY,
  decision_records INTEGER,
  postmortems INTEGER,
  reused_lessons INTEGER,
  living_playbooks INTEGER,
  onboarding_links INTEGER,
  knowledge_decay_risk REAL
);
