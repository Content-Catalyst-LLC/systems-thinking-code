# Nonlinear overshoot dynamics example.
function simulate_overshoot(; months=36, r=0.07, K=0.60, delay=6)
    pressure = 0.40
    history = [pressure]
    rows = []
    for month in 0:months
        perceived = history[max(1, length(history) - delay)]
        pressure = clamp(pressure + r * pressure * (1 - perceived / K), 0.0, 1.2)
        push!(rows, (month=month, pressure=pressure, overshoot=max(0.0, pressure-K)))
        push!(history, pressure)
    end
    return rows
end

for row in simulate_overshoot()
    println(row)
end
