thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
dependency_load = 0.55
for threshold in thresholds
    status = dependency_load > threshold ? "fails" : "absorbs"
    println("threshold=", threshold, " load=", dependency_load, " status=", status)
end
