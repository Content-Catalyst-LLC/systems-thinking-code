# complex_adaptive_social_change_diagnostics.R
# Base R workflow for complex adaptive systems and social change.

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

timeseries_path <- file.path(tables_dir, "complex_adaptive_social_change_timeseries.csv")
summary_path <- file.path(tables_dir, "complex_adaptive_social_change_summary.csv")

if (!file.exists(timeseries_path)) {
  stop(paste("Missing complex_adaptive_social_change_timeseries.csv at", timeseries_path, "Run the Python workflow first."))
}

social <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(social, social$scenario), function(df) df[nrow(df), ])
)

avg_momentum <- aggregate(transformation_momentum ~ scenario, data = social, FUN = mean)
peak_resistance <- aggregate(resistance_index ~ scenario, data = social, FUN = max)
final_adoption <- last_by_scenario[, c("scenario", "adoption_index")]
final_legitimacy <- last_by_scenario[, c("scenario", "legitimacy_index")]
final_learning <- last_by_scenario[, c("scenario", "learning_capacity_index")]

names(avg_momentum)[2] <- "average_transformation_momentum"
names(peak_resistance)[2] <- "peak_resistance_index"
names(final_adoption)[2] <- "final_adoption_index"
names(final_legitimacy)[2] <- "final_legitimacy_index"
names(final_learning)[2] <- "final_learning_capacity_index"

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_momentum, peak_resistance, final_adoption, final_legitimacy, final_learning)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$final_adoption_index >= 70 &
    diagnostics$final_legitimacy_index >= 60,
  "transformational pathway",
  ifelse(
    diagnostics$peak_resistance_index >= 55,
    "contested change requiring deeper coalition and governance learning",
    "limited diffusion pathway"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(social$scenario)
  plot(
    NA,
    xlim = range(social$period),
    ylim = range(social[[metric]], na.rm = TRUE),
    xlab = "Period",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- social[social$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("adoption_index", "Adoption index", "Social Adoption by Scenario", "social_adoption_trajectories.png")
plot_metric("trust_index", "Trust index", "Trust by Social Change Scenario", "social_trust_trajectories.png")
plot_metric("resistance_index", "Resistance index", "Resistance by Scenario", "social_resistance_trajectories.png")
plot_metric("institutional_response_index", "Institutional response index", "Institutional Response by Scenario", "institutional_response_trajectories.png")
plot_metric("learning_capacity_index", "Learning capacity index", "Learning Capacity by Scenario", "learning_capacity_trajectories.png")
plot_metric("legitimacy_index", "Legitimacy index", "Legitimacy by Social Change Scenario", "legitimacy_trajectories.png")
plot_metric("transformation_momentum", "Transformation momentum", "Transformation Momentum by Scenario", "transformation_momentum_trajectories.png")

final_table <- last_by_scenario[, c(
  "scenario",
  "adoption_index",
  "trust_index",
  "resistance_index",
  "institutional_response_index",
  "movement_capacity_index",
  "learning_capacity_index",
  "legitimacy_index",
  "transformation_momentum"
)]

write.csv(
  final_table,
  file.path(tables_dir, "complex_adaptive_social_change_final_diagnostics.csv"),
  row.names = FALSE
)

print(final_table)
