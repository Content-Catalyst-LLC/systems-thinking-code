# Dependency-light Julia climate feedback sensitivity scan.
# Run with: julia julia/nonlinear_climate_feedback_dynamics.jl

function forcing(co2, reference)
    return 5.35 * log(co2 / reference)
end

function simulate(feedback_multiplier; years=80, co2=420.0, emissions=40.0, decline=0.04)
    temp = 1.2
    heat = 0.0
    for year in 0:years
        emissions *= (1.0 - decline)
        co2 += (emissions / 7.8) * 0.55
        f = forcing(co2, 280.0)
        heat += f * 0.035
        target = 0.78 * f * feedback_multiplier
        temp += 0.10 * (target - temp) + heat * 0.006
    end
    return (co2=co2, temp=temp, heat=heat)
end

for multiplier in [1.15, 1.25, 1.35]
    result = simulate(multiplier)
    println("feedback_multiplier=", multiplier, " final_temp=", round(result.temp, digits=3), " final_co2=", round(result.co2, digits=2))
end
