# Institutional memory accumulation and decay sketch.
memory = 0.45
for t in 1:8
    retained_learning = 0.08
    forgetting = 0.04 * memory
    global memory = memory + retained_learning - forgetting
    println((period=t, memory=round(memory, digits=4)))
end
