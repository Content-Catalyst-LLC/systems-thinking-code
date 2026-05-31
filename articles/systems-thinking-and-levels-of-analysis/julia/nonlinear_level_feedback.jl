# Nonlinear level feedback example

function nonlinear_feedback(x)
    threshold = 70.0
    if x < threshold
        return x + 0.05 * x
    else
        return x + 0.15 * x - 5.0
    end
end

x = 40.0
println("period,state")
for t in 1:15
    global x = nonlinear_feedback(x)
    println("$t,$(round(x, digits=2))")
end
