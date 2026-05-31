# Delayed balancing behavior using base R.

periods <- 25
value <- rep(80, periods)
goal <- 50
correction <- 0.45
delay <- 3

for (i in (delay + 1):periods) {
  value[i] <- value[i - 1] + correction * (goal - value[i - delay])
}

print(data.frame(period = 1:periods, value = value))
