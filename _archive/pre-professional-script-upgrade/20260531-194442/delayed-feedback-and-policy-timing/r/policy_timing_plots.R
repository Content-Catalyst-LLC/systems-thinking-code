# Policy timing plots using base R.
data <- read.csv("../data/processed/outcomes.csv")
png("../outputs/figures/policy_timing_outcome_score.png", width = 900, height = 600)
plot(data$month, data$outcome_score, type = "n", xlab = "Month", ylab = "Outcome score", main = "Policy Timing Scenario Outcomes")
for (scenario in unique(data$scenario_id)) {
  subset_data <- data[data$scenario_id == scenario, ]
  lines(subset_data$month, subset_data$outcome_score, lwd = 2)
}
legend("bottomright", legend = unique(data$scenario_id), lwd = 2)
dev.off()
