# Summarize advantage, need, and network access by actor group.
root <- getwd()
actors <- read.csv(file.path(root, "data", "raw", "synthetic_actors.csv"))
summary_table <- aggregate(cbind(initial_advantage, initial_capacity, need_score, network_connections) ~ actor_group, data = actors, FUN = mean)
write.csv(summary_table, file.path(root, "outputs", "tables", "r_distributional_advantage_tables.csv"), row.names = FALSE)
