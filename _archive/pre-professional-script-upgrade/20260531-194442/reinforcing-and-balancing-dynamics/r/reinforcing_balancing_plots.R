# Reinforcing and balancing dynamics example using base R.

period <- 1:20
reinforcing <- numeric(20)
balancing <- numeric(20)
reinforcing[1] <- 10
balancing[1] <- 85

goal <- 50
for (i in 2:20) {
  reinforcing[i] <- reinforcing[i - 1] + 0.12 * reinforcing[i - 1]
  balancing[i] <- balancing[i - 1] + 0.20 * (goal - balancing[i - 1])
}

results <- data.frame(period = period, reinforcing = reinforcing, balancing = balancing)
print(results)
