`%||%` <- function(a, b) if (!is.null(a)) a else b
# Distributional commons burden summary. Synthetic data only.
script_dir <- dirname(normalizePath(sys.frame(1)$ofile %||% getwd(), mustWork = FALSE))
base_dir <- normalizePath(file.path(script_dir, ".."), mustWork = FALSE)
impacts <- read.csv(file.path(base_dir, "data", "synthetic_distributional_impacts.csv"))
impacts$burden_minus_benefit <- impacts$depletion_burden_share - impacts$benefit_share
summary_table <- aggregate(burden_minus_benefit ~ resource_id, impacts, mean)
dir.create(file.path(base_dir, "outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
write.csv(summary_table, file.path(base_dir, "outputs", "tables", "r_distributional_commons_summary.csv"), row.names = FALSE)
