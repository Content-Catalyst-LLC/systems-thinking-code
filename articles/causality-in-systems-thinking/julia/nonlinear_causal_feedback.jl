# Nonlinear causal feedback with threshold behavior

function threshold_response(stress, threshold=70.0)
    stress < threshold ? 0.25 * stress : 0.25 * threshold + 1.15 * (stress - threshold)
end

println("stress,response")
for stress in 40:5:100
    println("$stress,$(round(threshold_response(stress), digits=2))")
end
