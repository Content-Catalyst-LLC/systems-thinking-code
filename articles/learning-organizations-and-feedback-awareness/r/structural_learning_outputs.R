root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
d <- read.csv(file.path(root, "data", "raw", "synthetic_structural_changes.csv"))
d$structural_change_count <- d$feedback_routine_change + d$metric_change + d$authority_change + d$memory_system_change + d$workload_redesign + d$trust_repair_action
summary <- aggregate(structural_change_count ~ unit_id, d, sum)
write.csv(summary, file.path(root, "outputs", "tables", "r_structural_learning_outputs.csv"), row.names = FALSE)
