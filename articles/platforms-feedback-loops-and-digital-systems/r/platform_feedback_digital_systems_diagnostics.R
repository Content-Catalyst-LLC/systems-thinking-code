# Base R platform systems workflow.
# Purpose: summarize platform feedback, amplification, trust, dependency, governance, and risk scenarios.

resolve_article_root <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- args[grepl("^--file=", args)]
  if (length(file_arg) > 0) {
    script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
    return(normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE))
  }
  normalizePath(getwd(), mustWork = TRUE)
}

ARTICLE_ROOT <- resolve_article_root()
setwd(ARTICLE_ROOT)

tables_dir <- file.path(ARTICLE_ROOT, "outputs", "tables")
figures_dir <- file.path(ARTICLE_ROOT, "outputs", "figures")

if (!dir.exists(figures_dir)) {
  dir.create(figures_dir, recursive = TRUE)
}

timeseries_path <- file.path(tables_dir, "platform_feedback_timeseries.csv")
summary_path <- file.path(tables_dir, "platform_feedback_summary_r.csv")

if (!file.exists(timeseries_path)) {
  stop("Missing platform_feedback_timeseries.csv. Run the Python workflow first.")
}

platform <- read.csv(timeseries_path, stringsAsFactors = FALSE)

last_by_scenario <- do.call(
  rbind,
  lapply(split(platform, platform$scenario), function(df) df[nrow(df), ])
)

avg_risk <- aggregate(platform_risk_index ~ scenario, data = platform, FUN = mean)
max_cascade <- aggregate(harmful_cascade_risk ~ scenario, data = platform, FUN = max)
max_backlog <- aggregate(moderation_backlog ~ scenario, data = platform, FUN = max)
min_trust <- aggregate(user_trust ~ scenario, data = platform, FUN = min)
avg_public_value <- aggregate(public_value_index ~ scenario, data = platform, FUN = mean)

names(avg_risk)[2] <- "average_platform_risk_index"
names(max_cascade)[2] <- "maximum_harmful_cascade_risk"
names(max_backlog)[2] <- "maximum_moderation_backlog"
names(min_trust)[2] <- "minimum_user_trust"
names(avg_public_value)[2] <- "average_public_value_index"

diagnostics <- Reduce(
  function(x, y) merge(x, y, by = "scenario"),
  list(avg_risk, max_cascade, max_backlog, min_trust, avg_public_value)
)

diagnostics$diagnostic <- ifelse(
  diagnostics$average_platform_risk_index >= 40 |
    diagnostics$maximum_harmful_cascade_risk >= 65,
  "high-risk extractive platform pathway",
  ifelse(
    diagnostics$average_platform_risk_index >= 26 |
      diagnostics$maximum_moderation_backlog >= 45,
    "moderate risk requiring governance redesign",
    "comparatively accountable platform pathway"
  )
)

write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(platform$scenario)
  plot(
    NA,
    xlim = range(platform$period),
    ylim = range(platform[[metric]], na.rm = TRUE),
    xlab = "Period",
    ylab = y_label,
    main = title
  )
  for (scenario_name in scenarios) {
    subset_data <- platform[platform$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("engagement_index", "Engagement index", "Engagement by Platform Scenario", "platform_engagement_trajectories.png")
plot_metric("harmful_cascade_risk", "Harmful cascade risk", "Harmful Cascade Risk by Platform Scenario", "platform_harmful_cascade_risk_trajectories.png")
plot_metric("moderation_backlog", "Moderation backlog", "Moderation Backlog by Platform Scenario", "platform_moderation_backlog_trajectories.png")
plot_metric("platform_dependency", "Platform dependency", "Platform Dependency by Scenario", "platform_dependency_trajectories.png")
plot_metric("governance_readiness", "Governance readiness", "Governance Readiness by Platform Scenario", "platform_governance_readiness_trajectories.png")
plot_metric("user_trust", "User trust", "User Trust by Platform Scenario", "platform_user_trust_trajectories.png")
plot_metric("public_value_index", "Public value index", "Public Value by Platform Scenario", "platform_public_value_trajectories.png")
plot_metric("platform_risk_index", "Platform risk index", "Platform Risk by Scenario", "platform_risk_trajectories.png")

final_table <- last_by_scenario[, c(
  "scenario",
  "engagement_index",
  "creator_metric_pressure",
  "harmful_cascade_risk",
  "moderation_backlog",
  "platform_dependency",
  "governance_readiness",
  "user_trust",
  "public_value_index",
  "platform_risk_index"
)]

write.csv(final_table, file.path(tables_dir, "platform_final_diagnostics.csv"), row.names = FALSE)
print(final_table)
