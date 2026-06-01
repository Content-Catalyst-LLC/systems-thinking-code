# Repair transition simulation.
function transition_path()
    symptomatic = [40, 38, 35, 31, 26, 21, 16, 12]
    repair = [8, 12, 16, 21, 27, 33, 38, 42]
    pressure = 90.0
    for t in eachindex(symptomatic)
        pressure = max(0, pressure + 4 - 0.25symptomatic[t] - 0.18repair[t])
        println((period=t-1, pressure=round(pressure, digits=2), symptomatic=symptomatic[t], repair=repair[t]))
    end
end

transition_path()
