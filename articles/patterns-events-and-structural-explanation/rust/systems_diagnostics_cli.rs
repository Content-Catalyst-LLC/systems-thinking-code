use std::env;

fn diagnose(risk: f64, resilience: f64) -> &'static str {
    if risk >= 70.0 && resilience <= 30.0 {
        "structural fragility rising"
    } else if risk <= 50.0 && resilience >= 50.0 {
        "adaptive capacity improving"
    } else {
        "mixed pattern requires review"
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let risk = args.get(1).and_then(|v| v.parse::<f64>().ok()).unwrap_or(73.0);
    let resilience = args.get(2).and_then(|v| v.parse::<f64>().ok()).unwrap_or(28.0);
    println!("diagnostic_status: {}", diagnose(risk, resilience));
}
