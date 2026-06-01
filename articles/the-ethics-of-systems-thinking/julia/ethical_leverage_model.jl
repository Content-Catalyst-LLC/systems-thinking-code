# Ethical leverage model.

function ethical_leverage(structural_change, repair_stock, power_redistribution, accountability)
    return max(0.0, min(100.0, 25.0 * structural_change + 0.22 * repair_stock + 22.0 * power_redistribution + 0.18 * accountability))
end

println("structural_change,repair_stock,power_redistribution,accountability,ethical_leverage")
println("0.84,70,0.78,74,$(round(ethical_leverage(0.84, 70, 0.78, 74), digits=3))")
