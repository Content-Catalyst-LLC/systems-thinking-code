# Dynamic boundary example for systems thinking

function simulate_boundary_score(periods::Int64, external_weight::Float64)
    measured_value = 220000.0
    internal_cost = 90000.0
    external_cost = 280000.0
    scores = Float64[]

    for t in 1:periods
        external_cost *= 1.03
        internal_cost *= 1.01
        push!(scores, measured_value - internal_cost - external_weight * external_cost)
    end

    return scores
end

println("Narrow boundary scores:")
println(simulate_boundary_score(10, 0.25))

println("Broad boundary scores:")
println(simulate_boundary_score(10, 1.0))
