# Fixes That Fail behavior plots using base R only.
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- if (length(file_arg)) sub("^--file=", "", file_arg[[1]]) else "r/fixes_that_fail_plots.R"
root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
dir.create(file.path(root, "outputs", "figures"), recursive = TRUE, showWarnings = FALSE)
runs <- read.csv(file.path(root, "data", "synthetic_model_runs.csv"))
png(file.path(root, "outputs", "figures", "fixes_that_fail_scenarios.png"), width = 900, height = 600)
plot(runs$period, runs$symptom_level, type = "n", xlab = "Period", ylab = "Symptom level", main = "Fixes That Fail: Scenario Comparison")
for (scenario in unique(runs$scenario)) {
  subset <- runs[runs$scenario == scenario, ]
  lines(subset$period, subset$symptom_level, lwd = 2)
}
legend("topleft", legend = unique(runs$scenario), lwd = 2, bty = "n")
dev.off()
