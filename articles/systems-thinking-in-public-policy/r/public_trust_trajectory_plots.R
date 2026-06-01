root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
results_path <- file.path(root, "outputs", "tables", "public_policy_scenario_results.csv")
figures <- file.path(root, "outputs", "figures")
dir.create(figures, recursive = TRUE, showWarnings = FALSE)
if (file.exists(results_path)) {
  policy_results <- read.csv(results_path)
  png(file.path(figures, "public_trust_trajectories.png"), width = 1000, height = 650)
  scenarios <- unique(policy_results$scenario)
  plot(NULL, xlim = range(policy_results$year), ylim = c(0, 100), xlab = "Year", ylab = "Public trust index", main = "Public Trust Trajectories by Policy Scenario")
  for (i in seq_along(scenarios)) {
    x <- policy_results[policy_results$scenario == scenarios[i], ]
    lines(x$year, x$public_trust, lwd = 2, lty = i)
  }
  legend("bottomright", legend = scenarios, lty = seq_along(scenarios), lwd = 2, cex = 0.8)
  dev.off()
}
