# ethical_systems_thinking_diagnostics.R
# Base R workflow for The Ethics of Systems Thinking.

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

timeseries_path <- file.path(tables_dir, "ethical_systems_thinking_timeseries.csv")
summary_path <- file.path(tables_dir, "ethical_systems_thinking_summary.csv")

if (!file.exists(timeseries_path)) {
  stop(paste("Missing ethical_systems_thinking_timeseries.csv at", timeseries_path, "Run the Python workflow first."))
}

ethics <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(ethics, ethics$scenario), function(df) df[nrow(df), ])
)

avg_harm <- aggregate(cumulative_harm ~ scenario, data = ethics, FUN = mean)
avg_accountability <- aggregate(accountability_index ~ scenario, data = ethics, FUN = mean)
avg_score <- aggregate(ethical_system_score ~ scenario, data = ethics, FUN = mean)
avg_model_risk <- aggregate(model_risk ~ scenario, data = ethics, FUN = mean)

names(avg_harm)[2] <- "average_cumulative_harm"
names(avg_accountability)[2] <- "average_accountability_index"
names(avg_score)[2] <- "average_ethical_system_score"
names(avg_model_risk)[2] <- "average_model_risk"

final_fields <- last_by_scenario[, c(
  "scenario",
  "ethical_system_score",
  "cumulative_harm",
  "accountability_index",
  "boundary_ethics_score",
  "repair_stock",
  "model_risk"
)]

names(final_fields) <- c(
  "scenario",
  "final_ethical_system_score",
  "final_cumulative_harm",
  "final_accountability_index",
  "final_boundary_ethics_score",
  "final_repair_stock",
  "final_model_risk"
)

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_harm, avg_accountability, avg_score, avg_model_risk, final_fields)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$final_ethical_system_score >= 65 &
    diagnostics$final_cumulative_harm <= 35,
  "ethically accountable systems pathway",
  ifelse(
    diagnostics$average_cumulative_harm >= 55 |
      diagnostics$average_model_risk >= 50,
    "high ethical risk requiring boundary and accountability redesign",
    ifelse(
      diagnostics$average_accountability_index >= 55,
      "partial accountability with remaining harm risk",
      "weak ethical systems capacity"
    )
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(ethics$scenario)
  plot(
    NA,
    xlim = range(ethics$period),
    ylim = range(ethics[[metric]], na.rm = TRUE),
    xlab = "Period",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- ethics[ethics$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("boundary_ethics_score", "Boundary ethics score", "Boundary Ethics by Scenario", "boundary_ethics_trajectories.png")
plot_metric("accountability_index", "Accountability index", "Accountability by Scenario", "accountability_trajectories.png")
plot_metric("cumulative_harm", "Cumulative harm", "Cumulative Harm by Scenario", "cumulative_harm_trajectories.png")
plot_metric("repair_stock", "Repair stock", "Repair Capacity by Scenario", "repair_stock_trajectories.png")
plot_metric("trust_stock", "Trust stock", "Trust by Scenario", "trust_trajectories.png")
plot_metric("ethical_leverage", "Ethical leverage", "Ethical Leverage by Scenario", "ethical_leverage_trajectories.png")
plot_metric("model_risk", "Model risk", "Model Risk by Scenario", "model_risk_trajectories.png")
plot_metric("ethical_system_score", "Ethical system score", "Ethical System Score by Scenario", "ethical_system_score_trajectories.png")

final_table <- last_by_scenario[, c(
  "scenario",
  "boundary_ethics_score",
  "accountability_index",
  "harm_pressure",
  "cumulative_harm",
  "repair_flow",
  "repair_stock",
  "accountability_memory",
  "trust_stock",
  "ethical_leverage",
  "model_risk",
  "ethical_system_score"
)]

write.csv(
  final_table,
  file.path(tables_dir, "ethical_systems_thinking_final_diagnostics.csv"),
  row.names = FALSE
)

print(final_table)
