# Threshold adoption sensitivity example.

function adoption_probability(exposure, threshold, trust)
    gap = exposure - threshold
    return max(0.0, min(1.0, 0.5 + gap + 0.25 * trust))
end

println("exposure,threshold,trust,adoption_probability")
for exposure in [0.2, 0.4, 0.6, 0.8]
    println("$(exposure),0.5,0.6,$(round(adoption_probability(exposure, 0.5, 0.6), digits=3))")
end
