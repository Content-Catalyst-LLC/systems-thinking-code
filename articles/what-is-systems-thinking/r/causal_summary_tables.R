# Causal summary tables.

get_script_dir <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)
  if (length(file_arg) > 0) return(dirname(normalizePath(sub("^--file=", "", file_arg))))
  getwd()
}

article_dir <- dirname(get_script_dir())
edges <- read.csv(file.path(article_dir, "data", "synthetic_causal_edges.csv"))
print(table(edges$polarity))
print(table(edges$delay))
