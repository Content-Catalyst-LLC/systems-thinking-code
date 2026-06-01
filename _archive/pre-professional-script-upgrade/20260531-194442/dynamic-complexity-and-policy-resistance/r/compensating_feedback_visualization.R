# Compensating feedback visualization.
compensation <- seq(0, 1.2, by = 0.1)
intended <- 100
net <- intended * (1 - compensation)
out <- data.frame(compensation = compensation, net_effect = net)
print(out)
