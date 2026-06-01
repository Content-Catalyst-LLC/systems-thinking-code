# Delayed feedback dynamics demonstration.

function simulate_delay(; goal=100.0, initial=40.0, delay=4, gain=0.25, steps=36)
    state = initial
    history = fill(initial, delay)
    rows = []
    for t in 0:steps
        perceived = history[1]
        correction = gain * (goal - perceived)
        push!(rows, (time=t, state=state, perceived=perceived, correction=correction))
        state += correction
        popfirst!(history)
        push!(history, state)
    end
    return rows
end

if abspath(PROGRAM_FILE) == @__FILE__
    println(first(simulate_delay(), 8))
end
