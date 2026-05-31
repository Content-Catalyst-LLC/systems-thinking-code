# Scenario comparison table.
out <- read.csv("../data/processed/outcomes.csv")
final_month <- max(out$month)
final <- out[out$month == final_month, ]
write.csv(final, "../outputs/tables/final_policy_timing_scenarios.csv", row.names = FALSE)
