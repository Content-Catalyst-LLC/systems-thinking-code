#!/usr/bin/env Rscript
# Professional systems-thinking R workflow for this article folder.
#
# Reads the Python-generated professional systems scenario output and produces
# summary diagnostics, decision-support tables, and base-R figures. This script
# uses base R only so it remains runnable on clean macOS/R installations.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- "--file="
script_path <- normalizePath(sub(file_arg, "", args[grep(file_arg, args)]), mustWork = FALSE)

if (length(script_path) == 0 || is.na(script_path) || script_path == "") {
  article_dir <- getwd()
} else {
  article_dir <- dirname(dirname(script_path))
}

article_slug <- basename(article_dir)
article_title <- tools::toTitleCase(gsub("-", " ", article_slug))

tables_dir <- file.path(article_dir, "outputs", "tables")
figures_dir <- file.path(article_dir, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

timeseries_path <- file.path(tables_dir, "professional_systems_scenario_timeseries.csv")
summary_path <- file.path(tables_dir, "professional_systems_scenario_summary.csv")

if (!file.exists(timeseries_path)) {
  py_script <- file.path(article_dir, "python", "run_professional_systems_workflow.py")
  if (file.exists(py_script)) {
    message("Python-generated timeseries not found; running Python workflow first.")
    status <- system2("python3", py_script)
    if (!identical(status, 0L)) {
      stop("Python workflow failed; cannot continue R workflow.")
    }
  } else {
    stop("Missing timeseries CSV and missing Python workflow script.")
  }
}

df <- read.csv(timeseries_path, stringsAsFactors = FALSE)

required_cols <- c(
  "scenario", "year", "outcome_index", "risk_index", "capacity_index",
  "trust_index", "institutional_memory_index", "system_stock_index",
  "burden_index", "equity_gap_index", "feedback_closure"
)

missing_cols <- setdiff(required_cols, names(df))
if (length(missing_cols) > 0) {
  stop(paste("Missing required columns:", paste(missing_cols, collapse = ", ")))
}

scenario_names <- sort(unique(df$scenario))

summary_rows <- lapply(scenario_names, function(s) {
  sub <- df[df$scenario == s, ]
  final <- sub[nrow(sub), ]
  data.frame(
    article_slug = article_slug,
    scenario = s,
    final_outcome_index = final$outcome_index,
    final_risk_index = final$risk_index,
    final_capacity_index = final$capacity_index,
    final_trust_index = final$trust_index,
    final_memory_index = final$institutional_memory_index,
    final_stock_index = final$system_stock_index,
    average_burden_index = mean(sub$burden_index),
    average_feedback_closure = mean(sub$feedback_closure),
    years_risk_above_70 = sum(sub$risk_index > 70),
    years_stock_below_50 = sum(sub$system_stock_index < 50),
    stringsAsFactors = FALSE
  )
})

summary_df <- do.call(rbind, summary_rows)
summary_df$professional_diagnostic <- ifelse(
  summary_df$final_outcome_index >= 75 & summary_df$final_risk_index <= 45,
  "Strong system trajectory",
  ifelse(
    summary_df$final_outcome_index >= 60 & summary_df$final_risk_index <= 60,
    "Improving but monitor burden, trust, and distribution",
    ifelse(
      summary_df$final_risk_index > 70,
      "High-risk trajectory requiring structural redesign",
      "Weak or uncertain trajectory"
    )
  )
)

write.csv(summary_df, summary_path, row.names = FALSE)

burden_trust <- aggregate(
  cbind(burden_index, trust_index, outcome_index, risk_index, equity_gap_index) ~ scenario,
  data = df,
  FUN = mean
)
names(burden_trust) <- c(
  "scenario", "average_burden", "average_trust", "average_outcome",
  "average_risk", "average_equity_gap"
)
burden_trust$burden_trust_warning <- ifelse(
  burden_trust$average_burden > 55 & burden_trust$average_trust < 50,
  "Burden is high and trust is weak; redesign access, feedback, and implementation capacity.",
  "No combined high-burden/low-trust warning under synthetic assumptions."
)
write.csv(
  burden_trust,
  file.path(tables_dir, "professional_burden_trust_diagnostics.csv"),
  row.names = FALSE
)

# Base R outcome plot
png(file.path(figures_dir, "professional_r_outcome_trajectories.png"), width = 1200, height = 750)
plot(
  NA,
  xlim = range(df$year),
  ylim = range(df$outcome_index, na.rm = TRUE),
  xlab = "Year",
  ylab = "Outcome index",
  main = paste(article_title, "— Outcome Trajectories")
)
for (s in scenario_names) {
  sub <- df[df$scenario == s, ]
  lines(sub$year, sub$outcome_index, lwd = 2)
}
legend("topleft", legend = scenario_names, lwd = 2, cex = 0.8)
dev.off()

# Base R risk plot
png(file.path(figures_dir, "professional_r_risk_trajectories.png"), width = 1200, height = 750)
plot(
  NA,
  xlim = range(df$year),
  ylim = range(df$risk_index, na.rm = TRUE),
  xlab = "Year",
  ylab = "Risk index",
  main = paste(article_title, "— Risk Trajectories")
)
for (s in scenario_names) {
  sub <- df[df$scenario == s, ]
  lines(sub$year, sub$risk_index, lwd = 2)
}
legend("topright", legend = scenario_names, lwd = 2, cex = 0.8)
dev.off()

validation <- data.frame(
  article_slug = article_slug,
  check = c("row_count", "scenario_count", "required_columns", "output_files"),
  status = c(
    ifelse(nrow(df) > 0, "pass", "fail"),
    ifelse(length(scenario_names) >= 4, "pass", "warning"),
    ifelse(length(missing_cols) == 0, "pass", "fail"),
    ifelse(file.exists(summary_path), "pass", "fail")
  ),
  detail = c(
    paste("Rows:", nrow(df)),
    paste("Scenarios:", length(scenario_names)),
    ifelse(length(missing_cols) == 0, "All required columns present.", paste(missing_cols, collapse = ", ")),
    paste("Summary path:", summary_path)
  ),
  stringsAsFactors = FALSE
)

write.csv(
  validation,
  file.path(tables_dir, "professional_r_validation_report.csv"),
  row.names = FALSE
)

if (any(validation$status == "fail")) {
  stop("R workflow validation failed; inspect professional_r_validation_report.csv")
}

message("Professional R workflow complete for: ", article_title)
message("Tables: ", tables_dir)
message("Figures: ", figures_dir)
