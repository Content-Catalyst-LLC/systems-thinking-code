# Base R oscillation visualization data
period <- 1:30
goal <- 100
value <- rep(40, 5)
for (t in period) {
  observed <- value[max(1, length(value) - 3)]
  value <- c(value, tail(value, 1) + 0.55 * (goal - observed))
}
plot(period, tail(value, 30), type = "l", xlab = "Period", ylab = "System state", main = "Delayed correction and oscillation")
abline(h = goal, lty = 2)
