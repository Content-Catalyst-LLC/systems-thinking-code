-- Professional SQL QA checks for Delayed Feedback and Policy Timing
SELECT article_slug, scenario, COUNT(*) AS row_count
FROM professional_timeseries
GROUP BY article_slug, scenario
HAVING COUNT(*) < 20;

SELECT article_slug, scenario, MAX(risk_index) AS peak_risk_index
FROM professional_timeseries
GROUP BY article_slug, scenario
HAVING MAX(risk_index) > 75;

SELECT article_slug, scenario, AVG(burden_index) AS average_burden, AVG(trust_index) AS average_trust
FROM professional_timeseries
GROUP BY article_slug, scenario
HAVING AVG(burden_index) > 55 AND AVG(trust_index) < 50;
