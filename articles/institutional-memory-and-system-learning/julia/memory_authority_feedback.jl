scenarios = Dict(
    "status_quo" => (0.48, 0.42, 0.38),
    "memory_authority_integration" => (0.86, 0.84, 0.80),
)
for (name, vals) in scenarios
    memory, authority, embedding = vals
    system_learning = memory * authority * embedding
    println(name, " system_learning=", round(system_learning, digits=3))
end
