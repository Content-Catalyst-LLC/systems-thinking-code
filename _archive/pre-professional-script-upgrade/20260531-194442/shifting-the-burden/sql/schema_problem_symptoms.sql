CREATE TABLE IF NOT EXISTS problem_symptoms (
  period INTEGER NOT NULL,
  domain TEXT NOT NULL,
  problem_pressure REAL NOT NULL,
  visible_symptom TEXT NOT NULL,
  PRIMARY KEY (period, domain)
);
