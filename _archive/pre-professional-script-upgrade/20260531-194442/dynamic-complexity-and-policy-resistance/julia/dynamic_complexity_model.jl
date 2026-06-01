# Dynamic complexity recurrence model.
function simulate(; months=24, policy=0.7, compensation=0.45, delay=4)
    y = fill(50.0, months)
    for t in 2:months
        lagged = t > delay ? y[t-delay] : y[1]
        y[t] = y[t-1] + 2.5 * policy - compensation * max(0, lagged - 50) / 10
    end
    return y
end

println(round.(simulate(), digits=2))
