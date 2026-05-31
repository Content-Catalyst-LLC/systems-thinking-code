# Nonlinear archetype dynamics example: limits to growth.
using DelimitedFiles

root = normpath(joinpath(@__DIR__, ".."))
out_dir = joinpath(root, "outputs", "tables")
mkpath(out_dir)

K = 100.0
r = 0.32
x = 8.0
rows = Any[["time" "state" "capacity_limit"]]

for t in 0:30
    push!(rows, [t round(x, digits=4) K])
    global x = x + r * x * (1 - x / K)
end

open(joinpath(out_dir, "julia_limits_to_growth.csv"), "w") do io
    for row in rows
        println(io, join(row, ","))
    end
end

println("Wrote Julia limits-to-growth output")
