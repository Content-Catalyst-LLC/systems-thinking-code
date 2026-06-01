# Placeholder sensitivity summary table.

sensitivity <- data.frame(
  parameter = c("demand_growth_rate", "productivity_per_staff", "hiring_rate", "turnover_rate"),
  expected_direction = c("increases backlog", "reduces backlog", "reduces backlog", "increases backlog"),
  priority_for_review = c("high", "high", "medium", "medium")
)

print(sensitivity)
