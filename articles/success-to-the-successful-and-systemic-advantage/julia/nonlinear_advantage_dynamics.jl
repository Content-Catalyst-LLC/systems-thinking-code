# Nonlinear cumulative advantage demonstration.
advantage = [82.0, 28.0, 24.0, 90.0]
feedback = 0.55
for t in 1:12
    total = sum(advantage)
    shares = advantage ./ total
    global advantage = advantage .+ feedback .* shares .* 10
end
println("Final advantage indices: ", round.(advantage, digits=2))
