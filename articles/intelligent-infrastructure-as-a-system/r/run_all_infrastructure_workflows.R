# Run all base R workflows from the article root, regardless of caller working directory.
args <- commandArgs(trailingOnly = FALSE)
file_arg <- args[grep("^--file=", args)]
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  root <- normalizePath(getwd(), mustWork = TRUE)
}
setwd(root)
source(file.path(root, "r", "intelligent_infrastructure_system_diagnostics.R"), chdir = TRUE)
cat("\nAll base R intelligent infrastructure workflows completed.\n")
