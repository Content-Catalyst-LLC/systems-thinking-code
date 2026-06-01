function next_stock(stock, regeneration, extraction, degradation)
    return max(0.0, stock + regeneration - extraction - degradation)
end
println(next_stock(100.0, 4.5, 2.8, 0.7))
