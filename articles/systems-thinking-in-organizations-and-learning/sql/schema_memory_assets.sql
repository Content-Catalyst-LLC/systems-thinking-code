CREATE TABLE IF NOT EXISTS memory_assets (
  team_id TEXT PRIMARY KEY,
  decision_records INTEGER NOT NULL,
  updated_playbooks INTEGER NOT NULL,
  onboarding_assets INTEGER NOT NULL,
  postmortems_reused INTEGER NOT NULL,
  key_person_dependency REAL NOT NULL
);
