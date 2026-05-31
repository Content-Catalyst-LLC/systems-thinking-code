# Summarize signed causal edges.
edges <- read.csv("data/synthetic_signed_edges.csv")
print(edges[, c("edge_id", "source_variable", "target_variable", "sign", "delay")])
