# Nonlinear policy-resistance example.
function policy_response(policy_strength, compensation, threshold)
    direct = policy_strength
    nonlinear_resistance = compensation * (policy_strength^2) / (threshold + policy_strength^2)
    return direct - nonlinear_resistance
end

for p in 0.1:0.2:1.1
    println((policy_strength=p, net_effect=round(policy_response(p, 0.8, 0.35), digits=3)))
end
