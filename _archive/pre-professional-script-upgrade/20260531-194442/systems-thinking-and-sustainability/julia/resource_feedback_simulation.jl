stock = 100.0
for year in 2026:2035
    global stock = max(0.0, stock + 3.0 - 3.8)
    println((year, stock))
end
