# Delayed policy dynamics example.
function delayed_response(months::Int, goal::Float64, delay::Int, correction::Float64)
    values = fill(0.35, delay + 1)
    for t in 1:months
        delayed_value = values[end - delay + 1]
        next_value = values[end] + correction * (goal - delayed_value)
        push!(values, clamp(next_value, 0.0, 1.8))
    end
    return values
end

println(delayed_response(24, 1.0, 5, 0.45))
