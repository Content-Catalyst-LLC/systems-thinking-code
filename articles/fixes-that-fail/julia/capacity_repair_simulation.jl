# Capacity repair simulation.
capacity = 1.0
for t in 1:12
    fix = t <= 6 ? 0.75 : 0.35
    repair = t <= 6 ? 0.10 : 0.80
    global capacity = clamp(capacity + 0.07 * repair - 0.06 * fix, 0.0, 1.5)
    println("period=$t capacity=$(round(capacity, digits=3))")
end
