CREATE TABLE IF NOT EXISTS growth_variables (
  year INTEGER PRIMARY KEY,
  system_scale REAL NOT NULL,
  demand_index REAL,
  service_quality REAL,
  public_trust REAL,
  governance_maturity REAL
);
