fn main() {
    let pressure = 0.86_f64;
    let recovery = 0.24_f64;
    let hidden_labor = 0.58_f64;
    let burnout_risk = (pressure * 0.50) + ((1.0 - recovery) * 0.30) + (hidden_labor * 0.20);
    println!("burnout_risk_proxy={:.3}", burnout_risk);
}
