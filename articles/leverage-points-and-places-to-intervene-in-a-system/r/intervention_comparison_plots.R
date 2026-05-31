# Basic intervention comparison plot using base R only
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_dir <- file.path(root, "data")
out_dir <- file.path(root, "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

runs <- read.csv(file.path(data_dir, "synthetic_model_runs.csv"))
runs$composite_change <- runs$trust_change + runs$burden_change + runs$capacity_change + runs$resilience_change
png(file.path(out_dir, "r_intervention_comparison.png"), width = 900, height = 600)
barplot(runs$composite_change, names.arg = runs$scenario, las = 2, main = "Composite Intervention Change", ylab = "Composite change")
dev.off()
