# Continuous stock-flow model demonstration.

function simulate_stock_flow(; initial_stock=100.0, inflow=12.0, outflow_fraction=0.05, dt=0.1, steps=240)
    stock = initial_stock
    rows = []
    for step in 0:steps
        t = step * dt
        outflow = outflow_fraction * stock
        push!(rows, (time=t, stock=stock, inflow=inflow, outflow=outflow))
        stock = max(0.0, stock + dt * (inflow - outflow))
    end
    return rows
end

if abspath(PROGRAM_FILE) == @__FILE__
    rows = simulate_stock_flow()
    println(first(rows, 5))
end
