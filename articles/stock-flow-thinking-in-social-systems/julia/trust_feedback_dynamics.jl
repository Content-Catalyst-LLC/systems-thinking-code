# Trust feedback dynamics demonstration.
function trust_feedback(months, trust, reliability, harm)
    values = Float64[]
    for _ in 0:months
        push!(values, trust)
        cooperation_effect = trust / 100.0
        trust = clamp(trust + reliability * cooperation_effect - harm, 0.0, 100.0)
    end
    return values
end

println(trust_feedback(12, 45.0, 5.0, 2.0))
