# Base R network dependency and cascade-risk diagnostics.
# Uses safe article-root handling and no external packages.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- "--file="
script_path <- NULL
match <- grep(file_arg, args, value = TRUE)
if (length(match) > 0) {
  script_path <- normalizePath(sub(file_arg, "", match[1]), mustWork = FALSE)
}

if (!is.null(script_path) && nzchar(script_path)) {
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
} else {
  wd <- getwd()
  article_root <- if (basename(wd) == "r") normalizePath(file.path(wd, ".."), mustWork = FALSE) else wd
}

setwd(article_root)

tables_dir <- file.path("outputs", "tables")
figures_dir <- file.path("outputs", "figures")
if (!dir.exists(figures_dir)) {
  dir.create(figures_dir, recursive = TRUE)
}

criticality_path <- file.path(tables_dir, "network_node_criticality.csv")
cascade_path <- file.path(tables_dir, "network_cascade_timeseries.csv")
summary_path <- file.path(tables_dir, "network_cascade_summary_r.csv")

if (!file.exists(criticality_path)) {
  stop("Missing network_node_criticality.csv. Run the Python workflow first.")
}
if (!file.exists(cascade_path)) {
  stop("Missing network_cascade_timeseries.csv. Run the Python workflow first.")
}

nodes <- read.csv(criticality_path, stringsAsFactors = FALSE)
cascade <- read.csv(cascade_path, stringsAsFactors = FALSE)

node_rank <- nodes[order(-nodes$criticality_index), ]
write.csv(node_rank, file.path(tables_dir, "network_node_criticality_ranked_r.csv"), row.names = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(cascade, cascade$scenario), function(df) df[nrow(df), ])
)

last_by_scenario$diagnostic <- ifelse(
  last_by_scenario$failed_count >= 8,
  "high cascade risk",
  ifelse(last_by_scenario$failed_count >= 4, "moderate cascade risk", "contained disruption")
)

write.csv(last_by_scenario, summary_path, row.names = FALSE)
print(last_by_scenario)

png(file.path(figures_dir, "network_node_criticality_rank.png"), width = 1200, height = 700)
barplot(
  height = node_rank$criticality_index,
  names.arg = node_rank$node_id,
  las = 2,
  cex.names = 0.72,
  main = "Network Node Criticality",
  ylab = "Criticality index"
)
grid()
dev.off()

png(file.path(figures_dir, "dependency_exposure_rank.png"), width = 1200, height = 700)
exposure_rank <- nodes[order(-nodes$dependency_exposure_score), ]
barplot(
  height = exposure_rank$dependency_exposure_score,
  names.arg = exposure_rank$node_id,
  las = 2,
  cex.names = 0.72,
  main = "Dependency Exposure by Node",
  ylab = "Dependency exposure score"
)
grid()
dev.off()

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(cascade$scenario)
  plot(
    NA,
    xlim = range(cascade$step),
    ylim = range(cascade[[metric]], na.rm = TRUE),
    xlab = "Cascade step",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- cascade[cascade$scenario == scenario_name, ]
    lines(subset_data$step, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("failed_count", "Failed node count", "Cascade Failure Count by Scenario", "cascade_failed_count_trajectories.png")
plot_metric("service_loss_index", "Service loss index", "Service Loss by Cascade Scenario", "cascade_service_loss_trajectories.png")

category_summary <- aggregate(
  cbind(criticality_index, dependency_exposure_score, bridge_approximation_score) ~ category,
  data = nodes,
  FUN = mean
)

write.csv(category_summary, file.path(tables_dir, "network_category_risk_summary_r.csv"), row.names = FALSE)
print(category_summary)
