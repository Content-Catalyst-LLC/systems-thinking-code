#!/usr/bin/env Rscript
# Run professional R workflows across all existing article folders.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- "--file="
script_path <- normalizePath(sub(file_arg, "", args[grep(file_arg, args)]), mustWork = FALSE)

if (length(script_path) == 0 || is.na(script_path) || script_path == "") {
  repo <- getwd()
} else {
  repo <- dirname(dirname(script_path))
}

articles_dir <- file.path(repo, "articles")
article_dirs <- list.dirs(articles_dir, full.names = TRUE, recursive = FALSE)

if (length(article_dirs) == 0) {
  stop("No article directories found.")
}

failures <- c()

for (article_dir in article_dirs) {
  workflow <- file.path(article_dir, "r", "run_professional_systems_workflow.R")
  slug <- basename(article_dir)
  if (!file.exists(workflow)) {
    failures <- c(failures, paste(slug, "missing workflow"))
    next
  }
  message("\n=== R workflow: ", slug, " ===")
  status <- system2("Rscript", workflow)
  if (!identical(status, 0L)) {
    failures <- c(failures, paste(slug, "exit", status))
  }
}

if (length(failures) > 0) {
  message("\nFailures:")
  for (failure in failures) {
    message("- ", failure)
  }
  quit(status = 1)
}

message("\nAll professional R workflows completed successfully.")
