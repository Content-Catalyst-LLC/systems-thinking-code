# Causal summary tables.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
edges <- read.csv(file.path(article_dir, "data", "synthetic_causal_edges.csv"))

print(table(edges$polarity))
print(table(edges$delay))
print(edges[, c("source", "target", "polarity", "delay")])
