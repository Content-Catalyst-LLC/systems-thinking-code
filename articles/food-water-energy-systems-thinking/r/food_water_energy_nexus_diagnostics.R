#!/usr/bin/env Rscript
# Base R food-water-energy systems workflow.
# Purpose: summarize nexus scenario results and visualize resource stress trajectories.
# Dependency policy: base R only. No tidyverse/readr/ggplot2 required.

resolve_article_root <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)

  if (length(file_arg) > 0) {
    script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
    candidate <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
    if (basename(candidate) == "food-water-energy-systems-thinking") {
      return(candidate)
    }
  }

  current <- normalizePath(getwd(), mustWork = TRUE)
  if (basename(current) == "food-water-energy-systems-thinking") {
    return(current)
  }

  parent_candidate <- normalizePath(file.path(current, ".."), mustWork = FALSE)
  if (basename(parent_candidate) == "food-water-energy-systems-thinking") {
    return(parent_candidate)
  }

  stop("Could not resolve article root. Run from the article root or through r/run_all_nexus_workflows.R.")
}

root_dir <- resolve_article_root()
setwd(root_dir)

tables_dir <- "outputs/tables"
figures_dir <- "outputs/figures"

if (!dir.exists(tables_dir)) {
  dir.create(tables_dir, recursive = TRUE)
}
if (!dir.exists(figures_dir)) {
  dir.create(figures_dir, recursive = TRUE)
}

timeseries_path <- file.path(tables_dir, "food_water_energy_nexus_timeseries.csv")
summary_path <- file.path(tables_dir, "food_water_energy_nexus_summary_r.csv")

if (!file.exists(timeseries_path)) {
  stop("Missing food_water_energy_nexus_timeseries.csv. Run: python3 python/run_all_nexus_workflows.py")
}

nexus <- read.csv(timeseries_path, stringsAsFactors = FALSE)
required_columns <- c(
  "year",
  "scenario",
  "groundwater_stock",
  "food_production_index",
  "water_security_index",
  "energy_security_index",
  "soil_health",
  "nexus_stress_index",
  "resilience_index"
)
missing_columns <- setdiff(required_columns, names(nexus))
if (length(missing_columns) > 0) {
  stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
}

last_by_scenario <- do.call(
  rbind,
  lapply(split(nexus, nexus$scenario), function(df) df[nrow(df), ])
)

stress_summary <- aggregate(
  cbind(nexus_stress_index, resilience_index) ~ scenario,
  data = nexus,
  FUN = mean
)

names(stress_summary)[2:3] <- c("average_nexus_stress_index", "average_resilience_index")

diagnostics <- merge(
  last_by_scenario[, c(
    "scenario",
    "groundwater_stock",
    "food_production_index",
    "water_security_index",
    "energy_security_index",
    "soil_health"
  )],
  stress_summary,
  by = "scenario"
)

diagnostics$diagnostic <- ifelse(
  diagnostics$average_nexus_stress_index >= 60,
  "high nexus fragility",
  ifelse(
    diagnostics$average_nexus_stress_index >= 40,
    "moderate stress requiring redesign",
    "comparatively resilient pathway"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  output_path <- file.path(figures_dir, output_name)
  png(output_path, width = 1200, height = 700)
  on.exit(dev.off(), add = TRUE)

  scenarios <- unique(nexus$scenario)
  metric_range <- range(nexus[[metric]], na.rm = TRUE)
  if (!all(is.finite(metric_range)) || metric_range[1] == metric_range[2]) {
    metric_range <- c(0, 100)
  }

  plot(
    NA,
    xlim = range(nexus$year, na.rm = TRUE),
    ylim = metric_range,
    xlab = "Year",
    ylab = y_label,
    main = title
  )

  for (scenario_name in scenarios) {
    subset_data <- nexus[nexus$scenario == scenario_name, ]
    lines(subset_data$year, subset_data[[metric]], lwd = 2)
  }

  legend("topright", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
}

plot_metric(
  metric = "groundwater_stock",
  y_label = "Groundwater stock",
  title = "Groundwater Stock by Food-Water-Energy Scenario",
  output_name = "nexus_groundwater_trajectories.png"
)

plot_metric(
  metric = "food_production_index",
  y_label = "Food production index",
  title = "Food Production by Nexus Scenario",
  output_name = "nexus_food_production_trajectories.png"
)

plot_metric(
  metric = "energy_security_index",
  y_label = "Energy security index",
  title = "Energy Security by Nexus Scenario",
  output_name = "nexus_energy_security_trajectories.png"
)

plot_metric(
  metric = "nexus_stress_index",
  y_label = "Nexus stress index",
  title = "Food-Water-Energy Nexus Stress by Scenario",
  output_name = "nexus_stress_trajectories.png"
)

plot_metric(
  metric = "resilience_index",
  y_label = "Resilience index",
  title = "Nexus Resilience by Scenario",
  output_name = "nexus_resilience_trajectories.png"
)

tradeoff_table <- data.frame()
for (scenario_name in unique(nexus$scenario)) {
  subset_data <- nexus[nexus$scenario == scenario_name, ]
  final_row <- subset_data[nrow(subset_data), ]

  tradeoff_table <- rbind(
    tradeoff_table,
    data.frame(
      scenario = scenario_name,
      final_groundwater_stock = final_row$groundwater_stock,
      final_food_production_index = final_row$food_production_index,
      final_water_security_index = final_row$water_security_index,
      final_energy_security_index = final_row$energy_security_index,
      final_nexus_stress_index = final_row$nexus_stress_index,
      final_resilience_index = final_row$resilience_index
    )
  )
}

write.csv(
  tradeoff_table,
  file.path(tables_dir, "food_water_energy_tradeoff_diagnostics.csv"),
  row.names = FALSE
)

cat("\nFood-water-energy R diagnostics completed.\n")
cat("Tables written to:", normalizePath(tables_dir), "\n")
cat("Figures written to:", normalizePath(figures_dir), "\n")
print(tradeoff_table)
