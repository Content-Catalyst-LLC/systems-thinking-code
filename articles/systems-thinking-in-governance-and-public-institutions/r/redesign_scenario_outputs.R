root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
raw <- file.path(root, "data", "raw")
out <- file.path(root, "outputs", "tables")
dir.create(out, recursive = TRUE, showWarnings = FALSE)
runs <- read.csv(file.path(raw, "synthetic_model_runs.csv"))
runs$governance_redesign_score <- (1 - runs$administrative_burden) * 0.18 + runs$trust_stock * 0.18 + runs$coordination_density * 0.16 + runs$institutional_capacity * 0.17 + runs$feedback_closure * 0.16 + runs$public_value_score * 0.15
write.csv(runs[, c("scenario", "public_value_score", "governance_redesign_score")], file.path(out, "r_redesign_scenarios.csv"), row.names = FALSE)
