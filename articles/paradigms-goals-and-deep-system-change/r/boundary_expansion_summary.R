# Boundary expansion summary.

costs <- read.csv(file.path("data", "synthetic_boundary_costs.csv"))
costs$expanded_boundary_cost <- costs$internal_cost + costs$externalized_cost
costs$externalized_share <- round(costs$externalized_cost / costs$expanded_boundary_cost, 3)

dir.create(file.path("outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
write.csv(costs, file.path("outputs", "tables", "boundary_expansion_summary.csv"), row.names = FALSE)
