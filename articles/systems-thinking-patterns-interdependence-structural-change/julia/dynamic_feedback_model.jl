# Systems Thinking: Dynamic Feedback Model in Julia
# Educational example only.

function simulate_balancing(target::Float64, initial::Float64, correction::Float64, delay::Int, steps::Int)
    values = zeros(Float64, steps)
    values[1] = initial

    for t in 2:steps
        delayed_index = max(1, t - delay)
        perceived_gap = target - values[delayed_index]
        values[t] = values[t - 1] + correction * perceived_gap
    end

    return values
end

values = simulate_balancing(100.0, 25.0, 0.18, 8, 80)

println("Balancing feedback with delay:")
for (i, value) in enumerate(values)
    println(i, ",", value)
end
