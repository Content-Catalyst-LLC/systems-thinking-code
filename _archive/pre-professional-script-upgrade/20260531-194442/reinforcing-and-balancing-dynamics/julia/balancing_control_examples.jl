# Balancing control example.

function simulate(; x0=85.0, goal=50.0, correction=0.2, periods=20)
    x = x0
    for t in 1:periods
        x = x + correction * (goal - x)
        println((t, x))
    end
end

simulate()
