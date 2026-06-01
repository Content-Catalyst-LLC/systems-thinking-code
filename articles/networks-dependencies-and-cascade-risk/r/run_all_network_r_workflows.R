# Run all base R workflows for this article with safe article-root handling.

args <- commandArgs(trailingOnly = FALSE)
file_arg <- "--file="
script_path <- NULL
match <- grep(file_arg, args, value = TRUE)
if (length(match) > 0) {
  script_path <- normalizePath(sub(file_arg, "", match[1]), mustWork = FALSE)
}

if (!is.null(script_path) && nzchar(script_path)) {
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
} else {
  wd <- getwd()
  article_root <- if (basename(wd) == "r") normalizePath(file.path(wd, ".."), mustWork = FALSE) else wd
}

setwd(article_root)
source(file.path("r", "network_dependency_cascade_diagnostics.R"))
cat("\nAll base R network workflows completed.\n")
