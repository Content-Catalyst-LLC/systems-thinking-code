-- Professional SQL schema for Feedback Loop Polarity and Causal Signs
CREATE TABLE IF NOT EXISTS professional_timeseries (
  article_slug TEXT NOT NULL,
  year INTEGER NOT NULL,
  scenario TEXT NOT NULL,
  system_stock_index REAL NOT NULL CHECK(system_stock_index BETWEEN 0 AND 120),
  capacity_index REAL NOT NULL CHECK(capacity_index BETWEEN 0 AND 100),
  trust_index REAL NOT NULL CHECK(trust_index BETWEEN 0 AND 100),
  memory_index REAL NOT NULL CHECK(memory_index BETWEEN 0 AND 100),
  burden_index REAL NOT NULL CHECK(burden_index BETWEEN 0 AND 100),
  equity_gap_index REAL NOT NULL CHECK(equity_gap_index BETWEEN 0 AND 100),
  risk_index REAL NOT NULL CHECK(risk_index BETWEEN 0 AND 100),
  outcome_index REAL NOT NULL CHECK(outcome_index BETWEEN 0 AND 100),
  PRIMARY KEY(article_slug, scenario, year)
);

CREATE VIEW IF NOT EXISTS professional_scenario_summary AS
SELECT article_slug, scenario,
       AVG(outcome_index) AS average_outcome_index,
       MAX(risk_index) AS peak_risk_index,
       AVG(burden_index) AS average_burden_index,
       MIN(system_stock_index) AS minimum_stock_index
FROM professional_timeseries
GROUP BY article_slug, scenario;
