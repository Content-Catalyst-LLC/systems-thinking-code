data_dir <- file.path("..", "data")
out_dir <- file.path("..", "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

outputs <- read.csv(file.path(data_dir, "synthetic_model_outputs.csv"))
baseline <- outputs[outputs$scenario_id == "baseline" & outputs$year == 10, ]

comparison <- outputs[outputs$year == 10, ]
comparison$capacity_difference_from_baseline <- comparison$system_capacity - baseline$system_capacity
comparison$demand_difference_from_baseline <- comparison$system_demand - baseline$system_demand
comparison$trust_difference_from_baseline <- comparison$trust_stock - baseline$trust_stock
comparison$risk_difference_from_baseline <- comparison$risk_stock - baseline$risk_stock

write.csv(comparison, file.path(out_dir, "baseline_counterfactual_tables.csv"), row.names = FALSE)
cat("Wrote baseline counterfactual table\n")
