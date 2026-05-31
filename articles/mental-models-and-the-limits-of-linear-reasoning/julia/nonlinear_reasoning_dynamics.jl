# Nonlinear response scaffold for mental models and limits of linear reasoning.
state = 50.0
for t in 1:12
    input = t <= 6 ? 6.0 : 2.5
    nonlinear_drag = 0.015 * state^1.2
    global state = state + input - nonlinear_drag
    println("period=", t, ", state=", round(state, digits=3), ", drag=", round(nonlinear_drag, digits=3))
end
