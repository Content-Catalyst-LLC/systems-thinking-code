# Base R AI and technology systems diagnostics.
# Reads Python-generated outputs and produces summary tables and figures.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = FALSE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
} else {
  article_root <- normalizePath(getwd(), mustWork = FALSE)
}
setwd(article_root)

tables_dir <- file.path("outputs", "tables")
figures_dir <- file.path("outputs", "figures")
if (!dir.exists(figures_dir)) dir.create(figures_dir, recursive = TRUE)

timeseries_path <- file.path(tables_dir, "ai_technology_systems_timeseries.csv")
summary_path <- file.path(tables_dir, "ai_technology_systems_summary.csv")

if (!file.exists(timeseries_path)) {
  stop("Missing ai_technology_systems_timeseries.csv. Run the Python workflow first from the article root.")
}

ai <- read.csv(timeseries_path, stringsAsFactors = FALSE)

avg_risk <- aggregate(ai_system_risk ~ scenario, data = ai, FUN = mean)
max_gap <- aggregate(false_positive_gap ~ scenario, data = ai, FUN = max)
max_backlog <- aggregate(human_review_backlog ~ scenario, data = ai, FUN = max)
min_trust <- aggregate(public_trust ~ scenario, data = ai, FUN = min)

names(avg_risk)[2] <- "average_ai_system_risk"
names(max_gap)[2] <- "maximum_false_positive_gap"
names(max_backlog)[2] <- "maximum_human_review_backlog"
names(min_trust)[2] <- "minimum_public_trust"

diagnostics <- Reduce(function(x, y) merge(x, y, by = "scenario"), list(avg_risk, max_gap, max_backlog, min_trust))
diagnostics$diagnostic <- ifelse(
  diagnostics$average_ai_system_risk >= 45 | diagnostics$maximum_false_positive_gap >= 25,
  "high-risk AI system",
  ifelse(
    diagnostics$average_ai_system_risk >= 28 | diagnostics$maximum_human_review_backlog >= 35,
    "moderate risk requiring stronger governance",
    "comparatively accountable AI pathway"
  )
)
write.csv(diagnostics, summary_path, row.names = FALSE)
print(diagnostics)

plot_metric <- function(metric, y_label, title, output_name) {
  png(file.path(figures_dir, output_name), width = 1200, height = 700)
  scenarios <- unique(ai$scenario)
  plot(NA, xlim = range(ai$period), ylim = range(ai[[metric]], na.rm = TRUE), xlab = "Period", ylab = y_label, main = title)
  for (scenario_name in scenarios) {
    subset_data <- ai[ai$scenario == scenario_name, ]
    lines(subset_data$period, subset_data[[metric]], lwd = 2)
  }
  legend("topleft", legend = scenarios, lwd = 2, cex = 0.8, bty = "n")
  grid()
  dev.off()
}

plot_metric("drift_index", "Drift index", "Model Drift by AI Governance Scenario", "ai_drift_trajectories.png")
plot_metric("feedback_bias_index", "Feedback bias index", "AI Feedback Bias by Scenario", "ai_feedback_bias_trajectories.png")
plot_metric("false_positive_gap", "False positive gap", "Group-Level False Positive Gap by Scenario", "ai_false_positive_gap_trajectories.png")
plot_metric("automation_burden", "Automation burden", "Automation Burden by Scenario", "ai_automation_burden_trajectories.png")
plot_metric("governance_readiness", "Governance readiness", "AI Governance Readiness by Scenario", "ai_governance_readiness_trajectories.png")
plot_metric("ai_system_risk", "AI system risk", "AI System Risk by Scenario", "ai_system_risk_trajectories.png")
plot_metric("public_trust", "Public trust", "Public Trust by AI Governance Scenario", "ai_public_trust_trajectories.png")

last_by_scenario <- do.call(rbind, lapply(split(ai, ai$scenario), function(df) df[nrow(df), ]))
final_table <- last_by_scenario[, c("scenario", "drift_index", "feedback_bias_index", "group_a_error", "group_b_error", "false_positive_gap", "automation_burden", "contestability_index", "governance_readiness", "ai_system_risk", "public_trust")]
write.csv(final_table, file.path(tables_dir, "ai_technology_final_diagnostics.csv"), row.names = FALSE)
print(final_table)
