# Delayed feedback archetype example: fixes that fail.
using DelimitedFiles

root = normpath(joinpath(@__DIR__, ".."))
out_dir = joinpath(root, "outputs", "tables")
mkpath(out_dir)

problem = 60.0
history = [0.0, 0.0, 0.0]
rows = Any[["time" "problem" "fix" "delayed_fix"]]

for t in 0:24
    fix = 0.35 * problem
    delayed = history[1]
    global problem = problem - 0.25 * fix + 0.18 * delayed + 4.0
    history = [history[2], history[3], fix]
    push!(rows, [t round(problem, digits=3) round(fix, digits=3) round(delayed, digits=3)])
end

open(joinpath(out_dir, "julia_fixes_that_fail.csv"), "w") do io
    for row in rows
        println(io, join(row, ","))
    end
end

println("Wrote Julia delayed-feedback output")
