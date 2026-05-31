# Delayed feedback scaffold.
buffer = [0.0, 0.0, 0.0]
state = 40.0
for t in 1:15
    action = t <= 7 ? 5.0 : 2.0
    delayed = popfirst!(buffer)
    push!(buffer, action)
    global state = state + action - 0.6 * delayed
    println("period=", t, ", action=", action, ", delayed_pushback=", delayed, ", state=", round(state, digits=3))
end
