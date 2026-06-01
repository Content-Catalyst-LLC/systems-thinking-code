# Signed feedback-network example for causal loop diagrams.
edges = [
    ("Public Trust", "Cooperation", 1),
    ("Cooperation", "Service Performance", 1),
    ("Service Performance", "Public Trust", 1),
    ("Workload", "Stress", 1),
    ("Stress", "Errors", 1),
    ("Errors", "Rework", 1),
    ("Rework", "Workload", 1),
]

println("Signed feedback edges:")
for (src, dst, sign) in edges
    label = sign > 0 ? "+" : "-"
    println("$src --$label--> $dst")
end
