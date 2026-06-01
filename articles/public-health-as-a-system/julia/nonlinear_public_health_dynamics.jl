# Lightweight Julia public health dynamics example.
# Run with: julia julia/nonlinear_public_health_dynamics.jl

function simulate(; population=100000.0, infected0=180.0, beta=0.39, gamma=0.20, prevention=0.42, weeks=52)
    susceptible = population - infected0
    infected = infected0
    recovered = 0.0
    for week in 0:weeks
        effective_beta = beta * (1.0 - prevention)
        new_infections = min(susceptible, effective_beta * susceptible * infected / population)
        recoveries = min(infected, gamma * infected)
        susceptible -= new_infections
        infected += new_infections - recoveries
        recovered += recoveries
    end
    return (susceptible=susceptible, infected=infected, recovered=recovered)
end

result = simulate()
println("Final infected: ", round(result.infected, digits=3))
