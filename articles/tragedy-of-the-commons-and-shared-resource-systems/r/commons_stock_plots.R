`%||%` <- function(a, b) if (!is.null(a)) a else b
# Base-R commons stock summary. Synthetic data only.
base_dir <- normalizePath(file.path(dirname(sys.frame(1)$ofile %||% getwd()), ".."), mustWork = FALSE)
if (!dir.exists(file.path(base_dir, "outputs", "tables"))) {
  dir.create(file.path(base_dir, "outputs", "tables"), recursive = TRUE)
}
resources <- read.csv(file.path(base_dir, "data", "synthetic_shared_resources.csv"))
resources$risk_margin <- resources$initial_stock - resources$critical_threshold
write.csv(resources, file.path(base_dir, "outputs", "tables", "r_commons_stock_summary.csv"), row.names = FALSE)
