# Stock-flow sensitivity example.

function next_stock(stock, inflow, outflow, dt)
    return stock + dt * (inflow - outflow)
end

println("dt,next_stock")
for dt in [0.25, 0.5, 1.0, 2.0]
    println("$(dt),$(round(next_stock(58.0, 4.5, 6.2, dt), digits=3))")
end
