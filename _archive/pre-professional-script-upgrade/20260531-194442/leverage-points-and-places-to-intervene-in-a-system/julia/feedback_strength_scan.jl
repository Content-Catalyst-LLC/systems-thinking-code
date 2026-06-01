# Feedback strength scan
for alpha in [0.1, 0.25, 0.5, 0.8]
    x = 10.0
    for _ in 1:10
        x += alpha * (50 - x)
    end
    println("alpha=", alpha, " final=", round(x, digits=2))
end
