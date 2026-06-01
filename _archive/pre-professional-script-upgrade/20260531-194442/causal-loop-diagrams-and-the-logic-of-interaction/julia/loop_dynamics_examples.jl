# Simple reinforcing loop dynamics example.
function reinforcing_loop(x0, rate, steps)
    values = zeros(Float64, steps + 1)
    values[1] = x0
    for t in 1:steps
        values[t + 1] = values[t] + rate * values[t]
    end
    values
end

println(reinforcing_loop(10.0, 0.08, 12))
