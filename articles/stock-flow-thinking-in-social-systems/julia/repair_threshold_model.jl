# Repair threshold model: repair must exceed ongoing harm.
function repair_threshold(months; stock=35.0, repair=2.5, harm=3.0)
    trajectory = Float64[]
    for _ in 0:months
        push!(trajectory, stock)
        stock = clamp(stock + repair - harm, 0.0, 100.0)
    end
    return trajectory
end

println("Insufficient repair final: ", repair_threshold(24, repair=2.5, harm=3.0)[end])
println("Sufficient repair final: ", repair_threshold(24, repair=4.5, harm=2.0)[end])
