# Summarize synthetic network edge weights by edge type.
root <- getwd()
edges <- read.csv(file.path(root, "data", "raw", "synthetic_network_edges.csv"))
summary_table <- aggregate(weight ~ edge_type, data = edges, FUN = mean)
write.csv(summary_table, file.path(root, "outputs", "tables", "r_network_visibility_summary.csv"), row.names = FALSE)
