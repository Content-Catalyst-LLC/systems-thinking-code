# Resilience threshold sensitivity.

function resilience_score(redundancy, modularity, learning, trust, response_variety)
    return 20 * redundancy + 18 * modularity + 24 * learning + 16 * trust + 22 * response_variety
end

println("domain,resilience_score")
println("urban_infrastructure,$(round(resilience_score(0.44, 0.40, 0.50, 0.48, 0.46), digits=3))")
println("institutional_learning,$(round(resilience_score(0.48, 0.54, 0.72, 0.60, 0.62), digits=3))")
