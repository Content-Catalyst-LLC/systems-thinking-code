# Feedback loop summary tables.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
loops <- read.csv(file.path(article_dir, "data", "synthetic_feedback_loops.csv"))
edges <- read.csv(file.path(article_dir, "data", "synthetic_causal_edges.csv"))

loop_counts <- as.data.frame(table(loops$loop_type))
names(loop_counts) <- c("loop_type", "count")

edge_counts <- as.data.frame(table(edges$polarity))
names(edge_counts) <- c("polarity", "count")

write.csv(loop_counts, file.path(article_dir, "outputs", "tables", "loop_type_counts.csv"), row.names = FALSE)
write.csv(edge_counts, file.path(article_dir, "outputs", "tables", "edge_polarity_counts.csv"), row.names = FALSE)

print(loop_counts)
print(edge_counts)
