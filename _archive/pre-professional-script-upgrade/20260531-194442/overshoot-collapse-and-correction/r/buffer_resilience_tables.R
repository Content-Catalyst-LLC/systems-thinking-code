# Buffer resilience table.
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!file.exists(file.path(root, "data", "processed", "indicators.csv"))) root <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)
indicators <- read.csv(file.path(root, "data", "processed", "indicators.csv"))
out_dir <- file.path(root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
latest <- do.call(rbind, lapply(split(indicators, indicators$domain), function(d) d[which.max(d$month), ]))
latest$buffer_status <- ifelse(latest$buffer_level < 0.34, "urgent_rebuild", "monitor")
write.csv(latest, file.path(out_dir, "buffer_resilience_latest.csv"), row.names = FALSE)
