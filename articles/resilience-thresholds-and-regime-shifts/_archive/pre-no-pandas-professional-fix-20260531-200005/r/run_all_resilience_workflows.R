#!/usr/bin/env Rscript
# Run professional base-R resilience workflows.
script_dir <- dirname(sys.frame(1)$ofile)
source(file.path(script_dir, "resilience_threshold_visualization.R"))
cat("\nAll R resilience workflows completed successfully.\n")
