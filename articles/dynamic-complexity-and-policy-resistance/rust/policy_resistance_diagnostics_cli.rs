use std::env;

fn net_effect(intended: f64, compensation: f64) -> f64 {
    intended * (1.0 - compensation)
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let intended = args.get(1).and_then(|s| s.parse::<f64>().ok()).unwrap_or(100.0);
    let compensation = args.get(2).and_then(|s| s.parse::<f64>().ok()).unwrap_or(0.45);
    println!("net_effect={:.3}", net_effect(intended, compensation));
}
