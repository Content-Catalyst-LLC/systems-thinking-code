# Nonlinear limits-to-growth example.
function simulate(; years=25, initial=100.0, rate=0.13, capacity=260.0)
    scale = initial
    rows = []
    for year in 0:years
        push!(rows, (year=year, scale=round(scale, digits=3), pressure=round(scale / capacity, digits=3)))
        scale += rate * scale * (1 - scale / capacity)
    end
    return rows
end

for row in simulate()
    println(row)
end
