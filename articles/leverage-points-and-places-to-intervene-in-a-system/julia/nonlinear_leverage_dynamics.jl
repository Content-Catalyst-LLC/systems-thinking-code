# Nonlinear leverage dynamics example
function simulate_leverage(; x0=0.2, strength=0.8, periods=25)
    x = Float64[x0]
    for _ in 1:periods
        current = x[end]
        push!(x, current + strength * current * (1 - current))
    end
    return x
end

println(round.(simulate_leverage(), digits=3))
