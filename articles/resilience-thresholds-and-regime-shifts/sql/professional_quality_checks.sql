-- Quality checks for resilience datasets.

-- Check for negative resilience or pressure values.
SELECT *
FROM resilience_timeseries
WHERE resilience < 0 OR pressure < 0;

-- Identify scenario-years that crossed threshold.
SELECT scenario_id, year, threshold_margin, regime
FROM resilience_timeseries
WHERE threshold_margin <= 0;

-- Prioritize high-vulnerability groups.
SELECT group_name, vulnerability_index, priority
FROM vulnerability_groups
WHERE vulnerability_index >= 70
ORDER BY vulnerability_index DESC;
