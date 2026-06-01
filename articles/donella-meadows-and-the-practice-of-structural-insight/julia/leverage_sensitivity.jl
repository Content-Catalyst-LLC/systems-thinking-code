# Leverage sensitivity example.

function leverage_score(information, rules, goals, paradigm, self_organization)
    return 18.0 * information + 20.0 * rules + 22.0 * goals + 24.0 * paradigm + 16.0 * self_organization
end

println("information,rules,goals,paradigm,self_organization,leverage_score")
println("0.78,0.74,0.80,0.76,0.72,$(round(leverage_score(0.78, 0.74, 0.80, 0.76, 0.72), digits=3))")
