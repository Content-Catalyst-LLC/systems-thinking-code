use std::env;

fn diagnose(trust: f64, capacity: f64, backlog: f64, resilience: f64) -> &'static str {
    if trust < 55.0 && backlog > 150.0 && resilience < 35.0 {
        "fragility_rising"
    } else if capacity > 60.0 && resilience > 45.0 {
        "resilience_improving"
    } else {
        "mixed_signal"
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let trust = args.get(1).and_then(|v| v.parse::<f64>().ok()).unwrap_or(50.0);
    let capacity = args.get(2).and_then(|v| v.parse::<f64>().ok()).unwrap_or(48.0);
    let backlog = args.get(3).and_then(|v| v.parse::<f64>().ok()).unwrap_or(176.0);
    let resilience = args.get(4).and_then(|v| v.parse::<f64>().ok()).unwrap_or(28.0);

    println!("system_status={}", diagnose(trust, capacity, backlog, resilience));
}
