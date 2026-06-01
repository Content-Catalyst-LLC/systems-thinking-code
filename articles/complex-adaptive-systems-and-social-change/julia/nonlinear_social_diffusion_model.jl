# Nonlinear social diffusion model for complex adaptive social change.

function clamp100(x)
    return max(0.0, min(100.0, x))
end

function simulate_adoption(initial_adoption, periods; network_reach=0.6, resistance=0.3, learning=0.5)
    adoption = initial_adoption
    rows = []
    for period in 0:periods
        push!(rows, (period=period, adoption=round(adoption, digits=3)))
        diffusion = network_reach * adoption * (100.0 - adoption) / 100.0 * 0.08
        adaptation = learning * 1.5
        opposition = resistance * adoption * 0.025
        adoption = clamp100(adoption + diffusion + adaptation - opposition)
    end
    return rows
end

rows = simulate_adoption(18.0, 48; network_reach=0.70, resistance=0.34, learning=0.82)
println("period,adoption")
for row in rows
    println("$(row.period),$(row.adoption)")
end
