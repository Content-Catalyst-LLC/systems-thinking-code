# run_all_complexity_workflows.R
# Runs base R diagnostics from the article root and generates Python outputs first if needed.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- "--file="
match <- grep(file_arg, args, value = TRUE)
if (length(match) > 0) {
  script_path <- normalizePath(sub(file_arg, "", match[1]), mustWork = FALSE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
} else {
  current <- normalizePath(getwd(), mustWork = FALSE)
  article_root <- if (basename(current) == "r") normalizePath(file.path(current, ".."), mustWork = FALSE) else current
}

setwd(article_root)

timeseries_path <- file.path(article_root, "outputs", "tables", "emergence_adaptation_complexity_timeseries.csv")
python_runner <- file.path(article_root, "python", "run_all_complexity_workflows.py")

if (!file.exists(timeseries_path) && file.exists(python_runner)) {
  message("Generating required Python outputs before R diagnostics...")
  status <- system2("python3", python_runner)
  if (!identical(status, 0L)) {
    stop("Python workflow failed; cannot continue R diagnostics.")
  }
}

source(file.path(article_root, "r", "emergence_adaptation_complexity_diagnostics.R"))
