source(file.path(dirname(sys.frame(1)$ofile), "_workflow_utils.R"))
root <- article_root(); ensure_dirs(root)
results_path <- file.path(root, "outputs", "tables", "public_policy_scenario_results.csv")
if (!file.exists(results_path)) stop("Run python/run_all_public_policy_workflows.py before this R script.")
policy_results <- read.csv(results_path)
fig <- file.path(root, "outputs", "figures", "public_trust_trajectories.png")
png(fig, width = 1000, height = 650)
scenarios <- unique(policy_results$scenario)
plot(NULL, xlim = range(policy_results$year), ylim = c(0, 100), xlab = "Year", ylab = "Public trust index", main = "Public Trust Trajectories by Policy Scenario")
for (i in seq_along(scenarios)) {
  x <- policy_results[policy_results$scenario == scenarios[i], ]
  lines(x$year, x$public_trust, lwd = 2, lty = i)
}
legend("bottomright", legend = scenarios, lty = seq_along(scenarios), lwd = 2, cex = 0.75)
dev.off()
cat("Wrote", fig, "\n")
