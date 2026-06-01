# Dependency-light Julia example for AI feedback dynamics.
# Run with: julia julia/ai_feedback_dynamics.jl

function clamp01(x)
    max(0.0, min(100.0, x))
end

risk = 25.0
governance = 45.0
feedback = 18.0
println("period,risk,governance,feedback")
for t in 0:24
    global risk, governance, feedback
    println("$t,$(round(risk,digits=3)),$(round(governance,digits=3)),$(round(feedback,digits=3))")
    feedback = clamp01(feedback + 0.8 - governance * 0.01)
    risk = clamp01(risk + feedback * 0.06 - governance * 0.04)
    governance = clamp01(governance + 0.35)
end
