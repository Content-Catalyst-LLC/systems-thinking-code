# Nonlinear feedback awareness demonstration for Learning Organizations and Feedback Awareness.
feedback = [0.18, 0.25, 0.38, 0.61, 0.74]
learning = 0.20
for f in feedback
    global learning = learning + 0.45 * f * (1 - learning)
    println(round(learning, digits=4))
end
