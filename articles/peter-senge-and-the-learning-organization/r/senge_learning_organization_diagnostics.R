# senge_learning_organization_diagnostics.R
# Base R workflow for Peter Senge and the learning organization.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)

if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- getwd()
}

setwd(article_root)

tables_dir <- file.path(article_root, "outputs", "tables")
figures_dir <- file.path(article_root, "outputs", "figures")

if (!dir.exists(tables_dir)) {
  dir.create(tables_dir, recursive = TRUE)
}

if (!dir.exists(figures_dir)) {
  dir.create(figures_dir, recursive = TRUE)
}

timeseries_path <- file.path(tables_dir, "senge_learning_organization_timeseries.csv")
summary_path <- file.path(tables_dir, "senge_learning_organization_summary.csv")

if (!file.exists(timeseries_path)) {
  stop(paste("Missing senge_learning_organization_timeseries.csv at", timeseries_path, "Run the Python workflow first."))
}

senge <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(senge, senge$scenario), function(df) df[nrow(df), ])
)

avg_learning <- aggregate(learning_capacity_score ~ scenario, data = senge, FUN = mean)
avg_defensive <- aggregate(defensive_routines_index ~ scenario, data = senge, FUN = mean)
avg_performance <- aggregate(organizational_performance ~ scenario, data = senge, FUN = mean)

names(avg_learning)[2] <- "average_learning_capacity_score"
names(avg_defensive)[2] <- "average_defensive_routines_index"
names(avg_performance)[2] <- "average_organizational_performance"

final_fields <- last_by_scenario[, c(
  "scenario",
  "learning_capacity_score",
  "defensive_routines_index",
  "adaptive_capacity",
  "organizational_performance",
  "learning_stock",
  "institutional_memory_stock"
)]

names(final_fields) <- c(
  "scenario",
  "final_learning_capacity_score",
  "final_defensive_routines_index",
  "final_adaptive_capacity",
  "final_organizational_performance",
  "final_learning_stock",
  "final_institutional_memory_stock"
)

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_learning, avg_defensive, avg_performance, final_fields)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$final_learning_capacity_score >= 65 &
    diagnostics$final_defensive_routines_index <= 30,
  "learning organization pathway",
  ifelse(
    diagnostics$average_defensive_routines_index >= 50,
    "defensive routines suppress organizational learning",
    ifelse(
      diagnostics$average_learning_capacity_score >= 50,
      "partial learning capacity with structural constraints",
      "low learning capacity"
    )
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(senge$scenario)
  plot(
    NA,
    xlim = range(senge$period),
    ylim = range(senge[[metric]], na.rm = TRUE),
    xlab = "Period",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- senge[senge$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("feedback_use_index", "Feedback use index", "Feedback Use by Scenario", "feedback_use_trajectories.png")
plot_metric("inquiry_strength", "Inquiry strength", "Mental Model Inquiry by Scenario", "inquiry_strength_trajectories.png")
plot_metric("shared_alignment", "Shared alignment", "Shared Vision Alignment by Scenario", "shared_alignment_trajectories.png")
plot_metric("defensive_routines_index", "Defensive routines index", "Defensive Routines by Scenario", "defensive_routines_trajectories.png")
plot_metric("learning_stock", "Learning stock", "Learning Stock by Scenario", "learning_stock_trajectories.png")
plot_metric("institutional_memory_stock", "Institutional memory stock", "Institutional Memory by Scenario", "institutional_memory_trajectories.png")
plot_metric("trust_stock", "Trust stock", "Trust Stock by Scenario", "trust_stock_trajectories.png")
plot_metric("adaptive_capacity", "Adaptive capacity", "Adaptive Capacity by Scenario", "adaptive_capacity_trajectories.png")
plot_metric("learning_capacity_score", "Learning capacity score", "Learning Capacity by Scenario", "learning_capacity_trajectories.png")

final_table <- last_by_scenario[, c(
  "scenario",
  "feedback_use_index",
  "inquiry_strength",
  "shared_alignment",
  "defensive_routines_index",
  "learning_stock",
  "institutional_memory_stock",
  "trust_stock",
  "adaptive_capacity",
  "organizational_performance",
  "learning_capacity_score"
)]

write.csv(
  final_table,
  file.path(tables_dir, "senge_learning_organization_final_diagnostics.csv"),
  row.names = FALSE
)

print(final_table)
