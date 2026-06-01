# Scenario comparison for intervention assumptions
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
scenarios <- read.csv(file.path(root, "data", "synthetic_scenarios.csv"))
interventions <- read.csv(file.path(root, "data", "synthetic_interventions.csv"))
out_dir <- file.path(root, "outputs")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

joined <- merge(interventions, scenarios, by = "scenario_id", all.x = TRUE)
write.csv(joined, file.path(out_dir, "r_scenario_interventions.csv"), row.names = FALSE)
print(joined)
