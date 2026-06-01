# Nonlinear platform feedback dynamics example.
# Run with: julia julia/nonlinear_platform_feedback_dynamics.jl

function clamp(x, lo=0.0, hi=100.0)
    return max(lo, min(hi, x))
end

engagement = 55.0
risk = 20.0
trust = 70.0
for t in 1:36
    engagement = clamp(engagement + 0.08 * engagement - 0.03 * risk)
    risk = clamp(risk + 0.06 * engagement - 0.05 * trust)
    trust = clamp(trust - 0.04 * risk + 1.2)
end
println("Final engagement=", round(engagement, digits=3), " risk=", round(risk, digits=3), " trust=", round(trust, digits=3))
