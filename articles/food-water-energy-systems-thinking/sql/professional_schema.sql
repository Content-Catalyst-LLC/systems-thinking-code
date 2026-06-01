-- Professional schema for food-water-energy nexus analysis.
-- Designed for SQLite/PostgreSQL-style adaptation.

CREATE TABLE IF NOT EXISTS nexus_scenarios (
  scenario TEXT PRIMARY KEY,
  description TEXT,
  policy_start_year INTEGER,
  climate_stress REAL,
  vulnerability_index REAL
);

CREATE TABLE IF NOT EXISTS nexus_timeseries (
  year INTEGER NOT NULL,
  scenario TEXT NOT NULL,
  groundwater_stock REAL NOT NULL,
  effective_withdrawal REAL NOT NULL,
  pumping_energy REAL NOT NULL,
  fossil_energy_exposure REAL NOT NULL,
  soil_health REAL NOT NULL,
  food_production_index REAL NOT NULL,
  water_security_index REAL NOT NULL,
  energy_security_index REAL NOT NULL,
  nexus_stress_index REAL NOT NULL,
  resilience_index REAL NOT NULL,
  PRIMARY KEY (scenario, year)
);

CREATE VIEW IF NOT EXISTS nexus_final_state AS
SELECT t.*
FROM nexus_timeseries t
JOIN (
  SELECT scenario, MAX(year) AS max_year
  FROM nexus_timeseries
  GROUP BY scenario
) m ON t.scenario = m.scenario AND t.year = m.max_year;
