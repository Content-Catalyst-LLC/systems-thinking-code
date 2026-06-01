function clamp100(x)
    return min(100.0, max(0.0, x))
end
function next_outcome(outcome, effort, burden, capacity)
    return clamp100(outcome + 0.2 * effort - 0.25 * burden + 0.1 * capacity)
end
println(next_outcome(42.0, 35.0, 24.0, 55.0))
