# Summarize implementation milestone completion.
m <- read.csv("../data/processed/implementation_milestones.csv")
summary_table <- aggregate(completion_ratio ~ policy_id, data = m, mean)
write.csv(summary_table, "../outputs/tables/implementation_lag_summary.csv", row.names = FALSE)
