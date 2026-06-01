# Adaptive learning organization model placeholder.
capacity = 0.50
for t in 1:6
    feedback_awareness = 0.12 + 0.03t
    structural_change = 0.08 + 0.02t
    global capacity = min(1.0, capacity + feedback_awareness * structural_change)
    println((period=t, capacity=round(capacity, digits=4)))
end
