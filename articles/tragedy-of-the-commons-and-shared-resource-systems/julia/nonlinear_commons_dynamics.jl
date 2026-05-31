# Synthetic nonlinear commons dynamics example.
function simulate(stock0, capacity, regen_rate, annual_use, years)
    stock = stock0
    values = Float64[]
    for year in 0:years
        push!(values, stock)
        regeneration = regen_rate * stock * max(0.0, 1.0 - stock / capacity)
        stock = max(0.0, stock + regeneration - annual_use)
    end
    return values
end

values = simulate(1000.0, 1400.0, 0.22, 120.0, 25)
println("Final synthetic commons stock: ", round(values[end], digits=2))
