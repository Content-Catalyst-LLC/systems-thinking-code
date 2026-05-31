# Dynamic behavior patterns in Julia
function reinforcing_growth(x0, r, steps)
    xs = Float64[x0]
    for _ in 1:steps
        push!(xs, xs[end] * (1 + r))
    end
    return xs
end

function balancing_goal_seek(x0, goal, k, steps)
    xs = Float64[x0]
    for _ in 1:steps
        push!(xs, xs[end] + k * (goal - xs[end]))
    end
    return xs
end

println("Reinforcing growth: ", reinforcing_growth(10.0, 0.10, 10))
println("Balancing goal seek: ", balancing_goal_seek(80.0, 30.0, 0.25, 10))
