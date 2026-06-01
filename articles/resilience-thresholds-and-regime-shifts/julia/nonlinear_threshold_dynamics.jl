# Nonlinear threshold dynamics example for resilience analysis.
# Run with: julia julia/nonlinear_threshold_dynamics.jl

function simulate_resilience(years::Int=35)
    resilience = 78.0
    pressure = 35.0
    rows = []
    for year in 0:years
        pressure += 2.2
        adaptive_gain = 1.1
        nonlinear_degradation = 2.0 + 0.0009 * pressure^2
        resilience = max(0.0, min(100.0, resilience + adaptive_gain - nonlinear_degradation))
        margin = resilience - pressure
        regime = margin <= 0 ? "shifted" : margin <= 10 ? "near_threshold" : "recoverable"
        push!(rows, (year, round(resilience, digits=2), round(pressure, digits=2), round(margin, digits=2), regime))
    end
    return rows
end

for row in simulate_resilience()
    println(join(row, ","))
end
