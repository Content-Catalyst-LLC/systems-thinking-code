# Nonlinear asset deterioration model for intelligent infrastructure.
# Dependency-light Julia example.

function clamp100(x)
    return max(0.0, min(100.0, x))
end

function simulate_condition(initial_condition, years; climate_stress=0.5, maintenance_strength=0.5)
    condition = initial_condition
    rows = []
    for year in 0:years
        push!(rows, (year=year, condition=round(condition, digits=3)))
        deterioration = 1.8 + climate_stress * (100.0 - condition) * 0.025
        maintenance = maintenance_strength * 2.2
        condition = clamp100(condition - deterioration + maintenance)
    end
    return rows
end

rows = simulate_condition(64.0, 20; climate_stress=0.55, maintenance_strength=0.70)
println("year,condition")
for row in rows
    println("$(row.year),$(row.condition)")
end
