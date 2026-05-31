# Minimal agent-style commons model with cooperative and high-use agents.
stock = 1000.0
capacity = 1400.0
regen_rate = 0.22
users = [60.0, 40.0, 35.0, 25.0]
for year in 1:25
    regeneration = regen_rate * stock * max(0.0, 1.0 - stock / capacity)
    total_use = sum(users)
    global stock = max(0.0, stock + regeneration - total_use)
end
println("Stock after mixed user strategies: ", round(stock, digits=2))
