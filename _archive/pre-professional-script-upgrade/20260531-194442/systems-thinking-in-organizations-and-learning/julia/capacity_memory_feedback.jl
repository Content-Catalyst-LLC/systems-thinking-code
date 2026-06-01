# Capacity-memory feedback placeholder.
memory_next(memory, embedded_learning, forgetting) = memory + embedded_learning - forgetting
println("Memory example: ", memory_next(0.52, 0.07, 0.04))
