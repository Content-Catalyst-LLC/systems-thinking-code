root <- getwd(); if (basename(root) == "r") root <- dirname(root)
rec <- read.csv(file.path(root, "data", "raw", "synthetic_recovery_indicators.csv"))
rec$recovery_supply <- rec$protected_focus_hours + rec$recovery_hours + rec$training_hours
summary <- aggregate(recovery_supply ~ role_id, rec, mean)
write.csv(summary, file.path(root, "outputs", "tables", "r_recovery_supply_summary.csv"), row.names = FALSE)
