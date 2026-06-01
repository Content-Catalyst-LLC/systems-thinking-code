-- Urban systems data model for SQLite-compatible diagnostics.
DROP TABLE IF EXISTS scenario_summary;
CREATE TABLE scenario_summary (
  scenario TEXT PRIMARY KEY,
  final_congestion_index REAL NOT NULL,
  final_affordability_index REAL NOT NULL,
  final_infrastructure_condition REAL NOT NULL,
  final_displacement_pressure REAL NOT NULL,
  average_congestion_index REAL NOT NULL,
  average_affordability_index REAL NOT NULL,
  minimum_infrastructure_condition REAL NOT NULL,
  maximum_displacement_pressure REAL NOT NULL,
  average_urban_resilience_index REAL NOT NULL,
  diagnostic TEXT NOT NULL
);

INSERT INTO scenario_summary VALUES
('Road expansion baseline', 52.0, 35.0, 40.0, 55.0, 49.0, 39.0, 38.0, 56.0, 42.0, 'moderate stress requiring redesign'),
('Deferred maintenance', 50.0, 33.0, 24.0, 58.0, 48.0, 37.0, 23.0, 59.0, 31.0, 'high urban fragility'),
('Transit housing coordination', 42.0, 49.0, 58.0, 40.0, 43.0, 50.0, 55.0, 43.0, 50.0, 'comparatively resilient urban pathway'),
('Integrated resilient urbanism', 38.0, 58.0, 68.0, 31.0, 39.0, 57.0, 63.0, 35.0, 59.0, 'comparatively resilient urban pathway');

DROP VIEW IF EXISTS high_risk_scenarios;
CREATE VIEW high_risk_scenarios AS
SELECT *
FROM scenario_summary
WHERE diagnostic IN ('high urban fragility', 'moderate stress requiring redesign')
ORDER BY average_urban_resilience_index ASC;

DROP VIEW IF EXISTS investment_priority;
CREATE VIEW investment_priority AS
SELECT
  scenario,
  CASE
    WHEN minimum_infrastructure_condition < 35 THEN 'maintenance and climate adaptation'
    WHEN average_affordability_index < 45 THEN 'housing affordability and anti-displacement'
    WHEN average_congestion_index > 55 THEN 'access, transit, and demand management'
    ELSE 'monitor and preserve resilience'
  END AS priority
FROM scenario_summary;
