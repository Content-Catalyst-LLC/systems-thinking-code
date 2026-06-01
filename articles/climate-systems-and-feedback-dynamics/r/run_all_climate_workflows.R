#!/usr/bin/env Rscript
args <- commandArgs(FALSE)
file_arg <- args[grep("--file=", args)]
if (length(file_arg) > 0) {
  this_file <- sub("--file=", "", file_arg[1])
  script_dir <- dirname(normalizePath(this_file))
} else {
  script_dir <- file.path(getwd(), "r")
}
source(file.path(script_dir, "climate_feedback_diagnostics.R"))
