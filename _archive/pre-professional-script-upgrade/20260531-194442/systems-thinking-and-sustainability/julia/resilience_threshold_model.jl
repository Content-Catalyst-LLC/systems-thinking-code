function resilience_score(values)
    return sum(values) / length(values)
end
println(resilience_score([0.56, 0.48, 0.62, 0.53, 0.45, 0.58]))
