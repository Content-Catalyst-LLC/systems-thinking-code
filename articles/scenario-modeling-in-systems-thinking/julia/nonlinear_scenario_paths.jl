# Nonlinear scenario path demonstration

function bounded_trust_update(trust, pressure)
    return clamp(trust + 0.02 * (100 - trust) - 0.05 * pressure^1.2, 0.0, 100.0)
end

trust = 70.0
for year in 1:10
    pressure = year * 2.5
    global trust = bounded_trust_update(trust, pressure)
    println((year=year, trust=round(trust, digits=2)))
end
