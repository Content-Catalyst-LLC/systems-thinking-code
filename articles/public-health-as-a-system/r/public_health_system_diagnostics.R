# Base R public health systems workflow.
# Purpose: summarize public health scenarios and visualize disease, trust, capacity, and risk trajectories.
# Uses only base R and assumes the working directory is the article root.

root <- normalizePath(getwd(), mustWork = FALSE)
if (basename(root) == "r") {
  root <- normalizePath(file.path(root, ".."), mustWork = FALSE)
  setwd(root)
}

tables_dir <- file.path(root, "outputs", "tables")
figures_dir <- file.path(root, "outputs", "figures")

if (!dir.exists(tables_dir)) dir.create(tables_dir, recursive = TRUE)
if (!dir.exists(figures_dir)) dir.create(figures_dir, recursive = TRUE)

timeseries_path <- file.path(tables_dir, "public_health_system_timeseries.csv")
summary_path <- file.path(tables_dir, "public_health_system_summary_from_r.csv")

if (!file.exists(timeseries_path)) {
  stop(paste0("Missing ", timeseries_path, ". Run the Python workflow first."))
}

health <- read.csv(timeseries_path, stringsAsFactors = FALSE)

required_columns <- c(
  "week", "scenario", "infected", "care_stress", "public_trust",
  "health_risk_index", "prevention_value_index"
)
missing_columns <- setdiff(required_columns, names(health))
if (length(missing_columns) > 0) {
  stop(paste("Missing required columns:", paste(missing_columns, collapse = ", ")))
}

peak_infected <- aggregate(infected ~ scenario, data = health, FUN = max)
peak_care_stress <- aggregate(care_stress ~ scenario, data = health, FUN = max)
average_trust <- aggregate(public_trust ~ scenario, data = health, FUN = mean)
average_risk <- aggregate(health_risk_index ~ scenario, data = health, FUN = mean)

names(peak_infected)[2] <- "peak_infected"
names(peak_care_stress)[2] <- "peak_care_stress"
names(average_trust)[2] <- "average_public_trust"
names(average_risk)[2] <- "average_health_risk_index"

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(peak_infected, peak_care_stress, average_trust, average_risk)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$peak_care_stress >= 1.25,
  "system overload risk",
  ifelse(
    diagnostics$average_health_risk_index >= 35,
    "moderate public health stress",
    "comparatively resilient public health pathway"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(health$scenario)
  plot(
    NA,
    xlim = range(health$week),
    ylim = range(health[[metric]], na.rm = TRUE),
    xlab = "Week",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- health[health$scenario == scenario_name, ]
    lines(subset_data$week, subset_data[[metric]], lwd = 2)
  }
  legend("topright", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("infected", "Infected population", "Infection Trajectories by Public Health Scenario", "public_health_infection_trajectories.png")
plot_metric("care_stress", "Care stress ratio", "Healthcare Capacity Stress by Scenario", "public_health_care_stress_trajectories.png")
plot_metric("public_trust", "Public trust index", "Public Trust Trajectories by Scenario", "public_health_trust_trajectories.png")
plot_metric("health_risk_index", "Health risk index", "Population Health Risk by Scenario", "public_health_risk_trajectories.png")
plot_metric("prevention_value_index", "Prevention value index", "Prevention Value by Scenario", "public_health_prevention_value_trajectories.png")

overload_table <- data.frame()
for (scenario_name in unique(health$scenario)) {
  subset_data <- health[health$scenario == scenario_name, ]
  overload_table <- rbind(
    overload_table,
    data.frame(
      scenario = scenario_name,
      overload_weeks = sum(subset_data$care_stress > 1.0),
      peak_care_stress = max(subset_data$care_stress, na.rm = TRUE),
      minimum_public_trust = min(subset_data$public_trust, na.rm = TRUE),
      final_prevention_value_index = tail(subset_data$prevention_value_index, 1)
    )
  )
}

write.csv(
  overload_table,
  file.path(tables_dir, "public_health_overload_trust_diagnostics.csv"),
  row.names = FALSE
)

print(overload_table)
