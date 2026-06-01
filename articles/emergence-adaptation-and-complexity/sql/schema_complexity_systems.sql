-- SQLite-compatible schema for synthetic emergence/adaptation/complexity workflows.
CREATE TABLE IF NOT EXISTS agent_states (
  run_id TEXT NOT NULL,
  period INTEGER NOT NULL,
  agent_id INTEGER NOT NULL,
  state_value REAL NOT NULL CHECK (state_value >= 0 AND state_value <= 1),
  PRIMARY KEY (run_id, period, agent_id)
);

CREATE TABLE IF NOT EXISTS complexity_indicators (
  run_id TEXT NOT NULL,
  period INTEGER NOT NULL,
  scenario TEXT NOT NULL,
  clustering_index REAL NOT NULL,
  diversity_index REAL NOT NULL,
  synchronization_index REAL NOT NULL,
  complexity_index REAL NOT NULL,
  PRIMARY KEY (run_id, period, scenario)
);

CREATE TABLE IF NOT EXISTS scenario_assumptions (
  scenario TEXT PRIMARY KEY,
  interaction_strength REAL NOT NULL,
  adaptation_rate REAL NOT NULL,
  noise REAL NOT NULL,
  institutional_guidance REAL NOT NULL,
  diversity_floor REAL NOT NULL
);
