capacity = 0.52
trust = 0.48
for t in 1:6
    capacity += 0.06 * trust - 0.02
    trust += 0.05 * capacity - 0.03
    capacity = clamp(capacity, 0, 1)
    trust = clamp(trust, 0, 1)
    println("period=", t, " capacity=", round(capacity, digits=3), " trust=", round(trust, digits=3))
end
