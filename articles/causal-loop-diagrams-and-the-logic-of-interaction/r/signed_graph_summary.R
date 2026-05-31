# Create a simple signed graph summary without external package dependencies.
base_dir <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!dir.exists(file.path(base_dir, "data"))) base_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

edges <- read.csv(file.path(base_dir, "data", "synthetic_causal_edges.csv"), stringsAsFactors = FALSE)
variables <- sort(unique(c(edges$source_variable, edges$target_variable)))
summary <- data.frame(
  variable = variables,
  outgoing = sapply(variables, function(v) sum(edges$source_variable == v)),
  incoming = sapply(variables, function(v) sum(edges$target_variable == v))
)
print(summary)
