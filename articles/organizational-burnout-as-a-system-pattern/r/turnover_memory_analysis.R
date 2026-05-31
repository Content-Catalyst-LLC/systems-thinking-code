root <- getwd(); if (basename(root) == "r") root <- dirname(root)
turnover <- read.csv(file.path(root, "data", "raw", "synthetic_turnover_events.csv"))
summary <- aggregate(cbind(departures, knowledge_loss_index, remaining_staff_load_increase) ~ role_id, turnover, mean)
write.csv(summary, file.path(root, "outputs", "tables", "r_turnover_memory_analysis.csv"), row.names = FALSE)
