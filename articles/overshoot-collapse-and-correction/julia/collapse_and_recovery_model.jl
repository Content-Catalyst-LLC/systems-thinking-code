# Collapse and recovery stock model.
function recovery_path(; months=30, pressure=0.72, stock=0.45, restoration=0.035)
    rows = []
    for month in 0:months
        depletion = max(0.0, pressure - 0.55) * 0.05
        stock = clamp(stock + restoration - depletion, 0.0, 1.0)
        pressure = clamp(pressure - 0.006, 0.0, 1.0)
        push!(rows, (month=month, stock=stock, pressure=pressure))
    end
    return rows
end

for row in recovery_path()
    println(row)
end
