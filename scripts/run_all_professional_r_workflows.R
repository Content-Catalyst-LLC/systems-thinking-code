#!/usr/bin/env Rscript
# Run professional R workflows across every article directory.
args <- commandArgs(trailingOnly = FALSE)
hit <- grep("--file=", args, value = TRUE)
repo <- if (length(hit) == 0) getwd() else dirname(dirname(normalizePath(sub("--file=", "", hit[1]), mustWork = FALSE)))
article_dirs <- list.dirs(file.path(repo, "articles"), full.names = TRUE, recursive = FALSE)
failures <- c()
for (article_dir in article_dirs) {
  workflow <- file.path(article_dir, "r", "run_professional_workflow.R")
  slug <- basename(article_dir)
  if (!file.exists(workflow)) { failures <- c(failures, paste(slug, "missing R workflow")); next }
  message("\n=== R professional workflow: ", slug, " ===")
  status <- system2("Rscript", workflow)
  if (!identical(status, 0L)) failures <- c(failures, paste(slug, "exit", status))
}
if (length(failures) > 0) { message("\nFailures:"); for (failure in failures) message("- ", failure); quit(status = 1) }
message("\nAll professional R workflows completed successfully.")
