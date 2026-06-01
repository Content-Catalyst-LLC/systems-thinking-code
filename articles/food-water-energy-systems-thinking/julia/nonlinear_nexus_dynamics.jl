# Lightweight Julia recurrence model for food-water-energy nexus dynamics.
# No external packages required.

groundwater = 1000.0
soil = 62.0
recharge = 28.0
withdrawal = 55.0
climate_stress = 0.18

println("year,groundwater,soil,nexus_stress")
for year in 0:30
    effective_withdrawal = withdrawal * (1.0 + climate_stress)
    global groundwater = max(0.0, groundwater + recharge - effective_withdrawal)
    global soil = max(0.0, min(100.0, soil + 0.5 - climate_stress * 2.0 - effective_withdrawal * 0.015))
    water_security = max(0.0, min(100.0, groundwater / 1000.0 * 100.0))
    stress = (100.0 - water_security) * 0.35 + (100.0 - soil) * 0.15 + climate_stress * 60.0 * 0.20
    println("$year,$(round(groundwater, digits=3)),$(round(soil, digits=3)),$(round(stress, digits=3))")
end
