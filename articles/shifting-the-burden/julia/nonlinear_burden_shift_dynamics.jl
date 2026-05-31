# Nonlinear burden-shift dynamics demonstration.
function simulate_burden_shift(periods::Int)
    pressure = 80.0
    capacity = 55.0
    dependency = 0.30
    rows = []

    for t in 0:(periods - 1)
        symptomatic = 35.0 + 8.0 * dependency
        repair = 8.0 + 3.0 * max(0, t - 5)
        capacity = max(0.0, capacity + 0.65 * repair - 0.22 * symptomatic)
        dependency = max(0.0, dependency + 0.011 * symptomatic - 0.015 * repair)
        pressure = max(0.0, pressure + 5.0 - 0.36 * symptomatic - 0.22 * capacity)
        push!(rows, (t, round(pressure, digits=2), round(capacity, digits=2), round(dependency, digits=3)))
    end

    return rows
end

for row in simulate_burden_shift(12)
    println(row)
end
