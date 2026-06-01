CREATE TABLE IF NOT EXISTS dependency_indicators (
  period INTEGER PRIMARY KEY,
  symptomatic_reliance REAL NOT NULL,
  fundamental_capacity REAL NOT NULL,
  dependency_ratio REAL NOT NULL
);
