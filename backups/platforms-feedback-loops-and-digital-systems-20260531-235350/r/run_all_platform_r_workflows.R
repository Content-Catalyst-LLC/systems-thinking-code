# Run all base R platform workflows with robust article-root handling.
args <- commandArgs(trailingOnly = FALSE)
file_arg <- args[grepl("^--file=", args)]
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = TRUE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = TRUE)
} else {
  article_root <- normalizePath(getwd(), mustWork = TRUE)
}
setwd(article_root)
source(file.path(article_root, "r", "platform_feedback_digital_systems_diagnostics.R"))
cat("\nAll base R platform workflows completed.\n")
