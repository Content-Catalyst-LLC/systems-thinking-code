# Nonlinear social accumulation example using synthetic assumptions.
function simulate_social_stock(; months=36, initial=40.0, repair=3.0, harm=2.0, threshold=70.0)
    stock = initial
    values = Float64[]
    for _ in 0:months
        push!(values, stock)
        nonlinear_gain = stock > threshold ? 0.4 : 0.0
        stock = clamp(stock + repair + nonlinear_gain - harm, 0.0, 100.0)
    end
    return values
end

values = simulate_social_stock()
println("Final stock value: ", round(values[end], digits=2))
