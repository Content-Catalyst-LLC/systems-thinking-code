# Continuous stock-flow Euler approximation.
function simulate_stock(initial, inflow, outflow, dt, steps)
    values = Float64[initial]
    stock = initial
    for _ in 1:steps
        stock += dt * (inflow(stock) - outflow(stock))
        push!(values, stock)
    end
    return values
end

values = simulate_stock(50.0, s -> 4.0 + 0.05 * max(80.0 - s, 0.0), s -> 3.0, 1.0, 12)
println(values)
