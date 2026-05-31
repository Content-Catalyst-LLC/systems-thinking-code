# Scenario comparison placeholder using synthetic scenarios
scenarios <- read.csv("../data/synthetic_scenarios.csv")
scenarios$timing_risk_score <- scenarios$delay_multiplier * 10 + scenarios$shock_size - scenarios$capacity_investment
print(scenarios[, c("scenario_id", "scenario_name", "timing_risk_score")])
