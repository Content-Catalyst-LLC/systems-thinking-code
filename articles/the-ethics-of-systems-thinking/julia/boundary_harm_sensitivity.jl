# Boundary harm sensitivity.

function boundary_harm(consequences_experienced, consequences_counted)
    return max(0.0, consequences_experienced - consequences_counted)
end

println("domain,experienced,counted,boundary_harm")
println("urban_redevelopment,9,4,$(boundary_harm(9, 4))")
println("public_health,8,4,$(boundary_harm(8, 4))")
