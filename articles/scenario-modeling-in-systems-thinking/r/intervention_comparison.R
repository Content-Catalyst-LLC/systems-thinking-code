data_dir <- file.path("..", "data")
out_dir <- file.path("..", "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

interventions <- read.csv(file.path(data_dir, "synthetic_interventions.csv"))
interventions$illustrative_score <- interventions$capacity_boost * 40 +
  interventions$burden_reduction * 35 +
  interventions$repair_flow * 25

write.csv(interventions, file.path(out_dir, "r_intervention_comparison.csv"), row.names = FALSE)
cat("Wrote R intervention comparison\n")
