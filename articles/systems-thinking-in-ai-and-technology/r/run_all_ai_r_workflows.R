args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
if (length(file_arg) > 0) {
  script_path <- normalizePath(sub("^--file=", "", file_arg[1]), mustWork = FALSE)
  article_root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
} else {
  article_root <- normalizePath(getwd(), mustWork = FALSE)
}
setwd(article_root)
source(file.path("r", "ai_technology_systems_diagnostics.R"))
cat("\nAll base R AI and technology workflows completed.\n")
