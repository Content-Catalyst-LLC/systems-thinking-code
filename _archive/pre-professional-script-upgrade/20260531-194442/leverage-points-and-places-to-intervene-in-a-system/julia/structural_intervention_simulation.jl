# Compare old and redesigned structures
function run_model(parameter_only::Bool)
    trust = 0.35
    burden = 0.75
    history = []
    for _ in 1:12
        if parameter_only
            burden -= 0.01
            trust += 0.005
        else
            burden -= 0.04
            trust += 0.02 + 0.03 * (1 - burden)
        end
        push!(history, (trust=max(0, min(1, trust)), burden=max(0, min(1, burden))))
    end
    return history
end

println("parameter only: ", last(run_model(true)))
println("structural redesign: ", last(run_model(false)))
