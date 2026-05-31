# Robustness scan scaffold.
policies = Dict("baseline" => [0.40, 0.62, 0.72], "early_repair" => [0.62, 0.78, 0.84], "burden_reduction" => [0.58, 0.74, 0.80])
for (policy, outcomes) in policies
    println(policy, " worst-case resilience = ", minimum(outcomes))
end
