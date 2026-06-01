# Allocation feedback: prior advantage versus need-adjusted scoring.
advantage = [82.0, 28.0, 24.0, 90.0]
need = [22.0, 86.0, 91.0, 18.0]
performance_only = 0.85 .* advantage .+ 0.05 .* need
need_adjusted = 0.45 .* advantage .+ 0.30 .* need .+ 0.20 .* (100 .- advantage)
println("Performance-only scores: ", round.(performance_only, digits=2))
println("Need-adjusted scores: ", round.(need_adjusted, digits=2))
