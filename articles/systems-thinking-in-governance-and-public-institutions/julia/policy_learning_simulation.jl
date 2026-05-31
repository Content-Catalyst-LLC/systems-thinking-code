feedback_closure = [0.31, 0.33, 0.46, 0.53, 0.61, 0.79]
public_value = [0.49, 0.52, 0.62, 0.67, 0.72, 0.81]
for i in eachindex(feedback_closure)
    learning_index = feedback_closure[i] * public_value[i]
    println("scenario=", i, " policy_learning_index=", round(learning_index, digits=3))
end
