# Robustness scan over simple demand and capacity assumptions

for demand_growth in [0.02, 0.03, 0.04, 0.05]
    for capacity_growth in [0.01, 0.03, 0.05]
        score = capacity_growth - demand_growth
        println((demand_growth=demand_growth, capacity_growth=capacity_growth, robustness_margin=round(score, digits=3)))
    end
end
