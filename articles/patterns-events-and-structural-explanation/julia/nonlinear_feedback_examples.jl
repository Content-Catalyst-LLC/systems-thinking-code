# Nonlinear feedback example.

function simulate_nonlinear_feedback(; periods=20, trust=62.0, risk=52.0)
    for period in 1:periods
        risk_growth = 0.04 * risk * (1 + max(0, 60 - trust) / 60)
        trust_loss = 0.03 * risk
        risk += risk_growth - 1.0
        trust -= trust_loss - 0.4
        println((period=period, trust=round(trust, digits=2), risk=round(risk, digits=2)))
    end
end

simulate_nonlinear_feedback()
