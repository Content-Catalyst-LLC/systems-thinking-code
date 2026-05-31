# Capacity and recovery stock-flow scaffold.
capacity = 80.0
for t in 1:10
    workload = 58 + 4t
    recovery = 10 - 0.3t
    depletion = max(0, workload / 10 - recovery / 3)
    global capacity = capacity + recovery * 0.6 - depletion * 1.4
    println("period=", t, ", capacity=", round(capacity, digits=2))
end
