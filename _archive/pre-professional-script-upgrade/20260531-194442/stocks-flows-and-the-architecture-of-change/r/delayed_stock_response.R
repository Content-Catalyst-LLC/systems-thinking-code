# Demonstrate delayed stock response.
simulate_delay <- function(initial = 50, target = 80, delay = 3, periods = 15) {
  values <- numeric(periods + 1)
  values[1] <- initial
  for (t in seq_len(periods)) {
    perceived_index <- max(1, t - delay)
    perceived <- values[perceived_index]
    inflow <- 0.2 * max(target - perceived, 0)
    values[t + 1] <- values[t] + inflow - 2
  }
  data.frame(period = 0:periods, stock = values)
}
print(simulate_delay())
