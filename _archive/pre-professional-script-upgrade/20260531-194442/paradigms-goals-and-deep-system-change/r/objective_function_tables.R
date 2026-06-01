# Objective-function table summary.

data_path <- file.path("data", "synthetic_objective_functions.csv")
objectives <- read.csv(data_path)
objectives$orientation <- ifelse(objectives$burden_penalty > 0.5, "burden-aware", "narrower")

dir.create(file.path("outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
write.csv(objectives, file.path("outputs", "tables", "objective_function_summary.csv"), row.names = FALSE)
