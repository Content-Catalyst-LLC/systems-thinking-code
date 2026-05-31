# Perception gap table
indicators <- read.csv("../data/synthetic_indicators.csv")
indicators$gap <- indicators$actual_risk - indicators$perceived_risk
print(indicators[, c("period", "gap")])
