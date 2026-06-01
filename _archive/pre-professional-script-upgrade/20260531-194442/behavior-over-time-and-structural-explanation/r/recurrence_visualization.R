# Recurrence visualization for synthetic event types
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
events <- read.csv(file.path(root, "data", "synthetic_events.csv"))
out_dir <- file.path(root, "outputs")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

tab <- as.data.frame(table(events$event_type))
names(tab) <- c("event_type", "count")
write.csv(tab, file.path(out_dir, "r_recurrence_counts.csv"), row.names = FALSE)

png(file.path(out_dir, "r_recurrence_counts.png"), width = 900, height = 600)
barplot(tab$count, names.arg = tab$event_type, las = 2, main = "Recurring Event Types", ylab = "Count")
dev.off()
