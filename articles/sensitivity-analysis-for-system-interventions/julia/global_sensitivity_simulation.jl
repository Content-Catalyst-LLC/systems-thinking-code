# Synthetic global sensitivity simulation scaffold.
function resilience(delay, demand, repair, harm, trust, buffer)
    clamp(0.55 - 0.025 * delay - 1.5 * demand + 1.7 * repair - 1.8 * harm + 0.22 * trust + 0.75 * buffer, 0.0, 1.0)
end

println("Example resilience score: ", resilience(6, 0.04, 0.08, 0.05, 0.6, 0.15))
