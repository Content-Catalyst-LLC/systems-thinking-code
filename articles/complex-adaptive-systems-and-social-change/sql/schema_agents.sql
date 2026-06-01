CREATE TABLE IF NOT EXISTS social_agents (
  agent_id TEXT PRIMARY KEY,
  agent_group TEXT NOT NULL,
  baseline_trust REAL CHECK (baseline_trust BETWEEN 0 AND 1),
  adoption_threshold REAL CHECK (adoption_threshold BETWEEN 0 AND 1),
  network_reach REAL CHECK (network_reach BETWEEN 0 AND 1),
  resource_access REAL CHECK (resource_access BETWEEN 0 AND 1),
  vulnerability REAL CHECK (vulnerability BETWEEN 0 AND 1),
  initial_adoption BOOLEAN NOT NULL DEFAULT FALSE
);
