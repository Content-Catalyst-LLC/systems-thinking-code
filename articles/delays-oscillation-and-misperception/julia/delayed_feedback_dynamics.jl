# Delayed feedback dynamics example
function delayed_feedback(; goal=50.0, initial=80.0, correction=0.25, delay=3, periods=24)
    values = fill(initial, delay + 1)
    rows = []
    for t in 1:periods
        observed = values[max(1, length(values) - delay)]
        next_value = values[end] + correction * (goal - observed)
        push!(values, next_value)
        push!(rows, (t, next_value, observed))
    end
    return rows
end

for row in delayed_feedback()
    println(row)
end
