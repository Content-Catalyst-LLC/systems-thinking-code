# Nonlinear accumulation with capacity pressure.
function step(stock, capacity, growth_rate)
    return stock + growth_rate * stock * (1 - stock / capacity)
end

stock = 10.0
for period in 1:20
    global stock = step(stock, 100.0, 0.18)
    println((period = period, stock = round(stock, digits = 3)))
end
