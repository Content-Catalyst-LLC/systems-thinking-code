# Nonlinear reinforcing dynamics example.

function simulate(; x0=5.0, r=0.35, k=100.0, periods=30)
    x = x0
    rows = []
    for t in 1:periods
        x = x + r * x * (1 - x / k)
        push!(rows, (t, x))
    end
    return rows
end

for row in simulate()
    println(row)
end
