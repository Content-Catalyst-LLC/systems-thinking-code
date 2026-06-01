CREATE TABLE IF NOT EXISTS objective_functions (
  objective_id TEXT PRIMARY KEY,
  objective_name TEXT NOT NULL,
  throughput_weight REAL NOT NULL,
  cost_weight REAL NOT NULL,
  access_weight REAL NOT NULL,
  dignity_weight REAL NOT NULL,
  resilience_weight REAL NOT NULL,
  burden_penalty REAL NOT NULL,
  harm_penalty REAL NOT NULL
);
