# Event distribution summary.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
events <- read.csv(file.path(article_dir, "data", "synthetic_events.csv"))

print(table(events$event_type))
print(table(events$location))
print(aggregate(severity ~ system_area, data = events, FUN = mean))
