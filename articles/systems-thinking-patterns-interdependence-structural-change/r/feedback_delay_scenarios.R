# Systems Thinking: Feedback and Delay Scenarios in R
# Educational example only.

library(tidyverse)

time_steps <- 80

simulate_balancing_delay <- function(target = 100, initial = 25, correction = 0.18, delay = 1) {
  values <- numeric(time_steps)
  values[1] <- initial

  for (t in 2:time_steps) {
    delayed_index <- max(1, t - delay)
    perceived_gap <- target - values[delayed_index]
    values[t] <- values[t - 1] + correction * perceived_gap
  }

  tibble(
    time = 1:time_steps,
    value = values,
    delay = delay
  )
}

scenario_data <- bind_rows(
  simulate_balancing_delay(delay = 1),
  simulate_balancing_delay(delay = 4),
  simulate_balancing_delay(delay = 8),
  simulate_balancing_delay(delay = 12)
)

overshoot_summary <- scenario_data |>
  group_by(delay) |>
  summarise(
    max_value = max(value),
    min_value = min(value),
    final_value = last(value),
    max_overshoot = max(value) - 100,
    .groups = "drop"
  )

dir.create("../outputs", showWarnings = FALSE, recursive = TRUE)

write_csv(scenario_data, "../outputs/r_balancing_delay_scenarios.csv")
write_csv(overshoot_summary, "../outputs/r_balancing_delay_overshoot_summary.csv")

print(overshoot_summary)
