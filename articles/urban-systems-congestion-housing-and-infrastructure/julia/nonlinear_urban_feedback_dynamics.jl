# Dependency-light Julia urban feedback simulation.
function clamp01(x)
    return max(0.0, min(100.0, x))
end

function run_model(years::Int=30)
    congestion = 48.0
    affordability = 44.0
    infrastructure = 62.0
    displacement = 40.0
    for year in 1:years
        congestion = clamp01(congestion + 0.65 - affordability * 0.004 + displacement * 0.006)
        affordability = clamp01(affordability + 0.35 - congestion * 0.015 - displacement * 0.01)
        infrastructure = clamp01(infrastructure + 0.45 - 1.20 - congestion * 0.01)
        displacement = clamp01(displacement + 0.18 + affordability * -0.004 + congestion * 0.005)
    end
    resilience = clamp01(0.25 * (100 - congestion) + 0.25 * affordability + 0.30 * infrastructure + 0.20 * (100 - displacement))
    println("Urban feedback simulation")
    println("congestion=", round(congestion, digits=3))
    println("affordability=", round(affordability, digits=3))
    println("infrastructure=", round(infrastructure, digits=3))
    println("displacement=", round(displacement, digits=3))
    println("resilience=", round(resilience, digits=3))
end

run_model()
