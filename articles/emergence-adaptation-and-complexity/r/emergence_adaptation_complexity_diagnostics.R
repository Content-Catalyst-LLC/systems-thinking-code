# emergence_adaptation_complexity_diagnostics.R
# Base R complexity systems workflow.
# Purpose: summarize emergence/adaptation scenarios and visualize complexity indicators.
# This file safely resolves the article root whether sourced or run through Rscript.

resolve_article_root <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- "--file="
  match <- grep(file_arg, args, value = TRUE)
  if (length(match) > 0) {
    script_path <- normalizePath(sub(file_arg, "", match[1]), mustWork = FALSE)
    return(normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE))
  }

  current <- normalizePath(getwd(), mustWork = FALSE)
  if (basename(current) == "r") {
    return(normalizePath(file.path(current, ".."), mustWork = FALSE))
  }
  if (basename(current) == "python") {
    return(normalizePath(file.path(current, ".."), mustWork = FALSE))
  }
  return(current)
}

article_root <- resolve_article_root()
setwd(article_root)

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")

dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

timeseries_path <- file.path(tables_dir, "emergence_adaptation_complexity_timeseries.csv")
summary_path <- file.path(tables_dir, "emergence_adaptation_complexity_summary.csv")

if (!file.exists(timeseries_path)) {
  python_runner <- file.path(article_root, "python", "run_all_complexity_workflows.py")
  if (file.exists(python_runner)) {
    message("Missing timeseries CSV. Running Python workflow first from article root...")
    status <- system2("python3", python_runner)
    if (!identical(status, 0L)) {
      stop("Python workflow failed; cannot continue R diagnostics.")
    }
  }
}

if (!file.exists(timeseries_path)) {
  stop(paste("Missing", basename(timeseries_path), "after Python workflow attempt."))
}

complexity <- read.csv(timeseries_path, stringsAsFactors = FALSE)

required_columns <- c(
  "period", "scenario", "system_mean", "clustering_index", "diversity_index",
  "synchronization_index", "complexity_index"
)
missing_columns <- setdiff(required_columns, names(complexity))
if (length(missing_columns) > 0) {
  stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
}

avg_complexity <- aggregate(complexity_index ~ scenario, data = complexity, FUN = mean)
peak_complexity <- aggregate(complexity_index ~ scenario, data = complexity, FUN = max)
avg_diversity <- aggregate(diversity_index ~ scenario, data = complexity, FUN = mean)
avg_synchronization <- aggregate(synchronization_index ~ scenario, data = complexity, FUN = mean)

names(avg_complexity)[2] <- "average_complexity_index"
names(peak_complexity)[2] <- "peak_complexity_index"
names(avg_diversity)[2] <- "average_diversity_index"
names(avg_synchronization)[2] <- "average_synchronization_index"

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_complexity, peak_complexity, avg_diversity, avg_synchronization)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$average_synchronization_index >= 0.85,
  "over-synchronized fragile pattern",
  ifelse(
    diagnostics$average_diversity_index >= 0.85,
    "high volatility and weak coherence",
    "adaptive complex pattern"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(complexity$scenario)
  plot(
    NA,
    xlim = range(complexity$period),
    ylim = range(complexity[[metric]], na.rm = TRUE),
    xlab = "Period",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- complexity[complexity$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topright", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric(
  metric = "complexity_index",
  y_label = "Complexity index",
  title = "Complexity Trajectories by Scenario",
  output_name = "complexity_index_trajectories.png"
)

plot_metric(
  metric = "clustering_index",
  y_label = "Clustering index",
  title = "Emergent Clustering by Scenario",
  output_name = "clustering_index_trajectories.png"
)

plot_metric(
  metric = "diversity_index",
  y_label = "Diversity index",
  title = "Diversity Trajectories by Scenario",
  output_name = "diversity_index_trajectories.png"
)

plot_metric(
  metric = "synchronization_index",
  y_label = "Synchronization index",
  title = "Synchronization Trajectories by Scenario",
  output_name = "synchronization_index_trajectories.png"
)

plot_metric(
  metric = "system_mean",
  y_label = "System mean state",
  title = "System Mean State by Scenario",
  output_name = "system_mean_trajectories.png"
)

pattern_table <- data.frame()
for (scenario_name in unique(complexity$scenario)) {
  subset_data <- complexity[complexity$scenario == scenario_name, ]
  final_row <- subset_data[nrow(subset_data), ]

  pattern_table <- rbind(
    pattern_table,
    data.frame(
      scenario = scenario_name,
      final_complexity_index = final_row$complexity_index,
      final_clustering_index = final_row$clustering_index,
      final_diversity_index = final_row$diversity_index,
      final_synchronization_index = final_row$synchronization_index,
      final_system_mean = final_row$system_mean
    )
  )
}

write.csv(
  pattern_table,
  file.path(tables_dir, "emergence_pattern_diagnostics.csv"),
  row.names = FALSE
)

print(pattern_table)
message("Base R complexity diagnostics completed from article root: ", article_root)
