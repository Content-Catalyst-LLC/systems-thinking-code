# Dynamic cross-scale example

function simulate_cross_scale(periods::Int=12)
    micro_burden = 60.0
    meso_capacity = 65.0
    macro_stress = 70.0

    println("period,micro_burden,meso_capacity,macro_stress")
    for t in 1:periods
        micro_burden += 0.05 * macro_stress - 0.03 * meso_capacity
        meso_capacity += 0.02 * (100 - micro_burden) - 0.01 * macro_stress
        macro_stress += 0.5 - 0.01 * meso_capacity
        println("$t,$(round(micro_burden, digits=2)),$(round(meso_capacity, digits=2)),$(round(macro_stress, digits=2))")
    end
end

simulate_cross_scale()
