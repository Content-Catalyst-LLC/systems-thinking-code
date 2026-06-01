`%||%` <- function(a, b) if (!is.null(a)) a else b
# Restoration action summary. Synthetic data only.
script_dir <- dirname(normalizePath(sys.frame(1)$ofile %||% getwd(), mustWork = FALSE))
base_dir <- normalizePath(file.path(script_dir, ".."), mustWork = FALSE)
actions <- read.csv(file.path(base_dir, "data", "synthetic_restoration_actions.csv"))
actions$cost_per_recovery_point <- actions$annual_cost / pmax(actions$expected_recovery_rate * 100, 1)
dir.create(file.path(base_dir, "outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
write.csv(actions, file.path(base_dir, "outputs", "tables", "r_restoration_summary.csv"), row.names = FALSE)
