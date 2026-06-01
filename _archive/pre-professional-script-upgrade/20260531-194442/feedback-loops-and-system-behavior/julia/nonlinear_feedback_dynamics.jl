# Nonlinear feedback dynamics example.

function logistic_feedback(x0::Float64, r::Float64, k::Float64, periods::Int64)
    values = Float64[x0]
    x = x0
    for _ in 1:periods
        x = x + r * x * (1 - x / k)
        push!(values, x)
    end
    return values
end

values = logistic_feedback(5.0, 0.35, 100.0, 30)
println("period,value")
for (i, v) in enumerate(values)
    println("$(i-1),$(round(v, digits=3))")
end
