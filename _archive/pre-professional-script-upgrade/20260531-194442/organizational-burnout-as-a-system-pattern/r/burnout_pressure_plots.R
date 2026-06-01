root <- normalizePath(file.path(dirname(sys.frame(1)$ofile %||% getwd()), ".."), mustWork = FALSE)
if (!dir.exists(file.path(root, "outputs", "tables"))) dir.create(file.path(root, "outputs", "tables"), recursive = TRUE)
data <- read.csv(file.path(root, "data", "raw", "synthetic_workload_events.csv"))
data$visible_demand <- data$visible_workload + data$meeting_load + data$rework_hours
data$pressure_index <- round(data$visible_demand / data$capacity_index, 3)
write.csv(data[, c("period", "role_id", "visible_demand", "capacity_index", "pressure_index")], file.path(root, "outputs", "tables", "r_burnout_pressure.csv"), row.names = FALSE)
