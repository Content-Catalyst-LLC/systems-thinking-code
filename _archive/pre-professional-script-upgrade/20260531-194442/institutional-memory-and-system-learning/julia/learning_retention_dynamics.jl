captured = [0.62, 0.67, 0.71, 0.76, 0.82]
usable = [0.31, 0.39, 0.48, 0.60, 0.72]
for i in eachindex(captured)
    println("period=", i, " retention=", round(usable[i] / captured[i], digits=3))
end
