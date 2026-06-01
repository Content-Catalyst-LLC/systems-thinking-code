root <- getwd(); if (basename(root) == "r") root <- dirname(root)
hidden <- read.csv(file.path(root, "data", "raw", "synthetic_hidden_labor.csv"))
hidden$total_hidden_labor <- hidden$coordination_hours + hidden$emotional_labor_hours + hidden$informal_mentoring_hours + hidden$workaround_hours + hidden$unpaid_extra_hours
summary <- aggregate(total_hidden_labor ~ role_id, hidden, mean)
write.csv(summary, file.path(root, "outputs", "tables", "r_hidden_labor_summary.csv"), row.names = FALSE)
