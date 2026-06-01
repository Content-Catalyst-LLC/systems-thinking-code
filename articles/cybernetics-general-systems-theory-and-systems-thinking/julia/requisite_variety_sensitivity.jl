# Requisite variety sensitivity example.

function variety_gap(disturbance_variety, response_variety)
    return max(0.0, disturbance_variety - response_variety)
end

println("domain,disturbance_variety,response_variety,variety_gap")
println("ai_platform_governance,0.88,0.52,$(round(variety_gap(0.88, 0.52), digits=3))")
println("infrastructure_operations,0.70,0.74,$(round(variety_gap(0.70, 0.74), digits=3))")
