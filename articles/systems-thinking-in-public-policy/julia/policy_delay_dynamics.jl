backlog = 100.0
capacity = 45.0
for year in 0:10
    global capacity += year >= 4 ? 2.0 : 0.0
    global backlog = max(0.0, backlog + 8.0 - capacity * 0.15)
    println((year, round(capacity, digits=2), round(backlog, digits=2)))
end
