# Dynamic interdependence example for Wholes, Parts, and Interdependence

function simulate_interdependence(periods::Int=20)
    capacity = 70.0
    stress = 30.0
    resilience = 45.0
    rows = []

    for t in 1:periods
        stress = stress + 3.0 + 0.04 * capacity - 0.08 * resilience
        capacity = capacity - 0.05 * stress + 0.03 * resilience
        resilience = resilience + 1.5 - 0.04 * stress
        push!(rows, (period=t, capacity=round(capacity, digits=2), stress=round(stress, digits=2), resilience=round(resilience, digits=2)))
    end

    return rows
end

for row in simulate_interdependence()
    println(row)
end
