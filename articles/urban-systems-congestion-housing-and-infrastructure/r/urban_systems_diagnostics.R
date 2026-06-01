# Base R urban systems diagnostics.
# Reads Python-generated urban_systems_timeseries.csv and exports summaries and figures.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = FALSE)
  root_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
} else {
  cwd <- normalizePath(getwd(), mustWork = FALSE)
  if (basename(cwd) == "r") {
    root_dir <- normalizePath(file.path(cwd, ".."), mustWork = FALSE)
  } else {
    root_dir <- cwd
  }
}

tables_dir <- file.path(root_dir, "outputs", "tables")
figures_dir <- file.path(root_dir, "outputs", "figures")
if (!dir.exists(figures_dir)) dir.create(figures_dir, recursive = TRUE)

timeseries_path <- file.path(tables_dir, "urban_systems_timeseries.csv")
summary_path <- file.path(tables_dir, "urban_systems_r_summary.csv")

if (!file.exists(timeseries_path)) {
  stop("Missing urban_systems_timeseries.csv. Run the Python workflow first.")
}

urban <- read.csv(timeseries_path, stringsAsFactors = FALSE)

avg_congestion <- aggregate(congestion_index ~ scenario, data = urban, FUN = mean)
avg_affordability <- aggregate(affordability_index ~ scenario, data = urban, FUN = mean)
avg_resilience <- aggregate(urban_resilience_index ~ scenario, data = urban, FUN = mean)
min_infrastructure <- aggregate(infrastructure_condition ~ scenario, data = urban, FUN = min)
max_displacement <- aggregate(displacement_pressure ~ scenario, data = urban, FUN = max)

names(avg_congestion)[2] <- "average_congestion_index"
names(avg_affordability)[2] <- "average_affordability_index"
names(avg_resilience)[2] <- "average_urban_resilience_index"
names(min_infrastructure)[2] <- "minimum_infrastructure_condition"
names(max_displacement)[2] <- "maximum_displacement_pressure"

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_congestion, avg_affordability, avg_resilience, min_infrastructure, max_displacement)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$average_urban_resilience_index < 35 |
    diagnostics$minimum_infrastructure_condition < 30,
  "high urban fragility",
  ifelse(
    diagnostics$average_congestion_index > 55 |
      diagnostics$average_affordability_index < 45,
    "moderate stress requiring redesign",
    "comparatively resilient urban pathway"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(urban$scenario)
  plot(
    NA,
    xlim = range(urban$year),
    ylim = range(urban[[metric]], na.rm = TRUE),
    xlab = "Year",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- urban[urban$scenario == scenario_name, ]
    lines(subset_data$year, subset_data[[metric]], lwd = 2)
  }
  legend("topright", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("congestion_index", "Congestion index", "Congestion Trajectories by Urban Scenario", "urban_congestion_trajectories.png")
plot_metric("affordability_index", "Affordability index", "Housing-Transport Affordability by Urban Scenario", "urban_affordability_trajectories.png")
plot_metric("infrastructure_condition", "Infrastructure condition", "Infrastructure Condition by Urban Scenario", "urban_infrastructure_condition_trajectories.png")
plot_metric("displacement_pressure", "Displacement pressure", "Displacement Pressure by Urban Scenario", "urban_displacement_pressure_trajectories.png")
plot_metric("access_index", "Access index", "Urban Access by Scenario", "urban_access_trajectories.png")
plot_metric("urban_resilience_index", "Urban resilience index", "Urban Resilience by Scenario", "urban_resilience_trajectories.png")

tradeoff_table <- data.frame()
for (scenario_name in unique(urban$scenario)) {
  subset_data <- urban[urban$scenario == scenario_name, ]
  final_row <- subset_data[nrow(subset_data), ]
  tradeoff_table <- rbind(
    tradeoff_table,
    data.frame(
      scenario = scenario_name,
      final_congestion_index = final_row$congestion_index,
      final_affordability_index = final_row$affordability_index,
      final_infrastructure_condition = final_row$infrastructure_condition,
      final_displacement_pressure = final_row$displacement_pressure,
      final_access_index = final_row$access_index,
      final_urban_resilience_index = final_row$urban_resilience_index
    )
  )
}

write.csv(tradeoff_table, file.path(tables_dir, "urban_systems_tradeoff_diagnostics.csv"), row.names = FALSE)
print(tradeoff_table)
