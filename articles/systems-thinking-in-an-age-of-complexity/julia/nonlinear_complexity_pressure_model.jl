# Nonlinear complexity pressure model.

function clamp_value(x, low, high)
    return max(low, min(high, x))
end

function complexity_pressure(interdependence, feedback, delay, adaptation, uncertainty)
    base = 22 * interdependence + 22 * feedback + 18 * delay + 16 * adaptation + 22 * uncertainty
    nonlinear_boost = 12 * interdependence * feedback * delay
    return clamp_value(base + nonlinear_boost, 0.0, 120.0)
end

println("scenario,complexity_pressure")
println("fragmented_reaction,$(round(complexity_pressure(0.82, 0.76, 0.74, 0.34, 0.80), digits=3))")
println("accountable_transformation,$(round(complexity_pressure(0.68, 0.58, 0.46, 0.78, 0.56), digits=3))")
