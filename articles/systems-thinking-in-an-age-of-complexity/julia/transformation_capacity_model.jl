# Transformation capacity model.

function transformation_capacity(ethical_leverage, learning_stock, accountability, resilience_stock, boundary_inclusion, harm_stock)
    return max(0.0, min(100.0, 26 * ethical_leverage + 0.20 * learning_stock + 0.22 * accountability + 0.16 * resilience_stock + 14 * boundary_inclusion - 0.12 * harm_stock))
end

println("ethical_leverage,learning_stock,accountability,resilience_stock,boundary_inclusion,harm_stock,transformation_capacity")
println("0.84,76,78,72,0.82,28,$(round(transformation_capacity(0.84, 76, 78, 72, 0.82, 28), digits=3))")
