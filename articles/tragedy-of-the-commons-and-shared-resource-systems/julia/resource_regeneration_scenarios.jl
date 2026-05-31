# Resource regeneration scenario comparison.
function final_stock(regen_rate, use, restoration)
    stock = 1000.0
    for year in 1:25
        regeneration = regen_rate * stock * max(0.0, 1.0 - stock / 1400.0)
        stock = max(0.0, stock + regeneration + restoration - use)
    end
    return stock
end
for use in [90.0, 110.0, 140.0]
    println("annual_use=", use, ", final_stock=", round(final_stock(0.22, use, 20.0), digits=2))
end
