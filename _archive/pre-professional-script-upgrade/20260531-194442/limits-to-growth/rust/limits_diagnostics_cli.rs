// Lightweight CLI scaffold for limits-to-growth diagnostics.
use std::env;

fn diagnose(scale: f64, capacity: f64) -> &'static str {
    let pressure = scale / capacity;
    if pressure >= 1.1 { "overshoot risk" }
    else if pressure >= 0.9 { "constraint emerging" }
    else { "within modeled capacity" }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let scale = args.get(1).and_then(|v| v.parse::<f64>().ok()).unwrap_or(220.0);
    let capacity = args.get(2).and_then(|v| v.parse::<f64>().ok()).unwrap_or(260.0);
    println!("scale={:.2} capacity={:.2} diagnosis={}", scale, capacity, diagnose(scale, capacity));
}
