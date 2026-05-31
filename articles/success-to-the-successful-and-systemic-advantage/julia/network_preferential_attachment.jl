# Lightweight preferential attachment sketch.
degrees = Dict("A001"=>10, "A003"=>2, "A005"=>1, "A008"=>12)
total_degree = sum(values(degrees))
for (node, degree) in degrees
    println(node, ", attachment_probability=", round(degree / total_degree, digits=3))
end
