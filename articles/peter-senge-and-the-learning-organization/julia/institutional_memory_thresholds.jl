# Institutional memory threshold example.

function memory_gap(baseline, target)
    return max(0.0, target - baseline)
end

println("asset,baseline,target,memory_gap")
println("decision_logs,34,80,$(memory_gap(34, 80))")
println("knowledge_base,50,82,$(memory_gap(50, 82))")
