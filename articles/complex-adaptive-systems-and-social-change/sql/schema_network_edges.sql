CREATE TABLE IF NOT EXISTS network_edges (
  edge_id INTEGER PRIMARY KEY,
  source_agent_id TEXT NOT NULL REFERENCES social_agents(agent_id),
  target_agent_id TEXT NOT NULL REFERENCES social_agents(agent_id),
  tie_strength REAL CHECK (tie_strength BETWEEN 0 AND 1),
  trust_bridge BOOLEAN DEFAULT FALSE
);
