# Nonlinear fixes-that-fail demonstration with base Julia.
function simulate(periods::Int=14)
    problem = 100.0
    capacity = 1.0
    results = []
    for t in 1:periods
        fix = min(1.0, problem / 140.0)
        nonlinear_side_effect = 16.0 * fix^2
        capacity = max(0.2, capacity - 0.04 * fix + 0.015)
        problem = max(0.0, problem + 8.0 - 24.0 * fix + nonlinear_side_effect + 8.0 * (1.0 - capacity))
        push!(results, (t=t, problem=problem, capacity=capacity, fix=fix))
    end
    return results
end

for row in simulate()
    println(row)
end
