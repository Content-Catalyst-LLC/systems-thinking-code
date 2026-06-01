nodes = ["power_grid", "water_utility", "hospital", "telecom_network"]
threshold = Dict("power_grid" => 0.9, "water_utility" => 0.45, "hospital" => 0.50, "telecom_network" => 0.55)
dependencies = Dict(
    "water_utility" => Dict("power_grid" => 0.70),
    "hospital" => Dict("power_grid" => 0.55, "water_utility" => 0.35, "telecom_network" => 0.30),
    "telecom_network" => Dict("power_grid" => 0.60)
)
failed = Set(["power_grid"])
for step in 0:4
    println("step=", step, " failed=", collect(failed))
    new_failed = Set{String}()
    for node in nodes
        if node in failed
            continue
        end
        providers = get(dependencies, node, Dict{String, Float64}())
        load = sum([providers[p] for p in keys(providers) if p in failed])
        if load > threshold[node]
            push!(new_failed, node)
        end
    end
    if isempty(new_failed)
        break
    end
    union!(failed, new_failed)
end
