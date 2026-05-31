# Compare simple stock-flow scenarios.
scenario <- c("baseline", "prevention", "repair", "balanced")
inflow <- c(4, 4, 7, 7)
outflow <- c(5, 3.5, 5, 3.5)
net <- inflow - outflow
print(data.frame(scenario, inflow, outflow, net))
