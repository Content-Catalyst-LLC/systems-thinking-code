# Nonlinear threshold behavior demonstration.

function threshold_response(x; threshold=100.0)
    if x < threshold
        return 0.02 * x
    else
        return 0.08 * x
    end
end

function simulate_threshold(; initial=50.0, stress_inflow=5.0, steps=30)
    stress = initial
    rows = []
    for t in 0:steps
        loss = threshold_response(stress)
        push!(rows, (time=t, stress=stress, loss=loss))
        stress = stress + stress_inflow - loss
    end
    return rows
end

if abspath(PROGRAM_FILE) == @__FILE__
    println(first(simulate_threshold(), 10))
end
