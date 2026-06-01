function next_outcome(outcome, effort, burden, capacity)
    return clamp(outcome + 0.2 * effort - 0.25 * burden + 0.1 * capacity, 0.0, 100.0)
end
println(next_outcome(42.0, 35.0, 24.0, 55.0))
