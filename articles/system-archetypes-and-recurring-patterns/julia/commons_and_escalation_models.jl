# Commons depletion and escalation toy models.
using DelimitedFiles

root = normpath(joinpath(@__DIR__, ".."))
out_dir = joinpath(root, "outputs", "tables")
mkpath(out_dir)

resource = 100.0
rows = Any[["time" "resource_stock" "extraction" "regeneration"]]

for t in 0:30
    extraction = t < 15 ? 25.0 : 15.0
    regeneration = 0.08 * resource
    global resource = max(0.0, resource + regeneration - extraction)
    push!(rows, [t round(resource, digits=3) extraction round(regeneration, digits=3)])
end

open(joinpath(out_dir, "julia_commons_model.csv"), "w") do io
    for row in rows
        println(io, join(row, ","))
    end
end

println("Wrote Julia commons model")
