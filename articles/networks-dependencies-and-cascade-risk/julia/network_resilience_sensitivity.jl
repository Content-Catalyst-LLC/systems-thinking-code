redundancy = [0.2, 0.4, 0.6, 0.8]
diversity = 0.55
modularity = 0.50
visibility = 0.65
for r in redundancy
    score = 0.30*r + 0.25*diversity + 0.25*modularity + 0.20*visibility
    println("redundancy=", r, " resilience_score=", round(score, digits=3))
end
