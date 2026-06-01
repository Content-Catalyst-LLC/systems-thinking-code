function public_value(access, trust, equity, capacity)
    return 0.25access + 0.25trust + 0.25equity + 0.25capacity
end
println(public_value(70.0, 65.0, 58.0, 62.0))
