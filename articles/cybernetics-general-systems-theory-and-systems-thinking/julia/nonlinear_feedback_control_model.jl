# Nonlinear feedback-control model for cybernetic systems.

function clamp_value(x, low, high)
    return max(low, min(high, x))
end

function simulate_feedback(initial_state, reference_goal, periods; control_strength=0.42, disturbance=0.58)
    state = initial_state
    rows = []
    for period in 0:periods
        error = reference_goal - state
        control_action = clamp_value(abs(error) * control_strength, 0.0, 100.0)
        direction = error >= 0 ? 1.0 : -1.0
        push!(rows, (period=period, state=round(state, digits=3), error=round(error, digits=3), control=round(control_action, digits=3)))
        state = clamp_value(state + direction * control_action * 0.18 - disturbance * 1.8, 0.0, 100.0)
    end
    return rows
end

rows = simulate_feedback(46.0, 70.0, 48)
println("period,state,error,control_action")
for row in rows
    println("$(row.period),$(row.state),$(row.error),$(row.control)")
end
