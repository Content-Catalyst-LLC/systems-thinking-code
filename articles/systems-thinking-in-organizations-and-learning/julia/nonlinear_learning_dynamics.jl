# Nonlinear organizational learning dynamics placeholder.
capacity_next(capacity, learning, turnover, depletion) = capacity + learning - turnover - depletion
println("Capacity example: ", capacity_next(0.65, 0.08, 0.04, 0.05))
