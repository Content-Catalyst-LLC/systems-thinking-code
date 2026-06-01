-- Professional climate systems schema for synthetic scenario analysis.
-- Designed for reproducible systems-thinking workflows, not official projections.

CREATE TABLE IF NOT EXISTS climate_scenarios (
    scenario_id INTEGER PRIMARY KEY,
    scenario_name TEXT NOT NULL UNIQUE,
    policy_delay_years INTEGER NOT NULL,
    emissions_decline_rate REAL NOT NULL,
    adaptation_capacity REAL NOT NULL,
    vulnerability_index REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS climate_timeseries (
    scenario_name TEXT NOT NULL,
    year INTEGER NOT NULL,
    emissions_gtco2 REAL NOT NULL,
    co2_ppm REAL NOT NULL,
    forcing_wm2 REAL NOT NULL,
    temperature_anomaly_c REAL NOT NULL,
    ocean_heat_index REAL NOT NULL,
    effective_sink_fraction REAL NOT NULL,
    risk_index REAL NOT NULL,
    PRIMARY KEY (scenario_name, year)
);

CREATE VIEW IF NOT EXISTS climate_scenario_summary AS
SELECT
    scenario_name,
    MAX(year) AS final_year,
    SUM(emissions_gtco2) AS cumulative_emissions_gtco2,
    MAX(temperature_anomaly_c) AS maximum_temperature_anomaly_c,
    AVG(risk_index) AS average_risk_index
FROM climate_timeseries
GROUP BY scenario_name;
