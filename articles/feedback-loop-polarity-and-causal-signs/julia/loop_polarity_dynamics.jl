# Compute loop polarity from signed edges.
signs = [1, 1, 1]
polarity = prod(signs)
println(polarity > 0 ? "reinforcing" : "balancing")
