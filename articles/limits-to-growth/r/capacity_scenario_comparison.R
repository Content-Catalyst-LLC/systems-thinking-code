# Capacity scenario comparison.
base_dir <- getwd()
input <- file.path(base_dir, "data", "synthetic_scenarios.csv")
rows <- read.csv(input)
summary <- rows[, c("scenario", "growth_rate", "constraint_capacity", "delay", "policy_note")]
out_dir <- file.path(base_dir, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(summary, file.path(out_dir, "capacity_scenario_comparison.csv"), row.names = FALSE)
