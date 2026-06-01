data_dir <- file.path("..", "data")
out_dir <- file.path("..", "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

outcomes <- read.csv(file.path(data_dir, "synthetic_distributional_outcomes.csv"))
summary <- aggregate(cbind(access_index, burden_index, risk_index) ~ scenario_id, data = outcomes, FUN = mean)

write.csv(summary, file.path(out_dir, "distributional_scenario_summary.csv"), row.names = FALSE)
cat("Wrote distributional scenario summary\n")
