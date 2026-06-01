#!/usr/bin/env Rscript
# Professional resilience threshold visualization using base R only.
# Reads Python-generated CSV outputs and exports diagnostic tables and PNG figures.

root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
tables_dir <- file.path(root, "outputs", "tables")
figures_dir <- file.path(root, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

results_path <- file.path(tables_dir, "resilience_threshold_regime_results.csv")
if (!file.exists(results_path)) {
  stop("Missing input file: ", results_path, ". Run python/run_all_resilience_workflows.py first.")
}

results <- read.csv(results_path, stringsAsFactors = FALSE)

scenarios <- unique(results$scenario)
summary_rows <- lapply(scenarios, function(s) {
  subset_rows <- results[results$scenario == s, ]
  data.frame(
    scenario = s,
    final_resilience = tail(subset_rows$resilience, 1),
    final_pressure = tail(subset_rows$pressure, 1),
    minimum_threshold_margin = min(subset_rows$threshold_margin),
    maximum_recovery_time = max(subset_rows$recovery_time_index),
    years_near_threshold = sum(subset_rows$regime == "near threshold"),
    years_shifted = sum(subset_rows$regime == "shifted regime"),
    stringsAsFactors = FALSE
  )
})
scenario_summary <- do.call(rbind, summary_rows)
scenario_summary$resilience_diagnostic <- ifelse(
  scenario_summary$years_shifted > 0,
  "High regime-shift risk",
  ifelse(
    scenario_summary$years_near_threshold > 0,
    "Early warning threshold risk",
    ifelse(
      scenario_summary$minimum_threshold_margin < 20,
      "Stressed but recoverable",
      "Resilience maintained"
    )
  )
)

write.csv(scenario_summary, file.path(tables_dir, "resilience_r_scenario_summary.csv"), row.names = FALSE)
print(scenario_summary)

# Plot resilience trajectories using base R.
png(file.path(figures_dir, "resilience_trajectories_base_r.png"), width = 1200, height = 750, res = 150)
plot(
  NA,
  xlim = range(results$year),
  ylim = range(results$resilience),
  xlab = "Year",
  ylab = "Resilience stock index",
  main = "Resilience Trajectories by Scenario"
)
line_types <- seq_along(scenarios)
for (i in seq_along(scenarios)) {
  s <- scenarios[i]
  subset_rows <- results[results$scenario == s, ]
  lines(subset_rows$year, subset_rows$resilience, lwd = 2, lty = line_types[i])
}
legend("bottomleft", legend = scenarios, lty = line_types, lwd = 2, cex = 0.75)
dev.off()

# Plot threshold margin trajectories.
png(file.path(figures_dir, "threshold_margin_trajectories_base_r.png"), width = 1200, height = 750, res = 150)
plot(
  NA,
  xlim = range(results$year),
  ylim = range(results$threshold_margin),
  xlab = "Year",
  ylab = "Threshold margin",
  main = "Threshold Margin by Scenario"
)
abline(h = 0, lty = 2)
for (i in seq_along(scenarios)) {
  s <- scenarios[i]
  subset_rows <- results[results$scenario == s, ]
  lines(subset_rows$year, subset_rows$threshold_margin, lwd = 2, lty = line_types[i])
}
legend("topright", legend = scenarios, lty = line_types, lwd = 2, cex = 0.75)
dev.off()

# Early warning diagnostic export from R perspective.
early_warning_rows <- lapply(scenarios, function(s) {
  subset_rows <- results[results$scenario == s, ]
  near_years <- subset_rows$year[subset_rows$regime == "near threshold"]
  shifted_years <- subset_rows$year[subset_rows$regime == "shifted regime"]
  data.frame(
    scenario = s,
    first_near_threshold_year = ifelse(length(near_years) > 0, min(near_years), NA),
    first_shifted_year = ifelse(length(shifted_years) > 0, min(shifted_years), NA),
    peak_recovery_time = max(subset_rows$recovery_time_index),
    lowest_margin = min(subset_rows$threshold_margin),
    stringsAsFactors = FALSE
  )
})
early_warning_table <- do.call(rbind, early_warning_rows)
write.csv(early_warning_table, file.path(tables_dir, "resilience_r_early_warning_diagnostics.csv"), row.names = FALSE)
print(early_warning_table)
