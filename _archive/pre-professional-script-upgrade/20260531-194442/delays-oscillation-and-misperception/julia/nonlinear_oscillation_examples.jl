# Nonlinear oscillation placeholder
function nonlinear_delay(; x0=0.4, r=3.2, delay=2, periods=30)
    values = fill(x0, delay + 1)
    for _ in 1:periods
        xdelay = values[end-delay]
        push!(values, r * xdelay * (1 - values[end]))
    end
    return values
end

println(nonlinear_delay())
