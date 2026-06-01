-- Quality checks for synthetic climate systems outputs.

-- Negative emissions are not expected in the default demonstration scenarios.
SELECT scenario_name, year, emissions_gtco2
FROM climate_timeseries
WHERE emissions_gtco2 < 0;

-- CO2 concentration must remain positive.
SELECT scenario_name, year, co2_ppm
FROM climate_timeseries
WHERE co2_ppm <= 0;

-- Identify years at or above a 2C synthetic warning threshold.
SELECT scenario_name, MIN(year) AS first_year_above_2c
FROM climate_timeseries
WHERE temperature_anomaly_c >= 2.0
GROUP BY scenario_name;
