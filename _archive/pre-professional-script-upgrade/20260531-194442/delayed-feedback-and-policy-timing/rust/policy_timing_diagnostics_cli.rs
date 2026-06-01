use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let lag: f64 = args.get(1).and_then(|v| v.parse().ok()).unwrap_or(12.0);
    let correction: f64 = args.get(2).and_then(|v| v.parse().ok()).unwrap_or(0.5);
    let risk = lag * correction;
    println!("policy_timing_risk_score={:.3}", risk);
}
