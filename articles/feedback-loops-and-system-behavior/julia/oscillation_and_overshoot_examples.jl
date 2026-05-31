# Delayed balancing feedback example with overshoot.

function delayed_balancing(goal::Float64, initial::Float64, correction::Float64, delay::Int64, periods::Int64)
    history = fill(initial, delay + 1)
    value = initial
    rows = Tuple{Int64, Float64}[]
    for t in 1:periods
        observed = history[1]
        value = value + correction * (goal - observed)
        popfirst!(history)
        push!(history, value)
        push!(rows, (t, value))
    end
    return rows
end

println("period,value")
for (period, value) in delayed_balancing(100.0, 40.0, 0.35, 5, 40)
    println("$period,$(round(value, digits=3))")
end
