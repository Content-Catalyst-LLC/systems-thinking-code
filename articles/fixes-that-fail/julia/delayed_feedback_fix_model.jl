# Delayed feedback fix model.
function simulate(periods::Int=12, delay::Int=3)
    problem = 100.0
    delayed = zeros(delay)
    for t in 1:periods
        fix = min(1.0, problem / 150.0)
        harm = popfirst!(delayed) * 20.0
        problem = max(0.0, problem + 7.0 - 28.0 * fix + harm)
        push!(delayed, fix)
        println("period=$t problem=$(round(problem, digits=2)) fix=$(round(fix, digits=3)) delayed_harm=$(round(harm, digits=2))")
    end
end

simulate()
