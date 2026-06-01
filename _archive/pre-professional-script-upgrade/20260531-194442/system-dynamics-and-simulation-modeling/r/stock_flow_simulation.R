# Stock-flow simulation in R using synthetic assumptions.

simulate_stock <- function(initial_stock = 100, inflow_rate = 12, outflow_fraction = 0.05, steps = 24) {
  stock <- initial_stock
  rows <- list()
  for (t in 0:steps) {
    inflow <- inflow_rate
    outflow <- outflow_fraction * stock
    rows[[length(rows) + 1]] <- data.frame(
      time = t,
      stock = stock,
      inflow = inflow,
      outflow = outflow,
      net_flow = inflow - outflow
    )
    stock <- max(0, stock + inflow - outflow)
  }
  do.call(rbind, rows)
}

if (sys.nframe() == 0) {
  print(head(simulate_stock()))
}
