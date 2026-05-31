# Dependency and capacity model.
capacity = 55.0
dependency = 0.25

for t in 0:9
    symptomatic = 20 + 3t
    repair = 10 + 2t
    global capacity = max(0.0, capacity + 0.5repair - 0.2symptomatic)
    global dependency = max(0.0, dependency + 0.01symptomatic - 0.012repair)
    println((period=t, capacity=round(capacity, digits=2), dependency=round(dependency, digits=3)))
end
