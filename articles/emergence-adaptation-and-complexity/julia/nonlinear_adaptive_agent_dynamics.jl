# Dependency-light Julia sketch for adaptive agent dynamics.
function clamp01(x)
    min(1.0, max(0.0, x))
end

function run_model(periods::Int=20, agents::Int=40)
    states = [mod(i * 0.137, 1.0) for i in 1:agents]
    for _ in 1:periods
        next_states = similar(states)
        for i in 1:agents
            left = states[mod1(i - 1, agents)]
            right = states[mod1(i + 1, agents)]
            local = (left + right) / 2
            next_states[i] = clamp01(states[i] + 0.18 * (local - states[i]) + 0.01 * sin(i))
        end
        states = next_states
    end
    println("Julia adaptive model final mean = ", sum(states) / length(states))
end

run_model()
