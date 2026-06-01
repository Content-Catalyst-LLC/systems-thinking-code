#!/usr/bin/env julia
# Professional dynamic sensitivity model for Feedback Loops and System Behavior
function clamp01(x, lo=0.0, hi=100.0)
    return max(lo, min(hi, x))
end
base_stock = 80; base_capacity = 49; base_burden = 42
regen = 0.025; degrade = 4.7
function simulate(pressure_reduction, capacity_investment; years=30)
    stock = base_stock; capacity = base_capacity; burden = base_burden
    for year in 0:years
        pressure = (degrade + 2.1 * year * 0.45) * (1.0 - pressure_reduction)
        burden = clamp01(burden + pressure * 0.08 - capacity_investment * 0.35)
        capacity = clamp01(capacity + capacity_investment - burden * 0.015)
        stock = clamp01(stock + stock * regen - pressure - burden * 0.035 + capacity * 0.025, 0.0, 120.0)
    end
    risk = clamp01(100 - (0.45 * stock + 0.35 * capacity - 0.20 * burden))
    return stock, capacity, burden, risk
end
println("pressure_reduction,capacity_investment,final_stock,final_capacity,final_burden,final_risk")
for pr in 0.0:0.1:0.5, ci in 0.0:0.5:3.0
    stock, capacity, burden, risk = simulate(pr, ci)
    println(join([round(pr, digits=2), round(ci, digits=2), round(stock, digits=2), round(capacity, digits=2), round(burden, digits=2), round(risk, digits=2)], ","))
end
