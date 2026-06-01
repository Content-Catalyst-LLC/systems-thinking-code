# meadows_structural_insight_diagnostics.R
# Base R workflow for Donella Meadows and structural insight.

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

timeseries_path <- file.path(tables_dir, "meadows_structural_insight_timeseries.csv")
summary_path <- file.path(tables_dir, "meadows_structural_insight_summary.csv")

if (!file.exists(timeseries_path)) {
  stop(paste("Missing meadows_structural_insight_timeseries.csv at", timeseries_path, "Run the Python workflow first."))
}

meadows <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(meadows, meadows$scenario), function(df) df[nrow(df), ])
)

avg_resource <- aggregate(resource_stock ~ scenario, data = meadows, FUN = mean)
min_resource <- aggregate(resource_stock ~ scenario, data = meadows, FUN = min)
avg_overshoot <- aggregate(overshoot_index ~ scenario, data = meadows, FUN = mean)
avg_insight <- aggregate(structural_insight_score ~ scenario, data = meadows, FUN = mean)

names(avg_resource)[2] <- "average_resource_stock"
names(min_resource)[2] <- "minimum_resource_stock"
names(avg_overshoot)[2] <- "average_overshoot_index"
names(avg_insight)[2] <- "average_structural_insight_score"

final_fields <- last_by_scenario[, c(
  "scenario",
  "resource_stock",
  "trust_stock",
  "resilience_capacity",
  "leverage_quality",
  "structural_insight_score"
)]

names(final_fields) <- c(
  "scenario",
  "final_resource_stock",
  "final_trust_stock",
  "final_resilience_capacity",
  "final_leverage_quality",
  "final_structural_insight_score"
)

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_resource, min_resource, avg_overshoot, avg_insight, final_fields)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$final_resource_stock >= 60 &
    diagnostics$average_overshoot_index <= 20 &
    diagnostics$average_structural_insight_score >= 60,
  "structural leverage pathway",
  ifelse(
    diagnostics$average_overshoot_index >= 35 |
      diagnostics$minimum_resource_stock <= 30,
    "overshoot risk requiring deeper leverage",
    "partial improvement with remaining structural risk"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(meadows$scenario)
  plot(
    NA,
    xlim = range(meadows$period),
    ylim = range(meadows[[metric]], na.rm = TRUE),
    xlab = "Period",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- meadows[meadows$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("resource_stock", "Resource stock", "Resource Stock by Scenario", "resource_stock_trajectories.png")
plot_metric("consumption_flow", "Consumption flow", "Consumption Flow by Scenario", "consumption_flow_trajectories.png")
plot_metric("regeneration_flow", "Regeneration flow", "Regeneration Flow by Scenario", "regeneration_flow_trajectories.png")
plot_metric("overshoot_index", "Overshoot index", "Overshoot by Scenario", "overshoot_trajectories.png")
plot_metric("leverage_quality", "Leverage quality", "Leverage Quality by Scenario", "leverage_quality_trajectories.png")
plot_metric("trust_stock", "Trust stock", "Trust Stock by Scenario", "trust_stock_trajectories.png")
plot_metric("resilience_capacity", "Resilience capacity", "Resilience Capacity by Scenario", "resilience_capacity_trajectories.png")
plot_metric("structural_insight_score", "Structural insight score", "Structural Insight by Scenario", "structural_insight_trajectories.png")

final_table <- last_by_scenario[, c(
  "scenario",
  "resource_stock",
  "perceived_resource_stock",
  "consumption_flow",
  "regeneration_flow",
  "overshoot_index",
  "leverage_quality",
  "trust_stock",
  "institutional_learning_stock",
  "resilience_capacity",
  "structural_insight_score"
)]

write.csv(
  final_table,
  file.path(tables_dir, "meadows_structural_insight_final_diagnostics.csv"),
  row.names = FALSE
)

print(final_table)
