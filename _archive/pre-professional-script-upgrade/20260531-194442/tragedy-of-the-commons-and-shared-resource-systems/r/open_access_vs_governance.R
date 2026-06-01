`%||%` <- function(a, b) if (!is.null(a)) a else b
# Compare open-access and governed commons scenarios. Synthetic data only.
script_dir <- dirname(normalizePath(sys.frame(1)$ofile %||% getwd(), mustWork = FALSE))
base_dir <- normalizePath(file.path(script_dir, ".."), mustWork = FALSE)
runs <- read.csv(file.path(base_dir, "data", "synthetic_model_runs.csv"))
runs$net_system_value <- runs$total_benefit - runs$total_depletion_cost
summary_table <- aggregate(net_system_value ~ scenario + commons_status, runs, mean)
dir.create(file.path(base_dir, "outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
write.csv(summary_table, file.path(base_dir, "outputs", "tables", "r_open_access_vs_governance.csv"), row.names = FALSE)
