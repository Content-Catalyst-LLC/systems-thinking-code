use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let pressure: f64 = args.get(1).and_then(|v| v.parse().ok()).unwrap_or(0.72);
    let stock: f64 = args.get(2).and_then(|v| v.parse().ok()).unwrap_or(0.48);
    let buffer: f64 = args.get(3).and_then(|v| v.parse().ok()).unwrap_or(0.35);
    let risk = 0.45 * pressure + 0.35 * (1.0 - stock) + 0.20 * (1.0 - buffer);
    println!("overshoot_diagnostic_risk={:.3}", risk);
}
