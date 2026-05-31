# Nonlinear timing feedback example.
function nonlinear_policy_response(x, threshold, strength)
    if x < threshold
        return x + strength * (threshold - x)
    else
        return x - 0.5 * strength * (x - threshold)^2
    end
end

state = 0.4
for t in 1:20
    global state = nonlinear_policy_response(state, 1.0, 0.2)
    println((t, state))
end
