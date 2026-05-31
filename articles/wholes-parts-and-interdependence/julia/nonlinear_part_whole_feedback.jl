# Nonlinear part-whole feedback example

function nonlinear_feedback(x0::Float64=0.42, r::Float64=3.2, periods::Int=25)
    x = x0
    rows = []
    for t in 1:periods
        x = r * x * (1.0 - x)
        push!(rows, (period=t, state=round(x, digits=5)))
    end
    return rows
end

for row in nonlinear_feedback()
    println(row)
end
