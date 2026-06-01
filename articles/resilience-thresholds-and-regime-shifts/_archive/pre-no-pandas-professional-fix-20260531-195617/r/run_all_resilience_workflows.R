# Run all professional R workflows for the resilience article.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_dir <- dirname(sub("^--file=", "", file_arg[1]))
  root <- normalizePath(file.path(script_dir, ".."), mustWork = FALSE)
} else {
  root <- getwd()
}
setwd(root)

source(file.path("r", "resilience_threshold_visualization.R"))
source(file.path("r", "early_warning_diagnostics.R"))

cat("All R resilience workflows completed successfully.\n")
