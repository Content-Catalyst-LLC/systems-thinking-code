memory = 0.52
for t in 1:8
    learning = 0.055 + 0.01 * t
    documentation = 0.045 + 0.005 * t
    sharing = 0.035
    turnover_loss = (t in [2, 5, 7]) ? 0.05 : 0.025
    forgetting = 0.028
    obsolescence = 0.018
    global memory = clamp(memory + learning + documentation + sharing - turnover_loss - forgetting - obsolescence, 0, 1)
    println("period=", t, " memory=", round(memory, digits=3))
end
