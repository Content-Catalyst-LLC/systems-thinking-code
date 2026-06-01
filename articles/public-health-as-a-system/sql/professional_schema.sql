-- Public health systems schema for professional prototyping.
-- Designed for synthetic or de-identified aggregate data only.

CREATE TABLE IF NOT EXISTS public_health_scenarios (
  scenario_id INTEGER PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  population INTEGER NOT NULL,
  intervention_start_week INTEGER NOT NULL,
  prevention_strength REAL NOT NULL,
  vulnerability_index REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS public_health_timeseries (
  scenario_id INTEGER NOT NULL,
  week INTEGER NOT NULL,
  susceptible REAL NOT NULL,
  infected REAL NOT NULL,
  recovered REAL NOT NULL,
  severe_cases REAL NOT NULL,
  care_capacity REAL NOT NULL,
  care_stress REAL NOT NULL,
  public_trust REAL NOT NULL,
  health_risk_index REAL NOT NULL,
  prevention_value_index REAL NOT NULL,
  PRIMARY KEY (scenario_id, week),
  FOREIGN KEY (scenario_id) REFERENCES public_health_scenarios(scenario_id)
);

CREATE VIEW IF NOT EXISTS scenario_peak_stress AS
SELECT
  scenario_id,
  MAX(infected) AS peak_infected,
  MAX(care_stress) AS peak_care_stress,
  AVG(public_trust) AS average_public_trust,
  AVG(health_risk_index) AS average_health_risk_index
FROM public_health_timeseries
GROUP BY scenario_id;
