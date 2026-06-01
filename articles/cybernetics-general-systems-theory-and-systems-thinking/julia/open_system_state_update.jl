# Open-system state update example.

function next_state(state, inflow, outflow, environmental_exchange)
    return state + inflow - outflow + environmental_exchange
end

println("state,inflow,outflow,environmental_exchange,next_state")
println("46,8,5,2,$(next_state(46, 8, 5, 2))")
