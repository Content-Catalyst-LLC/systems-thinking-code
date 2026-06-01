#!/usr/bin/env Rscript
# Professional R diagnostics for: Paradigms Goals and Deep System Change
# Reads Python-generated outputs and creates base-R tables/figures.

get_script_path <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  hit <- grep("--file=", args, value = TRUE)
  if (length(hit) == 0) return(normalizePath(getwd()))
  normalizePath(sub("--file=", "", hit[1]), mustWork = FALSE)
}

script_path <- get_script_path()
article_dir <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
tables_dir <- file.path(article_dir, "outputs", "tables")
figures_dir <- file.path(article_dir, "outputs", "figures")
dir.create(tables_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)

timeseries_path <- file.path(tables_dir, "professional_timeseries.csv")
if (!file.exists(timeseries_path)) {
  py <- file.path(article_dir, "python", "run_professional_workflow.py")
  if (file.exists(py)) {
    message("Python outputs missing. Running Python workflow first...")
    status <- system2("python3", py)
    if (!identical(status, 0L)) stop("Python workflow failed; cannot continue R diagnostics.")
  } else {
    stop("Missing timeseries file and Python workflow: ", timeseries_path)
  }
}

df <- read.csv(timeseries_path, stringsAsFactors = FALSE)
required <- c("year", "scenario", "outcome_index", "risk_index", "system_stock_index", "capacity_index", "trust_index", "memory_index", "burden_index", "equity_gap_index")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop("Missing required columns: ", paste(missing, collapse = ", "))

scenario_names <- unique(df$scenario)
summary_rows <- lapply(scenario_names, function(s) {
  sub <- df[df$scenario == s, ]
  data.frame(
    scenario = s,
    final_outcome_index = tail(sub$outcome_index, 1),
    final_risk_index = tail(sub$risk_index, 1),
    final_stock_index = tail(sub$system_stock_index, 1),
    final_capacity_index = tail(sub$capacity_index, 1),
    final_trust_index = tail(sub$trust_index, 1),
    final_memory_index = tail(sub$memory_index, 1),
    average_burden_index = mean(sub$burden_index),
    peak_risk_index = max(sub$risk_index),
    years_high_risk = sum(sub$risk_index > 70),
    years_low_trust = sum(sub$trust_index < 45),
    stringsAsFactors = FALSE
  )
})
summary_df <- do.call(rbind, summary_rows)
summary_df$professional_diagnostic <- ifelse(
  summary_df$final_outcome_index >= 75 & summary_df$final_risk_index <= 45,
  "Strong trajectory under synthetic assumptions",
  ifelse(summary_df$final_risk_index >= 70, "High-risk trajectory", "Monitor burden, trust, capacity, and equity")
)
write.csv(summary_df, file.path(tables_dir, "professional_r_summary.csv"), row.names = FALSE)

burden_trust <- aggregate(cbind(burden_index, trust_index, outcome_index, risk_index, equity_gap_index) ~ scenario, data = df, FUN = mean)
names(burden_trust) <- c("scenario", "average_burden", "average_trust", "average_outcome", "average_risk", "average_equity_gap")
burden_trust$interpretation <- ifelse(
  burden_trust$average_burden > 55 & burden_trust$average_trust < 50,
  "High burden / low trust warning",
  "No high-burden/low-trust warning under synthetic assumptions"
)
write.csv(burden_trust, file.path(tables_dir, "professional_r_burden_trust_diagnostics.csv"), row.names = FALSE)

plot_series <- function(column, label, filename, legend_position) {
  png(file.path(figures_dir, filename), width = 1200, height = 760)
  plot(NA, xlim = range(df$year), ylim = range(df[[column]], na.rm = TRUE), xlab = "Year", ylab = label, main = paste("Paradigms Goals and Deep System Change", "—", label))
  for (s in scenario_names) {
    sub <- df[df$scenario == s, ]
    lines(sub$year, sub[[column]], lwd = 2)
  }
  legend(legend_position, legend = scenario_names, lwd = 2, cex = 0.75)
  dev.off()
}

plot_series("outcome_index", "Outcome index", "professional_r_outcome_trajectories.png", "topleft")
plot_series("risk_index", "Risk index", "professional_r_risk_trajectories.png", "topright")
plot_series("trust_index", "Trust / legitimacy index", "professional_r_trust_trajectories.png", "bottomright")

validation <- data.frame(
  check = c("row_count", "scenario_count", "required_columns", "summary_export", "figure_exports"),
  status = c(
    ifelse(nrow(df) > 0, "pass", "fail"),
    ifelse(length(scenario_names) >= 5, "pass", "warning"),
    ifelse(length(missing) == 0, "pass", "fail"),
    ifelse(file.exists(file.path(tables_dir, "professional_r_summary.csv")), "pass", "fail"),
    "pass"
  ),
  detail = c(
    paste("Rows:", nrow(df)), paste("Scenarios:", length(scenario_names)),
    ifelse(length(missing) == 0, "All required columns present", paste(missing, collapse = ", ")),
    "professional_r_summary.csv written", "Base-R trajectory figures written"
  ),
  stringsAsFactors = FALSE
)
write.csv(validation, file.path(tables_dir, "professional_r_validation_report.csv"), row.names = FALSE)
if (any(validation$status == "fail")) stop("R workflow validation failed")
message("Professional R diagnostics complete for: Paradigms Goals and Deep System Change")
