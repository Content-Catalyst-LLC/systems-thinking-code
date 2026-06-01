root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
d <- read.csv(file.path(root, "data", "raw", "synthetic_feedback_signals.csv"))
d$distortion <- 1 - (d$signal_quality * d$timeliness * d$authority_connection)
write.csv(d[, c("period", "unit_id", "distortion")], file.path(root, "outputs", "tables", "r_signal_distortion.csv"), row.names = FALSE)
