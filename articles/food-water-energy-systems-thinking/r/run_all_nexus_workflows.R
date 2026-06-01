#!/usr/bin/env Rscript
# Run all base R workflows for the food-water-energy article.
# Dependency policy: base R only. No tidyverse/readr/ggplot2 required.

resolve_runner_root <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)

  if (length(file_arg) > 0) {
    script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
    candidate <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
    if (basename(candidate) == "food-water-energy-systems-thinking") {
      return(candidate)
    }
  }

  current <- normalizePath(getwd(), mustWork = TRUE)
  if (basename(current) == "food-water-energy-systems-thinking") {
    return(current)
  }

  if (basename(current) == "r") {
    parent <- normalizePath(file.path(current, ".."), mustWork = TRUE)
    if (basename(parent) == "food-water-energy-systems-thinking") {
      return(parent)
    }
  }

  stop("Could not resolve article root. Run this script from the article root or with Rscript r/run_all_nexus_workflows.R.")
}

root_dir <- resolve_runner_root()
setwd(root_dir)

source(file.path("r", "food_water_energy_nexus_diagnostics.R"), local = FALSE)
cat("\nAll base R food-water-energy workflows completed.\n")
