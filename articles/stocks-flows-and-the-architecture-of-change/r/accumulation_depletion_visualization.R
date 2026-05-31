# Visualize a simple accumulation/depletion trajectory.
period <- 0:10
stock <- 55 + cumsum(c(0, rep(-1, 10)))
plot(period, stock, type = "b", xlab = "Period", ylab = "Stock value", main = "Accumulation and Depletion Example")
