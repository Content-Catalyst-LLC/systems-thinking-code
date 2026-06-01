# Repair capacity threshold example.

function repair_quality(repair_depth, voice, structural_change)
    return 100.0 * (0.40 * repair_depth + 0.25 * voice + 0.35 * structural_change)
end

println("repair_type,repair_quality")
println("community_governance,$(round(repair_quality(0.84, 0.86, 0.78), digits=3))")
