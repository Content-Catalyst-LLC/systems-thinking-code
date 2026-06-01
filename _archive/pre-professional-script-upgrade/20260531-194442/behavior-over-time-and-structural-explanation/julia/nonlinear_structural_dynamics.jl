# Nonlinear structural dynamics example
function logistic_growth(x0, r, k, steps)
    xs = Float64[x0]
    for _ in 1:steps
        x = xs[end]
        push!(xs, x + r * x * (1 - x / k))
    end
    return xs
end

println(logistic_growth(5.0, 0.45, 100.0, 30))
