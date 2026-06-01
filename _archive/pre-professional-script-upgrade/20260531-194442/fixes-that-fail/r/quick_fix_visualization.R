# Quick-fix immediate relief table.
problem <- 100
strength <- c(0.10, 0.25, 0.40, 0.55, 0.70)
remaining <- pmax(0, problem * (1 - strength))
print(data.frame(fix_strength = strength, remaining_problem = remaining))
