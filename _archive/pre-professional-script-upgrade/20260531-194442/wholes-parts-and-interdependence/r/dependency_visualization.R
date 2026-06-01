# Dependency visualization for Wholes, Parts, and Interdependence

article_dir <- dirname(dirname(normalizePath(commandArgs(trailingOnly = FALSE)[grep("--file=", commandArgs(trailingOnly = FALSE))][1] |> sub("--file=", "", x = _))))
if (is.na(article_dir)) article_dir <- getwd()

edges_path <- file.path(article_dir, "data", "synthetic_dependency_edges.csv")
edges <- read.csv(edges_path)

print(edges[, c("source", "target", "dependency_type", "weight")])

output_dir <- file.path(article_dir, "outputs", "tables")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(edges, file.path(output_dir, "dependency_edges_summary.csv"), row.names = FALSE)
