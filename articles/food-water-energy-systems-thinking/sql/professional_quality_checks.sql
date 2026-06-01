-- Quality checks for food-water-energy nexus outputs.

-- Check impossible negative values.
SELECT scenario, year, groundwater_stock, nexus_stress_index, resilience_index
FROM nexus_timeseries
WHERE groundwater_stock < 0
   OR nexus_stress_index < 0
   OR resilience_index < 0;

-- Identify high-stress scenario years.
SELECT scenario, COUNT(*) AS high_stress_years
FROM nexus_timeseries
WHERE nexus_stress_index >= 60
GROUP BY scenario
ORDER BY high_stress_years DESC;

-- Final scenario comparison.
SELECT scenario, groundwater_stock, food_production_index, water_security_index, energy_security_index, nexus_stress_index, resilience_index
FROM nexus_final_state
ORDER BY nexus_stress_index DESC;
