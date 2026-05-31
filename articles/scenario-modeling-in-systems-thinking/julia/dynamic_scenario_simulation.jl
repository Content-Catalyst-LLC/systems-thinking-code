# Synthetic dynamic scenario simulation example

function run_scenario(capacity_growth, demand_growth; years=10)
    capacity = 100.0
    demand = 95.0
    rows = []
    for year in 0:years
        push!(rows, (year=year, capacity=capacity, demand=demand, gap=demand-capacity))
        capacity *= (1 + capacity_growth)
        demand *= (1 + demand_growth)
    end
    return rows
end

for row in run_scenario(0.03, 0.025)
    println(row)
end
