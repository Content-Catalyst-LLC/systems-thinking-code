# Summarize synthetic causal-loop edge tables.
base_dir <- normalizePath(file.path(dirname(commandArgs(trailingOnly = FALSE)[1]), ".."), mustWork = FALSE)
# Fallback for interactive use
if (!dir.exists(file.path(base_dir, "data"))) base_dir <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!dir.exists(file.path(base_dir, "data"))) base_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

edges <- read.csv(file.path(base_dir, "data", "synthetic_causal_edges.csv"), stringsAsFactors = FALSE)
print(table(edges$polarity))
print(edges[, c("edge_id", "source_variable", "target_variable", "polarity", "delay_steps")])
