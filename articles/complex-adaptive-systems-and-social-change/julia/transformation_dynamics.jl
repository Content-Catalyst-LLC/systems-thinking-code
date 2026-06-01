# Transformation dynamics scoring example.

function momentum(adoption, trust, institutional_response, learning, resistance)
    return max(0.0, min(100.0, 0.30 * adoption + 0.22 * trust + 0.20 * institutional_response + 0.18 * learning - 0.20 * resistance))
end

println("adoption,trust,institutional_response,learning,resistance,momentum")
println("70,65,60,72,32,$(round(momentum(70, 65, 60, 72, 32), digits=3))")
