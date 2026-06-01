# Cyber-physical resilience threshold example.

function cyber_dependency(connectivity, vendor_lockin, fallback_capacity)
    return max(0.0, min(100.0, 0.4 * connectivity + 0.4 * vendor_lockin + 0.2 * (100 - fallback_capacity)))
end

println("connectivity,vendor_lockin,fallback_capacity,dependency")
for connectivity in [30, 60, 90]
    println("$(connectivity),70,40,$(round(cyber_dependency(connectivity, 70, 40), digits=3))")
end
