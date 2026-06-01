# Delay response table for article examples
indicators <- read.csv("../data/synthetic_indicators.csv")
indicators$misperception_gap <- indicators$actual_risk - indicators$perceived_risk
print(indicators[, c("period", "actual_risk", "perceived_risk", "misperception_gap")])
