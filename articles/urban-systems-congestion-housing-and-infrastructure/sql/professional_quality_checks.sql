-- Quality checks for urban systems scenario summary.
SELECT 'row_count' AS check_name, COUNT(*) AS value FROM scenario_summary;
SELECT 'bounded_indicator_violations' AS check_name, COUNT(*) AS value
FROM scenario_summary
WHERE final_congestion_index NOT BETWEEN 0 AND 100
   OR final_affordability_index NOT BETWEEN 0 AND 100
   OR final_infrastructure_condition NOT BETWEEN 0 AND 100
   OR final_displacement_pressure NOT BETWEEN 0 AND 100
   OR average_urban_resilience_index NOT BETWEEN 0 AND 100;
SELECT * FROM high_risk_scenarios;
SELECT * FROM investment_priority;
