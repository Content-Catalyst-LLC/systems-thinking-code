# Overshoot and recovery model.
function simulate(; years=30)
    scale = 100.0
    resource = 1000.0
    for year in 0:years
        extraction = 0.10 * scale
        regeneration = 0.035 * resource
        resource = max(0.0, resource + regeneration - extraction)
        growth_rate = 0.15 * (resource / 1000.0) - (resource < 250 ? 0.08 : 0.0)
        println((year=year, scale=round(scale, digits=2), resource=round(resource, digits=2), growth_rate=round(growth_rate, digits=3)))
        scale = max(1.0, scale + growth_rate * scale)
    end
end

simulate()
