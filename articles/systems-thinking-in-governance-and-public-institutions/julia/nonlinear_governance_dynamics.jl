trust = 0.50
for t in 1:8
    reliability = 0.45 + 0.03 * t
    fairness = 0.42 + 0.025 * t
    accountability = 0.38 + 0.03 * t
    burden = max(0.25, 0.78 - 0.05 * t)
    opacity = max(0.25, 0.62 - 0.04 * t)
    trust = clamp(trust + 0.06 * ((reliability + fairness + accountability) / 3) - 0.05 * ((burden + opacity) / 2), 0, 1)
    println("period=", t, " trust=", round(trust, digits=3))
end
