use std::env;

fn threshold_response(stress: f64, threshold: f64) -> f64 {
    if stress < threshold {
        0.25 * stress
    } else {
        0.25 * threshold + 1.15 * (stress - threshold)
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let stress = args.get(1).and_then(|s| s.parse::<f64>().ok()).unwrap_or(75.0);
    let threshold = args.get(2).and_then(|s| s.parse::<f64>().ok()).unwrap_or(70.0);
    let response = threshold_response(stress, threshold);

    println!("stress,response,threshold");
    println!("{:.2},{:.2},{:.2}", stress, response, threshold);
}
