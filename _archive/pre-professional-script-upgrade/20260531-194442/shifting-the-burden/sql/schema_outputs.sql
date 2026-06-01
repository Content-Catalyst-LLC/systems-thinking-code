CREATE TABLE IF NOT EXISTS model_outputs (
  scenario TEXT NOT NULL,
  metric TEXT NOT NULL,
  value REAL NOT NULL,
  PRIMARY KEY (scenario, metric)
);
