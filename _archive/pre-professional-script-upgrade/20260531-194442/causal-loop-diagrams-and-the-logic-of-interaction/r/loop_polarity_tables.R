# Calculate loop polarity from the predefined synthetic loop table.
base_dir <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!dir.exists(file.path(base_dir, "data"))) base_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

edges <- read.csv(file.path(base_dir, "data", "synthetic_causal_edges.csv"), stringsAsFactors = FALSE)
loops <- read.csv(file.path(base_dir, "data", "synthetic_feedback_loops.csv"), stringsAsFactors = FALSE)
signs <- setNames(ifelse(edges$polarity == "positive", 1, -1), edges$edge_id)

loops$calculated_polarity <- sapply(strsplit(loops$edge_sequence, "[|]"), function(ids) {
  product <- prod(signs[ids], na.rm = TRUE)
  ifelse(product > 0, "reinforcing", "balancing")
})
print(loops[, c("loop_id", "loop_name", "expected_polarity", "calculated_polarity")])
