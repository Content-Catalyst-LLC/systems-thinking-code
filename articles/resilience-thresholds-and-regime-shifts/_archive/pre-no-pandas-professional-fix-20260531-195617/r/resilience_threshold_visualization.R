# Professional base-R visualization for resilience, thresholds, and regime shifts.

root <- normalizePath(file.path(dirname(commandArgs(trailingOnly = FALSE)[1]), ".."), mustWork = FALSE)
# The line above is not reliable under Rscript --file, so use working directory fallback.
if (!file.exists(file.path(root, "outputs"))) {
  root <- getwd()
}
if (basename(root) == "r") {
  root <- normalizePath(file.path(root, ".."), mustWork = FALSE)
}

table_dir <- file.path(root, "outputs", "tables")
figure_dir <- file.path(root, "outputs", "figures")
dir.create(table_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figure_dir, recursive = TRUE, showWarnings = FALSE)

results_path <- file.path(table_dir, "resilience_threshold_regime_results.csv")
if (!file.exists(results_path)) {
  stop("Missing resilience_threshold_regime_results.csv. Run the Python workflow first.")
}

results <- read.csv(results_path, stringsAsFactors = FALSE)
scenarios <- unique(results$scenario)

summary_rows <- lapply(scenarios, function(s) {
  x <- results[results$scenario == s, ]
  data.frame(
    scenario = s,
    final_resilience = tail(x$resilience, 1),
    final_pressure = tail(x$pressure, 1),
    minimum_threshold_margin = min(x$threshold_margin),
    maximum_recovery_time = max(x$recovery_time_index),
    years_near_threshold = sum(x$regime == "near threshold"),
    years_shifted = sum(x$regime == "shifted regime"),
    stringsAsFactors = FALSE
  )
})
summary <- do.call(rbind, summary_rows)
summary$resilience_diagnostic <- ifelse(
  summary$years_shifted > 0,
  "High regime-shift risk",
  ifelse(summary$years_near_threshold > 0, "Early warning threshold risk", "Resilience maintained")
)
write.csv(summary, file.path(table_dir, "r_resilience_threshold_summary.csv"), row.names = FALSE)
print(summary)

png(file.path(figure_dir, "r_resilience_trajectories.png"), width = 1200, height = 700)
plot(NULL, xlim = range(results$year), ylim = range(results$resilience), xlab = "Year", ylab = "Resilience stock index", main = "Resilience trajectories by scenario")
for (s in scenarios) {
  x <- results[results$scenario == s, ]
  lines(x$year, x$resilience, lwd = 2)
}
legend("bottomleft", legend = scenarios, lwd = 2, bty = "n", cex = 0.8)
dev.off()

png(file.path(figure_dir, "r_threshold_margin_trajectories.png"), width = 1200, height = 700)
plot(NULL, xlim = range(results$year), ylim = range(results$threshold_margin), xlab = "Year", ylab = "Threshold margin", main = "Threshold margin by scenario")
abline(h = 0, lty = 2)
for (s in scenarios) {
  x <- results[results$scenario == s, ]
  lines(x$year, x$threshold_margin, lwd = 2)
}
legend("bottomleft", legend = scenarios, lwd = 2, bty = "n", cex = 0.8)
dev.off()
