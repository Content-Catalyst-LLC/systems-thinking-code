# Nonlinear feedback-delay model for Forrester-style system dynamics.

function clamp_value(x, low, high)
    return max(low, min(high, x))
end

function simulate_backlog(initial_backlog, periods; capacity=46.0, delay=4, correction_strength=0.42)
    backlog = initial_backlog
    history = [backlog]
    rows = []
    for period in 0:periods
        perceived = length(history) <= delay ? history[1] : history[end-delay]
        correction = max(0.0, correction_strength * (perceived - 25.0))
        service = capacity * 0.42 + correction * 0.15
        push!(rows, (period=period, backlog=round(backlog, digits=3), perceived=round(perceived, digits=3)))
        backlog = clamp_value(backlog + 3.0 - service, 0.0, 200.0)
        push!(history, backlog)
    end
    return rows
end

rows = simulate_backlog(58.0, 48)
println("period,backlog,perceived_backlog")
for row in rows
    println("$(row.period),$(row.backlog),$(row.perceived)")
end
