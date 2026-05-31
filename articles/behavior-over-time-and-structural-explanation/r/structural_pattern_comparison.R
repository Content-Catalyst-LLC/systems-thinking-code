# Compare causal edge patterns by polarity
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
edges <- read.csv(file.path(root, "data", "synthetic_causal_edges.csv"))
out_dir <- file.path(root, "outputs")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

polarity_counts <- as.data.frame(table(edges$polarity))
names(polarity_counts) <- c("polarity", "count")
write.csv(polarity_counts, file.path(out_dir, "r_causal_polarity_counts.csv"), row.names = FALSE)
print(polarity_counts)
