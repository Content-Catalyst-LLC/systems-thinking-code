# Scenario comparison for dynamic complexity.
path <- file.path("data", "raw", "synthetic_scenarios.csv")
if (file.exists(path)) {
  scenarios <- read.csv(path)
  scenarios$resistance_index <- round(scenarios$compensation_strength + scenarios$boundary_cost_weight / 2, 3)
  print(scenarios[order(-scenarios$resistance_index), ])
}
