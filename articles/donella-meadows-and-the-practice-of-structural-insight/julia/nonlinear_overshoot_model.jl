# Nonlinear overshoot model for Meadows-inspired structural insight.

function clamp_value(x, low, high)
    return max(low, min(high, x))
end

function simulate_resource(initial_resource, periods; consumption_pressure=0.62, regeneration_capacity=0.50)
    resource = initial_resource
    rows = []
    for period in 0:periods
        consumption = clamp_value(consumption_pressure * 9.0 + max(0.0, 70.0 - resource) * 0.04, 0.0, 100.0)
        regeneration = clamp_value(regeneration_capacity * 6.0 + 2.5, 0.0, 100.0)
        push!(rows, (period=period, resource=round(resource, digits=3), consumption=round(consumption, digits=3), regeneration=round(regeneration, digits=3)))
        resource = clamp_value(resource - consumption + regeneration, 0.0, 100.0)
    end
    return rows
end

rows = simulate_resource(82.0, 60)
println("period,resource,consumption,regeneration")
for row in rows
    println("$(row.period),$(row.resource),$(row.consumption),$(row.regeneration)")
end
