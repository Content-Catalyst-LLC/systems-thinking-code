# Nonlinear threshold sensitivity scaffold.
threshold_response(x, threshold) = x < threshold ? 0.3 + 0.4 * x : 0.6 + 1.2 * (x - threshold)
for x in 0.1:0.2:1.1
    println((x = x, response = threshold_response(x, 0.7)))
end
