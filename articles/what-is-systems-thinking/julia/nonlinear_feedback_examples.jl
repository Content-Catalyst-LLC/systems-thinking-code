# Nonlinear feedback example.

function logistic_growth(x0, rate, carrying_capacity, periods)
    x = x0
    rows = []
    for period in 1:periods
        x = x + rate * x * (1 - x / carrying_capacity)
        push!(rows, (period=period, value=round(x, digits=4)))
    end
    return rows
end

for row in logistic_growth(5.0, 0.35, 100.0, 30)
    println(row)
end
