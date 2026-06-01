root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
d <- read.csv(file.path(root, "data", "raw", "synthetic_memory_assets.csv"))
d$retained_memory_index <- (d$decision_records + d$postmortems + d$reused_lessons + d$living_playbooks + d$onboarding_links) * (1 - d$knowledge_decay_risk)
write.csv(d[, c("unit_id", "retained_memory_index")], file.path(root, "outputs", "tables", "r_memory_retention.csv"), row.names = FALSE)
