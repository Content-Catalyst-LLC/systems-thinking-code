# forrester_system_dynamics_diagnostics.R
# Base R workflow for Jay Forrester and system dynamics.

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

timeseries_path <- file.path(tables_dir, "forrester_system_dynamics_timeseries.csv")
summary_path <- file.path(tables_dir, "forrester_system_dynamics_summary.csv")

if (!file.exists(timeseries_path)) {
  stop(paste("Missing forrester_system_dynamics_timeseries.csv at", timeseries_path, "Run the Python workflow first."))
}

sd <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(sd, sd$scenario), function(df) df[nrow(df), ])
)

avg_backlog <- aggregate(backlog_stock ~ scenario, data = sd, FUN = mean)
avg_resistance <- aggregate(resistance_index ~ scenario, data = sd, FUN = mean)
avg_performance <- aggregate(system_performance ~ scenario, data = sd, FUN = mean)
max_correction <- aggregate(corrective_action ~ scenario, data = sd, FUN = max)

names(avg_backlog)[2] <- "average_backlog_stock"
names(avg_resistance)[2] <- "average_policy_resistance_index"
names(avg_performance)[2] <- "average_system_performance"
names(max_correction)[2] <- "maximum_corrective_action"

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_backlog, avg_resistance, avg_performance, max_correction)
)

final_fields <- last_by_scenario[, c(
  "scenario",
  "backlog_stock",
  "capacity_stock",
  "trust_stock",
  "institutional_learning_stock",
  "system_performance"
)]

names(final_fields) <- c(
  "scenario",
  "final_backlog_stock",
  "final_capacity_stock",
  "final_trust_stock",
  "final_institutional_learning_stock",
  "final_system_performance"
)

diagnostics <- merge(diagnostics, final_fields, by = "scenario")

diagnostics$diagnostic <- ifelse(
  diagnostics$average_system_performance >= 65 &
    diagnostics$final_backlog_stock <= 45,
  "structural improvement pathway",
  ifelse(
    diagnostics$average_policy_resistance_index >= 35,
    "high policy resistance and delayed correction",
    "partial improvement requiring deeper feedback redesign"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(sd$scenario)
  plot(
    NA,
    xlim = range(sd$period),
    ylim = range(sd[[metric]], na.rm = TRUE),
    xlab = "Period",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- sd[sd$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("backlog_stock", "Backlog stock", "Backlog Stock by Scenario", "backlog_stock_trajectories.png")
plot_metric("capacity_stock", "Capacity stock", "Capacity Stock by Scenario", "capacity_stock_trajectories.png")
plot_metric("corrective_action", "Corrective action", "Corrective Action by Scenario", "corrective_action_trajectories.png")
plot_metric("resistance_index", "Policy resistance index", "Policy Resistance by Scenario", "policy_resistance_trajectories.png")
plot_metric("trust_stock", "Trust stock", "Trust Stock by Scenario", "trust_stock_trajectories.png")
plot_metric("institutional_learning_stock", "Institutional learning stock", "Institutional Learning by Scenario", "institutional_learning_trajectories.png")
plot_metric("system_performance", "System performance", "System Performance by Scenario", "system_performance_trajectories.png")

final_table <- last_by_scenario[, c(
  "scenario",
  "backlog_stock",
  "capacity_stock",
  "perceived_backlog",
  "corrective_action",
  "investment_flow",
  "service_flow",
  "resistance_index",
  "trust_stock",
  "institutional_learning_stock",
  "system_performance"
)]

write.csv(
  final_table,
  file.path(tables_dir, "forrester_system_dynamics_final_diagnostics.csv"),
  row.names = FALSE
)

print(final_table)
