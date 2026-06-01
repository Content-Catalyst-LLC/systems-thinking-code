# Objective-function scan.

scores = Dict(
    "throughput" => 0.82,
    "access" => 0.66,
    "dignity" => 0.63,
    "burden" => 0.45,
    "harm" => 0.38,
)

for access_weight in 0.0:0.25:1.0
    value = (1 - access_weight) * scores["throughput"] + access_weight * scores["access"] + 0.5 * scores["dignity"] - 0.4 * scores["burden"] - 0.4 * scores["harm"]
    println("access_weight=", access_weight, " objective=", round(value, digits=3))
end
