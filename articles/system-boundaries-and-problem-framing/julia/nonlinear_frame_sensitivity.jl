# Nonlinear frame sensitivity example

function nonlinear_assessment(value, internal_cost, external_cost, inclusion_ratio)
    legitimacy_bonus = 50000 * inclusion_ratio^2
    external_penalty = 0.000002 * external_cost^2
    return value - internal_cost - external_penalty + legitimacy_bonus
end

for inclusion in [0.25, 0.50, 0.75, 1.00]
    score = nonlinear_assessment(220000.0, 90000.0, 280000.0, inclusion)
    println("inclusion_ratio=$(inclusion), score=$(round(score, digits=2))")
end
