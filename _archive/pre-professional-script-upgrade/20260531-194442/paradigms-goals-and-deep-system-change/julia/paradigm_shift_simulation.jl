# Paradigm shift simulation: old goal vs new goal.

function simulate(goal_weight_access, goal_weight_throughput)
    access = 0.45
    throughput = 0.70
    burden = 0.65
    for _ in 1:8
        throughput += 0.04 * goal_weight_throughput
        access += 0.05 * goal_weight_access - 0.02 * burden
        burden += 0.03 * goal_weight_throughput - 0.05 * goal_weight_access
        access = clamp(access, 0.0, 1.0)
        throughput = clamp(throughput, 0.0, 1.0)
        burden = clamp(burden, 0.0, 1.0)
    end
    return (access=access, throughput=throughput, burden=burden)
end

println("old paradigm: ", simulate(0.15, 1.0))
println("new paradigm: ", simulate(0.90, 0.45))
