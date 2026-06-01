# Dynamic capacity constraint model.
function simulate(; years=20)
    scale = 100.0
    capacity = 220.0
    for year in 0:years
        investment = year < 5 ? 8.0 : 18.0
        degradation = 0.04 * scale
        capacity = max(50.0, capacity + investment - degradation)
        pressure = scale / capacity
        growth_rate = max(0.0, 0.14 * (1 - max(0.0, pressure - 1.0)))
        println((year=year, scale=round(scale, digits=2), capacity=round(capacity, digits=2), pressure=round(pressure, digits=2)))
        scale += growth_rate * scale
    end
end

simulate()
