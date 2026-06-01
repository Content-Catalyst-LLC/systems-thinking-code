# systems_thinking_age_complexity_diagnostics.R
# Base R workflow for Systems Thinking in an Age of Complexity.

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

timeseries_path <- file.path(tables_dir, "systems_thinking_age_complexity_timeseries.csv")
summary_path <- file.path(tables_dir, "systems_thinking_age_complexity_summary.csv")

if (!file.exists(timeseries_path)) {
  stop(paste("Missing systems_thinking_age_complexity_timeseries.csv at", timeseries_path, "Run the Python workflow first."))
}

complexity <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(complexity, complexity$scenario), function(df) df[nrow(df), ])
)

avg_complexity <- aggregate(complexity_pressure ~ scenario, data = complexity, FUN = mean)
avg_readiness <- aggregate(systems_readiness_score ~ scenario, data = complexity, FUN = mean)
avg_harm <- aggregate(harm_stock ~ scenario, data = complexity, FUN = mean)
avg_accountability <- aggregate(accountability_score ~ scenario, data = complexity, FUN = mean)

names(avg_complexity)[2] <- "average_complexity_pressure"
names(avg_readiness)[2] <- "average_systems_readiness_score"
names(avg_harm)[2] <- "average_harm_stock"
names(avg_accountability)[2] <- "average_accountability_score"

final_fields <- last_by_scenario[, c(
  "scenario",
  "systems_readiness_score",
  "complexity_pressure",
  "harm_stock",
  "resilience_stock",
  "learning_stock",
  "accountability_score",
  "transformation_capacity"
)]

names(final_fields) <- c(
  "scenario",
  "final_systems_readiness_score",
  "final_complexity_pressure",
  "final_harm_stock",
  "final_resilience_stock",
  "final_learning_stock",
  "final_accountability_score",
  "final_transformation_capacity"
)

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_complexity, avg_readiness, avg_harm, avg_accountability, final_fields)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$final_systems_readiness_score >= 65 &
    diagnostics$final_harm_stock <= 35,
  "accountable transformation pathway",
  ifelse(
    diagnostics$average_complexity_pressure >= 65 &
      diagnostics$average_systems_readiness_score <= 45,
    "complexity exceeds institutional response capacity",
    ifelse(
      diagnostics$average_harm_stock >= 55,
      "high harm accumulation requiring boundary and repair redesign",
      ifelse(
        diagnostics$average_accountability_score >= 55,
        "partial readiness with remaining complexity risk",
        "fragmented or brittle systems capacity"
      )
    )
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
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("complexity_pressure", "Complexity pressure", "Complexity Pressure by Scenario", "complexity_pressure_trajectories.png")
plot_metric("resilience_capacity", "Resilience capacity", "Resilience Capacity by Scenario", "resilience_capacity_trajectories.png")
plot_metric("feedback_amplification", "Feedback amplification", "Feedback Amplification by Scenario", "feedback_amplification_trajectories.png")
plot_metric("accountability_score", "Accountability score", "Accountability by Scenario", "accountability_trajectories.png")
plot_metric("harm_stock", "Harm stock", "Harm Stock by Scenario", "harm_stock_trajectories.png")
plot_metric("learning_stock", "Learning stock", "Learning Stock by Scenario", "learning_stock_trajectories.png")
plot_metric("trust_stock", "Trust stock", "Trust by Scenario", "trust_trajectories.png")
plot_metric("transformation_capacity", "Transformation capacity", "Transformation Capacity by Scenario", "transformation_capacity_trajectories.png")
plot_metric("systems_readiness_score", "Systems readiness score", "Systems Readiness by Scenario", "systems_readiness_trajectories.png")

final_table <- last_by_scenario[, c(
  "scenario",
  "complexity_pressure",
  "resilience_capacity",
  "feedback_amplification",
  "accountability_score",
  "harm_pressure",
  "resilience_stock",
  "learning_stock",
  "trust_stock",
  "accountability_memory",
  "harm_stock",
  "transformation_capacity",
  "systems_readiness_score"
)]

write.csv(
  final_table,
  file.path(tables_dir, "systems_thinking_age_complexity_final_diagnostics.csv"),
  row.names = FALSE
)

print(final_table)
