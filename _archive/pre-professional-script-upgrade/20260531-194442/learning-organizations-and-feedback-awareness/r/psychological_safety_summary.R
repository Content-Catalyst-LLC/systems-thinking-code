root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
d <- read.csv(file.path(root, "data", "raw", "synthetic_psychological_safety_indicators.csv"))
d$safety_index <- (d$speak_up_score + d$leader_response_score + d$closure_score) / 3
summary <- aggregate(safety_index ~ unit_id, d, mean)
write.csv(summary, file.path(root, "outputs", "tables", "r_psychological_safety_summary.csv"), row.names = FALSE)
