#!/usr/bin/env Rscript
# Run base R public health workflows with safe path handling.

resolve_root <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- "--file="
  script_args <- args[startsWith(args, file_arg)]
  if (length(script_args) > 0) {
    script_path <- normalizePath(sub(file_arg, "", script_args[[1]]), mustWork = FALSE)
    return(normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE))
  }
  cwd <- normalizePath(getwd(), mustWork = FALSE)
  if (basename(cwd) == "r") {
    return(normalizePath(file.path(cwd, ".."), mustWork = FALSE))
  }
  return(cwd)
}

root <- resolve_root()
source(file.path(root, "r", "public_health_system_diagnostics.R"), chdir = TRUE)
cat("\nAll base R public health workflows completed.\n")
