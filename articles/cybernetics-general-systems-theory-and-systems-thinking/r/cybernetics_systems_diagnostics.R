# cybernetics_systems_diagnostics.R
# Base R workflow for cybernetics, general systems theory, and systems thinking.

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

timeseries_path <- file.path(tables_dir, "cybernetics_systems_timeseries.csv")
summary_path <- file.path(tables_dir, "cybernetics_systems_summary.csv")

if (!file.exists(timeseries_path)) {
  stop(paste("Missing cybernetics_systems_timeseries.csv at", timeseries_path, "Run the Python workflow first."))
}

cyber <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(cyber, cyber$scenario), function(df) df[nrow(df), ])
)

cyber$absolute_error <- abs(cyber$error_signal)

avg_variety_gap <- aggregate(variety_gap ~ scenario, data = cyber, FUN = mean)
avg_regulation <- aggregate(regulation_quality ~ scenario, data = cyber, FUN = mean)
avg_accountability <- aggregate(accountability_index ~ scenario, data = cyber, FUN = mean)
avg_abs_error <- aggregate(absolute_error ~ scenario, data = cyber, FUN = mean)

names(avg_variety_gap)[2] <- "average_variety_gap"
names(avg_regulation)[2] <- "average_regulation_quality"
names(avg_accountability)[2] <- "average_accountability_index"
names(avg_abs_error)[2] <- "average_absolute_error"

final_fields <- last_by_scenario[, c(
  "scenario",
  "system_state",
  "response_variety",
  "learning_capacity",
  "trust_index",
  "regulation_quality",
  "accountability_index"
)]

names(final_fields) <- c(
  "scenario",
  "final_system_state",
  "final_response_variety",
  "final_learning_capacity",
  "final_trust_index",
  "final_regulation_quality",
  "final_accountability_index"
)

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_variety_gap, avg_regulation, avg_accountability, avg_abs_error, final_fields)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$average_variety_gap <= 15 &
    diagnostics$average_regulation_quality >= 65 &
    diagnostics$average_accountability_index >= 60,
  "accountable adaptive regulation",
  ifelse(
    diagnostics$average_variety_gap >= 35,
    "response variety insufficient for disturbance variety",
    ifelse(
      diagnostics$average_absolute_error >= 25,
      "feedback delay or weak regulation creates persistent error",
      "partial regulation with remaining systems risk"
    )
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(cyber$scenario)
  plot(
    NA,
    xlim = range(cyber$period),
    ylim = range(cyber[[metric]], na.rm = TRUE),
    xlab = "Period",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- cyber[cyber$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("system_state", "System state", "System State by Scenario", "system_state_trajectories.png")
plot_metric("error_signal", "Error signal", "Error Signal by Scenario", "error_signal_trajectories.png")
plot_metric("control_action", "Control action", "Control Action by Scenario", "control_action_trajectories.png")
plot_metric("response_variety", "Response variety", "Response Variety by Scenario", "response_variety_trajectories.png")
plot_metric("variety_gap", "Variety gap", "Requisite Variety Gap by Scenario", "variety_gap_trajectories.png")
plot_metric("learning_capacity", "Learning capacity", "Learning Capacity by Scenario", "learning_capacity_trajectories.png")
plot_metric("trust_index", "Trust index", "Trust by Scenario", "trust_trajectories.png")
plot_metric("regulation_quality", "Regulation quality", "Regulation Quality by Scenario", "regulation_quality_trajectories.png")
plot_metric("accountability_index", "Accountability index", "Accountability by Scenario", "accountability_trajectories.png")

final_table <- last_by_scenario[, c(
  "scenario",
  "system_state",
  "observed_state",
  "reference_goal",
  "error_signal",
  "control_action",
  "disturbance_pressure",
  "response_variety",
  "variety_gap",
  "learning_capacity",
  "trust_index",
  "regulation_quality",
  "accountability_index"
)]

write.csv(
  final_table,
  file.path(tables_dir, "cybernetics_systems_final_diagnostics.csv"),
  row.names = FALSE
)

print(final_table)
