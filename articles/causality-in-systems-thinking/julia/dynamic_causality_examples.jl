# Dynamic causality example for systems thinking

function simulate_dynamic_causality(periods::Int=20)
    trust = 64.0
    capacity = 58.0
    demand = 70.0
    rows = []

    for t in 1:periods
        delay = max(1.0, demand / max(capacity, 1.0) * 10.0)
        trust += capacity / 140.0 - delay / 18.0
        capacity += trust / 120.0 - demand / 180.0
        demand += max(0.0, 65.0 - trust) * 0.05
        push!(rows, (t, round(trust, digits=2), round(capacity, digits=2), round(demand, digits=2), round(delay, digits=2)))
    end

    return rows
end

println("period,trust,capacity,demand,delay")
for row in simulate_dynamic_causality()
    println(join(row, ","))
end
