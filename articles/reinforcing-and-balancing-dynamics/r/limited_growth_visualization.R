# Limited growth using base R.

periods <- 30
x <- numeric(periods)
x[1] <- 5
r <- 0.35
K <- 100

for (i in 2:periods) {
  x[i] <- x[i - 1] + r * x[i - 1] * (1 - x[i - 1] / K)
}

print(data.frame(period = 1:periods, value = x))
