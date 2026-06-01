# Nonlinear learning-loop model for Senge-inspired learning organizations.

function clamp_value(x, low, high)
    return max(low, min(high, x))
end

function simulate_learning(initial_learning, periods; feedback=0.70, safety=0.68, defensiveness=0.30)
    learning = initial_learning
    rows = []
    for period in 0:periods
        learning_flow = feedback * 4.5 + safety * 3.8 - defensiveness * 2.2
        forgetting_flow = defensiveness * 2.6
        push!(rows, (period=period, learning=round(learning, digits=3)))
        learning = clamp_value(learning + learning_flow - forgetting_flow, 0.0, 100.0)
    end
    return rows
end

rows = simulate_learning(34.0, 48)
println("period,learning_stock")
for row in rows
    println("$(row.period),$(row.learning)")
end
