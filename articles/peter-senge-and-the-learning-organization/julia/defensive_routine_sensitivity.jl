# Defensive routine sensitivity example.

function learning_capacity(feedback, inquiry, memory, defensiveness)
    return max(0.0, min(100.0, 0.30 * feedback + 0.25 * inquiry + 0.25 * memory - 0.20 * defensiveness))
end

println("feedback,inquiry,memory,defensiveness,learning_capacity")
println("78,76,70,22,$(round(learning_capacity(78, 76, 70, 22), digits=3))")
println("48,30,44,76,$(round(learning_capacity(48, 30, 44, 76), digits=3))")
