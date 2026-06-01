# Dynamic systems examples for "What Is Systems Thinking?"

function stock_flow(initial_stock, inflow, outflow_rate, periods)
    stock = initial_stock
    rows = []
    for period in 1:periods
        outflow = stock * outflow_rate
        stock = stock + inflow - outflow
        push!(rows, (period=period, stock=round(stock, digits=2), inflow=inflow, outflow=round(outflow, digits=2)))
    end
    return rows
end

for row in stock_flow(100.0, 12.0, 0.08, 24)
    println(row)
end
