# Policy resistance threshold example.

function net_policy_impact(intervention, compensating_feedback)
    return intervention - compensating_feedback
end

println("intervention,compensating_feedback,net_policy_impact")
println("40,16,$(round(net_policy_impact(40.0, 16.0), digits=3))")
println("40,34,$(round(net_policy_impact(40.0, 34.0), digits=3))")
