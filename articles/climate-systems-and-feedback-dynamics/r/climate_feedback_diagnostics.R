#!/usr/bin/env Rscript
# Base R climate systems workflow.
# Reads default Python outputs and creates trajectory figures and diagnostic tables.

root <- normalizePath(file.path(dirname(commandArgs(trailingOnly = FALSE)[grep("--file=", commandArgs(trailingOnly = FALSE))][1]), ".."), mustWork = FALSE)
if (is.na(root) || grepl("NA", root)) {
  root <- getwd()
}

tables_dir <- file.path(root, "outputs", "tables")
figures_dir <- file.path(root, "outputs", "figures")
if (!dir.exists(figures_dir)) dir.create(figures_dir, recursive = TRUE)

timeseries_path <- file.path(tables_dir, "climate_feedback_scenario_timeseries.csv")
summary_path <- file.path(tables_dir, "climate_feedback_scenario_summary.csv")

if (!file.exists(timeseries_path)) {
  stop("Missing climate_feedback_scenario_timeseries.csv. Run the Python workflow first.")
}

climate <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(rbind, lapply(split(climate, climate$scenario), function(df) df[nrow(df), ]))
cumulative <- aggregate(emissions_gtco2 ~ scenario, data = climate, sum)
names(cumulative)[2] <- "cumulative_emissions_gtco2"

diagnostics <- merge(
  last_by_scenario[, c("scenario", "co2_ppm", "temperature_anomaly_c", "risk_index")],
  cumulative,
  by = "scenario"
)
diagnostics$diagnostic <- ifelse(
  diagnostics$temperature_anomaly_c >= 2.5,
  "high warming and adaptation risk",
  ifelse(diagnostics$temperature_anomaly_c >= 2.0, "threshold warning", "lower-risk transition pathway")
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(climate$scenario)
  yrange <- range(climate[[metric]], na.rm = TRUE)
  plot(
    NA,
    xlim = range(climate$year),
    ylim = yrange,
    xlab = "Year",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- climate[climate$scenario == scenario_name, ]
    lines(subset_data$year, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.75, bty = "n")
  grid()
  dev.off()
}

plot_metric("emissions_gtco2", "Annual emissions (GtCO2)", "Emissions Trajectories by Climate Scenario", "climate_emissions_trajectories.png")
plot_metric("co2_ppm", "Atmospheric CO2 concentration (ppm)", "Atmospheric CO2 Stock Trajectories", "climate_co2_stock_trajectories.png")
plot_metric("temperature_anomaly_c", "Temperature anomaly (°C)", "Simplified Temperature Response by Scenario", "climate_temperature_trajectories.png")
plot_metric("risk_index", "Climate risk index", "Climate Risk Trajectories by Scenario", "climate_risk_trajectories.png")

threshold_table <- data.frame()
for (scenario_name in unique(climate$scenario)) {
  subset_data <- climate[climate$scenario == scenario_name, ]
  above_2c <- subset_data[subset_data$temperature_anomaly_c >= 2.0, ]
  first_year_above_2c <- if (nrow(above_2c) == 0) NA else min(above_2c$year)
  threshold_table <- rbind(
    threshold_table,
    data.frame(
      scenario = scenario_name,
      first_year_above_2c = first_year_above_2c,
      final_temperature_anomaly_c = tail(subset_data$temperature_anomaly_c, 1),
      maximum_risk_index = max(subset_data$risk_index, na.rm = TRUE)
    )
  )
}

write.csv(threshold_table, file.path(tables_dir, "climate_threshold_diagnostics.csv"), row.names = FALSE)
print(threshold_table)
