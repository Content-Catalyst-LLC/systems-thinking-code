# Goal comparison plots for synthetic systems scenarios.
# Run from the article directory with: Rscript r/goal_comparison_plots.R

data_path <- file.path("data", "synthetic_scenario_outputs.csv")
if (!file.exists(data_path)) {
  stop("Run this script from the article directory: articles/paradigms-goals-and-deep-system-change")
}

scenario_data <- read.csv(data_path)
output_dir <- file.path("outputs", "figures")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

png(file.path(output_dir, "scenario_total_score.png"), width = 900, height = 600)
plot(
  scenario_data$year,
  scenario_data$total_score,
  xlab = "Year",
  ylab = "Total score",
  main = "Goal Structures and Scenario Outcomes",
  pch = 19
)
legend("topleft", legend = unique(scenario_data$scenario_name), bty = "n")
dev.off()
