# Dynamic systems example for patterns and structural explanation.

function simulate_backlog(; periods=18, backlog=120.0, capacity=55.0)
    rows = []
    for period in 1:periods
        incoming = 11.0 + period * 0.25
        completed = max(5.0, capacity / 6.0 - backlog / 150.0)
        backlog = backlog + incoming - completed
        capacity = capacity - backlog / 500.0 + 0.5
        push!(rows, (period=period, backlog=round(backlog, digits=2), capacity=round(capacity, digits=2)))
    end
    return rows
end

for row in simulate_backlog()
    println(row)
end
