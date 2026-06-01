# Resilience threshold example.

function resilience_capacity(buffer_depth, self_organization, trust, ecological_regeneration)
    return max(0.0, min(100.0, 0.30 * buffer_depth + 0.25 * self_organization + 0.20 * trust + 0.25 * ecological_regeneration))
end

println("buffer_depth,self_organization,trust,regeneration,resilience")
println("72,78,66,70,$(round(resilience_capacity(72, 78, 66, 70), digits=3))")
