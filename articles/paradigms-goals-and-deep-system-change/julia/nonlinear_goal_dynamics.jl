# Nonlinear goal dynamics example for systems thinking.

function step(x, goal, correction_strength)
    gap = goal - x
    nonlinear_response = correction_strength * tanh(gap)
    return clamp(x + nonlinear_response, 0.0, 1.0)
end

x = 0.25
goal = 0.80
for t in 1:12
    global x = step(x, goal, 0.35)
    println("t=", t, " state=", round(x, digits=3))
end
