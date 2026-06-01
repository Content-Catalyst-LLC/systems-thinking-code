# intelligent_infrastructure_system_diagnostics.R
# Base R workflow for intelligent infrastructure systems.
# Uses robust article-root detection so it works from Terminal, runners, or Rscript.

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

timeseries_path <- file.path(tables_dir, "intelligent_infrastructure_timeseries.csv")
summary_path <- file.path(tables_dir, "intelligent_infrastructure_summary.csv")

if (!file.exists(timeseries_path)) {
  stop(paste("Missing intelligent_infrastructure_timeseries.csv at", timeseries_path, "Run the Python workflow first."))
}

infra <- read.csv(timeseries_path, stringsAsFactors = FALSE)

final_year <- max(infra$year)
final_rows <- infra[infra$year == final_year, ]

avg_risk <- aggregate(risk_score ~ scenario, data = final_rows, FUN = mean)
avg_resilience <- aggregate(resilience_score ~ scenario, data = final_rows, FUN = mean)
max_cyber <- aggregate(cyber_physical_dependency ~ scenario, data = final_rows, FUN = max)
high_risk <- aggregate(risk_score ~ scenario, data = final_rows, FUN = function(x) sum(x >= 55))
low_resilience <- aggregate(resilience_score ~ scenario, data = final_rows, FUN = function(x) sum(x <= 45))

names(avg_risk)[2] <- "final_average_risk_score"
names(avg_resilience)[2] <- "final_average_resilience_score"
names(max_cyber)[2] <- "maximum_cyber_physical_dependency"
names(high_risk)[2] <- "high_risk_asset_count"
names(low_resilience)[2] <- "low_resilience_asset_count"

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_risk, avg_resilience, max_cyber, high_risk, low_resilience)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$high_risk_asset_count >= 4 |
    diagnostics$final_average_resilience_score < 42,
  "high infrastructure fragility",
  ifelse(
    diagnostics$final_average_risk_score >= 42 |
      diagnostics$maximum_cyber_physical_dependency >= 60,
    "moderate risk requiring governance and maintenance redesign",
    "comparatively resilient intelligent infrastructure pathway"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  yearly <- aggregate(infra[[metric]], by = list(year = infra$year, scenario = infra$scenario), FUN = mean)
  names(yearly)[3] <- metric

  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(yearly$scenario)
  plot(
    NA,
    xlim = range(yearly$year),
    ylim = range(yearly[[metric]], na.rm = TRUE),
    xlab = "Year",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- yearly[yearly$scenario == scenario_name, ]
    lines(subset_data$year, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric(
  metric = "risk_score",
  y_label = "Average risk score",
  title = "Infrastructure Risk by Scenario",
  output_name = "infrastructure_risk_trajectories.png"
)

plot_metric(
  metric = "resilience_score",
  y_label = "Average resilience score",
  title = "Infrastructure Resilience by Scenario",
  output_name = "infrastructure_resilience_trajectories.png"
)

plot_metric(
  metric = "cyber_physical_dependency",
  y_label = "Average cyber-physical dependency",
  title = "Cyber-Physical Dependency by Scenario",
  output_name = "cyber_physical_dependency_trajectories.png"
)

plot_metric(
  metric = "condition",
  y_label = "Average asset condition",
  title = "Asset Condition by Scenario",
  output_name = "asset_condition_trajectories.png"
)

plot_metric(
  metric = "maintenance_action_score",
  y_label = "Average maintenance action score",
  title = "Maintenance Action by Scenario",
  output_name = "maintenance_action_trajectories.png"
)

asset_rank <- final_rows[order(-final_rows$risk_score), c(
  "scenario",
  "asset_id",
  "category",
  "condition",
  "risk_score",
  "resilience_score",
  "cyber_physical_dependency",
  "maintenance_action_score",
  "equity_priority"
)]

write.csv(
  asset_rank,
  file.path(tables_dir, "intelligent_infrastructure_asset_risk_rank.csv"),
  row.names = FALSE
)

category_summary <- aggregate(
  cbind(risk_score, resilience_score, cyber_physical_dependency, maintenance_action_score) ~ scenario + category,
  data = final_rows,
  FUN = mean
)

write.csv(
  category_summary,
  file.path(tables_dir, "intelligent_infrastructure_category_summary.csv"),
  row.names = FALSE
)

print(asset_rank)
print(category_summary)
