# Policy resistance plots using base R.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile %||% getwd()), ".."), mustWork = FALSE)
input <- file.path(root, "outputs", "tables", "policy_resistance_summary.csv")
if (!file.exists(input)) {
  input <- file.path(root, "data", "raw", "synthetic_scenarios.csv")
}
message("Use this script after running python/policy_resistance_simulation.py for full plots.")
