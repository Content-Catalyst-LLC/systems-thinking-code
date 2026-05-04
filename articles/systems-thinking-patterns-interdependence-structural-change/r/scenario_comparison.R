# Systems Thinking: Scenario Comparison in R
# Educational example only.

library(tidyverse)

assumptions <- read_csv("../data/scenario_assumptions.csv", show_col_types = FALSE)

simulate_capacity <- function(initial_capacity, baseline_inflow, baseline_outflow,
                              disruption_pressure, learning_rate, recovery_rate,
                              steps = 80) {
  capacity <- numeric(steps)
  resilience <- numeric(steps)

  capacity[1] <- initial_capacity
  resilience[1] <- 0.55

  for (t in 2:steps) {
    disruption <- ifelse(t >= 25 & t <= 42, disruption_pressure, 0)
    learning_gain <- learning_rate * resilience[t - 1] * capacity[t - 1]
    capacity[t] <- max(0, capacity[t - 1] + baseline_inflow + learning_gain - baseline_outflow - disruption)
    resilience[t] <- min(1, max(0, resilience[t - 1] + recovery_rate * (capacity[t] / 100) - 0.015 * (disruption > 0)))
  }

  tibble(time = 1:steps, capacity = capacity, resilience = resilience)
}

results <- assumptions |>
  rowwise() |>
  do(
    simulate_capacity(
      initial_capacity = .$initial_capacity,
      baseline_inflow = .$baseline_inflow,
      baseline_outflow = .$baseline_outflow,
      disruption_pressure = .$disruption_pressure,
      learning_rate = .$learning_rate,
      recovery_rate = .$recovery_rate
    ) |>
      mutate(scenario = .$scenario)
  ) |>
  ungroup()

summary <- results |>
  group_by(scenario) |>
  summarise(
    min_capacity = min(capacity),
    final_capacity = last(capacity),
    final_resilience = last(resilience),
    .groups = "drop"
  )

dir.create("../outputs", showWarnings = FALSE, recursive = TRUE)

write_csv(results, "../outputs/r_scenario_capacity_results.csv")
write_csv(summary, "../outputs/r_scenario_capacity_summary.csv")

print(summary)
