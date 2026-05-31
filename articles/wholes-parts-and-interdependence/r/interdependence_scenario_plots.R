# Interdependence scenario summary

script_args <- commandArgs(trailingOnly = FALSE)
file_arg <- script_args[grep("--file=", script_args)]
script_path <- if (length(file_arg) > 0) sub("--file=", "", file_arg[1]) else "r/interdependence_scenario_plots.R"
article_dir <- dirname(dirname(normalizePath(script_path)))

scenarios <- read.csv(file.path(article_dir, "data", "synthetic_scenarios.csv"))
scenarios$risk_score <- round(scenarios$shock_size / (scenarios$redundancy_multiplier * scenarios$coordination_multiplier + 0.01), 2)
print(scenarios[, c("scenario_id", "scenario_name", "risk_score")])

output_dir <- file.path(article_dir, "outputs", "tables")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(scenarios, file.path(output_dir, "interdependence_scenario_scores.csv"), row.names = FALSE)
