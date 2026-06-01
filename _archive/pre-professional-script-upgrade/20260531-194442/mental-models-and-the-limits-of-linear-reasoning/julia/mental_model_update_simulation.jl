# Mental model update scaffold.
belief = 0.80
for t in 1:10
    observed = 0.45 + 0.03 * t
    expected = belief
    learning_rate = 0.25
    global belief = belief + learning_rate * (observed - expected)
    println("period=", t, ", updated_belief=", round(belief, digits=3))
end
