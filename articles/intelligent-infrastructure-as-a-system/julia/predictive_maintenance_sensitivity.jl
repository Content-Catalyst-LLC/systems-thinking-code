# Predictive maintenance sensitivity example.

function priority_score(condition, criticality, redundancy, equity)
    return 0.35 * (100 - condition) + 0.30 * criticality + 0.20 * (100 - redundancy) + 0.15 * equity
end

conditions = [40, 55, 70, 85]
println("condition,priority_score")
for c in conditions
    println("$(c),$(round(priority_score(c, 85, 35, 80), digits=3))")
end
