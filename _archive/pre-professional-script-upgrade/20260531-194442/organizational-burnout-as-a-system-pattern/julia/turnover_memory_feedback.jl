# Turnover and institutional memory feedback scaffold.
memory = 0.72
burnout = 0.40
for t in 1:8
    turnover = 0.04 + burnout * 0.10
    global memory = max(0, memory - turnover * 0.8 + 0.03)
    global burnout = min(1, burnout + (1 - memory) * 0.08)
    println("period=", t, ", turnover=", round(turnover, digits=3), ", memory=", round(memory, digits=3), ", burnout=", round(burnout, digits=3))
end
