# Synthetic nonlinear burnout dynamics teaching scaffold.
function burnout_next(burnout, pressure, recovery; a=0.18, b=0.12)
    return clamp(burnout + a * pressure * (1 + burnout) - b * recovery, 0.0, 1.0)
end

burnout = 0.35
for t in 1:12
    pressure = 0.55 + 0.025t
    recovery = max(0.15, 0.45 - 0.015t)
    global burnout = burnout_next(burnout, pressure, recovery)
    println("period=", t, ", burnout=", round(burnout, digits=3))
end
