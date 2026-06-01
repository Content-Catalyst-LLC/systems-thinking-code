# Delayed limit scenario summary.
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!file.exists(file.path(root, "data", "processed", "overshoot_scenarios.csv"))) root <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)
scenarios <- read.csv(file.path(root, "data", "processed", "overshoot_scenarios.csv"))
out_dir <- file.path(root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
scenarios$delay_risk_index <- round(scenarios$growth_rate * scenarios$feedback_delay * (1 - scenarios$correction_strength), 3)
write.csv(scenarios, file.path(out_dir, "delayed_limit_scenario_summary.csv"), row.names = FALSE)
