# Base R visualization for synthetic archetype model runs.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_path <- file.path(root, "data", "synthetic_model_runs.csv")
out_dir <- file.path(root, "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

runs <- read.csv(data_path)
png(file.path(out_dir, "synthetic_problem_trajectories.png"), width = 900, height = 650)
plot(
  runs$time_step,
  runs$problem_level,
  type = "n",
  xlab = "Time step",
  ylab = "Problem level",
  main = "Synthetic archetype scenario trajectories"
)
for (scenario in unique(runs$scenario_id)) {
  subset_rows <- runs[runs$scenario_id == scenario, ]
  lines(subset_rows$time_step, subset_rows$problem_level, lwd = 2)
}
legend("topleft", legend = unique(runs$scenario_id), lwd = 2, bty = "n")
dev.off()
cat("Wrote figure to", out_dir, "\n")
