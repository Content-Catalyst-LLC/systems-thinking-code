# Simple signed-network influence example.
variables = ["Trust", "Cooperation", "Performance"]
A = [0 1 0; 0 0 1; 1 0 0]
state = [0.5, 0.4, 0.6]
for step in 1:5
    global state = clamp.(state .+ 0.1 .* (A * state), 0.0, 1.0)
    println("step=", step, " state=", Dict(zip(variables, state)))
end
